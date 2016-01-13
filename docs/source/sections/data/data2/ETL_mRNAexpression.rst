mRNA Expression
===============

Gene expression data for the TCGA project has been produced by two different centers, using several
different platforms and fundamentally different pipelines.  Most of the data, from each center, was
produced using the Illumina HiSeq platform and for that reason the first two BigQuery tables containing
gene expression data are based on those specific subsets of the TCGA mRNA expression data:

- the majority of the data was produced by the `UNC LCCC <https://unclineberger.org/>`_ and the resulting normalized RSEM values are stored in `one table <https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM>`_
- and a subset of the data was produced by the `BC GSC <http://www.bcgsc.ca/>`_ and the resulting normalized RPKM values are stored in `another table <https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.mRNA_BCGSC_HiSeq_RPKM>`_


UNC RNAseqV2 Pipeline
---------------------

A ``DESCRIPTION.txt`` file describing the algorithms,
methods, and protocols used to produce the Level-1, Level-2, and Level-3 data
can be obtained from the TCGA DCC.

The BigQuery table was populated using the values in files matching the pattern
``%.rsem.genes.normalized\_results``. These raw "RSEM genes normalized results” 
files have two columns, both of which are stored in the BigQuery table.  The first
column contains the ``gene_id`` which contains two parts separated by a ``|``, *eg*: ``TP53|7157``.
The second column contains the ``normalized_count`` representing the expression value for that gene.

The ``gene\_id`` column is split into two components and stored as separate columns: 
``original\_gene\_symbol`` and ``gene\_id``.  Based on the ``gene_id``, the current HGNC approved
gene symbol is 
`looked up <http://www.genenames.org/help/rest-web-service-help>`_ 
and added as a third column: ``HGNC_gene_symbol``.


BCGSC RNAseq Pipeline
---------------------

A ``DESCRIPTION.txt`` file describing the algorithms,
methods, and protocols used to produce the Level-1, Level-2, and Level-3 data
can be obtained from the TCGA DCC.

The BigQuery table was populated using the values in files matching the pattern
``%.gene.quantification.txt``. These raw “gene quantification” files have
four columns: ``gene``, ``raw\_counts``, ``median\_length\_normalized``, and ``RPKM``.
From these the ``gene`` and the ``RPKM`` values are stored in the BigQuery table.
The ``gene`` string contains either two or three parts, similarly
separated by a ``\|``, *eg* ``TP53\|7157\_calculated`` or ``Mir\_1302\|?\|3of7\_calculated``.

The ``gene`` string is split into two or three components and stored as separate columns:
``original_gene_symbol`` and ``gene_id`` and, if there is a third component, a ``gene_addenda`` column.
If one component is simply ``?``, that character string is replaced by a ``NULL`` value.
Finally, the current HGNC approved gene symbol is
`looked up <http://www.genenames.org/help/rest-web-service-help>`_ 
and added as an additonal column: ``HGNC_gene_symbol``.

