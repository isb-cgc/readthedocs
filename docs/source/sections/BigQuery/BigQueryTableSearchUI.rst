******************************
ISB-CGC BigQuery Table Search 
******************************

The ISB-CGC BigQuery Table Search user interface (URL) is a discovery tool that allows users to explore and search for ISB-CGC hosted BigQuery tables. 

**Note**: Users are not required to already have a Google Cloud Platform (GCP) project to learn more about the tables hosted by ISB-CGC. 

.. image:: BigQueryTableSearchUI.png
   :align: center



Currently, ISB-CGC hosts over 300 Open Access BigQuery Tables. Each table has been manually curated to include detailed table and field descriptions allowing users to search for tables of interest using a wild card search or via number of filters including: 

Status
======
You can find out what tables are current, deprecated or archived. 

Catgories
==========
The tables are grouped into 4 high-level categories: 

* Clinical Biospecimen Data (includes clinical tables with patient demographic data, Biospecimen data with detailed sample information)

* File Metadata (includes tables with information about files available at the GDC, including GCS paths, creation dates, sizes, etc)

* Genomic Reference Database (examples include  COSMIC, ClinVar, cytoBand, dbSNP, Ensembl, Ensembl2Reactome)

* Processed-omics  Datasets (gene expression, miRNA expression, copy number, somatic mutations, methylation)

Reference Genome Build
======================
You can filter for tables that contain data for hg19 or hg38. In a few cases, there are tables for which information from both genome builds can be found. For example, tables that include liftover coordinates between the reference builds. 

Source
======================
Search through the sources of our BigQuery tables using the Source filter. Sources of available tables are listed and searchable using the source filter.

Data Type
===========
The data type filter allows you to filter for the filters of interest. 

Advanced Filters
================
For users already familiar with the BigQuery tables (including dataset ID, table ID, table description, or a particular field name), you can use the advanced filters. 
The advanced filters allow users to search by dataset ID, table ID, table description or a field name of interest. 

Labels
=======


 
