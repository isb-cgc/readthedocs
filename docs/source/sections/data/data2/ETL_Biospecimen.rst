Biospecimen
===========

The 
`Biospecimen_data <https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Biospecimen_data>`_ 
table contains one row per TCGA sample.  Each TCGA sample is
uniquely represented by a 
`TCGA barcode <https://wiki.nci.nih.gov/display/TCGA/TCGA+barcode>`_
of length 16, *eg* ``TCGA-2G-AAM4-10A``.  (For more information on how TCGA barcodes
were created and how to *"read"* a TCGA barcode, click on the preceding link.)

XML Parsing
-----------

The TCGA data at the DCC exists in XML files which have been uploaded into
Google Cloud Storage.
Selected fields from these XML files
were then extracted and loaded into the “Biospecimen_data” table in BigQuery.

Some of the biospecimen values in the XML files are available on a per-slide
and/or per-portion basis, and these have been aggregated and averaged.
The number of slides and the number of portions per sample is also included 
in the table.

Filters
-------

-  Samples for which ``is\_ffpe=True`` were removed.
-  Patients or Samples for which ``Project`` value was *not* ``TCGA`` were removed.

Transforms
----------

-  ``pregnancies`` and ``total_number_of_pregnancies`` were merged into a
   single ``pregnancies`` field. Counts above four are represented as
   ``4+`` (e.g: [0,1,2,3,4+])
-  ``number\_of\_lymphnodes\_examined`` and ``lymph\_node\_examined\_count`` were
   merged into a single ``number\_of\_lymphnodes\_examined`` field


