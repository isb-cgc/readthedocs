************************************************
Accessing TCGA Controlled Data
************************************************
To obtain access to TCGA controlled-access data (either through the Web Application or programmatically) 
you must associate your Google identity with a valid NIH login that is associated with a dbGaP project 
(either an eRA account ID or an NIH account User ID) through the Web Application.  This association
is created when you successfully authenticated through NIH.  Your NIH identity will then be 
checked against the current dbGaP whitelist to verify that you are authorized to view and access
the TCGA controlled data.

Visit `electronic Research Administration (eRA) <http://era.nih.gov>`_ for more information on 
registering for a NIH eRA account. NIH staff may utilize their NIH log-in. 
(For additional instructions, please refer to `Data Access Request Instructions <http://www.genome.gov/20019654>`_, 
dbGap Data Access `Request Portal <http://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?login=&page=login>`_, 
and `Understanding Data Security <http://isb-cancer-genomics-cloud.readthedocs.org/en/latest/sections/data/data2/TCGA_Data_Security.html>`_). 

Once you have authenticated to NIH via the web-app, and your dbGaP authorization has been verified, the 
Google identity associated with your account will have access to the controlled-data for 24 hours.

For more information on applying for dbGaP authorization to access TCGA controlled access, please see our 
Frequently Asked Questions (FAQ) 
`page <http://http://isb-cancer-genomics-cloud.readthedocs.org/en/latest/sections/FAQ.html?>`_ 
or the "How to" `Apply for Controlled Access Data Video <http://www.youtube.com/watch?v=-3tUBeKbP5c>`_.

Linking your NIH and Google identities
**************************************
To link your NIH identity with your Google identity (ie the Google account you used to login to the ISB-CGC system), 
select the "persona" icon next to your login name (A in the image below) after you have signed in to the ISB-CGC Web Application.  

.. image:: personaeicon-NIHLoginAssoc.png
   :scale: 50
   :align: center

You will then see the following page:

.. image:: NIHAssociationPage.png
   :scale: 50
   :align: center
   
Now you need to associate your Google identity with your NIH identity.  (Your NIH identity is the one associated
with your dbGaP application and authorization to work with TCGA controlled data.) 
To do this, select the "Associate with eRA Commons Account" link (highlighted in diagram above, and labeled A).  
You will then be re-directed to an NIH login page to be authenticated by NIH:

.. image:: iTrust.png
   :scale: 50
   :align: center

If you have an eRA identification, use this to sign in through panel A (see example above).  
If you have an NIH PIV card, use that to sign in through panel B on this page (see above).  
Once you have been authenticated by NIH, and your NIH identity has been verified to be on
the current dbGaP whitelist, you will have access to controlled data for 24 hours.  
(To renew your access, you will need to repeat this process.)

.. image:: LogInandUnlink.png
   :scale: 50
   :align: center

Please note: the ISB-CGC system will enforce one-to-one relationship between NIH identities
and Google identites.  In other words, a single NIH identity may not be used to attempt to
gain access to to controlled data by multiple Google identities.
If you need to *unlink* your eRA account from your Google account (for example if you want to
change which Google identity you use to sign in to the ISB-CGC platform), you may do so by
selecting "Unlink <GoogleID> from the NIH username <eRA Commons ID>" (link B in the screen above).

To end your web-app session, just "Sign Out" by using the pull-down below your name 
(see image below, A).  After you sign out from the ISB-CGC web-app, your Google identity may 
still be signed in to your browser, so you may want to also sign out of the browser.

.. image:: SignOut.png
   :scale: 50
   :align: center

Extending Your Access by 24 hours From Now
******************************************
Once you have received permission to view controlled access data, your user login page will look like the screenshot below. If you need to extend your access to controlled data for another 24 hours from now (e.g. if your compute job is still running on data that is controlled access), select the link "Extend controlled access period to 24 hours from now" (red box on figure below).  Your time of access will be extended to 24 hours from the time you push the link. 

.. image:: 24hrExtension.png
   :scale: 50
   :align: center


Available TCGA Data: Open- and Controlled-Access
################################################

Open Access Data 
================

All of the open-access data hosted by the ISB-CGC is immediately accessible to all users, without
NIH authentication nor dbGaP authorization required.  These open-access data can be explored
both through the Web Application and through the `Programmatic User Interface <../Prog-APIs.rst>`_.  
For additional details about all hosted data sets, please see this `section <../Hosted-Data.rst>`_.

The **Open-Access** TCGA data hosted by the ISB-CGC Platform includes:

• Clinical (de-identified) and Biospecimen data: these data were originally provided in XML files (Level-1) by the DCC;
• Somatic mutation data: these data were originally provided in MAF files (Level-2) by the DCC;
• DNA copy-number segments: these data were originally provided as segmentation files (Level-3) by the DCC;
• DNA methylation data: these data were originally provided as TSV files (Level-3) by the DCC;
• Gene (mRNA) expression data: these data were originally provided as TSV files (Level-3) by the DCC;
• microRNA expression data: these data were originally provided as TSV files (Level-3) by the DCC;
• Protein expression data: these data were origially provided as TSV files (Level-3) by the DCC; and
• TCGA Annotations data: annotations were obtained from the TCGA Annotations Manager

Controlled-Access Data
======================

Controlled-access data is accessible only to users who have been authenticated by NIH
and whose dbGaP authorization has been verified.

The **Controlled-Access** TCGA data hosted by the ISB-CGC Platform includes:

• SNP array CEL files: these Level-1 data files were provided by the DCC and include over 22,000 files for both tumor and matched-normal samples;
• VCF files: these Level-2 data files were provided by the DCC and include over 15,000 files produced by several different centers (primarily Broad and BCGSC);
• MAF files: these *protected* mutation files (Level-2) were provided by the DCC (note that these files were not generated uniformly for all tumor types);
• DNA-seq BAM files: these Level-1 data files were provided by CGHub (roughly 90% of these BAM files containe exome data, the remaining 10% contain whole-genome data);
• mRNA- and microRNA-seq BAM and/or FASTQ files: these Level-1 data files were provided by CGHub;
• finally, BAM index (BAI) files are available for all BAM files;

Your Responsibilities 
=====================
You should think about securing controlled data within the context of your GCP project in the same way 
that you would think about securing controlled data that you might download to a file-server or 
compute-cluster at your own institution. Your responsibilities for data protection are the same in a 
cloud environment. For more information, please refer to 
`NIH Security Best Practices for Controlled-Access Data <http://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/GetPdf.cgi?document_name=dbgap_2b_security_procedures.pdf>`_.

NIH has tried to provide as much information as possible for PIs, institutional signing officials (SOs) and 
the IT staff who will be supporting these projects, to make sure they understand their responsibilities.” 
(Ref: `The Cloud, dbGaP and the NIH blog post 03.27.2015 <http://datascience.nih.gov/blog/cloud>`_)


