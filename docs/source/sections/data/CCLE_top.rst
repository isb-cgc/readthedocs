*************
CCLE Data Set
*************

About the Cancer Cell Line Encyclopedia
-----------------------------------------

The `Cancer Cell Line Encyclopedia <https://depmap.org/portal/ccle/>`_ (CCLE) project is an effort to conduct a detailed genetic characterization of a large panel of human cancer cell lines. The CCLE provides public access analysis and visualization of DNA copy number, mRNA expression, mutation data and more, for 1000 cancer cell lines. 

About the Cancer Cell Line Encyclopedia Data
--------------------------------------------

The CCLE aligned reads (BAM files) are currently available in an open-access Cloud Storage bucket which you can browse `here <https://console.cloud.google.com/storage/browser/gdc-ccle-open/>`_.

A set of BigQuery tables containing CCLE data are available in the ``isb-cgc.CCLE_bioclin_v0`` `data set <https://console.cloud.google.com/bigquery?p=isb-cgc&d=CCLE_bioclin_v0&page=dataset>`_. This data has been updated and reformatted from the original data set ``isb-cgc.ccle_201602_alpha`` `data set <https://console.cloud.google.com/bigquery?p=isb-cgc&d=ccle_201602_alpha&page=dataset>`_ to look more like the newer TCGA and TARGET datasets, to optimize usage in the cancer research community.

Accessing the Cancer Cell Line Encyclopedia Data on the Cloud
---------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc.GDC_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the CCLE files. Here is an example:

.. code-block:: sql

  SELECT legacy.*, file_gdc_url
  FROM `isb-cgc.GDC_metadata.rel22_fileData_legacy` as legacy, `isb-cgc.GDC_metadata.rel22_GDCfileID_to_GCSurl` as GCSurl
  WHERE program_name = 'CCLE'
  AND legacy.file_gdc_id = GCSurl.file_gdc_id
