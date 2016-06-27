Annotations
===========

The TCGA Annotations BigQuery
`table <https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Annotations>`__
was created based on the contents of the JSON file obtained from the TCGA
Annotation manager `Web Service
API <https://wiki.nci.nih.gov/display/TCGA/TCGA+Annotations+Web+Service+User's+Guide>`__.
The deeply nested JSON file was first flattened, and then a subset of the 
fields were selected to be loaded into the BigQuery table.  In the flattening
process, sub-level field names were prefixed with the parent name, separated by
an underscore.  These names were then abbreviated to shorter names,
as specified in the table below.
Please refer directly to BigQuery for the table 
`schema <https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Annotations>`__

+------------------------------------------------------------------------------+----------------------------+
| Original field name                                                          | New field name             |
+==============================================================================+============================+
| annotationCategory\_annotationClassification\_annotationClassificationName   | annotationClassification   |
+------------------------------------------------------------------------------+----------------------------+
| annotationCategory\_categoryId                                               | annotationCategoryId       |
+------------------------------------------------------------------------------+----------------------------+
| annotationCategory\_categoryName                                             | annotationCategoryName     |
+------------------------------------------------------------------------------+----------------------------+
| id                                                                           | annotationId               |
+------------------------------------------------------------------------------+----------------------------+
| items\_disease\_abbreviation                                                 | Study                      |
+------------------------------------------------------------------------------+----------------------------+
| items\_item                                                                  | itemBarcode                |
+------------------------------------------------------------------------------+----------------------------+
| items\_itemType\_itemTypeName                                                | itemTypeName               |
+------------------------------------------------------------------------------+----------------------------+
| notes\_noteText                                                              | annotationNoteText         |
+------------------------------------------------------------------------------+----------------------------+
| notes\_dateAdded                                                             | dateAdded                  |
+------------------------------------------------------------------------------+----------------------------+
| notes\_dateEdited                                                            | dateEdited                 |
+------------------------------------------------------------------------------+----------------------------+

Sample and Participant barcodes are filled in (*ie* not null) whenever the
"itemBarcode" is at least 16 or 12 characters long, respectively.  For example, a
"Shipped Portion" would result in a filled in "ParticipantBarcode" and
"SampleBarcode" fields. Please note, however, that the annotation applies *only* to the item
specified in the "itemBarcode" field, the *type* of the item is specified in the "itemTypeName" field.

