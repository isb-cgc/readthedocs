*****************
GENIE Data Set
*****************

About the AACR Project Genomics Evidence Neoplasia Information Exchange
------------------------------------------------------------------------

The `AACR Project Genomics Evidence Neoplasia Information Exchange <https://gdc.cancer.gov/about-gdc/contributed-genomic-data-cancer-research/genie>`_ contains data generated from an international pan-cancer registry to serve as an evidence base for the entire cancer community. Genomic and baseline clinical data from more than 40,000 tumors has been made available in the GDC, following the efforts of AACR’s strategic and technical partners, Sage Bionetworks and Memorial Sloan Kettering Cancer Center. 

About the AACR Project Genomics Evidence Neoplasia Information Exchange Data
---------------------------------------------------------------------------------

The GENIE data set includes masked annotations, somatic mutations, gene level copy number scores, and transcript fusion analysis. The program analyzed more than 44,000 cases. The Genomic Data Commons (GDC) currently has MAF, TXT, and TSV controlled data available. 

For more information on GENIE data, please refer to the site below:

- `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22projects.program.name%22%2C%22value%22%3A%5B%22GENIE%22%5D%7D%7D%5D%7D>`_

Accessing the AACR Project Genomics Evidence Neoplasia Information Exchange Data on the Cloud
-------------------------------------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the GENIE files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'GENIE'
  AND active.file_gdc_id = GCSurl.file_gdc_id
  
Accessing the GENIE Data in Google BigQuery
------------------------------------------------

ISB-CGC has GENIE data, such as clinical, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with GENIE selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The GENIE tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.GENIE`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.GENIE_versioned`` contains previously released tables, as well as the most current table.
