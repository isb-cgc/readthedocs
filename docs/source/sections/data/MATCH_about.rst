*****************
MATCH Data Set
*****************

About the Molecular Analysis for Therapy Choice (MATCH) Program
------------------------------------------------------------
`Molecular Analysis for Therapy Choice <https://www.cancer.gov/about-cancer/treatment/clinical-trials/nci-supported/nci-match>`_ (MATCH) is a precision medicine cancer treatment clinical trial which investigated the effectiveness of treating cancer based on the specific genetic changes in a person's tumor.

About the Molecular Analysis for Therapy Choice Data Set
---------------------------------------------------------------------
Data from the MATCH Program are available at the `Genomics Data Commons (GDC) <https://portal.gdc.cancer.gov/>`_.  It includes data for over 15 primary sites and at least eight disease types.

Accessing the MATCH Data on the Cloud
-------------------------------------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the MATCH files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'MATCH'
  AND active.file_gdc_id = GCSurl.file_gdc_id


Accessing the MATCH Data in Google BigQuery
------------------------------------------------

ISB-CGC has MATCH data, such as clinical and metadata, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with MATCH selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The MATCH tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.MATCH`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.MATCH_versioned`` contains previously released tables, as well as the most current table.
