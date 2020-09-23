Variant Data in BigQuery
************************

Here we illustrate how variant data is stored in ISB-CGC BigQuery tables using our own internal ETL pipeline. 

VCFs
====

ISB-CGC has developed an extract, transform and load (ETL) pipeline to take controlled access VCF files found at Genomic Data Commons (GDC) and transform those terabytes of variant data into one large and flattened Google BigQuery table. The transforms pipeline ISB-CGC has developed allows researchers to query, use command line tools, or use a programming language of their choice to gain statistical insights of an analysis.


.. toctree::
   :maxdepth: 1
   :hidden:
   
   ControlledAccessVCF
   
 
How To Query The Tables
=======================

Using BigQuery the variant tables can used to analyze the data through SQL queries. 

.. toctree::
   :maxdepth: 1
   :hidden:
   
   VariantSQLExamples
