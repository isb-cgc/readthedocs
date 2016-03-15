******************************
Data Releases and Future Plans
******************************

Release Notes
#############

* September 21, 2015: draft set of BigQuery tables (not publicly released)
   * ``isb-cgc:tcga_201507_alpha`` dataset containing clinical, biospecimen, somatic mutation calls and Level-3 TCGA data available at the TCGA DCC as of July 2015

* October 4, 2015: complete data upload from TCGA DCC, including controlled-access data

* November 2, 2015: first public release of TCGA open-access data in BigQuery tables
   * ``isb-cgc:tcga_201510_alpha`` dataset contains updated set of BigQuery tables, based on data available at the TCGA DCC as of October 2015
   * includes ``Annotations`` table with information about redacted samples, etc
   * ``isb-cgc:platform_reference`` contains annotation information for the Illumina DNA Methylation platform.

* November 16, 2015: initial upload of data from CGHub into Google Cloud Storage complete (not publicly released)

* December 12, 2015: curated TCGA cohort lists available in ``isb-cgc:tcga_cohorts`` dataset

* December 26, 2015: public release of new ``isb-cgc:genome_reference`` dataset, with ``miRTarBase`` table

* January 10, 2016: ``GENCODE_r19`` and ``miRBase_v20`` tables added to ``isb-cgc:genome_reference`` dataset

* February 19, 2016: CCLE RNAseq and DNAseq bam files imported into Google Genomics

* February 22, 2016: Kaviar database now available in the ``isb-cgc:genome_reference`` dataset

* February 26, 2016: new CCLE dataset in BigQuery includes sample metadata, mutation calls, copy-number segments, and expression data (metadata includes full cloud-storage-path for world-readable BAM and SNP CEL files, and Genomics dataset- and readgroupset-ids for sequence data imported into Google Genomics)

* March 14, 2016: with the release of our Web-App, controlled-data is now accessible (programmatically) to users who have previously obtained dbGaP approval for TCGA data and go through the NIH authentication process built-in to the Web-App.

Future Plans
############

We expect that our future plans will continually evolve based on user feedback, research priorities, and the dynamic nature of the Google Cloud Platform.  
Tell us what is important to you at feedback@isb-cgc.org

Near-Term
=========

* Enable access to controlled data in GCS by authorized users (March)
* Upload new data from CGHub into GCS (March)
* Complete update of data from DCC into GCS (April)
* New set of BigQuery tables based on new data at the TCGA DCC (April/May)

Longer-Term
===========

* Import a subset of TCGA VCF files and sequence-level data into Google Genomics

