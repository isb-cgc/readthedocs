******************************
Data Releases and Future Plans
******************************

Release Notes
#############

* September 21, 2015: draft set of **BigQuery** tables (not publicly released)
   * ``isb-cgc:tcga_201507_alpha`` dataset containing clinical, biospecimen, somatic mutation calls and Level-3 TCGA data available at the TCGA DCC as of July 2015

* October 4, 2015: complete data upload from TCGA DCC, including controlled-access data

* November 2, 2015: first public release of TCGA open-access data in **BigQuery** tables
   * ``isb-cgc:tcga_201510_alpha`` dataset contains updated set of BigQuery tables, based on data available at the TCGA DCC as of October 2015
   * includes ``Annotations`` table with information about redacted samples, etc
   * ``isb-cgc:platform_reference`` contains annotation information for the Illumina DNA Methylation platform.

* November 16, 2015: initial upload of data from CGHub into **Google Cloud Storage** (GCS) complete (not publicly released)

* December 12, 2015: curated TCGA cohort lists available in ``isb-cgc:tcga_cohorts`` **BigQuery** dataset

* December 26, 2015: public release of new ``isb-cgc:genome_reference`` **BigQuery** dataset: the first table is based on the just-published ``miRTarBase`` release 6.1

* January 10, 2016: ``GENCODE_r19`` and ``miRBase_v20`` tables added to the ``isb-cgc:genome_reference`` **BigQuery** dataset

* February 19, 2016: CCLE RNAseq and DNAseq bam files imported into **Google Genomics**

* February 22, 2016: Kaviar database now available in the ``isb-cgc:genome_reference`` **BigQuery** dataset

* February 26, 2016: new CCLE dataset in **BigQuery** ``isb-cgc:ccle_201602_alpha`` includes sample metadata, mutation calls, copy-number segments, and expression data (metadata includes full cloud-storage-path for world-readable BAM and SNP CEL files, and Genomics dataset- and readgroupset-ids for sequence data imported into Google Genomics)

* March 14, 2016: with the release of our **Web-App**, controlled-data is now accessible (programmatically) to users who have previously obtained dbGaP approval for TCGA data and go through the NIH authentication process built-in to the Web-App.

* April 28, 2016: ``GO_Ontology`` and ``GO_Annotations`` tables added to the ``isb-cgc:genome_reference`` **BigQuery** dataset

* May 3, 2016: new ``isb-cgc:tcga_seq_metadata`` **BigQuery** dataset contains metadata and FastQC metrics for thousands of TCGA DNA-seq and RNA-seq data files:
    * ``CGHub_Manifest`` table contains metadata for all TCGA files at CGHub as of April 27th, 2016
    * ``GCS_listing_27apr2016`` table contains metadata for all TCGA files hosted by ISB-CGC in GCS 
    * ``RNAseq_FastQC`` table contains metrics derived from FastQC runs on the RNAseq data files, including urls to the FastQC html reports that you can cut and paste directly into your browser
    * ``WXS_FastQC`` table contains metrics derived from FastQC runs on the exome DNAseq data files

* May 9, 2016: new ``Ensembl2Reactome`` and ``miRBase2Reactome`` tables added to the ``isb-cgc:genome_reference`` **BigQuery** dataset

Future Plans
############

We have recently brought our CGHub-mirror up-to-date with new TCGA data deposited at CGHub in the past few months.
We are currently (May 2016) in the  midst of re-uploading TCGA data from the DCC and will be providing an updated
BigQuery dataset based on this data in June.

We expect that our future plans will continually evolve based on user feedback, research priorities, and the dynamic nature of the Google Cloud Platform.  
Tell us what is important to you at feedback@isb-cgc.org

