mRNA Expression
===============

Although gene expression data for the TCGA project was produced by two different centers, only the data produced by the 
UNC RSEM pipeline was incorporated into the GDC.  The GDC has also reprocessed that data against HG38 resulting in a second
BigQuery table.:


- the data produced by the `UNC LCCC <https://unclineberger.org/>`_ and the resulting normalized RSEM values are stored in `one table <https://console.cloud.google.com/bigquery?p=isb-cgc&d=TCGA_hg19_data_v0&t=RNAseq_Gene_Expression_UNC_RSEM&page=table>`_
- and the data produced by the `GDC <https://gdc.cancer.gov/>`_ and the resulting normalized RPKM values are stored in `another table <https://console.cloud.google.com/bigquery?p=isb-cgc&d=TCGA_hg38_data_v0&t=RNAseq_Gene_Expression&page=table>`_


UNC RNAseqV2 Pipeline
---------------------

A ``DESCRIPTION.txt`` file describing the algorithms,
methods, and protocols used to produce the Level-1, Level-2, and Level-3 data
can be obtained from the TCGA DCC.

The BigQuery table was populated using the values in files matching the pattern

``%.rsem.genes.normalized\_results``. These raw "RSEM genes normalized results" 

files have two columns, both of which are stored in the BigQuery table.  The first
column contains the ``gene_id`` which contains two parts separated by a ``|``, *eg*: ``TP53|7157``.
The second column contains the ``normalized_count`` representing the expression value for that gene.

The ``gene\_id`` column is split into two components and stored as separate columns:
``original\_gene\_symbol`` and ``gene\_id``.  Based on the ``gene_id``, the current HGNC approved
gene symbol is
`looked up <http://www.genenames.org/help/rest-web-service-help>`_
and added as a third column: ``HGNC_gene_symbol``.


GDC RNAseq Pipeline
---------------------

The original DCC genomic data was reprocessed against the ``HG38`` genomic build.

The ``gene`` string is split into two or three components and stored as separate columns:
``original_gene_symbol`` and ``gene_id`` and, if there is a third component, a ``gene_addenda`` column.
If one component is simply ``?``, that character string is replaced by a ``NULL`` value.
Finally, the current HGNC approved gene symbol is `looked up <http://www.genenames.org/help/rest-web-service-help>`_ 
and added as an additional column: ``HGNC_gene_symbol``.

