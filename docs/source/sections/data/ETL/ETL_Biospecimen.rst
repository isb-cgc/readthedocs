Biospecimen
===========

The 
`Biospecimen <https://console.cloud.google.com/bigquery?p=isb-cgc&d=TCGA_bioclin_v0&t=Biospecimen&page=table>`_ 
table contains one row per TCGA sample.  Each TCGA sample is
uniquely represented by a 
`TCGA barcode <https://docs.gdc.cancer.gov/Encyclopedia/pages/TCGA_Barcode/>`_
of length 16, *eg* ``TCGA-2G-AAM4-10A``.  (For more information on how TCGA barcodes
were created and how to *"read"* a TCGA barcode, click on the preceding link.)

XML Parsing
-----------

The TCGA data at the DCC exists in XML files which have been uploaded into
Google Cloud Storage.
Selected fields from these XML files
were then extracted and loaded into the "Biospecimen" table in BigQuery.

Some of the biospecimen values in the XML files are available on a per-slide
and/or per-portion basis, and these have been aggregated and averaged.
The number of slides and the number of portions per sample is also included 
in the table.

Filters
-------

-  Samples for which ``is\_ffpe=True`` were removed.
-  Patients or Samples for which ``Project`` value was *not* ``TCGA`` were removed.

The following fields were extracted from the ssf XML file: 

- ``days\_to\_sample\_procurement``
- ``tissue\_anatomic\_site``
- ``tissue\_anatomic\_site\_description``
- ``tissue\_anatomic\_site``
