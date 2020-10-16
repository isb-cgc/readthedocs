Variant Data in BigQuery
************************


Variant Call Files (VCFs)
=========================

ISB-CGC has developed an extract, transform and load (ETL) pipeline to take controlled access VCF files found at Genomic Data Commons (GDC) and transform those terabytes of variant data into query-able Google BigQuery tables. Our pipeline allows researchers to query, use command line tools, or use a programming language of their choice to gain statistical insights of an analysis.


.. toctree::
   :maxdepth: 1
   :hidden:
   
   ControlledAccessVCF
   
 
How To Query The Tables
=======================

The variant tables can used to queried using SQL.  

.. toctree::
   :maxdepth: 1
   :hidden:
   
   VariantSQLExamples
