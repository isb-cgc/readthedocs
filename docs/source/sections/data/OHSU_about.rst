*************
OHSU Data Set
*************

About the Oregon Health & Science University
--------------------------------------------

The `Oregon Health & Science University <https://www.ohsu.edu/>`_ contains data generated from Chronic neutrophilic leukemia (CNL), atypical chronic myeloid leukemia (aCML), and unclassified myelodysplastic syndrome/myeloproliferative neoplasms (MDS/MPN-U) are a group of rare, heterogeneous myeloid disorders. 

About the Oregon Health & Science University Data
-------------------------------------------------

Whole-exome and RNA sequencing on a cohort of over 100 cases of these rare hematologic malignancies and present the complete survey of the genomic landscape of these diseases to date. The project identification in the GDC Data Portal is `OHSU-CNL <https://portal.gdc.cancer.gov/projects/OHSU-CNL>`_. 

For more information on the OHSU data, please refer to these sites:

- `dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001799.v1.p1>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22OHSU%22%5D%7D%7D%5D%7D&searchTableTab=files>`_

Accessing OHSU Data on the Cloud
--------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc.GDC_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the OHSU files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc.GDC_metadata.rel22_fileData_active` as active, `isb-cgc.GDC_metadata.rel22_GDCfileID_to_GCSurl` as GCSurl
  WHERE program_name = 'OHSU'
  AND active.file_gdc_id = GCSurl.file_gdc_id
  
