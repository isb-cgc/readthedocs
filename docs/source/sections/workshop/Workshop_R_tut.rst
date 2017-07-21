.. _R-workshop:

***************
Analysis with R
***************

Differential gene expression associated with HPV integration
############################################################

In this example, we will study the potential effects of HPV integration on the
expression of recurrent target genes in CESC and HNSC tumors. This example
demonstrates using R to issue BigQuery queries involving multiple tables across
multiple data sets. We will also show users how to bring in their own data to
use in conjunction with the TCGA data already available as BigQuery tables. In
this exercise, we will reproduce some figures from Tang et. al. [1] to visualize
altered expression of host genes frequently targeted by HPV.

References:
Tang et. al. The landscape of viral expression and host gene fusion and adaptation in human cancer.
Nature Communications 4, Article number:2513|doi:10.1038/ncomms3513

Loading libraries
=================

.. code-block:: r

    require(bigrquery,quietly = TRUE) || install.packages('bigrquery',verbose = FALSE)
    require(httpuv, quietly = TRUE) || install.packages('httpuv',verbose=FALSE)
    require(ggplot2,quietly = TRUE) || install.packages('ggplot2',verbose = FALSE)

Your project ID
===============

You will be using your own project ID. At certain points in the code, it will
be necessary to complete the code.

.. code-block:: r

    main_cloud_project = "isb-cgc"
    my_cloud_project   = "your_project_id"
    tcga_data_set      = "TCGA_hg38_data_v0"

First query
===========

Now let's see if things are working.

.. code-block:: r

    bigrquery::list_tables(main_cloud_project, tcga_data_set)

In this tutorial, we will be investigating two studies using two existing
BigQuery tables. Additionally, we're going to BYOD "Bring your own data".

.. code-block:: r

	study=c('TCGA-CESC','TCGA-HNSC')

	clinical_table = "`isb-cgc.TCGA_bioclin_v0.Clinical`"

Constructing Queries
====================

One of the great things about working in a scripting environment, is that our
analysis -- the queries -- we write, can be constructed programmatically.
That makes it easy to apply the same structured queries to many questions.
In the next code block is an example of how to do that.

.. code-block:: r

	sqlQuery = paste("SELECT case_barcode, project_short_name AS project, hpv_calls, hpv_status ",
	                 "FROM ", clinical_table,
	                 " WHERE project_short_name in (",paste(shQuote(study),collapse = ','),")",sep="")

	sqlQuery

	hpv_table = query_exec(sqlQuery,project = my_cloud_project)

	dim(hpv_table)

	head(hpv_table)

	# We can do some quality control ...
	# Assert that if hpv_calls is NA, hpv_status is Negative
	stopifnot((is.na(hpv_table$hpv_calls) && hpv_table$hpv_status=="Negative") || !is.na(hpv_table$hpv_calls))

	# Let's explore the cohort
	ggplot(data=hpv_table, aes(x=hpv_status, fill=project)) + geom_bar(stat="count", position=position_dodge())

Uploading Data
==============

The exact location of HPV integration is not available in the TCGA data,
so instead we'll get a list of frequently targeted genes that was published
with this paper:

*Ka-Wei Tang et. al. The Landscape of viral expression and host gene fusion and adaptation in human cancer. doi:10.1038/ncomms3513*

(Supplementary Data 2: Integration analysis results)

We will access the data from our workshop bucket using the command line or from
the Google Cloud Console. Using the cloud console, go to https://console.cloud.google.com and find the
workshop bucket.

Using the google command line tool:

.. code-block:: none

	gsutil cp gs://isb-cgc-workshop/data/Larsson/ncomms3513-s3.tsv .
	gsutil cp gs://isb-cgc-workshop/data/Larsson/ncomms3513-s3_Schema.json .


Now the data is in our directory, but we need to transform it into a BQ table.
To do that, we need to create a data set in our project. We can do this from within the BigQuery
web UI by clicking on the little blue triangle next to your project ID on the left.
Or we can do this on the command line using the bq command line tool.

