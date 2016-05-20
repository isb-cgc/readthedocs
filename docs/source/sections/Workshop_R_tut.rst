************************
ISB-CGC Workshops at NCI
************************

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
    require(tidyr,quietly = TRUE) || install.packages('tidyr',verbose = FALSE)
    require(dplyr,quietly = TRUE) || install.packages('dplyr',verbose = FALSE)
    require(ggplot2,quietly = TRUE) || install.packages('ggplot2',verbose = FALSE)
    require(broom,quietly = TRUE) || install.packages('broom',verbose = FALSE)


Your project ID
===============

You will be using your own project ID. At certain points in the code, it will
be necessary to complete the code.

.. code-block:: r

    main_cloud_project="isb-cgc"
    my_cloud_project  = "your_project_id"
    tcga_data_set     = "tcga_201510_alpha"

First query
===========

Now let's see if things are working.

.. code-block:: r

    bigrquery::list_tables(main_cloud_project, tcga_ds)

In this tutorial, we will be investigating two studies using two existing
Biq Query tables. Additionally, we're going to BYOD "Bring your own data".

.. code-block:: r

	study=c('CESC','HNSC')

	clinical_table = "[isb-cgc:tcga_201510_alpha.Clinical_data]"
	gexp_table     = "[isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM]"


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

	gsutil cp gs://isb-cgc-workshop/ncomms3513-s3.tsv .
	gsutil cp gs://isb-cgc-workshop/ncomms3513-s3_Schema.json .


Now the data is in our directory, but we need to transform it into a BQ table.
To do that, we need to create a data set in our project. We can do this from within the Big query
web UI by clicking on the little blue triangle next to your project ID on the left.
Or we can do this on the command line using the bq command line tool.

.. code-block:: none

	gcloud init

	bq help

	bq ls

	bq mk mydataset

	bq load --source_format CSV --field_delimiter "\t"  --schema ncomms3513-s3_Schema.json  mydataset.ncomms3513_s3 ncomms3513-s3.tsv

Now we can directly query our own data, and start to combine it with other tables.
