***************
NCICCR Data Set
***************

About the NCI Center for Cancer Research
-----------------------------------------

The `NCI Center for Cancer Research <https://ccr.cancer.gov/>`_ (NCICCR) conducted a study on the Genomic Variation in Diffuse Large B Cell Lymphomas (DLBCL) through an integrative analysis of genetic lesions in 574 diffuse large B cell lymphomas (DLBCL). The study investigated genomic structural variation, genetic alteration, and its effect on the development and biology of lymphomas by using high throughput sequencing, gene expression, and methylation status.

About the NCI Center for Cancer Research Data
---------------------------------------------

There were around 489 cases that were phenotyped, contributing Authorized-Access, individual-level data. The Genomic Data Commons currently has around 957 controlled access BAM files available. The Project ID in the GDC Data Portal is `NCICCR-DLBCL <https://portal.gdc.cancer.gov/projects/NCICCR-DLBCL>`_.

For more information on the NCICCR data, please refer to these sites:

- `dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001444.v2.p1>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22NCICCR%22%5D%7D%7D%5D%7D>`_

Accessing the NCI Center for Cancer Research Data on the Cloud
---------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the NCICCR files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'NCICCR'
  AND active.file_gdc_id = GCSurl.file_gdc_id

Accessing the NCICCR Data in Google BigQuery
------------------------------------------------

ISB-CGC has NCICCR data, such as clinical, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with NCICCR selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The NCICCR tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.NCICCR`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.NCICCR_versioned`` contains previously released tables, as well as the most current table.
