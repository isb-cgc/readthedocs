**************
WCDT Data Set
**************

About the Genomic Characterization of Metastatic Castration Resistant Prostate Cancer
---------------

The overarching goal of the Genomic Characterization of Metastatic Castration-Resistant Prostate Cancer study is to illuminate molecular mechanisms of acquired resistance to therapeutic agents, and particularly androgen signaling inhibitors, in the treatment of metastatic castration-resistant prostate cancer (mCRPC).

About the Genomic Characterization of Metastatic Castration Resistant Prostate Cancer Data
--------------------

West Coast Prostrate Cancer Dream Team (WCDT) data is available from the biopsies of castration-resistant prostate cancer metastases collected during the study. The data consists of 101 cases with over 202 whole-genome sequencing files and 792 RNA sequencing files consisting of 83TB of data. The Project ID in the GDC Data Portal is `WCDT-MCRPC <https://portal.gdc.cancer.gov/projects/WCDT-MCRPC>`_.

For more information on the WCDT data, please refer to these sites:

- `dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001648.v1.p1>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22WCDT%22%5D%7D%7D%5D%7D>`_

Accessing Genomic Characterization of Metastatic Castration Resistant Prostate Cancer Data on the Cloud
--------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the WCDT files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'WCDT'
  AND active.file_gdc_id = GCSurl.file_gdc_id

Accessing the WCDT Data in Google BigQuery
------------------------------------------------

ISB-CGC has WCDT data, such as clinical and RNA-seq, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with WCDT selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The WCDT tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.WCDT`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.WCDT_versioned`` contains previously released tables, as well as the most current table.
