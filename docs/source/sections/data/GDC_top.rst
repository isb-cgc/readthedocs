*****************
NCI-GDC Overview
*****************

The `NCI's Genomic Data Commons <https://gdc.cancer.gov/>`_ 
(NCI-GDC) provides the cancer research community with a 
unified data repository that enables data sharing across cancer genomic studies in 
support of precision medicine.

The `GDC Data Portal <https://portal.gdc.cancer.gov/>`_ allows users to search for
and download data directly via your web browser or using the 
`GDC Data Transfer Tool <https://gdc.cancer.gov/access-data/gdc-data-transfer-tool>`_.
So-called "legacy" data that the NCI-GDC "inherited" from previous data coordinating
centers (*eg* the TCGA-DCC and CGHub), is available in the 
`Legacy Archive <https://portal.gdc.cancer.gov/legacy-archive/search/f>`_, while a 
`"harmonized" <https://gdc.cancer.gov/about-data/gdc-data-harmonization>`_ 
data set (re-aligned to GRCh38/hg38 and re-processed by the GDC) is available
at the main `Data Portal <https://portal.gdc.cancer.gov/>`_.

The ISB-CGC is hosting much of this data (both "legacy" and "harmonized" in
Google Cloud Storage (GCS), meaning that you may *not* need to download any
data from the GDC if you're planning on running your analyses on the Google
Cloud Platform.

In order to help users determine which data at the GDC is available on the
ISB-CGC platform, we have created a set of metadata tables in BigQuery
(based on `GDC Data Release 5.0 <https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/>`_)
in the `isb-cgc:GDC_metadata <https://bigquery.cloud.google.com/dataset/isb-cgc:GDC_metadata>`_ dataset:

- `rel5_caseData <https://bigquery.cloud.google.com/table/isb-cgc:GDC_metadata.rel5_caseData>`_:  contains a complete list of all
17268 cases
existing

- `rel5_current_fileData <https://bigquery.cloud.google.com/table/isb-cgc:GDC_metadata.rel5_current_fileData>`_:

- `rel5_legacy_fileData <https://bigquery.cloud.google.com/table/isb-cgc:GDC_metadata.rel5_legacy_fileData>`_:

- `rel5_aliquot2caseIDmap <https://bigquery.cloud.google.com/table/isb-cgc:GDC_metadata.rel5_aliquot2caseIDmap>`_:

- `rel5_slide2caseIDmap <https://bigquery.cloud.google.com/table/isb-cgc:GDC_metadata.rel5_slide2caseIDmap>`_:

- `GDCfileID_to_GCSurl <https://bigquery.cloud.google.com/table/isb-cgc:GDC_metadata.GDCfileID_to_GCSurl>`_:

