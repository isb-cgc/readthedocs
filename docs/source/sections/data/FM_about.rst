**************************************************
FM Data Set
**************************************************

About the Foundation Medicine
------------------------------

The `Foundation Medicine Adult Cancer Clinical Data Set <https://gdc.cancer.gov/about-gdc/contributed-genomic-data-cancer-research/foundation-medicine/foundation-medicine>`_ (FM) was a study conducted by Foundation Medicine Inc. (FMI), which is a molecular information company that specializes in precision medicine. FMI has generated genomic profiles for thousands of cancer patients, which they designed to match each patient with a personalized treatment plan.

About the Foundation Medicine Data
------------------------------------

FM data set consists of more than 18,000 unique solid tumor samples that underwent genomic profiling on a single uniform platform as part of standard clinical care. The data set is derived from the FoundationOne® genomic profiling assay version 2 that interrogates exonic regions of 287 cancer-related genes and selected introns from 19 genes known to undergo rearrangements in human cancer. The Genomic Data Commons (GDC) currently has VCF, TSV, and MAF data available. There are more than 36,008 VCF files, 84 TSV files, and 42 MAF files available with, 36,050 of them that are Controlled Access and 84 files, which are Open Access. The project identification in the GDC Data Portal is `FM-AD <https://portal.gdc.cancer.gov/projects/FM-AD>`_.

For more information on the FM data, please refer to these sites:

- `dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001179.v1.p1>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22FM%22%5D%7D%7D%5D%7D&searchTableTab=files>`_


Accessing the Foundation Medicine Data on the Cloud
----------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the FM files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'FM'
  AND active.file_gdc_id = GCSurl.file_gdc_id

Accessing the FM Data in Google BigQuery
------------------------------------------------

ISB-CGC has FM data, such as clinical, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with FM selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The FM tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.FM`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.FM_versioned`` contains previously released tables, as well as the most current table.
