Somatic Mutations
=================

The `MAF table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Somatic_Mutation_calls>`__ in
BigQuery contains somatic mutation calls from 30 tumor types.

Data-cleaning steps for each MAF file
-------------------------------------

-  Remove any rows where the “build” column is not “37”
-  Remove any lines where the “chr” is not in [1-22,X,Y]
-  Remove any lines where the “Mutation\_Status” is not “Somatic”
-  Remove any lines where the “Sequencer” is not an Illumina platform
-  Replace column names with Oncotator required column names

-  'ncbi\_build' : 'build’ , 'chromosome' : 'chr' ,'start\_position' :
   'start' ,'end\_position' : 'end', 'reference\_allele' : 'ref\_allele'
    ,'tumor\_seq\_allele1' : 'tum\_allele1'  

Merging Oncotator output
------------------------

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
----------------------------------

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
---------------------------

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


