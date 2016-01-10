BigQuery Data ETL
=================

Data Quality and General Formatting
-----------------------------------

-  All data uploaded into ISB-CGC BigQuery tables have a consistent
   UTF-8 character set formatting. If the encoding of a character from
   the raw files could not be detected, the characters are simply
   ignored. The character encodings are detected using the Python
   library `Chardet <https://www.google.com/url?q=https://pypi.python.org/pypi/chardet&sa=D&usg=AFQjCNEqIpFiwf3f-ynJmNtP1ZqXe-TvRg>`__.
-  All missing information value strings such as: 'none', 'None',
   'NONE', 'null', 'Null', 'NULL', , 'NA', '\_\_UNKNOWN\_\_', <empty
   spaces>, and '?'; are represented as NULL values in the BigQuery
   tables.
-  The numbers are stored as integer or float value columns, whenever
   possible. The scientific number format (e.g. 10E2) and thousand
   separator comma is not used in any of the number columns.
-  The End of File (EOF) and End of Line (EOL) delimiters, including
   CTRL-M characters, are removed while loading data into BigQuery.
-  Single and double quotes around the values are removed. The quotes
   within a value are not changed.
-  The SDRF file was parsed to find the correct association between the
   aliquot barcode and the Level-3 data file(s), wherever needed and
   possible.

Data Types
----------

CNV
~~~

Each individual CNV Level-3 data archive has 4 output files - two based on the hg18 reference, and two based on the hg19 reference. 
The BigQuery `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Copy_Number_segments&sa=D&usg=AFQjCNHs3vCBx_G7ls1NlgFYHwoBj1-xfw>`__ is populated only with the files ending with "nocnv\_hg19.seg.txt". 
The "num_probes: and "segment_mean" in the raw files is sometimes represented in Exponential Scientific Notation (8.7E+07) and are converted to INT or FLOAT values.

Formatting
^^^^^^^^^^

-  "num_probes" column values are stored as integer values in BigQuery
   tables. Exponential Scientific notation is not used to represent the
   integers.
-  "segment_mean" column values are formatted to 4 point float values.
   Values represented in Exponential Scientific notation in the raw
   files are converted to float values.
-  The aliquot barcode information was obtained from the SDRF file
   associated with the Level-3 data file.

Methylation
~~~~~~~~~~~

The BigQuery
 \ `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.DNA_Methylation_betas&sa=D&usg=AFQjCNFuAXrnRbAzG0U4-f1uPmY8xC6gSQ>`__ \ is
populated only with the files matching the pattern -
%.HumanMethylation%.txt. The data from both 27k and 450k platform are
merged together into a single table. If there are samples that were run
on both platforms, then the 450k data takes precedence and the duplicate
27k data is removed from the table. The table has a platform column
indicating the name of the platform for each sample.

Filters
^^^^^^^

-  Filter out rows with "Beta\_value" is NA or NULL.

Formatting
^^^^^^^^^^

-  Round "Beta\_value" to two digit float (e.g: 0.88). The original
   beta\_value is 14 digit precision floating number.

Output
^^^^^^

-  Only "Probe\_Id", "Beta\_Value" from the data file are stored in the
   BigQuery table.
-  The aliquot barcode information was obtained from the SDRF file
   associated with the Level-3 data file.


miRNA
~~~~~

The current ISB TCGA data pipeline uses a Perl script
(expression\_matrix\_mimat.pl) from Andy Chu at BCGSC which reads the
isoform data files and outputs expression values for "mature microRNAs". 
It outputs a matrix with a consistent number of mature microRNAs, in
which the microRNAs are referred to using a combination of the microRNA
gene name and the unique accession number, eg:
"hsa-mir-21.MIMAT0000076" - both the microRNA name and accession number
are stored as separate columns in the BigQuery
\ `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.miRNA_expression&sa=D&usg=AFQjCNGPgJ1sAHyrdUV6jqHeNs5ZTjc2KQ>`__\ .
The entire matrix is melted into a flat structure(tidy data) and loaded
into the table. The isoform files were searched with the following
pattern - "%.isoform.quantification.txt". The aliquot barcode
information was obtained from the SDRF file associated with the Level-3
isoform data file.

