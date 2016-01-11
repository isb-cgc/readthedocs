mRNA bcgsc
----------

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
--------

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


