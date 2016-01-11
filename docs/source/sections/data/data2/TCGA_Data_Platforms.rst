*************************************
Understanding the TCGA Data Platforms
*************************************

When working with any of the data types, it is important to also be aware of both the *platform* that was used to generate the underlying raw data as well as the 
*pipeline* that was used to process the data.  For example, over the course of the TCGA study, DNA methlyation data was obtained using first the Illumina
HumanMethylation27 platform, and later using the HumanMethylation450 platform.  Any analysis that combines data from these two platforms across a cohort of
samples should take this into consideration.  Another example where multiple platforms and/or pipelines were used to produce a single data type is the Level-3 gene
expression data: most tumor samples were processed at UNC and the normalized gene-expression values are based on the RSEM method, while some tumor samples were
processed at BCGSC and the normalized gene-expression values are based on RPKM.