.. code-block:: none

	gcloud init

	bq help

	bq ls

	bq mk workspace

	bq load --source_format CSV --field_delimiter "\t"  --schema ncomms3513-s3_Schema.json workspace.ncomms3513_s3 ncomms3513-s3.tsv

Integrating with the expression data
====================================

Now we can directly query our own data, and start to combine it with other tables.
Let's try it out!

This next query is going to select the genes that were associated with HPV
integration in CESC and HNSC tumors.

.. code-block:: r

	sqlQuery = "
	SELECT
	  Overlapping_genes,
	  Cancer
	FROM
	  `isb-cgc-04-0030.workspace.ncomms3513_s3`
	WHERE
	  Cancer IN ('TCGA-CESC','TCGA-HNSC')
	  AND Overlapping_genes <> 'Intergenic'
	GROUP BY
	  Cancer,
	  Overlapping_genes
	  "

	affected_genes = query_exec(sqlQuery,project = my_cloud_project)

	head(affected_genes)

	table(affected_genes$Cancer)

Next, with those offen affected genes, we will query gene expression data.

.. code-block:: r

	query <- "
	SELECT
	  project_short_name,
	  gene_name,
	  AVG(HTSeq__FPKM) as mean_expression
	FROM
	  `isb-cgc.TCGA_hg38_data_v0.RNAseq_Gene_Expression`
	WHERE
	  project_short_name IN ('TCGA-CESC','TCGA-HNSC')
	  AND gene_name IN (
	    SELECT
	      Overlapping_genes AS gene_name
	    FROM
	      `isb-cgc-04-0030.workspace.ncomms3513_s3`
	    WHERE
	      Cancer IN ('TCGA-CESC','TCGA-HNSC')
	      AND Overlapping_genes <> 'Intergenic'
	    GROUP BY
	      gene_name )
	GROUP BY
	  project_short_name,
	  gene_name
	ORDER BY
	  mean_expression"

	# running the query.
	mean_affected_genes = query_exec(query, project = my_cloud_project)

	# we'll create some more meaningful x-axis labels
	mean_affected_genes$xlabel <- paste0(mean_affected_genes$project_short_name, "_", mean_affected_genes$gene_name)

	# Now we can visualize it.
	qplot(data=mean_affected_genes,
	      x=factor(x = xlabel, ordered = T, levels = xlabel),
	      y=mean_expression,
	      col=project_short_name) +
	      theme(axis.text.x = element_text(angle = 90, hjust = 1, size=4)) +
	      xlab("Project_Gene")


Computing Statistics
====================

Instead, if we want to get the actual gene expression values, we could query
for that, and retrieve it as a data.frame.

.. code-block:: r

	sqlQuery = "
	SELECT
	  case_barcode,
	  sample_barcode,
	  project_short_name,
	  gene_name,
	  HTSeq__FPKM
	FROM
	  `isb-cgc.TCGA_hg38_data_v0.RNAseq_Gene_Expression`
	WHERE
	  project_short_name IN ('CESC','HNSC')
	  AND gene_name IN (
	  SELECT
	    Overlapping_genes as gene_name
	  FROM
	    `isb-cgc-04-0030.workspace.ncomms3513_s3`
	  WHERE
	    Cancer IN ('TCGA-CESC','TCGA-HNSC')
	    AND Overlapping_genes <> 'Intergenic'
	  GROUP BY
	    gene_name )
		"

	gexp_affected_genes = query_exec(sqlQuery,project = my_cloud_project)

	#view results
	head(gexp_affected_genes)

	# a couple different ways to look at the results
	#qplot(data=gexp_affected_genes, x=project_short_name, y=HTSeq__FPKM, col=gene_name, geom="boxplot")
	#qplot(data=gexp_affected_genes, x=project_short_name, y=log2(HTSeq__FPKM), col=gene_name, geom="boxplot")
	qplot(data=gexp_affected_genes, x=log2(HTSeq__FPKM+1), col=gene_name, geom="density") + facet_wrap(~ project_short_name)

Not all the samples listed in the clinical data have gene expression data, however.
Let's filter the hpv_table to match the samples to those in gexp_affected_genes

