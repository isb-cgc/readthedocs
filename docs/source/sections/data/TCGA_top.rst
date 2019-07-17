*************
TCGA Data Set
*************

About the TCGA Program
----------------------

The Cancer Genome Atlas (TCGA) is a comprehensive and coordinated effort to 
accelerate the understanding of the molecular basis of cancer through the 
application of genome analysis technologies, including large-scale 
genome sequencing.

The overarching goal of TCGA is to improve our ability to diagnose, 
treat and prevent cancer. To achieve this goal in a scientifically rigorous 
manner, the National Cancer Institute (NCI) and the National Human Genome 
Research Institute (NHGRI) used a phased-in strategy to launch TCGA. 
A pilot project developed and tested the research framework needed to 
systematically explore the entire spectrum of genomic changes involved 
in more than 20 types of human cancer.

This massive effort was launched in 2006.  
The final samples were shipped in mid-2014,
and analysis of the data produced by this program continues to this day.

For more information please visit the official 
`TCGA website <https://cancergenome.nih.gov/>`_.


About the TCGA Data
-------------------

The ISB-CGC hosts approximately 1 petabyte of TCGA_ data in Google Cloud
Storage (GCS_) and in BigQuery_.  

.. _TCGA: http://cancergenome.nih.gov/
.. _GCS: https://cloud.google.com/storage/
.. _BigQuery: https://cloud.google.com/bigquery/

The ISB-CGC platform is one of NCI's 
`Cloud Resources <https://datascience.cancer.gov/data-commons/cloud-resources>`_ 
and our mission is to host the TCGA data in the cloud so that researchers around the world 
may work with the data without needing 
to download and store the data at their own local institutions.

The vast majority (over 99%) of this **petabyte** of data consists of low-level sequence data, 
currently stored as files in Google Cloud Storage (see figure below).  Over the course of the TCGA project, 
this low-level (*"Level 1"*) data has been processed through a set of standardized pipelines and 
the resulting high-level (*"Level 3"*) data is frequently the data that is used
in most downstream analyses.  The ISB-CGC platform aims to make these different types of data 
accessible to the widest possible variety of users within the cancer research community, 
using the most appropriate Google Cloud Platform technologies.

.. image:: TCGASizeandComplexity.PNG
   :scale: 50
   :align: center

We recommend that you review important information about data security and data access
in these sections:

.. toctree::
   :maxdepth: 1

   data2/TCGA_Data_Security
   data2/TCGA_Access

TCGA Data Platforms
+++++++++++++++++++

When working with any of the data types, it is important to also be aware of both the *platform* that was used to generate the underlying raw data as well as the 
*pipeline* that was used to process the data.  For example, over the course of the TCGA study, DNA methlyation data was obtained using first the Illumina
HumanMethylation27 platform, and later using the HumanMethylation450 platform.  Any analysis that combines data from these two platforms across a cohort of
samples should take this into consideration.  Another example where multiple platforms and/or pipelines were used to produce a single data type is the Level-3 gene
expression data: most tumor samples were processed at UNC and the normalized gene-expression values are based on the RSEM method, while some tumor samples were
processed at BCGSC and the normalized gene-expression values are based on RPKM.

TCGA Data Types
+++++++++++++++

The TCGA dataset is unique in that the tumor samples were assayed using a standard set of platforms and pipelines in order to produce a comprehensive dataset including:

* DNA sequencing of tumor samples and matched-normals (typically blood samples) in order to detect somatic mutations;
* SNP array based DNA copy-number and genotyping analysis of tumor samples and matched-normals;
* DNA methylation of tumor samples;
* messenger RNA (mRNA) expression analysis of the tumor samples to capture the gene expression profile;
* micro-RNA (miRNA) expression profiling of the tumor samples;

In addition, protein expression for a significant fraction (~20%) of all tumor samples was obtained using RPPA (reverse phase protein array).

TCGA Data Levels
++++++++++++++++

For each *type* of data, there are typically three *levels* of data:
* Level 1 typically represents raw, un-normalized data
* Level 2 typically represents an intermediate level of processing and/or normalization of the data;
* Level 3 typically represents aggregated, normalized, and/or segmented data.

The results of integrative or pan-cancer analyses are sometimes referred to as "Level 4" data.  More information about
`Data Level Classification <https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/data-levels>`_ can be found on the NCI page.

For more information about the original data source repository and data access classes (open *vs* controlled),
please refer to these sections:

.. toctree::
   :maxdepth: 1

   data2/byAccessClass
   data2/bySourceRepo

TCGA Data Repository History
++++++++++++++++++++++++++++++
Historically, the data being hosted by the ISB-CGC was obtained from two former TCGA data
repositories:

* **TCGA DCC**: the TCGA Data Coordinating Center which provided a **Data Portal** from which users could download open-access or controlled-access data.  This portal provided access to all TCGA data *except* for the low-level sequence data. 
* **CGHub**:  the **Cancer Genomics Hub** was NCI's current secure data repository for all TCGA BAM and FASTQ sequence data files.

As of June 2016, the official data repository for all TCGA and other NCI CCG data is
the `NCI Genomic Data Commons <https://gdc.cancer.gov/>`_.  The original TCGA data,
aligned to the hg19 human reference genome is available from the NCI-GDC's 
`legacy archive <https://portal.gdc.cancer.gov/legacy-archive/search/f>`_ 
while the new "harmonized" data, realigned to hg38 is available from
the NCI-GDC's main `data portal <https://portal.gdc.cancer.gov/>`_.
