*****************
CPTAC Data Set
*****************

About the NCI Clinical Proteomic Tumor Analysis Consortium
------------------------------------------------------------
The `National Cancer Institute’s Clinical Proteomic Tumor Analysis Consortium <https://proteomics.cancer.gov/programs/cptac>`_ (CPTAC) is a national effort to accelerate the understanding of the molecular basis of cancer through the application of large-scale proteome and genome analysis or proteogenomics.

About the NCI Clinical Proteomic Tumor Analysis Consortium Data Set
---------------------------------------------------------------------

CPTAC data consists of whole-genome sequencing, whole-exome sequencing, RNA sequencing, and miRNA sequencing.  The program analyzed more than 700 cases. The Genomic Data Commons (GDC) currently has controlled VCF, TSV, and BAM data available. The Project ID in the GDC Data Portal is `CPTAC-2 <https://portal.gdc.cancer.gov/projects/CPTAC-2>`_ and `CPTAC-3 <https://portal.gdc.cancer.gov/projects/CPTAC-3>`_.


For more information on the CPTAC data, please refer to these sites:

- `CPTAC-2 dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000892>`_
- `CPTAC-3 dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001287.v5.p4>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D&searchTableTab=files>`_

Accessing the NCI Clinical Proteomic Tumor Analysis Consortium Data on the Cloud
----------------------------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc.GDC_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the CPTAC files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc.GDC_metadata.rel22_fileData_active` as active, `isb-cgc.GDC_metadata.rel22_GDCfileID_to_GCSurl` as GCSurl
  WHERE program_name = 'CPTAC'
  AND active.file_gdc_id = GCSurl.file_gdc_id