Filters
^^^^^^^

-   The pipeline is run only on the hg19 isoform files and others are
   filtered out.

mRNA bcgsc
~~~~~~~~~~

The mrna bcgsc  BigQuery
\ `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.mRNA_BCGSC_HiSeq_RPKM&sa=D&usg=AFQjCNHGoaSTTA93ZnPTHDJzcN0VREmvWg>`__\  is
populated only with the files matching the pattern
-%.gene.quantification.txt'. The raw “gene quantification” files have
four columns: gene, raw\_counts, median\_length\_normalized, and RPKM.
 The information in the gene and RPKM columns is stored in a BigQuery
table.  The gene string contains either two or three parts, similarly
separated by a “\|”, eg “TP53\|7157\_calculated” or
“Mir\_1302\|?\|3of7\_calculated”.

Formatting
^^^^^^^^^^

-  ‘gene’ column field value is split into ‘original\_gene\_symbol',
   ‘gene\_id’ , and ‘gene\_addenda’ columns.
-  The “\_calculated” string is stripped off from the “gene\_id” value.
   “?” is replaced with a null value.
-  Based on the ‘gene\_id’ columns, HGNC approved gene symbol is added
   as a new column “HGNC\_gene\_symbol”. The HGNC approved symbols were
   obtained from the following url:
   \ `http://rest.genenames.org/fetch/status/Approve <https://www.google.com/url?q=http://rest.genenames.org/fetch/status/Approved&sa=D&usg=AFQjCNHVRPnQGE0KLpbqF7KUePUWqr9uPg>`__\ d.

mRNA unc
~~~~~~~~

The mrna UNC BigQuery
\ `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM&sa=D&usg=AFQjCNFDandkapnU15Btk5cnsxT2q9I2uw>`__\  is
populated only with the files matching the pattern -
'%.rsem.genes.normalized\_results'. The raw “RSEM genes normalized
results” files have two columns, the contents of which will be stored in
a BigQuery table.  The first column contains the gene\_id, and the
second the normalized\_count.  The gene\_id string contains two parts:
the gene symbol, and the gene id, separated by a “\|”, eg: “TP53\|7157”.

Formatting
^^^^^^^^^^

-  The ‘gene\_id’ column is split into 'original\_gene\_symbol' and
   'gene\_id'- both are stored as separate columns in BigQuery.
-  Based on the ‘gene\_id’, HGNC approved gene symbol is added as a new
   column “HGNC\_gene\_symbol”.

 

Protein
~~~~~~~

The raw protein data file contains just two columns: The "Composite Element REF", which corresponds to the third column in the antibody
annotation file, and the estimated expression value for that particular
protein. The "Composite Element REF" was parsed to generate additional
information(see details in the formatting section). The BigQuery
 `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Protein_RPPA_data>`__ was
populated with all TCGA Level-3 RPPA data matching the pattern -
"%\_RPPA\_Core.protein\_expression%.txt".

The antibody annotation files are parsed to get the relationship between
the antibody name and the associated proteins, and genes. Below is the
detailed explanation about the generation of the antibody, gene, protein
map.

  Generation of Composite\_element\_ref, gene, and protein name map
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

      (Manual Curation of the gene and protein names)

-  Check the antibody annotation files for missing columns.

-  If “protein\_name” is missing, generate one from
   “composite\_element\_ref”

-  Make a map of ‘composite\_element\_ref’,’ gene\_name’,
   ‘protein\_name’ values.
-  Check any other variant of the gene and protein symbols in the table.
-  HGNC Validation

-  If the gene symbol is in the HGNC approved symbols, ‘Approved’.
    Gene\_symbol = Gene\_symbol.
-  If not, check the Alias symbols. If found,  Gene\_symbol =
   Alias\_symbol.
-  If not, check the Previous symbols. If found, Gene\_symbol =
   “Approved” Gene\_symbol.
