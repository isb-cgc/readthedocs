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
an underscore.  These names were then abbreviated to shorter names,
as specified in the table below.
Please refer directly to BigQuery for the table 
`schema <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_bioclin_v0.Annotations>`__


+------------------------------------------------------------------------------+----------------------------+
| Original field name                                                          | New field name             |
+==============================================================================+============================+
| items\_disease\_abbreviation                                                 | project_short_name         |
+------------------------------------------------------------------------------+----------------------------+
| items_item                                                                   | entity_barcode             |
+------------------------------------------------------------------------------+----------------------------+
| items_itemType_itemTypeName                                                  | entity_type                |
+------------------------------------------------------------------------------+----------------------------+
| annotationCategory\_categoryName                                             | category                   |
+------------------------------------------------------------------------------+----------------------------+
| annotationCategory\_annotationClassification\_annotationClassificationName   | Classification             |
+------------------------------------------------------------------------------+----------------------------+
| notes\_noteText                                                              | notes                      |
+------------------------------------------------------------------------------+----------------------------+
| notes_dateAdded                                                              | date_created               |
+------------------------------------------------------------------------------+----------------------------+
| notes\_dateEdited                                                            | date_edited                |
+------------------------------------------------------------------------------+----------------------------+
| not available                                                                | case_gdc_id                |
+------------------------------------------------------------------------------+----------------------------+
| not available                                                                | case_barcode               |
+------------------------------------------------------------------------------+----------------------------+
| not available                                                                | sample_barcode             |
+------------------------------------------------------------------------------+----------------------------+
| not available                                                                | aliqout_barcode            |
+------------------------------------------------------------------------------+----------------------------+

Sample and Cases barcodes are filled in (*ie* not null) whenever the
"itemBarcode" is at least 16 or 12 characters long, respectively.  For example, a
"Shipped Portion" would result in a filled in "ParticipantBarcode" and
"SampleBarcode" fields. Please note, however, that the annotation applies *only* to the item
specified in the "itemBarcode" field, the *type* of the item is specified in the "itemTypeName" field
with the following caveat.  If an annotation is on the participant, then it applies to all
its samples, if on a sample, to all its portions but does not apply to other samples for that
participant, and so on down to the aliquot, which only applies to that aliquot.

