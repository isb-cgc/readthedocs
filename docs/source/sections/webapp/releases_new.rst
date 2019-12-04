###################
Release Notes
###################

text test

===================
April 2016
===================

What's New
===========

===================
March 2016
===================

What's New
===========

**March 14, 2016**

With the release of our Web-App, controlled-data is now accessible (programmatically) to users who have previously obtained dbGaP approval for TCGA data and go through the NIH authentication process built-in to the Web-App

Known Issues and Workarounds
=============================

**March 14, 2016**

version `v1.0 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.0>`_

- When working with a worksheet two plots will be generated occasionally
- Axis labels and tick values sometimes overlap and get cutoff
- Page elongated when Cubby Hole plot generated and there are lots of values in the y axis

===================
February 2016
===================

What's New
===========

**February 26, 2016**

New CCLE dataset in BigQuery isb-cgc:ccle_201602_alpha includes sample metadata, mutation calls, copy-number segments, and expression data (metadata includes full cloud-storage-path for world-readable BAM and SNP CEL files, and Genomics dataset- and readgroupset-ids for sequence data imported into Google Genomics)

**February 22, 2016**

Kaviar database now available in the isb-cgc:genome_reference BigQuery dataset

**February 19, 2016**

CCLE RNAseq and DNAseq bam files imported into Google Genomics

===================
January 2016
===================

What's New
===========

**January 10, 2016**

GENCODE_r19 and miRBase_v20 tables added to the isb-cgc:genome_reference BigQuery dataset

===================
December 2015
===================

What's New
===========

**December 26, 2015**

Public release of new isb-cgc:genome_reference BigQuery dataset: the first table is based on the just-published miRTarBase release 6.1

**December, 12, 2015**

Curated TCGA cohort lists available in isb-cgc:tcga_cohorts BigQuery dataset

**December 3, 2015**

version `v0.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.0>`_

First tagged release of the web-app 

Known Issues and Workarounds
=============================


**December 23, 2015**

version `v0.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.1>`_

Treemap graphs in cohort details and cohort creation pages will not apply its own filters to itself. For example, if you select a study, the study treemap graph will not update 

Cohort file list download not working

===================
November 2015
===================

What's New
===========

**November 16, 2015**

Initial upload of data from CGHub into Google Cloud Storage (GCS) complete (not publicly released)

**November 2, 2015**

First public release of TCGA open-access data in BigQuery tables

- isb-cgc:tcga_201510_alpha dataset contains updated set of BigQuery tables, based on data available at the TCGA DCC as of October 2015
- includes Annotations table with information about redacted samples, etc
- isb-cgc:platform_reference contains annotation information for the Illumina DNA Methylation platform

===================
October 2015 
===================

What's New
===========

**October 4, 2015**

Complete data upload from TCGA DCC, including controlled-access data

===================
September 2015 
===================

What's New
===========

**September 21, 2015** 

Draft set of BigQuery tables (not publicly released)

- isb-cgc:tcga_201507_alpha dataset containing clinical, biospecimen, somatic mutation calls and Level-3 TCGA data available at the TCGA DCC as of July 2015

