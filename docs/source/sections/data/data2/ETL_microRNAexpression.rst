microRNA Expression
===================

The current ISB TCGA data pipeline uses a Perl script
``expression\_matrix\_mimat.pl`` provided by BCGSC which reads the
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
-------

-   The pipeline is run only on the hg19 isoform files and others are
   filtered out.

