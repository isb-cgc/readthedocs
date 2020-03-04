**************
WCDT Data Set
**************

About the Genomic Characterization of Metastatic Castration Resistant Prostate Cancer
---------------

The overarching goal of the Genomic Characterization of Metastatic Castration-Resistant Prostate Cancer study is to illuminate molecular mechanisms of acquired resistance to therapeutic agents, and particularly androgen signaling inhibitors, in the treatment of metastatic castration-resistant prostate cancer (mCRPC).

About the Genomic Characterization of Metastatic Castration Resistant Prostate Cancer Data
--------------------

WCDT data is available from the biopsies of castration-resistant prostate cancer metastases collected during the study. The data consists of 101 cases with over 202 whole-genome sequencing files and 792 RNA sequencing files consisting of 83TB of data. The project identification in the GDC Data Portal is `WCDT-MCRPC <https://portal.gdc.cancer.gov/projects/WCDT-MCRPC>`_.

For more information on the HCMI data, please refer to these sites:

- `dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001486.v2.p2>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22WCDT%22%5D%7D%7D%5D%7D>`_

Accessing Genomic Characterization of Metastatic Castration Resistant Prostate Cancer Data on the Cloud
--------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc.GDC_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the WCDT files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc.GDC_metadata.rel22_fileData_active` as active, `isb-cgc.GDC_metadata.rel22_GDCfileID_to_GCSurl` as GCSurl
  WHERE program_name = 'WCDT'
  AND active.file_gdc_id = GCSurl.file_gdc_id
