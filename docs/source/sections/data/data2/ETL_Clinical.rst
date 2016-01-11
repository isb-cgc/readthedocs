Clinical
========

Selection of Clinical Metadata Fields
-------------------------------------

XML features with tag  “procurement\_status=Competed” which exist in at
least 20% of the patients in each Study are considered for the metadata.
A few important features like smoking, pregnancy etc were added to the
list as necessary. Selected clinical fields from the clinical and
auxiliary XML files were extracted and loaded into a “clinical data”
\ `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Clinical_data&sa=D&usg=AFQjCNHP0Em9YewAXdL_vgIpbRzGiF2Dgg>`__\  in
BigQuery.  Each row in the table contains all the information for a
single patient, with only the most recent follow-up information included
(for the patients where multiple follow-up sections exist in the
clinical XML file). Clinical BigQuery table is at patient-level.

Parsing Clinical XML
--------------------

A clinical XML file is divided into admin and patient blocks, and each
of them is processed separately.

Patient block iteration

In the first step, while iterating through the patient block, the
elements (XML tags) and their values are collected. While parsing the
follow-up block, only the most recent follow-up sub-block elements info
is obtained (that which have the highest sequence number). Since the
clinical XML is nested along with element tag repetitions, care is taken
not to replace the upper block element values with the lower block
element values. In the last step, patient elements and
follow-up elements are merged with preference given to
follow-up elements.

Formatting
----------

-  for all patients who are "Alive",

-  days\_to\_last\_known\_alive  is set to days\_to\_last\_followup
-  days\_to\_death is set to NULL

-  for all patients who are "Dead", we should have

-  days\_to\_last\_known\_alive  is set to days\_to\_death
-  days\_to\_last\_followup is set to NULL
-  if days\_to\_last\_followup or is available , vital\_status  is set
   to 'Alive'.

-  The following fields are extracted from the cqcf block of the XML
   file: ‘gleason\_score\_combined', 'country',
   'history\_of\_prior\_malignancy', 'frozen\_specimen\_anatomic\_site'
-  hpv\_calls, hpv\_status,
   mononucleotide\_and\_dinucleotide\_marker\_panel\_analysis\_status,
   and mononucleotide\_marker\_panel\_analysis\_status from the
   Auxiliary XML are added to the Clinical metadata table, if the batch
   numbers of the both Clinical and Auxiliary XML files matches.
-  BMI column is calculated based on the height and weight column.


