*****************
TRIO Data Set
*****************

About Translational Research in Oncology
------------------------------------------------------------------------

The `Translational Research in Oncology <https://www.trioncology.org/>`_ contains data generated from an international pan-cancer registry to serve as an evidence base for the entire cancer community. Genomic and baseline clinical data from more than 40,000 tumors has been made available in the GDC, following the efforts of AACR’s strategic and technical partners, Sage Bionetworks and Memorial Sloan Kettering Cancer Center. 

About the Translational Research in Oncology Data
---------------------------------------------------------------------------------

The TRIO data set includes whole genome sequencing (WGS) sequencing reads for 339 cases in the project TRIO-CRU.

For more information on TRIO data, please refer to the site below:

- `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22projects.program.name%22%2C%22value%22%3A%5B%22TRIO%22%5D%7D%7D%5D%7D>`_

Accessing the TRIO Data on the Cloud
-------------------------------------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the TRIO files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'TRIO'
  AND active.file_gdc_id = GCSurl.file_gdc_id
  
Accessing the TRIO Data in Google BigQuery
------------------------------------------------

ISB-CGC has TRIO data, such as clinical and metadata, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with TRIO selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The TRIO tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.TRIO`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.TRIO_versioned`` contains previously released tables, as well as the most current table.
