*****************
MP2PRT Data Set
*****************

About MP2PRT
------------------------------------------------------------------------

The Molecular Profiling to Predict Response to Treatment (MP2PRT) program is part of the NCI's Cancer Moonshot Initiative. This study "Identification of Genetic Changes Associated with Relapse and/or Adaptive Resistance in Patients Registered as Favorable Histology Wilms Tumor on AREN03B2" performs genomic characterization on trio cases (normal tissue, tumor tissue at time of diagnosis, tumor tissue at time of relapse) from patients who relapsed with Favorable Histology Wilms Tumor. 

About MP2PRT Data
---------------------------------------------------------------------------------

The MP2PRT data set includes one project MP2PRT-WT with 52 cases. Data categories include sequencing reads, transcriptome profiling, simple nucleotide variation and copy number variation.

For more information on MP2PRT data, please refer to the site below:

- `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22projects.program.name%22%2C%22value%22%3A%5B%22MP2PRT%22%5D%7D%7D%5D%7D>`_

Accessing the MP2PRT Data on the Cloud
-------------------------------------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the MP2PRT files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'MP2PRT'
  AND active.file_gdc_id = GCSurl.file_gdc_id


Accessing the MP2PRT Data in Google BigQuery
------------------------------------------------

ISB-CGC has MP2PRT data, such as clinical and metadata, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://bq-search.isb-cgc.org/>`_ with MP2PRT selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The MP2PRT tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.MP2PRT`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.MP2PRT_versioned`` contains previously released tables, as well as the most current table.
