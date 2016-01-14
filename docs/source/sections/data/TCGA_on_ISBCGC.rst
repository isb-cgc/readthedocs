****************
Hosted TCGA Data 
****************

All TCGA *metadata* is considered open-access.  In other words, information *about* controlled-access data 
files is open-access.  Metadata can be obtained programmatically using the ISB-CGC programmatic API.

An overview of the TCGA data currently hosted on the ISB-CGC platform is provided in the two sections below.
The first section breaks the data down by access class (open *vs* controlled), and the second section breaks
it down by original source repository (DCC *and* CGHub).

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

in BigQuery
-----------

The information scattered over tens of thousands of XML and TSV files is provided in a *much more accessible* form in
For more details about these BigQuery tables, including tutorials and code examples in 
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

TCGA Data by Source Repository
##############################

TCGA Data at the DCC
====================

Complete sets of open-access and controlled-access data archives were copied from the DCC on October 4th, 2015
into Google Cloud Storage.

Note that for every archive at the DCC, there may be multiple revisions of an archive.  A list of the current 
`latest archives <http://tcga-data.nci.nih.gov/datareports/resources/latestarchive>`_
can be obtained from the DCC.
The archive 
`naming convention <https://wiki.nci.nih.gov/display/TCGA/TCGA+Data+Archives#TCGADataArchives-NamingConventions>`_
includes the disease code, the platform/pipeline name, the archive type (*eg* data level), the serial index
(which is often the batch number), and the revision number.
If you want to check whether there is a newer version of a specific archive at the DCC than what we currently
have on the ISB-CGC platform, you can check the date column in the latest archive report mentioned above,
or you can compare the archive name to these lists of 
`open-access archives <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/DCC_archives.04oct2015.open.tsv>`_
and 
`controlled-access archives <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/DCC_archives.04oct2015.cntl.tsv>`_
based on our most recent upload.

Note that all "bio" archives (containing clinical, biospecimen, and other types of XML files) were recently migrated to a new
XSD which is not backwards compatible with the previous XSD.  This update took place over the course of the 
month of December 2015 and  none of these new archives are included in any of the current ISB-CGC BigQuery tables or files in GCS.

TCGA Data at CGHub
==================

The complete 
`listing <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/GCS_listing.v2.tsv>`_
of the TCGA data files from CGHub that are currently available in Google Cloud Storage (GCS)
contains the following three columns of information: 

* unique CGHub id for the file, 
* the partial GCS object path, and
* the size of the file in bytes.

The latest complete CGHub manifest can be 
`downloaded directly from CGHub <https://cghub.ucsc.edu/reports/SUMMARY_STATS/LATEST_MANIFEST.tsv>`_ (67 MB spreadsheet).

