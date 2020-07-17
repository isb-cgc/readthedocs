************************************************
Accessing Controlled Data
************************************************

Accessing **controlled data** is achieved in two different ways, depending on how you are using it: 

  - `Interactive computing <Controlled-data-Interactive.html>`_ (*e.g.* the Web App or R Studio) or, 
    * Provides access to controlled data for 24 hours at a time
    * Uses your *personal* credentials
      
  - `Programmatic computing <Controlled-data-GCP.html>`_ (*e.g.* a program running from a Google Virtual Machine Compute Engine you have started).
    * Provides access to controlled data for seven days at a time
    * Uses the credentials of a *service account*, acting on your behalf
    
You can use both methods at the same time; they are not mutually exclusive.


No matter which way you intend to request controlled access via ISB-CGC, you'll need the following first:

   * A Google identity
   * An NIH or eRA account
   * dbGaP permission for each type of controlled access data of interest, linked to your NIH or eRA account
   

.. image:: Controlled-Access-Flowchart.png
   :align: center

**You must have a Google identity**

If you don't have a Google Identity yet, please see the  `ISB-CGC Quick-Start Guide <HowToGetStartedonISB-CGC.html>`_. 

**You must have either an NIH or eRA account.**

Before you can access *any* controlled-data hosted by the ISB-CGC,
you must first associate your Google identity (which you use to sign in to the ISB-CGC WebApp and
access the Google Cloud) with a valid NIH or eRA account associated with a dbGaP data-access request

Visit `electronic Research Administration (eRA) <http://era.nih.gov>`_ for more information on 
registering for a NIH eRA account. NIH staff may utilize their NIH log-in. 
(For additional instructions, please refer to `Tips for Preparing a Successful Data Access Request <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/GetPdf.cgi?document_name=GeneralAAInstructions.pdf>`_, 
and `Understanding Data Security <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/TCGA_Data_Security.html>`_).  Please be sure to review the Data Use Certification Agreement for `TCGA controlled data <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000178.v9.p8>`_ and `TARGET controlled data <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000218.v17.p6>`_. 

This is done through the Web App: you will 
first be redirected to an NIH login page, and once you have successfully authenticated,
ISB-CGC will store an association between your NIH identity and your Google identity.
(Note that this should be a one-to-one association.)

**Your eRA (or NIH) account must be linked to dbGaP permissions.**

Once you have authenticated, ISB-CGC will check which datasets, e.g. TCGA controlled data and/or TARGET controlled data you have been authorized (by dbGaP) to access.  ISB-CGC obtains an updated whitelist for each of the hosted datasets from
dbGaP every day.  If you have just recently been granted access by dbGaP, there may be a 24 hour
delay before you will be able to request access to these data on ISB-CGC.

For more information on applying for dbGaP authorization to access controlled data, please see 
the "How to" `Apply for Controlled Access Data Video <http://www.youtube.com/watch?v=-3tUBeKbP5c>`_.

Once you have authenticated to NIH via the Web App, and your dbGaP authorization has been verified, the 
Google identity associated with your account will have access to the controlled-data for 24 hours.

.. toctree::
   :maxdepth: 1
   :hidden:
   
   Controlled-data-Interactive
   Controlled-data-GCP
   
   