.. code-block:: r

	require(tidyr,quietly = TRUE) || install.packages('tidyr',verbose = FALSE)
	require(dplyr,quietly = TRUE) || install.packages('dplyr',verbose = FALSE)
	require(broom,quietly = TRUE) || install.packages('broom',verbose = FALSE)

	# let's get rid of 'indeterminate' samples
	hpv_table = dplyr::filter(hpv_table, hpv_status != "Indeterminate", case_barcode %in% gexp_affected_genes$case_barcode)

T-tests
=======

Now, we are going to perform t.tests on expression by hpv_status and study.

.. code-block:: r

	gxps <- merge(x=gexp_affected_genes, y=hpv_table, by=c("project_short_name","case_barcode"))

	# Performing a t-test between hpv+ and hpv- by project_short_name and gene
	res0 <- gxps %>%
	group_by(project_short_name, gene_name) %>%
	do(tidy(t.test(log2(HTSeq__FPKM+1) ~ hpv_status, data=.))) %>%
	ungroup() %>%
	arrange(desc(statistic))

	# These are the top 5 results ...
	top5 <- select(top_n(res0, 5, statistic), project_short_name, gene_name)

	# Let's subset the data by the top 5 results...
	res1 <- merge(x=top5, y=gxps) %>% mutate( Project_Gene = paste0(project_short_name, "_", gene_name))

	# now we can plot the results...
	ggplot(res1, aes(x=Project_Gene, y=log2(HTSeq__FPKM+1), fill=hpv_status)) + geom_boxplot()


Making BigQueries
=================

Previously, we downloaded data and performed some work on it. But another way to work
is to compute  as much as possible in the cloud, and use R to visualize summary results.

Please see: https://cloud.google.com/bigquery/query-reference

.. code-block:: r

	sqlQuery = "
	SELECT
	  case_barcode,
	  sample_barcode,
	  project_short_name,
	  gene_name,
	  HTSeq__FPKM
	FROM
	  `isb-cgc.TCGA_hg38_data_v0.RNAseq_Gene_Expression`
	WHERE
	  project_short_name = 'TCGA-CESC'
	  AND case_barcode IN (
	  SELECT
	    case_barcode
	  FROM
	    `isb-cgc.TCGA_bioclin_v0.Clinical`
	  WHERE
	    hpv_status = 'Positive' )
	  AND gene_name IN (
	  SELECT
	    Overlapping_genes AS gene_name
	  FROM
	    `isb-cgc-04-0030.workspace.ncomms3513_s3`
	  WHERE
	    Cancer = 'TCGA-CESC'
	    AND Overlapping_genes <> 'Intergenic'
	  GROUP BY
	    gene_name )
	"

	q1 = query_exec(sqlQuery,project = cloud_project_workshop)

	dim(q1)

Now lets make a small change, and get gene expression for subjects that are hpv negative.

.. code-block:: r

	sqlQuery = "
	SELECT
	  case_barcode,
	  sample_barcode,
	  project_short_name,
	  gene_name,
	  HTSeq__FPKM
	FROM
	  `isb-cgc:TCGA_hg38_data_v0.RNAseq_Gene_Expression`
	WHERE
	  project_short_name = 'TCGA-CESC'
	  AND case_barcode IN (
	  SELECT
	    case_barcode
	  FROM
	    `isb-cgc.TCGA_bioclin_v0.Clinical`
	  WHERE
	    hpv_status = 'Negative' )
	  AND gene_name IN (
	  SELECT
	    Overlapping_genes AS gene_name
	  FROM
	    `isb-cgc-04-0030.workspace.ncomms3513_s3`
	  WHERE
	    Cancer = 'TCGA-CESC'
	    AND Overlapping_genes <> 'Intergenic'
	  GROUP BY
	    gene_name )
	"

	q2 <- query_exec(sqlQuery,project = cloud_project_workshop)

	dim(q2)

Now we merge the previous two queries, and compute T statistics using
BigQuery built in functions, SQRT, MEAN, STDDEV, POW, COUNT, and LOG2.

Please see: https://cloud.google.com/bigquery/query-reference

