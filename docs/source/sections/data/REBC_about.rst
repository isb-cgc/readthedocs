*****************
REBC Data Set
*****************

About REBC
------------------------------------------------------------------------

REBC studies comprehensive genomic characterization of radiation-related papillary thyroid cancer in the Ukraine after the 1986 Chernobyl nuclear power plan accident. This accident released radioactive contaminants into the surrounding areas in Ukraine, Belarus, and Russia, causing an increased occurrence of thyroid cancer among individuals who were children at the time of the accident or born not long afterwards.

About REBC
---------------------------------------------------------------------------------

The REBC data set includes one project REBC-THYR with 440 cases. Data categories include sequencing reads, transcriptome profiling, simple nucleotide variation and copy number variation.

For more information on REBC data, please refer to the site below:

- `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22projects.program.name%22%2C%22value%22%3A%5B%22REBC%22%5D%7D%7D%5D%7D>`_

Accessing the REBC Data on the Cloud
-------------------------------------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the REBC files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'REBC'
  AND active.file_gdc_id = GCSurl.file_gdc_id
  
Accessing the TRIO Data in Google BigQuery
------------------------------------------------

ISB-CGC has REBC data, such as clinical and metadata, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with REBC selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The REBC tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.REBC`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.REBC_versioned`` contains previously released tables, as well as the most current table.
