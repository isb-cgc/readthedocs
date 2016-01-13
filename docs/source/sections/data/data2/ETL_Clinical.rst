Clinical
========

The
`Clinical <https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Clinical>`_
table contains one row per TCGA participant (aka patient or donor).  
Each TCGA participant is uniquely represented by a
`TCGA barcode <https://wiki.nci.nih.gov/display/TCGA/TCGA+barcode>`_
of length 12, *eg* ``TCGA-2G-AAM4``.  (For more information on how TCGA barcodes
were created and how to *"read"* a TCGA barcode, click on the preceding link.)

Clinical Feature Selection
--------------------------

In the first pass, any
XML features with the tag ``procurement\_status=Completed``
which were found to exist in at
least 20% of the participants in any one Study (aka tumor-type) were considered for selection.
A few important features related to smoking, pregnancy, *etc* were added to the
list during a manual-curation pass. 

Selected fields from the both the clinical and
auxiliary XML files were then extracted and loaded into the BigQuery table.

Additionally, only the most recent follow-up information was included
(for patients where multiple follow-up sections existed in the
clinical XML file). 

XML Parsing 
-----------

Each clinical XML file is divided into ``admin`` and ``patient`` blocks, and
each of these were processed separately.

While iterating through the patient block of information, all elements
(XML tags) and their values were collected.  For ``follow-up`` blocks, only the
most recent (based on sequence number) sub-block elements were kept.

In the final pass, patient elements and follow-up elements were carefully 
merged with preference given to follow-up elements.

Transforms
----------

Different survival-related fields are completed based on the value of the ``vital_status`` field:

-  for all patients with ``vital_status=Alive``:

   -  days\_to\_last\_known\_alive should not be NULL
   -  days\_to\_last\_known\_alive is set to days\_to\_last\_followup
   -  days\_to\_death is set to NULL

-  for all patients with ``vital_status=Dead``:

   -  days\_to\_death should not be NULL (if it is NULL, and days\_to\_last\_followup is not NULL, then vital\_status is set to "Alive"
   -  days\_to\_last\_known\_alive  is set to days\_to\_death
   -  days\_to\_last\_followup is set to NULL

The following fields were extracted from the cqcf block of the XML file: 

- ``gleason\_score\_combined``, 
- ``country``,
- ``history\_of\_prior\_malignancy``, 
- ``frozen\_specimen\_anatomic\_site``

When an auxiliary XML file exists for a participant, and the batch numbers in 
both the clinical XML and the auxiliary XML file match, the following fields
are extracted from the auxiliary XML file and added to the Clinical table:

-  ``hpv\_calls``, 
-  ``hpv\_status``,
-  ``mononucleotide\_and\_dinucleotide\_marker\_panel\_analysis\_status``,
-  ``mononucleotide\_marker\_panel\_analysis\_status``.

Finally, the patient BMI was calculated based on the ``height`` and ``weight`` values
(when both were present) and was added to the Clinical table.

