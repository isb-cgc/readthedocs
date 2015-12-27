Reference Data
==============

ISB-CGC Hosted Reference Data
-----------------------------

In order to facilitate working with the TCGA data tables that the ISB-CGC is hosting in BigQuery, additional
reference data tables have also been created, others are hosted by Google Genomics, 
and suggestions for more are welcome at feedback@isb-cgc.org.

DNA Methylation Platform Annotation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Most of the DNA Methylation data produced by the TCGA project was obtained using the Illumina 
Infinium HumanMethylation450 (aka 450k) BeadChip array.  Some of the earlier tumor types were assayed
on the older, 27k array.

Although additional details can be found at the Illumina_ webpage, we have uploaded the platform
annotation information into the BigQuery table isb-cgc:platform_reference.methylation_annotation

Each CpG locus is uniquely identified as described in this 
`technical note <http://www.illumina.com/content/dam/illumina-marketing/documents/products/technotes/technote_cpg_loci_identification.pdf>_`
and this unique identifier can be used to look up and cross-reference data between the TCGA DNA methylation data table
and the platform annotation table.

.. _Illumina: www.illumina.com

miRTarBase
~~~~~~~~~~
The recently updated miRTarBase_ database (release 6.1) is also available as a BigQuery table: 
isb-cgc:genome_reference.miRTarBase

.. _miRTarBase: http://nar.oxfordjournals.org/content/early/2015/11/19/nar.gkv1258.long

Other Sources
-------------

Google Genomics maintains a list of publicly available datasets here_, including **Reference Genomes**, 
the **Illumina Platinum Genomes**, information about the **Tute Genomics Annotation** table, *etc*.

.. _here: http://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/index.html

