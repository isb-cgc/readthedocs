******************************
Data Releases and Future Plans
******************************

Release Notes
#############

* September 21, 2015: first set of BigQuery tables (not publicly released)
   * ``isb-cgc:tcga_201507_alpha`` dataset containing clinical, biospecimen, somatic mutation calls and Level-3 TCGA data available at the TCGA DCC as of July 2015

* October 4, 2015: complete data upload from TCGA DCC, including controlled-access data

* November 2, 2015: first public release of TCGA open-access data in BigQuery tables
   * ``isb-cgc:tcga_201510_alpha`` dataset contains updated set of BigQuery tables, based on data available at the TCGA DCC as of October 2015
   * includes ``Annotations`` table with information about redacted samples, etc
   * ``isb-cgc:platform_reference`` contains annotation information for the Illumina DNA Methylation platform.

* November 16, 2015: initial upload of data from CGHub into Google Cloud Storage complete (not publicly released)

* December 26, 2015: public release of new ``isb-cgc:genome_reference`` dataset, with ``miRTarBase`` table

* January 10, 2016: ``GENCODE_r19`` and ``miRBase_v20`` tables added to ``isb-cgc:genome_reference`` dataset

Future Plans
############

We expect that our future plans will continually evolve based on user feedback, research priorities, and the dynamic nature of the Google Cloud Platform.  
Tell us what is important to you at feedback@isb-cgc.org

Near-Term
=========

* Enable access to controlled data in GCS by authorized users (January)
* Upload new data from CGHub into GCS (February)
* New set of BigQuery tables based on new data at the TCGA DCC (March)
* Upload TCGA MC3 VCF files from TCGA DCC into GCS (?)

Longer-Term
===========

* Import a subset of VCF files and sequence-level data into Google Genomics

