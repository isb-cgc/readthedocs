*************
CCLE Data Set
*************

About the Cancer Cell Line Encyclopedia
-----------------------------------------

The `Cancer Cell Line Encyclopedia <https://depmap.org/portal/ccle/>`_ (CCLE) project is an effort to conduct a detailed genetic characterization of a large panel of human cancer cell lines. The CCLE provides public access analysis and visualization of DNA copy number, mRNA expression, mutation data and more, for 1000 cancer cell lines. 

About the Cancer Cell Line Encyclopedia Data
--------------------------------------------

The CCLE aligned reads (BAM files) are currently available in an open-access Cloud Storage bucket which you can browse `here <https://console.cloud.google.com/storage/browser/gdc-ccle-open/>`_. CCLE data is also available in ISB-CGC Google BigQuery tables.

Accessing the Cancer Cell Line Encyclopedia Data on the Cloud
---------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the CCLE files. Here is an example:

.. code-block:: sql

  SELECT legacy.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_legacy_current` as legacy, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'CCLE'
  AND legacy.file_gdc_id = GCSurl.file_gdc_id

Accessing the CCLE Data in Google BigQuery
------------------------------------------------

ISB-CGC has CCLE data, such as clinical, biospecimen, copy number segment, RMA Expression and somatic mutation, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with CCLE selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The CCLE tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.CCLE`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.CCLE_versioned`` contains previously released tables, as well as the most current table.

Note that some of the tables in the isb-cgc-bq project were migrated from the isb-cgc project. If you were using data sets ``isb-cgc.ccle_201602_alpha``, ``isb-cgc.CCLE_bioclin_v0`` and ``isb-cgc.CCLE_hg19_data_v0``, they still exist but are deprecated.
