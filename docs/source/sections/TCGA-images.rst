****************************************
TCGA Radiology and Pathology Image Data
****************************************

The TCGA images from `The Cancer Imaging Archive <http://www.cancerimagingarchive.net/>`_ (TCIA)
as well as the pathology and diagnostic images previously available from the
`Cancer Digital Slide Archive <http://cancer.digitalslidearchive.net/>`_ (CDSA)
are all now available in the ISB-CGC open-access Google Cloud Storage (GCS) bucket,
`gs://isb-cgc-open/ <https://console.cloud.google.com/storage/browser/isb-cgc-open/>`_.

Metadata for these files can be found in BigQuery, in the ISB-CGC metadata 
`dataset <https://bigquery.cloud.google.com/dataset/isb-cgc:metadata>`_.

Radiology Images
################

Over 1.4 million radiology image files in 
`DICOM <https://en.wikipedia.org/wiki/DICOM>`_ format,
grouped together into over 20,000 zip files are available in Google Cloud Storage (GCS).
Each zip file may contain hundreds of images, or just a single image.

The BigQuery metadata table, ``isb-cgc.metadata.TCGA_radiology_images`` contains
the full urls to these zip files, and the unzipped files can be found in folders of the same name, *eg*:

.. code-block:: none

   gs://isb-cgc-open/TCIA/images/TCGA-GBM/TCGA-06-5413/TCIA.image.1.3.6.1.4.1.14519.5.2.1.4591.4001.275342915307453440215680715165.zip 
   gs://isb-cgc-open/TCIA/images/TCGA-GBM/TCGA-06-5413/TCIA.image.1.3.6.1.4.1.14519.5.2.1.4591.4001.275342915307453440215680715165/*.dcm

The metadata table also includes the patient identifier in TCGA "barcode" format,
*eg* TCGA-06-5413 (which is also part of the GCS url).  Other information available in the
table includes the body part examined, image modality, patient age, etc.

**UPDATE:** The TCIA images have been moved to a new bucket: ``gs://isb-tcia-open/`` and the individual ``*.dcm`` images have been removed.

Pathology Images
################

Over 30,000 TCGA tissue slide images in 
`SVS <http://openslide.org/formats/aperio/>`_ format, are also available in GCS.  
These files were uploaded from the 
`NCI-GDC legacy archive <https://gdc-portal.nci.nih.gov/legacy-archive/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22files.data_format%22,%22value%22:%5B%22SVS%22%5D%7D%7D%5D%7D>`_.

The BigQuery metadata table, ``isb-cgc.metadata.TCGA_slide_images`` contains 
the full urls to these SVS files, *eg* 
``gs://isb-cgc-open/NCI-GDC/legacy/TCGA/TCGA-GBM/Other/Diagnostic_image/208fa2ac-69a8-4851-b13e-1f000872bf7f/TCGA-06-5413-01Z-00-DX1.6c5e8a47-c2d0-4873-9b32-36857c5f67ac.svs``, 
as well as the TCGA case and sample "barcode" which can be used to join this table
with other TCGA clinical, biospecimen and molecular data tables.

