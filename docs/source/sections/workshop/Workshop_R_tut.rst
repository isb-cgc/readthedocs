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
    tcga_data_set      = "tcga_201510_alpha"

First query
===========

Now let's see if things are working.

.. code-block:: r

    bigrquery::list_tables(main_cloud_project, tcga_data_set)

In this tutorial, we will be investigating two studies using two existing
BigQuery tables. Additionally, we're going to BYOD "Bring your own data".

.. code-block:: r

	study=c('CESC','HNSC')

	clinical_table = "[isb-cgc:tcga_201510_alpha.Clinical_data]"

Constructing Queries
====================

One of the great things about working in a scripting environment, is that our
analysis -- the queries -- we write, can be constructed programmatically.
That makes it easy to apply the same structured queries to many questions.
In the next code block is an example of how to do that.

.. code-block:: r

	sqlQuery = paste("SELECT ParticipantBarcode, Study, hpv_calls, hpv_status ",
	                 "FROM ", clinical_table,
	                 " WHERE Study in (",paste(shQuote(study),collapse = ','),")",sep="")

	sqlQuery

	hpv_table = query_exec(sqlQuery,project = my_cloud_project)

	dim(hpv_table)

	head(hpv_table)

	# We can do some quality control ...
	# Assert that if hpv_calls is NA, hpv_status is Negative
	stopifnot((is.na(hpv_table$hpv_calls) && hpv_table$hpv_status=="Negative") || !is.na(hpv_table$hpv_calls))

	# Let's explore the cohort
	ggplot(data=hpv_table, aes(x=hpv_status, fill=Study)) + geom_bar(stat="count", position=position_dodge())

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
	  [isb-cgc-04-0030:workspace.ncomms3513_s3]
	WHERE
	  Cancer IN ('CESC','HNSC')
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
	  Study,
	  HGNC_gene_symbol,
	  AVG(normalized_count) as mean_expression
	FROM
	  [isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM]
	WHERE
	  Study IN ('CESC','HNSC')
	  AND SampleTypeLetterCode = 'TP'
	  AND HGNC_gene_symbol IN (
	    SELECT
	      Overlapping_genes AS HGNC_gene_symbol
	    FROM
	      [isb-cgc-04-0030:workspace.ncomms3513_s3]
	    WHERE
	      Cancer IN ('CESC','HNSC')
	      AND Overlapping_genes <> 'Intergenic'
	    GROUP BY
	      HGNC_gene_symbol )
	GROUP BY
	  Study,
	  HGNC_gene_symbol
	ORDER BY
	  mean_expression"

	# running the query.
	mean_affected_genes = query_exec(query, project = my_cloud_project)

	# we'll create some more meaningful x-axis labels
	mean_affected_genes$xlabel <- paste0(mean_affected_genes$Study, "_", mean_affected_genes$HGNC_gene_symbol)

	# Now we can visualize it.
	qplot(data=mean_affected_genes,
	      x=factor(x = xlabel, ordered = T, levels = xlabel),
	      y=mean_expression,
	      col=Study) +
	      theme(axis.text.x = element_text(angle = 90, hjust = 1, size=4)) +
	      xlab("Study_Gene")


Computing Statistics
====================

Instead, if we want to get the actual gene expression values, we could query
for that, and retrieve it as a data.frame.

