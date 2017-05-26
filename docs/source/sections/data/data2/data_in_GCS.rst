##############################
Data in Cloud Storage
##############################

At this time, all controlled-access data files are stored in Google Cloud Storage (GCS) 
in their original form, as obtained from the data repository.  This includes
these major data types and formats:

    - RNA-Seq **FASTQ** files (unaligned reads, typically compressed tar-files)
    - DNA-Seq and RNA-Seq **BAM** files (aligned reads)
    - Genome-Wide SNP6 array **CEL** files
    - Variant-calls in **VCF** files

In order to access these controlled data, a user of the ISB-CGC must first be 
authenticated by NIH (via the ISB-CGC web-app).
Upon successful authentication, the users's dbGaP authorization will be verified.  
These two steps are required before the user's
Google identity is added to the access control list (ACL) for the controlled data.  
At this time, this access must be renewed every 24 hours.


Summary of Data Available in GCS
================================

+----------+--------------+--------------+--------------+
+  Format  +   Data Type  +  # of Files  +  Total Size  +
+----------+--------------+--------------+--------------+
+  BAM     +  DNA-Seq     +     73487    +   1407 TB    +
+----------+--------------+--------------+--------------+
+  BAM     +  RNA-Seq     +     47818    +    216 TB    +
+----------+--------------+--------------+--------------+
+  FASTQ   +  RNA-Seq     +     13207    +     91 TB    +
+----------+--------------+--------------+--------------+
+  CEL     +  DNA (SNP6)  +     22529    +      1.6 TB  +
+----------+--------------+--------------+--------------+
+  VCF     +  DNA-Seq     +     47319    +      0.5 TB  +
+----------+--------------+--------------+--------------+


Working with data in GCS
========================

Working with large-scale data hosted by the ISB-CGC in Google Cloud Storage
requires some familiarity with tools such as the 
`Google Cloud SDK <https://cloud.google.com/sdk/>`_,
`Google Compute Engine <https://cloud.google.com/compute/>`_, 
`Virtual Machines <https://en.wikipedia.org/wiki/Virtual_machine>`_ and
`Docker <https://www.docker.com/what-docker#/VM>`_.

Please see our 
`DIY Workshop <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/DIYWorkshop.html>`_ 
and in particular the section on "Computing in the Cloud" for additional references and tutorial material.

Our metadata tables in BigQuery can be used to explore the available data and choose
which BAM files you're most interested in working with -- before you take on 
processing an entire petabyte of data!  Feel free to email us at info@isb-cgc.org
with questions.

BAM-slicing in the Cloud
========================

BAM files can vary in size from close to 1 TB down to 1 MB, and frequently a researcher
is only interested in extracting a small slice of the entire sequence.  This is referred
to as "BAM-slicing" and the latest release (`1.4 <https://github.com/samtools/htslib/releases/tag/1.4>`_) of the 
`htslib library <https://github.com/samtools/htslib>`_ adds the capability to 
perform BAM-slicing directly on BAM files in GCS to widely used tools such as
`samtools <https://github.com/samtools/samtools>`_.  
(You will need to build with ``--enable-libcurl``
to enable support for access to data both in GCS and S3.)
This new functionality allows you to run, for example:

.. code-block:: none

   $ ./samtools view gs://isb-cgc-open/NCI-GDC/legacy/CCLE/CCLE-LUSC/WXS/Aligned_reads/0a109993-2d5b-4251-bcab-9da4a611f2b1/C836.Calu-3.2.bam 7:140453130-140453140

If you want to access a controlled-access BAM file, you'll need to provide credentials first:

.. code-block:: none

   $ export GCS_OAUTH_TOKEN=`gcloud auth application-default print-access-token`

If you run into problems, it's a good idea to verify that you have the correct url and 
also that you have access to this file by using the 
`gsutil <https://cloud.google.com/storage/docs/gsutil>`_ command-line tool from the 
`cloud SDK <https://cloud.google.com/sdk/>`_:

.. code-block:: none

   $ gsutil ls -l gs://isb-cgc-open/NCI-GDC/legacy/CCLE/CCLE-LUSC/WXS/Aligned_reads/0a109993-2d5b-4251-bcab-9da4a611f2b1/C836.Calu-3.2.bam

Other Options for BAM-slicing
-----------------------------

The `NCI-GDC <https://gdc.cancer.gov/>`_ has also implemented a BAM-slicing API on top of
their data repository.  This API can be accessed programmatically as documented
`here <https://docs.gdc.cancer.gov/API/Users_Guide/BAM_Slicing/>`_ 
or interactively on any of the file-specific data-portal pages like 
`this one <https://gdc-portal.nci.nih.gov/files/91081819-79c8-4de6-bfdb-742df760c08b>`_
for a TCGA-BRCA whole-exome BAM file.  (The "BAM Slicing" button is in the upper
right corner of the page.)

The GA4GH API provides another option to BAM-slicing, and has been implemented
by Google on top of the database-backed Google Genomics technology.  You can
find more information about the GA4GH API 
`here <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/data2/data_in_GG.html>`_
with information about some open-access data hosted by the ISB-CGC which you
are welcome to experiment with.

