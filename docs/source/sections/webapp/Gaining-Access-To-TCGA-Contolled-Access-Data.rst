************************************************
Gaining Access to TCGA Controlled Access Data
************************************************
To obtain access to TCGA Controlled Access Data (either through the Web Application or Google Virtual Machines) you must associate a Google Account with a valid NIH login that is associated with a dbGaP project (either an eRA account ID or an NIH account User ID) through the Web Application. Visit `electronic Research Administration (eRA) <http://era.nih.gov>`_ for more information on registering for a NIH eRA account. NIH staff may utilize their NIH log-in. (See additional instructions at `Data Access Request Instructions <http://www.genome.gov/20019654>`_) dbGap Data Access `Request Portal <http://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?login=&page=login>`_; 

For more information on how to obtain dbGaP authorization to access TCGA controlled access data go to our `Frequently Asked Questions (FAQs) page, subsection Data Access** <http://http://isb-cancer-genomics-cloud.readthedocs.org/en/latest/sections/FAQ.html?>`_.


**Linking a valid NIH login with your Google Account** To link a valid NIH login with your Google Account that you have used to login to the ISB-CGC system, select the "persona" icon beside your login name (A in the image below) after you have logged into the ISB-CGC Web Application.  For more information see `FAQ Accounts and Cloud Projects <http://isb-cancer-genomics-cloud.readthedocs.org/en/latest/sections/FAQ.html?>`_ Section. 

.. image:: personaeicon-NIHLoginAssoc.png
   :scale: 50
   :align: center

You will then see the following page:

.. image:: NIHAssociationPage.png
   :scale: 50
   :align: center

**What data can I access if I don't have a dbGaP Authorization?** (or I have not done the ISB-CGC login in the last 24 hours)  You can access all the open access data in ISB-CGC, both through the Web Application as well as the `Programmatic User Interface <../Prog-APIs.rst>`_.  For more information about the Cloud Hosted Data go to `this part of our online documentation <../Hosted-Data.rst>`_.

**Non-eRA users** (Open Access Only)
************************************
The **Open-Access** TCGA data hosted by the ISB-CGC Platform includes:

• Clinical (de-identified) and Biospecimen data: these data were originally provided in XML files (Level-1) by the DCC;
• Somatic mutation data: these data were originally provided in MAF files (Level-2) by the DCC;
• DNA copy-number segments: these data were originally provided as segmentation files (Level-3) by the DCC;
• DNA methylation data: these data were originally provided as TSV files (Level-3) by the DCC;
• Gene (mRNA) expression data: these data were originally provided as TSV files (Level-3) by the DCC;
• microRNA expression data: these data were originally provided as TSV files (Level-3) by the DCC;
• Protein expression data: these data were origially provided as TSV files (Level-3) by the DCC; and
• TCGA Annotations data: annotations were obtained from the TCGA Annotations Manager

eRA Users (Authorized to Access Controlled Data)
************************************************
The **Controlled-Access** TCGA data hosted by the ISB-CGC Platform includes:

• SNP array CEL files: these Level-1 data files were provided by the DCC and include over 22,000 files for both tumor and matched-normal samples;
• VCF files: these Level-2 data files were provided by the DCC and include over 15,000 files produced by several different centers (primarily Broad and BCGSC);
• MAF files: these “protected” mutation files (Level-2) were provided by the DCC (note that these files were not generated uniformly for all tumor types);
• DNA-seq BAM files: these Level-1 data files were provided by CGHub;•over 37,000 of these files are available in Google Cloud Storage (GCS);
• roughly 90% of these BAM files containe exome data, the remaining 10% contain whole-genome data;
• BAM index (BAI) files are also available for all BAM files;
• mRNA- and microRNA-seq BAM files: these Level-1 data files were provided by CGHub;•over 13,000 mRNA-seq BAM files are available in GCS;
• over 16,000 miRNA-seq BAM files are available in GCS;

• mRNA-seq FASTQ files: these Level-1 data files were provided by CGHub and include over 11,000 tar files.



STILL NEEDS WORKING
* How to associate
* How to remove association
* 1:1 forced mapping for Google account and eRA ID
* Requirement to follow dbGaP DUC
* Need to revalidate after 24 hours (and times shown for validation)
* Validation validates both GUI as well as Virtual Machine (scripting through UNIX) interactions
