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

The ISB-CGC platform is one of the 
`NCI Cloud Resources <https://datascience.cancer.gov/data-commons/cloud-resources>`_ 
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

TCGA Data Platforms
+++++++++++++++++++

When working with any of the data types, it is important to also be aware of both the *platform* that was used to generate the underlying raw data as well as the 
*pipeline* that was used to process the data.  For example, over the course of the TCGA study, DNA methylation data was obtained using first the Illumina
HumanMethylation27 platform, and later using the HumanMethylation450 platform.  Any analysis that combines data from these two platforms across a cohort of
samples should take this into consideration.  Another example where multiple platforms and/or pipelines were used to produce a single data type is the Level-3 gene
expression data: most tumor samples were processed at UNC and the normalized gene-expression values are based on the RSEM method, while some tumor samples were
processed at BCGSC and the normalized gene-expression values are based on RPKM.

TCGA Data Levels
++++++++++++++++

For each *type* of data, there are typically three *levels* of data:
* Level 1 typically represents raw, un-normalized data
* Level 2 typically represents an intermediate level of processing and/or normalization of the data;
* Level 3 typically represents aggregated, normalized, and/or segmented data.

The results of integrative or pan-cancer analyses are sometimes referred to as "Level 4" data.  More information about
`Data Level Classification <https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/data-levels>`_ can be found on the NCI page.

TCGA Data Types
+++++++++++++++

The TCGA data set is unique in that the tumor samples were assayed using a standard set of platforms and pipelines in order to produce a comprehensive data set including:

* DNA sequencing of tumor samples and matched-normals (typically blood samples) in order to detect somatic mutations;
* SNP array based DNA copy-number and genotyping analysis of tumor samples and matched-normals;
* DNA methylation of tumor samples;
* messenger RNA (mRNA) expression analysis of the tumor samples to capture the gene expression profile;
* micro-RNA (miRNA) expression profiling of the tumor samples;

In addition, protein expression for a significant fraction (~20%) of all tumor samples was obtained using RPPA (reverse phase protein array).

Open-Access TCGA Data
=====================

The open-access TCGA data hosted by the ISB-CGC Platform includes:

* Clinical (de-identified) and Biospecimen data: these data were originally provided in XML files (Level-1) by the DCC
* Somatic mutation data:  these data were originally provided in MAF files (Level-2) by the DCC
* DNA copy-number segments:  these data were originally provided as segmentation files (Level-3) by the DCC
* DNA methylation data:  these data were originally provided as TSV files (Level-3) by the DCC
* Gene (mRNA) expression data:  these data were originally provided as TSV files (Level-3) by the DCC
* microRNA expression data:  these data were originally provided as TSV files (Level-3) by the DCC
* Protein expression data:  these data were originally provided as TSV files (Level-3) by the DCC
* TCGA Annotations data:  annotations were originally obtained from the TCGA Annotations Manager, and can now also be found on the `GDC Data Portal <https://portal.gdc.cancer.gov/annotations>`_

in Google Cloud Storage (GCS)
*****************************

The data files described above are available to all ISB-CGC users in an open-access GCS bucket (gs://isb-tcga-phs000178-open).

.. _in_BigQuery:

in BigQuery
***********

The information scattered over tens of thousands of XML and TSV files at the DCC is provided in a 
*much more accessible* form in a series of 
`BigQuery tables <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/data2/data_in_BQ.html#tcga-clinical-biospecimen-and-molecular-data>`_.  

For more details, please see our `github repositories <https://github.com/isb-cgc>`_ or our `Community Notebook Repository <https://github.com/isb-cgc/Community-Notebooks>`_ for tutorials and code examples in Python and R.

This `introductory tutorial <https://github.com/isb-cgc/examples-Python/blob/master/notebooks/The%20ISB-CGC%20open-access%20TCGA%20tables%20in%20BigQuery.ipynb>`_
gives a great overview of all of the tables and pointers on how to get started exploring them.  Be sure to check it out!

Controlled-Access TCGA Data
===========================

The controlled-access TCGA data hosted by the ISB-CGC Platform includes:

* SNP array CEL files:  these Level-1 data files were provided by the DCC and include over 22,000 files for both tumor and matched-normal samples
* VCF files:  these Level-2 data files were provided by the DCC and include over 15,000 files produced by several different centers (primarily Broad and BCGSC)
* MAF files:  these "protected" mutation files (Level-2) were provided by the DCC (note that these files were not generated uniformly for all tumor types)
* DNA-seq BAM files:  these Level-1 data files were provided by CGHub
   - over 37,000 of these files are available in Google Cloud Storage (GCS)
   - roughly 90% of these BAM files contain exome data, the remaining 10% contain whole-genome data
   - BAM index (BAI) files are also available for all BAM files
* mRNA- and microRNA-seq BAM files:  these Level-1 data files were provided by CGHub
   - over 13,000 mRNA-seq BAM files are available in GCS
   - over 16,000 miRNA-seq BAM files are available in GCS
* mRNA-seq FASTQ files:  these Level-1 data files were provided by CGHub and include over 11,000 tar files

in Google Cloud Storage
***********************

At this time, all of these controlled-access data files are stored in GCS in the original form, as obtained from the data repository.  

In order to access these controlled data, a user of the ISB-CGC must first be authenticated by NIH (via the ISB-CGC web-app).
Upon successful authentication, the user's dbGaP authorization will be verified.  These two steps are required before the user's
Google identity is added to the access control list (ACL) for the controlled data.  At this time, this access must be renewed
every 24 hours.


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
