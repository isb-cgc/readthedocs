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

* **TCGA DCC**: the TCGA Data Coordinating Center which provides a `Data Portal <https://tcga-data.nci.nih.gov/tcga/>`_ from which users may download open-access or controlled-access data.  This portal provides access to all TCGA data *except* for the low-level sequence data. 
* **CGHub**:  the `Cancer Genomics Hub <https://cghub.ucsc.edu>`_ is NCI's current secure data repository for all TCGA BAM and FASTQ sequence data files.

The ISB-CGC platform is one of NCI's `Cancer Genomics Cloud Pilots <https://cbiit.nci.nih.gov/ncip/nci-cancer-genomics-cloud-pilots>`_ 
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

The TCGA dataset is unique in that the tumor samples were assayed using a standard set of platforms and pipelines in order to produce a comprehensive dataset including:

* DNA sequencing of tumor samples and matched-normals (typically blood samples) in order to detect somatic mutations;
* SNP array based DNA copy-number and genotyping analysis of tumor samples and matched-normals;
* DNA methylation of tumor samples;
* messenger RNA (mRNA) expression analysis of the tumor samples to capture the gene expression profile;
* micro-RNA (miRNA) expression profiling of the tumor samples;

In addition, protein expression for a significant fraction (~20%) of all tumor samples was obtained using RPPA (reverse phase protein array).

TCGA Data Levels
================

For each *type* of data, there are typically three *levels* of data:
* Level 1 typically represents raw, un-normalized data
* Level 2 typically represents an intermediate level of processing and/or normalization of the data;
* Level 3 typically represents aggregated, normalized, and/or segmented data.

The results of integrative or pan-cancer analyses are sometimes referred to as "Level 4" data.  More information about
`Data Level Classification <https://wiki.nci.nih.gov/display/TCGA/Data+level>`_ can be found on the NCI wiki.

TCGA Data Platforms
===================

When working with any of the data types, it is important to also be aware of both the *platform* that was used to generate the underlying raw data as well as the 
*pipeline* that was used to process the data.  For example, over the course of the TCGA study, DNA methlyation data was obtained using first the Illumina
HumanMethylation27 platform, and later using the HumanMethylation450 platform.  Any analysis that combines data from these two platforms across a cohort of
samples should take this into consideration.  Another example where multiple platforms and/or pipelines were used to produce a single data type is the Level-3 gene
expression data: most tumor samples were processed at UNC and the normalized gene-expression values are based on the RSEM method, while some tumor samples were
processed at BCGSC and the normalized gene-expression values are based on RPKM.

TCGA Data Reports
=================

A number of useful `Data Reports <https://tcga-data.nci.nih.gov/datareports/dataReportsHome.htm>`_ 
are available directly from TCGA.  There are several different reports that you can access from that 
page, including these nice dashboards:

* **Data Statistics**:  this `dashboard <https://tcga-data.nci.nih.gov/datareports/statsDashboard.htm>`_ provides high-level statistics describing TCGA data content and usage.
* **Project Case Overview**:  this `dashboard <https://tcga-data.nci.nih.gov/datareports/projectCaseDashboard.htm>`_ provides a high-level snapshot of TCGA project progress through the multiple phases of sample analysis.

Understanding Data Access
#########################

* **Public Data**  Sometimes the word "public" is misinterpreted as meaning "open".  All of the TCGA data is *public* data, and much of it is *open*, meaning that it is accessible and available to *all* users; while some low-level TCGA data is *controlled* and restricted to authorized users.
* **Open-Access Data**  Depending on how you categorize the data, *most* of the TCGA data is open-access data.  This includes all de-identified clinical and biospecimen data, as well as all Level-3 molecular data including gene expression data, DNA methylation data, DNA copy-number data, protein expression data, somatic mutation calls, etc. 
* **Controlled-Access Data**  All low-level sequence data (both DNA-seq and RNA-seq), the raw SNP array data (CEL files), germline mutation calls, and a small amount of other data are treated as *controlled* data and require that a user be properly authenticated and have dbGaP-authorization prior to access these data.

