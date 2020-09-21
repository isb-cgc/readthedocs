Variant Data in BigQuery
************************

Here we illustrate how variant data is stored in ISB-CGC BigQuery tables using our own internal ETL pipeline. 

VCFs
====

ISB-CGC has developed an ETL pipeline to take controlled access VCF files found at Genomic Data Commons (GDC). This transforms pipeline is able to take the terabytes of variant data found at GDC and transform them into one large and flattened Google BigQuery table. The transforms pipeline ISB-CGC has developed allows researchers to query, use command line tools, or use a programming language of your choice to gain statistical insights of an analysis someone might be interested in.

.. toctree::
   :maxdepth: 1
   :hidden:
   
   
 
How To Query The Tables
=======================

Using BigQuery the variant tables can used to analyze the data through SQL queries. 

.. toctree::
   :maxdepth: 1
   :hidden:
   
   VariantSQLExamples
