*****************
ORGANOID Data Set
*****************

About the Pancreas Cancer Organoid Profiling Program
---------------

The Pancreas Cancer Organoid Profiling Program is from the `Organoid Profiling Identifies Common Responders to Chemotherapy in Pancreatic Cancer <https://pubmed.ncbi.nlm.nih.gov/29853643-organoid-profiling-identifies-common-responders-to-chemotherapy-in-pancreatic-cancer/>`_ study and contains data generated from a collection of patient-derived pancreatic normal and cancer organoids. 

About the Pancreas Cancer Organoid Profiling Data Set
--------------------

The data set consists of 70 cases and includes whole-genome, targeted exome, and RNA sequencing data on organoids as well as matched tumor and normal tissues. This dataset is a valuable resource for pancreas cancer researchers, and those looking to compare primary tissue to organoid culture. The NCI GDC houses all the clinical, biospecimen, and molecular characterization data with over 130 VCF, 298 BAM, 165 TXT, and 110 TSV files in around 21.89 TB of data.  The project identification in the GDC Data Portal is `ORGANOID-PANCREATIC <https://portal.gdc.cancer.gov/projects/ORGANOID-PANCREATIC>`_.

For more information on the ORGANOID data, please refer to these sites:

- `dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001611.v1.p1>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22ORGANOID%22%5D%7D%7D%5D%7D>`_

Accessing Pancreas Cancer Organoid Profiling Data on the Cloud
--------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc.GDC_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the ORGANOID files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc.GDC_metadata.rel22_fileData_active` as active, `isb-cgc.GDC_metadata.rel22_GDCfileID_to_GCSurl` as GCSurl
  WHERE program_name = 'ORGANOID'
  AND active.file_gdc_id = GCSurl.file_gdc_id
 
