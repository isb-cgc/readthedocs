
Variant Call Format (VCF)
========================


Variant Call Format (VCF) is the standard file format which stores identified variants within sequenced data. The creation of VCF files starts with the whole genome sequencing (WGS) or whole exome sequencing (WXS) process, resulting in FASTQ files. The file containing the sequenced genome is then aligned to the appropriate reference genome which then generates a SAM, BAM, or CRAM file. The last step is to generate the VCF file from either of the three alignment files; the differing aligned reads will be identified when comparing to the reference genome and written out to a VCF file.

As variant data is increasing and growing in size, researchers face the problem of being able to analyze all the new data arriving as well as the old data. The new and old VCF files that are being curated by all these programs (Ex. TCGA,TARGET, and FM) are stored as individual files on local computers or on High Performance Computing (HPCs) for download. Researchers face the problem of analyzing these large scale data at once to gain insights for the analysis they are running. 


Accessing Controlled Variant Data 
=================================
Some ISB-CGC Bigquery tables contain sensitive information about patients. These type of files are known as controlled access files. To obtain access to our controlled data, please follow the steps in our `Accessing Controlled Data <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/Gaining-Access-To-Controlled-Access-Data.html>`_ page to obtain permission.   


Flattened VCF BigQuery Table
============================

The approach that the ISB-CGC variant transforms tools took was to engineer a Google BiqQuery table that mimics a VCF file format. The flattened table format allows for an easy and familiar format if you have worked with VCF files in the past. The output of the table is shown to be “flat” because the structure of the generated table contains no form of nesting. The BigQuery table presented in the picture below is a file which was created through a python script with randomized values for each column to mimic a controlled access VCF file. This randomly generated file was done because the nature of the VCF files found on GDC contains sensitive patient information, which can not be displayed to the public. In this picture, we display a table generated to emulate a TCGA VCF file. The first 11 columns, seen in the image, begin just as a VCF file does. In addition to keeping a similar structure, the new table splits VCF columns such as NORMAL and TUMOR into their own individual columns. The objective of the flattened file is to bring ease and understandability to our users who have worked with VCF files in the past or who are brand new to this area of research. 

.. figure:: BigQuery_VCF_Flattened.png 
   :scale: 50
   :align: center
  
.. note:: The tables found in our repository are clustered based on CHROM, ID, analysis_workflow_type, and project_short_name. This will help with faster queries and reducing costs. 



      
