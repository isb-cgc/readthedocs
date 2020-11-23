Variant Data in BigQuery
************************

ISB-CGC has developed an extract, transform and load (ETL) pipeline to take controlled access Variant Call Format (VCF) files found at the Genomic Data Commons (GDC) and transform those terabytes of variant data into queryable Google BigQuery tables. Our pipeline allows researchers to query, use command line tools, or use a programming language of their choice to gain statistical insights of an analysis.

To learn more about the VCF format and the ISB-CGC variant data BigQuery tables, see the following section. 

.. toctree::
   :maxdepth: 1
   
   ControlledAccessVCF
   
 
How To Query The Tables
=======================

The variant data tables can be queried using SQL.  For examples, see `Variant Data SQL Query Examples <VariantSQLExamples.html>`_.

.. toctree::
   :maxdepth: 1
   :hidden:
   
   VariantSQLExamples
