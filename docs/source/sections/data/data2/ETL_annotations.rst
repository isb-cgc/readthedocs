TCGA Annotations
=======================

The TCGA Annotations BigQuery
`table <https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Annotations>`__
has been populated with the JSON file downloaded from the TCGA
Annotation manager `Web Service
API <https://wiki.nci.nih.gov/display/TCGA/TCGA+Annotations+Web+Service+User's+Guide>`__.
A few selected fields from the JSON file have been loaded into the
BigQuery table. Please refer to the
`schema <https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Annotations>`__
for all the selected fields. The JSON file from TCGA is
highly nested and has been flattened - the sub-level field names were
concatenated to the parent name with an underscore- before loading into
BigQuery. Some of the fields in the JSON file have been renamed with a
shorter name. The following table has the mapping of the original field
name and the new shorter field name.

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

Sample and Participant barcodes are be filled in whenever the
"itemBarcode" is longer than 16 or 12 characters respectively - i.e. a
"Shipped Portion" would result in a filled in "ParticipantBarcode" and
"SampleBarcode" fields. The annotation applies only to the item
specified in the "itemBarcode" field.