-  If not, Gene\_symbol = Gene\_symbol
-  The file generated is manually curated and fed back into the
   algorithm.

Formatting
^^^^^^^^^^

-  Duplicate the rows if there are multiple genes concatenated in the
   "gene\_name" value. For example: ‘gene\_name’ with value like ‘AKT1
   AKT2 AKT3’ is stored as three separate rows with each gene in a row.
-  'Protein\_Name' is split into 'Protein\_Basename', Phospho' and are
   stored as separate columns.
-  ‘Composite element ref’ is parsed to get 'validationStatus' and
   'antibodySource' – both are stored as separate columns in the
   BigQuery table.
-  Data from both Illumina GA and HiSeq platforms are stored in the same
   table.

 

MAF
~~~

The `MAF table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Somatic_Mutation_calls>`__ in
BigQuery contains somatic mutation calls from 30 tumor types.

Data-cleaning steps for each MAF file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Remove any rows where the “build” column is not “37”
-  Remove any lines where the “chr” is not in [1-22,X,Y]
-  Remove any lines where the “Mutation\_Status” is not “Somatic”
-  Remove any lines where the “Sequencer” is not an Illumina platform
-  Replace column names with Oncotator required column names

-  'ncbi\_build' : 'build’ , 'chromosome' : 'chr' ,'start\_position' :
   'start' ,'end\_position' : 'end', 'reference\_allele' : 'ref\_allele'
    ,'tumor\_seq\_allele1' : 'tum\_allele1'  

Merging Oncotator output
^^^^^^^^^^^^^^^^^^^^^^^^

-  Merge the oncotator output by disease\_type, change/add columns. This
   step in fact generates the final output that can be loaded into
   BigQuery. The next step loads the file and deletes the duplicates
-  Merge all the files by disease type.
-  The final columns to be stored in table. Note we have hard-coded some
   column name changes. Eg: Gc\_content to GC\_Content
-  Change column names

-  Replace strings:

-  "1000" : "\_1000"
-  " " : "\_" ( spaces replaced by underscore)
-  ")" : "" ( closing bracket to empty string)        
-  "(" : "\_"
-  "+" : "\_"
-  “-" : "\_" ( dashes to underscore)
-  “gencode" : "GENCODE"

-  

-  Add new columns

-  "Tumor\_Sample\_Barcode", "Tumor\_Patient\_Barcode",
   "Tumor\_Sample\_Type", "Normal\_Sample\_Barcode",
   "Normal\_Patient\_Barcode", "Normal\_Sample\_Type", "Study"

General Rules to remove duplicates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  for the cases where there is a "blood derived normal" and a "solid
   tissue normal", we prefer the blood derived normal

-  for the cases where there are multiple aliquots for one tumor sample,
   then we should first try to choose the "D" over the "W" aliquot, eg:

TCGA-B0-5695-01A-11D-1534-10; TCGA-B0-5695-01A-11W-1584-10

-  If both tumor aliquots have a "D" (or both have "W") in that spot,
   then the next way to choose one over the other is by looking at the
   final two digits which identify the "center" which did generated this
   data, eg:

TCGA-B2-4099-01A-02D-1251-10; TCGA-B2-4099-01A-02D-1458-08

and here is how I would choose:

first choose (01, 08, 14) which all correspond
to\ `  <https://www.google.com/url?q=http://broad.mit.edu&sa=D&usg=AFQjCNHnEPmO4IR1qZPXJKyzVVMeIxLlAg>`__\ `broad.mit.edu <https://www.google.com/url?q=http://broad.mit.edu&sa=D&usg=AFQjCNHnEPmO4IR1qZPXJKyzVVMeIxLlAg>`__

next choose (09,21,30) which all correspond
to\ `  <https://www.google.com/url?q=http://genome.wustl.edu&sa=D&usg=AFQjCNGDSSLCDrgNRsyjlYosH1jVUdeqCA>`__\ `genome.wustl.edu <https://www.google.com/url?q=http://genome.wustl.edu&sa=D&usg=AFQjCNGDSSLCDrgNRsyjlYosH1jVUdeqCA>`__

