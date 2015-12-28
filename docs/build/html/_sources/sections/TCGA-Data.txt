*******************
About the TCGA Data
*******************

The ISB-CGC hosts approximately 1 petabyte of TCGA_ data in Google Cloud
Storage (GCS_) and in BigQuery_.  

.. _TCGA: http://cancergenome.nih.gov/
.. _GCS: https://cloud.google.com/storage/
.. _BigQuery: https://cloud.google.com/bigquery/

The data being hosted by the ISB-CGC was obtained from the two main TCGA data
repositories:
* **TCGA DCC**: this is the TCGA Data Coordinating Center which provides a `Data Portal <https://tcga-data.nci.nih.gov/tcga/>_` from which users may download open-access or controlled-access data.  This portal provides access to all TCGA data *except* for the low-level sequence data. 
* **CGHub**:  this is NCI's current secure data repository for all TCGA BAM and FASTQ sequence data files.

The ISB-CGC platform is one of NCI's `Cancer Genomics Cloud Pilots <https://cbiit.nci.nih.gov/ncip/nci-cancer-genomics-cloud-pilots>_` 
and our mission is to host the TCGA data in the cloud so that researchers around the world may work with the data without needing 
to download and store the data at their own local institutions.

The vast majority (over 99%) of this **petabyte** of data consists of low-level sequence data, currently stored as files in
Google Cloud Storage.  Over the course of the TCGA project, this low-level (*"Level 1"*) data has been processed through 
a set of standardized pipelines and the the resulting high-level (*"Level 3"*) data is frequently the data that is used
in most downstream analyses.  The ISB-CGC platform aims to make these different types of data accessible to the widest
possible variety of users within the cancer research community, using the most appropriate Google Cloud Platform 
technologies.

An overview of the TCGA data is provided below, with links to additional sources of information.

Understanding the TCGA Data Types and Levels
############################################

TCGA Data Types
===============

TCGA Data Levels
================

Understanding Data Access
#########################

    * **Public Data**  Sometimes the word "public" is misinterpreted as meaning "open".  All of the TCGA data is *public* data, but some of it is *open*, meaning that it is accessible and available to *all* users; while some TCGA data is *controlled* and restricted to authorized users.
    * **Open-Access Data**  Depending on how you categorize the data, *most* of the TCGA data is open-access data.  This includes all de-identified clinical and biospecimen data, as well as all Level-3 molecular data including gene expression data, DNA methylation data, DNA copy-number data, protein expression data, somatic mutation calls, etc. 
    * **Controlled-Access Data**  All low-level sequence data (both DNA-seq and RNA-seq), the raw SNP array data (CEL files), germline mutation calls, and a small amount of other data are treated as *controlled* data and require that a user be properly authenticated and have dbGaP-authorization prior to access these data.

