
Variant Call Format (VCF)
========================

ADD NORMAL TUMOR BAM CAVEAT 
SQL JOIN EXAMPLES 
TARGET WGS vs WXS VCFs - SQL examples 

Variant Call Format files (VCF) are the standard file format to store identified variants within sequenced data. The creation of VCF files start from sequencing whole genomes (WGS) or whole exome sequencing (WXS) that create FASTQ files. The file containing the sequenced genome is then aligned to the appropriate reference genome which then generates a SAM, BAM, or CRAM files. The last step to generate the VCF file from either of the three alignment files, the differing aligned reads will be identified when comparing to the reference genome and written out to a VCF file.

As variant data is increasing and growing in size researchers face the problem of being able to analyze all the new data arriving as well as the old data. The new and old VCF files that are being curated by all these programs (Ex. TCGA,TARGET, and FM) are stored as individual files on local computers or on High Performance Computing (HPCs) for download. Researchers face the problem of analyzing these large scale data at once to gain insights for the analysis they are running. 


Accessing Controlled Variant Data 
=================================
Some ISB-CGC Bigquery tables contain sensitive information about patients. These type of files are known as controlled access files. To obtain access to our controlled data please follow the steps in our `Accessing Controlled Data <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/Gaining-Access-To-Controlled-Access-Data.html>`_ page to obtain permission.   



Flattened VCF BigQuery Table
============================

The approach that the ISB-CGC variant transforms tools took was to engineer an output that mimics a VCF file format. The flattened table format allows for an easy and familiar read if you have worked with VCF files in the past. The BigQuery table presented in the picture is a randomly generated file which is meant to resemble a controlled access VCF file. In this case we generated one that emulates a TCGA vcf file. The first 11 columns seen in the image begin just as a VCF file. In addition to keeping a similar structure to allow further analysis of information, columns such as NORMAL and TUMOR are split into their own individual columns. The objective of the flattened file is to bring ease and understandability to our users that work with VCF files in the past or brand new to this area of research. 

.. figure:: BigQuery_VCF_Flattened.png 
   :scale: 50
   :align: center
  
.. note:: The tables found in our repository are clustered based on CHROM, ID, analysis_workflow_type, and project_short_name. This will help with faster queries and reducing costs. 



      