.. code-block:: r

	q <- "
		WITH
		  ## we use the 'WITH' keyword in order to create a few
		  ## preliminary tables that we will use later on in the
		  ## query -- this helps in writing 'modular' SQL that
		  ## is easier to read
		  --
		  ## start by getting the list of genes of interest from
		  ## the paper's table (will result in a list of 106 genes)
		  geneList AS (
		  SELECT
		    Overlapping_genes AS gene_name
		  FROM
		    `isb-cgc-04-0030.workspace.ncomms3513_s3`
		  WHERE
		    Overlapping_genes <> 'Intergenic'
		  GROUP BY
		    gene_name ),
		  ## next, get the identifiers (barcodes) for all HPV+ cases
		  ## (will result in a list of 383 cases)
		  posCaseList AS (
		  SELECT
		    case_barcode
		  FROM
		    `isb-cgc.TCGA_bioclin_v0.Clinical`
		  WHERE
		    hpv_status = 'Positive' ),
		  ## now do the same for all HPV- cases
		  ## (will result in a list of 664 cases)
		  negCaseList AS (
		  SELECT
		    case_barcode
		  FROM
		    `isb-cgc.TCGA_bioclin_v0.Clinical`
		  WHERE
		    hpv_status = 'Negative' )
		  ##
		  ## Now we being our main SELECT statement, which actually
		  ## wraps a pair of SELECTs that are JOINed together
		  ##
		SELECT
		  p.gene_name AS gene,
		  p.project_short_name,
		  p.x AS x,
		  p.sx2 AS sx2,
		  p.nx AS nx,
		  o.y AS y,
		  o.sy2 AS sy2,
		  o.ny AS ny,
		  (p.x-o.y) / SQRT((p.sx2/p.nx) + (o.sy2/o.ny)) AS T
		FROM (
		    # first the gene expression summaries for hpv+ tumors
		  SELECT
		    project_short_name,
		    gene_name,
		    AVG(LOG(HTSeq__FPKM+1,2)) AS y,
		    POW(STDDEV(LOG(HTSeq__FPKM+1,2)),2) AS sy2,
		    COUNT(case_barcode) AS ny
		  FROM
		    `isb-cgc.TCGA_hg38_data_v0.RNAseq_Gene_Expression`
		  WHERE
		    project_short_name = 'TCGA-CESC'
		    AND case_barcode IN (
		    SELECT
		      case_barcode
		    FROM
		      posCaseList )
		    AND gene_name IN (
		    SELECT
		      gene_name
		    FROM
		      geneList )
		  GROUP BY
		    project_short_name,
		    gene_name
		  HAVING
		    ny>0
		    AND sy2>0) AS o
		JOIN (
		    # Then we get the gene expression summaries from hpv-
		  SELECT
		    project_short_name,
		    gene_name,
		    AVG(LOG(HTSeq__FPKM+1,2)) AS x,
		    POW(STDDEV(LOG(HTSeq__FPKM+1,2)),2) AS sx2,
		    COUNT(case_barcode) AS nx
		  FROM
		    `isb-cgc.TCGA_hg38_data_v0.RNAseq_Gene_Expression`
		  WHERE
		    project_short_name = 'TCGA-CESC'
		    AND case_barcode IN (
		    SELECT
		      case_barcode
		    FROM
		      negCaseList )
		    AND gene_name IN (
		    SELECT
		      gene_name
		    FROM
		      geneList )
		  GROUP BY
		    project_short_name,
		    gene_name
		  HAVING
		    nx>0
		    AND sx2>0) AS p
		ON
		  p.gene_name = o.gene_name
		  AND p.project_short_name = o.project_short_name
		GROUP BY
		  gene,
		  project_short_name,
		  x,
		  sx2,
		  nx,
		  y,
		  sy2,
		  ny,
		  T
		ORDER BY
		  T DESC
	 "

	 t_test_result <- query_exec(q, project = cloud_project_workshop)

	 head(t_test_result)


	# and we can see the same results in the previously done work.
	 res0

Extras
======

Transform gexp_affected_genes_df into a gexp-by-samples feature matrix

.. code-block:: r

	gexp_fm = tidyr::spread(gexp_affected_genes,gene_name,HTSeq__FPKM)

	gexp_fm[1:5,1:5]

