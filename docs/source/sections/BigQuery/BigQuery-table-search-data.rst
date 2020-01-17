================
Data Categories
================

Data made available by the ISB-CGC through BigQuery is organized into several *open-access* 
datasets, where a dataset is made up of multiple tables.  Datasets in BigQuery are uniquely identified based on the Google Cloud Platform (GCP) project name (in this case **isb-cgc**), and the dataset name, separated by a colon (or a period, in standard SQL),  *eg* ``isb-cgc.TCGA_bioclin_v0``.  Tables are uniquely identified by appending the table name,
preceded by a period, *eg* ``isb-cgc.TCGA_bioclin_v0.Clinical``.

Clinical Biospecimen Data
==========================

Patient case and sample information (includes clinical tables with patient demographic data, and biospecimen data with detailed sample information).

Clinical
--------

Patient diagnosis, exposures, and demographic data along with Clinical Annotation can be found. 

Biospecimen
------------

Information on cases tissue sample types, along with information on the generation process of data. 

File Metadata
==============

Information about raw data files including Google Cloud Storage paths (e.g. tables with information about files available at the GDC, including GCS paths, creation dates, file uuids, etc.)

Genomic Reference Database
===========================

Genomic information that can be used to cross-reference against processed-omics data tables (e.g. COSMIC, ClinVar, cytoBand, dbSNP, Ensembl, Ensembl2Reactome)

DNA methylation
----------------

Platform reference annnotations, lift over, and liftover to hg38 coordinates workflow is alailable.  Also, includes an extensive characterization of probes on multiple microarray workflows. 

Somatic Mutations
------------------

Refernce for human single nucleotide variations, microsatellites, small-scale insertions, and deletions from multiple tools and databases including Kaviar database. 

Genome Annotation
------------------



Processed -Omics Data
======================

Processed data primarily from the GDC for TCGA, TARGET and CCLE (i.e. raw data that has gone through GDC pipeline processing e.g. gene expression, miRNA expression, copy number, somatic mutations, methylation)

DNA methylation
----------------

Somatic Mutations
------------------

mRNA Expression
----------------

miRNA Expression
-----------------

Protein Quantification
-------------------------

Copy Number
------------

