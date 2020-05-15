******************
How To Get Started on ISB-CGC
******************

The ISB-CGC provides both interactive (through a `web application <https://isb-cgc.appspot.com/>`_) and programmatic access to data hosted by institutes such as the Genomic Data Commons (GDC) of the National Cancer Institute (NCI), and the Wellcome Trust Sanger Institute, leveraging many aspects of the Google Cloud Platform. To get started, you'll need a Google Cloud Project. Additionally, to access controlled data, you'll also need `dbGaP authorization <Gaining-Access-To-Controlled-Access-Data.html>`_.

.. image:: GettingStarted-Steps.png
   :align: center

Google Cloud Project Setup
-----------------------------------------------
A Google Cloud Project (GCP) is required to make use of all of the data, tools, and Google Cloud functionality.

**Obtain a Google identity**

  - Do you have a Google identity already (e.g. a Gmail account)? Your institutional email may be a Google identity (if your institution uses Google Apps), or you may have a personal Gmail address.
  - If not, it only takes a minute to `create a Google identity <https://accounts.google.com/signup/v2/webcreateaccount?dsh=308321458437252901&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount&flowName=GlifWebSignIn&flowEntry=SignUp#FirstName=&LastName=>`_.  You can even link a non-Gmail account (eg. scientist@nih.gov) as a Google identity by `this <https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp&nogm=true>`_ method.

**Ways to fund your Google Cloud work**

  - Create your own GCP project and take advantage of a one-time `$300 Google Credit <https://cloud.google.com/free/>`_.
  - If you have already used this one-time offer (or there is some other reason you cannot use it), please see the information here about how to request `ISB-CGC Cloud Credits <HowtoRequestCloudCredits.html>`_.

**Set up a Google Cloud Project**

  - `Registering the GCP project <Gaining-Access-To-Controlled-Access-Data.html#requirements-for-registering-a-google-cloud-project-service-account>`_
 
  - `Enable Required Google Cloud APIs <https://cloud.google.com/apis/docs/getting-started#enabling_apis>`_
  
Accessing and Analyzing Data via BigQuery
-----------------------------------------------
BigQuery is Google’s native big data analysis tool. It is a serverless, highly scalable data warehouse tool that allows researchers to find meaningful insights from data using standard SQL queries CHEAPLY, and FAST!

**Connect to ISB-CGC's cancer data tables in Google BigQuery**
 
  - To obtain access to the ISB-CGC open access project tables in BigQuery, users can link these tables to their GCP project as described `here <progapi/bigqueryGUI/LinkingBigQueryToIsb-cgcProject.html>`_.
  - To obtain access to the ISB-CGC controlled access project tables in BigQuery, users can link these tables to their GCP project as described `here <progapi/bigqueryGUI/LinkingISB-CGCtoCABQ.html>`_.
  
**Analyze, using ISB-CGC BiqQuery data** 

  - ISB-CGC provides quickstart guides, tutorials and examples in both R and Jupyter notebooks for BigQuery in the  `Tutorials <TutorialsAndHow-ToGuides.html>`_ and `Community Notebooks <HowTos.html>`_ sections of the documentation page. 
 

Accessing and Analyzing Data Stored in Google Cloud Storage 
---------------------------------------------------------------

All data are stored in GDC-owned Google Cloud Storage buckets. Both raw and processed data are stored in these buckets. Most of the raw data is controlled-access and requires proper authorization to access it. Processed data for the most part are open-access. The individual processed data files are stored in GDC-owned Google Cloud storage bucket.

**Access open-access Google Cloud Storage buckets**

  - All individual processed data files are accessible through GDC Google Cloud Storage buckets; ISB-CGC provides pointers to these files. Examples of how to find these URLs are in the section <Hosted-Data.html>`_, on each Program's documentation page.

**Access controlled data, if needed**

  - To access controlled data, users must first be authenticated by NIH (`via the ISB-CGC web-app <Gaining-Access-To-Controlled-Access-Data.html#interactive-access-to-controlled-data>`_). Upon successful authentication, user dbGaP authorization will be verified. These two steps are required before the user’s Google identity is added to the access control list (ACL) for the controlled data. At this time, this access must be renewed every 24 hours.
  
**Work with Google Compute and Virtual Machines (VMs)**

  - Working with large-scale data hosted by the ISB-CGC in Google Cloud Storage requires some familiarity with tools such as the `Google Cloud SDK <https://cloud.google.com/sdk/>`_, `Google Compute Engine <https://cloud.google.com/compute/>`_, `Virtual Machines <https://en.wikipedia.org/wiki/Virtual_machine>`_ and `Docker <https://www.docker.com/why-docker#/VM>`_.
  
.. toctree::
   :maxdepth: 1
   
   HowToGetStarted-Analysis
 
