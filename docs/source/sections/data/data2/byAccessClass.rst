TCGA Data by Access Class
#########################

Open-Access TCGA Data
=====================

The open-access TCGA data hosted by the ISB-CGC Platform includes:

* Clinical (de-identified) and Biospecimen data: these data were originally provided in XML files (Level-1) by the DCC;
* Somatic mutation data:  these data were originally provided in MAF files (Level-2) by the DCC;
* DNA copy-number segments:  these data were originally provided as segmentation files (Level-3) by the DCC;
* DNA methylation data:  these data were originally provided as TSV files (Level-3) by the DCC;
* Gene (mRNA) expression data:  these data were originally provided as TSV files (Level-3) by the DCC;
* microRNA expression data:  these data were originally provided as TSV files (Level-3) by the DCC;
* Protein expression data:  these data were origially provided as TSV files (Level-3) by the DCC; and
* TCGA Annotations data:  annotations were obtained from the `TCGA Annotations Manager <https://tcga-data.nci.nih.gov/annotations>`_

in Google Cloud Storage (GCS)
-----------------------------

The data files described above are available to all ISB-CGC users in an open-access GCS bucket (gs://isb-cgc-open).

.. _in_BigQuery:

in BigQuery
-----------

The information scattered over tens of thousands of XML and TSV files at the DCC is provided in a *much more accessible* form in
a series of BigQuery tables.  For more details, including tutorials and code examples in 
`Python <https://github.com/isb-cgc/examples-Python>`_ or 
`R <https://github.com/isb-cgc/examples-R>`_, please see our `github repositories <https://github.com/isb-cgc>`_.

This `introductory tutorial <https://github.com/isb-cgc/examples-Python/blob/master/notebooks/The%20ISB-CGC%20open-access%20TCGA%20tables%20in%20BigQuery.ipynb>`_
gives a great overview of all of the tables and pointers on how to get started exploring them.  Be sure to check it out!

Controlled-Access TCGA Data
===========================

The controlled-access TCGA data hosted by the ISB-CGC Platform includes:

* SNP array CEL files:  these Level-1 data files were provided by the DCC and include over 22,000 files for both tumor and matched-normal samples;
* VCF files:  these Level-2 data files were provided by the DCC and include over 15,000 files produced by several different centers (primarily Broad and BCGSC);
* MAF files:  these "protected" mutation files (Level-2) were provided by the DCC (note that these files were not generated uniformly for all tumor types);
* DNA-seq BAM files:  these Level-1 data files were provided by CGHub;
   - over 37,000 of these files are available in Google Cloud Storage (GCS);
   - roughly 90% of these BAM files containe exome data, the remaining 10% contain whole-genome data;
   - BAM index (BAI) files are also available for all BAM files;
* mRNA- and microRNA-seq BAM files:  these Level-1 data files were provided by CGHub;
   - over 13,000 mRNA-seq BAM files are available in GCS;
   - over 16,000 miRNA-seq BAM files are available in GCS;
* mRNA-seq FASTQ files:  these Level-1 data files were provided by CGHub and include over 11,000 tar files.

in Google Cloud Storage
-----------------------

At this time, all of these controlled-access data files are stored in GCS in the original form, as obtained from the data repository.  

In order to access these controlled data, a user of the ISB-CGC must first be authenticated by NIH (via the ISB-CGC web-app).
Upon successful authentication, the users's dbGaP authorization will be verified.  These two steps are required before the user's
Google identity is added to the access control list (ACL) for the controlled data.  At this time, this access must be renewed
every 24 hours.

in Google Genomics
------------------

In the future, BAM and VCF data will also be available in other forms in order to allow other modes of data
access (*eg* using the GA4GH API).  This will open up new, faster, more "cloud-aware" approaches to working with these data
(as illustrated by some of these Google Genomics `Cookbooks <https://googlegenomics.readthedocs.org/en/latest/sections/analyze_data.html>`_).