.. code-block:: r

	sqlQuery = "
	SELECT
	  ParticipantBarcode,
	  SampleBarcode,
	  Study,
	  HGNC_gene_symbol,
	  normalized_count
	FROM
	  [isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM]
	WHERE
	  Study IN ('CESC','HNSC')
	  AND SampleTypeLetterCode = 'TP'
	  AND HGNC_gene_symbol IN (
	  SELECT
	    Overlapping_genes as HGNC_gene_symbol
	  FROM
	    [your-project-id:workspace.ncomms3513_s3]
	  WHERE
	    Cancer IN ('CESC','HNSC')
	    AND Overlapping_genes <> 'Intergenic'
	  GROUP BY
	    HGNC_gene_symbol )
		"

	gexp_affected_genes = query_exec(sqlQuery,project = my_cloud_project)

	#view results
	head(gexp_affected_genes)

	# a couple different ways to look at the results
	#qplot(data=gexp_affected_genes, x=Study, y=normalized_count, col=HGNC_gene_symbol, geom="boxplot")
	#qplot(data=gexp_affected_genes, x=Study, y=log2(normalized_count), col=HGNC_gene_symbol, geom="boxplot")
	qplot(data=gexp_affected_genes, x=log2(normalized_count+1), col=HGNC_gene_symbol, geom="density") + facet_wrap(~ Study)

Not all the samples listed in the clinical data have gene expression data, however.
Let's filter the hpv_table to match the samples to those in gexp_affected_genes

.. code-block:: r

	require(tidyr,quietly = TRUE) || install.packages('tidyr',verbose = FALSE)
	require(dplyr,quietly = TRUE) || install.packages('dplyr',verbose = FALSE)
	require(broom,quietly = TRUE) || install.packages('broom',verbose = FALSE)

	# let's get rid of 'indeterminate' samples
	hpv_table = dplyr::filter(hpv_table, hpv_status != "Indeterminate", ParticipantBarcode %in% gexp_affected_genes$ParticipantBarcode)

T-tests
=======

Now, we are going to perform t.tests on expression by hpv_status and study.

.. code-block:: r

	gxps <- merge(x=gexp_affected_genes, y=hpv_table, by=c("Study","ParticipantBarcode"))

	# Performing a t-test between hpv+ and hpv- by study and gene
	res0 <- gxps %>%
	group_by(Study, HGNC_gene_symbol) %>%
	do(tidy(t.test(log2(normalized_count+1) ~ hpv_status, data=.))) %>%
	ungroup() %>%
	arrange(desc(statistic))

	# These are the top 5 results ...
	top5 <- select(top_n(res0, 5, statistic), Study, HGNC_gene_symbol)

	# Let's subset the data by the top 5 results...
	res1 <- merge(x=top5, y=gxps) %>% mutate( Study_Gene = paste0(Study, "_", HGNC_gene_symbol))

	# now we can plot the results...
	ggplot(res1, aes(x=Study_Gene, y=log2(normalized_count+1), fill=hpv_status)) + geom_boxplot()


Making BigQueries
=================

Previously, we downloaded data and performed some work on it. But another way to work
is to compute  as much as possible in the cloud, and use R to visualize summary results.

Please see: https://cloud.google.com/bigquery/query-reference

.. code-block:: r

	sqlQuery = "
	SELECT
	  ParticipantBarcode,
	  SampleBarcode,
	  Study,
	  HGNC_gene_symbol,
	  normalized_count
	FROM
	  [isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM]
	WHERE
	  Study = 'CESC'
	  AND SampleTypeLetterCode = 'TP'
	  AND ParticipantBarcode IN (
	  SELECT
	    ParticipantBarcode
	  FROM
	    [isb-cgc:tcga_201510_alpha.Clinical_data]
	  WHERE
	    hpv_status = 'Positive' )
	  AND HGNC_gene_symbol IN (
	  SELECT
	    Overlapping_genes AS HGNC_gene_symbol
	  FROM
	    [isb-cgc-04-0002:testVarsha.ncomms3513_s3]
	  WHERE
	    Cancer = 'CESC'
	    AND Overlapping_genes <> 'Intergenic'
	  GROUP BY
	    HGNC_gene_symbol )
	"

	q1 = query_exec(sqlQuery,project = cloud_project_workshop)

	dim(q1)

Now lets make a small change, and get gene expression for subjects that are hpv negative.

