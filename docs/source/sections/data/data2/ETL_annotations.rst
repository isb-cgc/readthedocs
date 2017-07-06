Annotations
===========

The TCGA Annotations BigQuery
`table <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_bioclin_v0.Annotations>`__
was created based on the contents of the JSON file obtained from the TCGA
Annotation manager `Web Service
API <https://wiki.nci.nih.gov/display/TCGA/TCGA+Annotations+Web+Service+User's+Guide>`__.
The deeply nested JSON file was first flattened, and then a subset of the 
fields were selected to be loaded into the BigQuery table.  In the flattening
process, sub-level field names were prefixed with the parent name, separated by
an underscore.  These names have now been updated to reflect their names in the Genome Data Commons (GDC) Annotations API.
Please refer directly to BigQuery for the table 
`schema <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_bioclin_v0.Annotations>`__

+------------------------------------------------------------------------------+----------------------------+
| Original field name                                                          | New field name             |
+==============================================================================+============================+
| annotationCategory\_annotationClassification\_annotationClassificationName   | classification             |
+------------------------------------------------------------------------------+----------------------------+
| annotationCategory\_categoryName                                             | category                   |
+------------------------------------------------------------------------------+----------------------------+
| items\_disease\_abbreviation                                                 | project_short_name         |
+------------------------------------------------------------------------------+----------------------------+
| items\_item                                                                  | entity_barcode             |
+------------------------------------------------------------------------------+----------------------------+
| items\_itemType\_itemTypeName                                                | entity_type                |
+------------------------------------------------------------------------------+----------------------------+
| notes\_noteText                                                              | notes                      |
+------------------------------------------------------------------------------+----------------------------+
| notes\_dateAdded                                                             | date_created               |
+------------------------------------------------------------------------------+----------------------------+
| notes\_dateEdited                                                            | date_edited                |
+------------------------------------------------------------------------------+----------------------------+

Sample and Participant barcodes are filled in (*ie* not null) whenever the
"entity_barcode" is at least 16 or 12 characters long, respectively.  For example, a
"Shipped Portion" would result in a filled in "case_barcode" and
"sample_barcode" fields. Please note, however, that the annotation applies *only* to the item
specified in the "entity_barcode" field, the *type* of the item is specified in the "entity_type" field
with the following caveat.  If an annotation is on the case, then it applies to all
its samples, if on a sample, to all its portions but does not apply to other samples for that
case, and so on down to the aliquot, which only applies to that aliquot.