next choose (10,12) which corresponds
to\ `  <https://www.google.com/url?q=http://hgsc.bcm.edu&sa=D&usg=AFQjCNGwuFEpglbGKZy0Vy7pPBFaOuVoLQ>`__\ `hgsc.bcm.edu <https://www.google.com/url?q=http://hgsc.bcm.edu&sa=D&usg=AFQjCNGwuFEpglbGKZy0Vy7pPBFaOuVoLQ>`__

next choose (13,31) which corresponds
to\ `  <https://www.google.com/url?q=http://bcgsc.ca&sa=D&usg=AFQjCNFDiYCi3Xsqp9d993xDcZ4O1v64KQ>`__\ `bcgsc.ca <https://www.google.com/url?q=http://bcgsc.ca&sa=D&usg=AFQjCNFDiYCi3Xsqp9d993xDcZ4O1v64KQ>`__

next choose (18,25) which corresponds
to\ `  <https://www.google.com/url?q=http://ucsc.edu&sa=D&usg=AFQjCNEMtV_drZ8zVeT8jnzrjM4OFS2wSA>`__\ `ucsc.edu <https://www.google.com/url?q=http://ucsc.edu&sa=D&usg=AFQjCNEMtV_drZ8zVeT8jnzrjM4OFS2wSA>`__

` <https://www.google.com/url?q=http://ucsc.edu&sa=D&usg=AFQjCNEMtV_drZ8zVeT8jnzrjM4OFS2wSA>`__

-  In case of a tie, this is completely arbitrary, but do this: take the
   last 4-char sequence in the barcode (21:25) and choose the one where
   that value is "greater".  Those 4-char substrings do sometimes
   include letters, so you should do a string comparison rather than
   casting these to integers

Check and remove duplicates
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  This step takes the output files generated in the previous step and
   removes duplicates. See section “General Rules to remove duplicates”
   above for the rules to remove duplicates.
-  Pseudo code for the rules:

-  The aliquots are selected in the below preference order

-  ("13:15", ["10"])  # blood aliquot
-  ("19:20", ["D"])   # select D over W
-  ("26:28", ["01", "08", "14", "09", "21", "30", "10", "12", "13",
   "31", "18", "25"]) ])

-  If tie, select the one which has greater number in (21:25) position,
   else return first aliquot(default)

-  remove any duplicates left after the above steps. Only unique
   mutations are stored in the table. A unique mutation is defined by
   (chr, start, end, tum\_allele1, tum\_allele2, tumor\_barcode).

 

Clinical
~~~~~~~~

Selection of Clinical Metadata Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^

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

 

Biospecimen
~~~~~~~~~~~

Parsing Biospecimen XML
^^^^^^^^^^^^^^^^^^^^^^^

Similarly, selected biospecimen fields from the biospecimen XML files
were extracted and loaded into a “biospecimen” table in BigQuery.
 Biospecimen BigQuery
\ `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Biospecimen_data&sa=D&usg=AFQjCNFWq7NUA2BkQ2br8PFG6VNySeFcxw>`__\  is
a sample-level.

In the first step, while iterating through the sample block the elements
(XML tags) and their values are collected. The slides’ info is averaged
across portions while iterating over the portions block. Also the
slides’ max and min values are calculated. The total number of slides
(num\_slides) and portions (num\_portions) is calculated for each
sample, along with the average, max and min values observed. All the
calculated and derived values are added as new columns in the BigQuery
tables.

Filters
^^^^^^^

-  Samples with "is\_ffpe: is True are removed.
-  Patients/Samples where the "Project" is "null" are removed.

Formatting
^^^^^^^^^^

-  "pregnancies" and "total_number_of_pregnancies" are be merged into a
   single "pregnancies" field. The counts above four are represented as
   "4+" (e.g: [0,1,2,3,4+])
-  "number\_of\_lymphnodes\_examined" and "lymph\_node\_examined\_count" are
   merged into a single "number\_of\_lymphnodes\_examined" column.
