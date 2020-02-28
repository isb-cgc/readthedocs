***************
NCICCR Data Set
***************

About the NCI Center for Cancer Research
-----------------------------------------

The `NCI Center for Cancer Research <https://ccr.cancer.gov/>`_ (NCICCR) conducted a study on the Genomic Variation in Diffuse Large B Cell Lymphomas (DLBCL) through an integrative analysis of genetic lesions in 574 diffuse large B cell lymphomas (DLBCL). The study investigated genomic structural variation, genetic alteration, and its effect on the development and biology of lymphomas by using high throughput sequencing, gene expression, and methylation status.

About the NCI Center for Cancer Research Data
---------------------------------------------

There were around 489 cases that were phenotyped contributing Authorized-Access, individual-level data. The Genomic Data Commons currently has around 957 controlled access BAM files available. The project identification in the GDC is `NCICCR-DLBCL <https://portal.gdc.cancer.gov/projects/NCICCR-DLBCL>`_.

For more information on the NCICCR data, please refer to these sites:

- `dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001444.v1.p1>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22NCICCR%22%5D%7D%7D%5D%7D>`_

Accessing NCICCR Data on the Cloud
--------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc.GDC_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the NCICCR files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc.GDC_metadata.rel22_fileData_active` as active, `isb-cgc.GDC_metadata.rel22_GDCfileID_to_GCSurl` as GCSurl
  WHERE program_name = 'NCICCR'
  AND active.file_gdc_id = GCSurl.file_gdc_id
