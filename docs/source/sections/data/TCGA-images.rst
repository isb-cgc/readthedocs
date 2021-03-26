****************************************
TCGA Radiology and Pathology Image Data Set
****************************************

The TCGA images from `The Cancer Imaging Archive <http://www.cancerimagingarchive.net/>`_ (TCIA) as well as the pathology and diagnostic images previously available from the `Cancer Digital Slide Archive <http://cancer.digitalslidearchive.net/>`_ (CDSA) are available in open-access Google Cloud Storage (GCS) buckets and can be explored through the ISB-CGC Web App.

Metadata for these files can be found in ISB-CGC Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with TCGA selected for filter PROGRAM and FILE METADATA selected for filter CATEGORY. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

Radiology Images
################

Over 1.4 million radiology image files in `DICOM <https://en.wikipedia.org/wiki/DICOM>`_ format, grouped together into over 20,000 ZIP files are available in a GCS bucket called `gs://isb-tcia-open/ <https://console.cloud.google.com/storage/browser/isb-tcia-open/>`_. Each ZIP file may contain hundreds of images or just a single image.

The BigQuery metadata table, ``isb-cgc-bq.TCGA.radiology_images_tcia_current`` contains the full URLs to these ZIP files, *e.g.*:

.. code-block:: none

  gs://isb-tcia-open/images/TCGA-GBM/TCGA-06-5413/TCIA.image.1.3.6.1.4.1.14519.5.2.1.4591.4001.275342915307453440215680715165.zip

The metadata table also includes the patient identifier in TCGA "barcode" format, *e.g.* TCGA-06-5413 (which is also part of the GCS URL).  Other information available in the table includes the body part examined, image modality, patient age, etc.

Pathology Images
################

Over 30,000 TCGA tissue slide images in `SVS <http://openslide.org/formats/aperio/>`_ format, are also available in GCS, in the open-access bucket `gs://gdc-tcga-phs000178-open/ <https://console.cloud.google.com/storage/browser/gdc-tcga-phs000178-open/>`_.

These files were uploaded from the `GDC legacy archive <https://portal.gdc.cancer.gov/legacy-archive/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22files.data_format%22,%22value%22:%5B%22SVS%22%5D%7D%7D%5D%7D>`_.

The BigQuery metadata table, ``isb-cgc-bq.TCGA.slide_images_gdc_current`` contains the full URLs to these SVS files, *e.g.*: 

.. code-block:: none

  gs://gdc-tcga-phs000178-open/9c4b1b5c-b5cf-48f6-bf41-047ceb8c883c/TCGA-CR-7365-01A-01-TS1.811bb2b7-66e3-4694-891b-10b436ec300d.svs

as well as image metadata and the TCGA case and sample "barcode" which can be used to join this table with other TCGA clinical, biospecimen and molecular data tables.
