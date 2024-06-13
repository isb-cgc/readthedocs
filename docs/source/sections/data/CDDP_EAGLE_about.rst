*****************
CDDP EAGLE Data Set
*****************

About the CDDP Environment And Genetics in Lung cancer Etiology (EAGLE) Program
------------------------------------------------------------
The `Environment And Genetics in Lung cancer Etiology <https://dceg.cancer.gov/research/who-we-study/cancer-cases-controls/eagle-study>`_ (EAGLE) program investigated the genetic and environmental determinants of lung cancer and smoking persistence. It integrated analysis of genetic, environmental, clinical, and behavioral data.

About the CDDP EAGLE Data Set
---------------------------------------------------------------------
Data from the CDDP EAGLE Program are available at the `Genomics Data Commons (GDC) <https://portal.gdc.cancer.gov/>`_.  It includes data from the Integrative Analysis of Lung Adenocarcinoma project.

Accessing the CDDP EAGLE Data on the Cloud
-------------------------------------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the CDDP EAGLE files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'CDDP_EAGLE'
  AND active.file_gdc_id = GCSurl.file_gdc_id


Accessing the CDDP EAGLE Data in Google BigQuery
------------------------------------------------

ISB-CGC has CDDP EAGLE data, such as clinical and metadata, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://bq-search.isb-cgc.org/>`_ with CDDP EAGLE selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The CDDP_EAGLE tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.CDDP_EAGLE`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.CDDP_EAGLE_versioned`` contains previously released tables, as well as the most current table.
