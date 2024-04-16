*****************
Exceptional Responders Data Set
*****************

About Exceptional Responders
------------------------------------------------------------------------

The Exceptional Responders Initiative is a pilot study to investigate the underlying molecular factors driving exceptional treatment responses of cancer patients to drug therapies. 

About Exceptional Responders Data
---------------------------------------------------------------------------------

Exceptional Responders has one project EXCEPTIONAL_RESPONDERS-ER with 84 cases spanning nine disease types and 20 primary sites. Data categories include sequencing reads, transcriptome profiling and simple nucleotide variation.

For more information on Exceptional Responders data, please refer to the site below:

- `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22projects.program.name%22%2C%22value%22%3A%5B%22EXCEPTIONAL_RESPONDERS%22%5D%7D%7D%5D%7D>`_

Accessing the Exceptional Responders Data on the Cloud
-------------------------------------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the Exceptional Responders files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'EXCEPTIONAL_RESPONDERS'
  AND active.file_gdc_id = GCSurl.file_gdc_id


Accessing the Exceptional Responders Data in Google BigQuery
------------------------------------------------

ISB-CGC has Exceptional Responders data, such as clinical, metadata, RNA-seq and somatic mutation stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://bq-search.isb-cgc.org/>`_ with EXCEPTIONAL RESPONDERS selected for filter PROGRAM. 
To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The Exceptional Responders tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.EXC_RESPONDERS`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.EXC_RESPONDERS_versioned`` contains previously released tables, as well as the most current table.