.. code-block:: r

	sqlQuery = "
	SELECT
	  ParticipantBarcode,
	  SampleBarcode,
	  Study,
	  HGNC_gene_symbol,
	  normalized_count
	FROM
	  [isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM]
	WHERE
	  Study = 'CESC'
	  AND SampleTypeLetterCode = 'TP'
	  AND ParticipantBarcode IN (
	  SELECT
	    ParticipantBarcode
	  FROM
	    [isb-cgc:tcga_201510_alpha.Clinical_data]
	  WHERE
	    hpv_status = 'Negative' )
	  AND HGNC_gene_symbol IN (
	  SELECT
	    Overlapping_genes AS HGNC_gene_symbol
	  FROM
	    [isb-cgc-04-0030:workspace.ncomms3513_s3]
	  WHERE
	    Cancer = 'CESC'
	    AND Overlapping_genes <> 'Intergenic'
	  GROUP BY
	    HGNC_gene_symbol )
	"

	q2 <- query_exec(sqlQuery,project = cloud_project_workshop)

	dim(q2)

Now we merge the previous two queries, and compute T statistics using
BigQuery built in functions, SQRT, MEAN, STDDEV, POW, COUNT, and LOG2.

Please see: https://cloud.google.com/bigquery/query-reference

.. code-block:: r

	q <- "
	SELECT
	  p.HGNC_gene_symbol AS gene,
	  p.study AS study,
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
	    Study,
	    HGNC_gene_symbol,
	    AVG(LOG2(normalized_count+1)) AS y,
	    POW(STDDEV(LOG2(normalized_count+1)),2) AS sy2,
	    COUNT(ParticipantBarcode) AS ny
	  FROM
	    [isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM]
	  WHERE
	    Study = 'CESC'
	    AND SampleTypeLetterCode = 'TP'
	    AND ParticipantBarcode IN (

		# selecting the patients... could also previously put this in a table
	    SELECT
	      ParticipantBarcode
	    FROM
	      [isb-cgc:tcga_201510_alpha.Clinical_data]
	    WHERE
	      hpv_status = 'Positive' )
	    AND HGNC_gene_symbol IN (

		# the list of associated genes
	    SELECT
	      Overlapping_genes AS HGNC_gene_symbol
	    FROM
	      [isb-cgc-04-0030:workspace.ncomms3513_s3]
	    WHERE
	      Overlapping_genes <> 'Intergenic'
	    GROUP BY
	      HGNC_gene_symbol )
	  GROUP BY
	    Study,
	    HGNC_gene_symbol) AS o

	JOIN (

	  # Then we get the gene expression summaries from hpv-
	  SELECT
	    Study,
	    HGNC_gene_symbol,
	    AVG(LOG2(normalized_count+1)) AS x,
	    POW(STDDEV(LOG2(normalized_count+1)),2) AS sx2,
	    COUNT(ParticipantBarcode) AS nx
	  FROM
	    [isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM]
	  WHERE
	    Study = 'CESC'
	    AND SampleTypeLetterCode = 'TP'
	    AND ParticipantBarcode IN (
	    SELECT
	      ParticipantBarcode
	    FROM
	      [isb-cgc:tcga_201510_alpha.Clinical_data]
	    WHERE
	      hpv_status = 'Negative' )
	    AND HGNC_gene_symbol IN (

		# the list of associated genes
	    SELECT
	      Overlapping_genes AS HGNC_gene_symbol
	    FROM
	      [isb-cgc-04-0030:workspace.ncomms3513_s3]
	    WHERE
	      Overlapping_genes <> 'Intergenic'
	    GROUP BY
	      HGNC_gene_symbol )
	  GROUP BY
	    Study,
	    HGNC_gene_symbol) AS p
	ON
	  p.HGNC_gene_symbol = o.HGNC_gene_symbol
	  AND p.Study = o.Study
	GROUP BY
	  gene,
	  Study,
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

	gexp_fm = tidyr::spread(gexp_affected_genes,HGNC_gene_symbol,normalized_count)

	gexp_fm[1:5,1:5]
