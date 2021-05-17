*************************
Variant Call Format (VCF)
*************************

Variant Call Format (VCF) is the standard file format which stores variants (structural variants such as SNPs and indels) identified from next generation sequencing data. More information on the specifications and the VCF file format can be found here: https://samtools.github.io/hts-specs/ 

As variant data continues to grow both in the amount of data generated as well as in size,  researchers face the challenge of having to identify ways to analyze large variant data sets.  The traditional way of downloading individual VCF files to compute on local machines is untenable and prohibitive.  As a solution to this problem, ISB-CGC has created a VCF extract, transform and load (ETL) pipeline that produces Google BigQuery tables that serve as central repositories for VCF files for a given cancer program (e.g. TCGA, TARGET). For example, the ETL process takes all VCF files from TARGET and transforms them into a single BigQuery table. Instead of analyzing variant data one VCF file at a time, with the variant data all in one central BigQuery table users will be able to query and interrogate the data without the need to download. In addition, we have ensured that the ETL process maintains the column composition of the VCF file format that researchers are familiar with. 


VCF BigQuery Table
===================

Because VCF files at the GDC contain sensitive patient information which cannot be displayed to the public, they are deemed controlled-access, meaning only authorized users can access the data. For the purposes of demonstration, we have generated a random VCF file that emulates a typical TCGA VCF file. The BigQuery table in the image below was generated using the randomized VCF file and mimics a controlled access VCF BigQuery table. 

.. note:: The actual BigQuery variant data tables are not randomized and are controlled access.

The first 11 columns, seen in the image, begin just as a VCF file does. In addition to keeping a similar structure, the new table splits VCF columns such as NORMAL and TUMOR into their own individual columns. The objective of the flattened file is to bring ease and understandability to our users who have worked with VCF files in the past or who are brand new to this area of research. 

.. figure:: BigQuery_VCF_Flattened.png 
   :scale: 50
   :align: center
  
.. note:: The tables found in our repository are clustered based on CHROM, ID, analysis_workflow_type, and project_short_name. This will help with faster queries and reducing costs. 


Accessing Controlled Variant Data 
=================================
Some ISB-CGC BigQuery tables contain sensitive information about patients. These type of files are known as controlled access files. To obtain access to this controlled data, please follow the steps in the `Accessing Controlled Data <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/Gaining-Access-To-Controlled-Access-Data.html>`_ page.   

Controlled access VCF BigQuery tables can be found in the project **isb-cgc-cbq**. All VCF tables on BigQuery are stored under their parent program. For instance, the GDC release 22 TARGET VCF BigQuery table will found in the data sets known as "TARGET" and "TARGET_versioned" in the project isb-cgc-cbq. 

ISB-CGC BigQuery Table Search 
-----------------------------
To see the available VCF BigQuery tables hosted on our Google Cloud projects, visit our `ISB-CGC BigQuery Table Search <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/BigQueryTableSearchUI.html>`_ and select **VCF** for the Filter **Data Type**. Preview of the data won't be available because the data is controlled access.


VCF Programs Available
^^^^^^^^^^^^^^^^^^^^^^
* TARGET 

VCF Programs Coming Soon
^^^^^^^^^^^^^^^^^^^^^^^^
* TCGA 
* FM 
* HCMI 
* VAREPOP
* ORGANOID
* CPTAC
* BEATAML 1.0 


      
