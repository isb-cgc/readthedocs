microRNA Expression
===================

The current ISB TCGA data pipeline uses a Perl script
``expression\_matrix\_mimat.pl`` provided by BCGSC which reads the
isoform data files and outputs expression values for "mature microRNAs". 
This output matrix contains a consistent number of mature microRNAs,
referred to using a combination of the microRNA
gene name and the unique accession number, eg:
"hsa-mir-21.MIMAT0000076".  During ETL, this string is split into two
parts and stored as separate columns in the BigQuery
\ `table <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.miRNAseq_Isoform_Expression>`_.
The entire matrix is then melted into a flat structure (known as the tidy data format) and loaded
into the table. 

Only the isoform files matching the pattern
``%.hg19.mirbase20.isoform.quantification.txt`` and containing hg19 data were used. The aliquot barcode
information was obtained from the SDRF file associated with the Level-3
isoform data file.

There is also a `table <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.miRNAseq_Expression>`_ with the expression data and corresponding tables reprocessed by the GDC
against the HG38 genomic build for `isoform <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg38_data_v0.miRNAseq_Isoform_Expression>`_ and 
`expression <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg38_data_v0.miRNAseq_Expression>`_

