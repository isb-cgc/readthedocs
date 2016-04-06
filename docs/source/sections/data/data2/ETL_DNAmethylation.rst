Methylation (DNA)
=================

The 
`DNA Methylation <https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.DNA_Methylation_betas>`_
table contains one row per CpG probe and TCGA aliquot.
Each TCGA aliquot is uniquely represented by a
`TCGA barcode <https://wiki.nci.nih.gov/display/TCGA/TCGA+barcode>`_
of length 24, *eg* ``TCGA-04-1517-01A-01D-0533-01``.  (For more information on how TCGA barcodes
were created and how to *"read"* a TCGA barcode, click on the preceding link.)

The platform annotation information needed to analyze this data is also available in a BigQuery table.  For more
information, see the Reference Data section of this documentation.

Platform
--------
DNA Methylation data was generated for the TCGA project using the Illlumina HumanMethylation27 BeadChip
and its successor, the 
`HumanMethylation450 <http://www.illumina.com/products/methylation_450_beadchip_kits.html>`_ 
BeadChip.

Pipeline
--------
DNA Methylation data was generated for the TCGA project at the JHU-USC genome characterization center.
A ``DESCRIPTION.txt`` file is included with each data archive at the DCC describing the algorithms,
methods, and protocols used to produce the Level-1, Level-2, and Level-3 data.

ETL Details
-----------

The BigQuery table is populated only with the files matching the pattern 
``%.HumanMethylation%.txt``. The data from both 27k and 450k platform have been 
merged together into a single table. A few samples were run on both platforms, and
for those samples, the 450k data takes precedence.
The table includes a platform column indicating the source of each data value.

In addition:

- any CpG probes for which the Level-3 ``Beta_Value`` is NA or NULL, are left out
- only the ``Probe_Id`` and ``Beta_Value`` fields from the Level-3 data files are stored in the BigQuery table


