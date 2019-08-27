******************
How To Get Started on ISB-CGC
******************

The ISB-CGC provides both interactive (through a `web application <https://isb-cgc.appspot.com/>`_) and programmatic access to data hosted by institutes such as the Genomic Data Commons GDC of the National Cancer Institute (NCI), and the Wellcome Trust Sanger Institute, leveraging many aspects of the Google Cloud Platform. 

`More about ISB-CGC <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/About-ISB-CGC.html>`_, `ISB-CGC Main Landing Page <https://isb-cgc.appspot.com/>`_, `Full documentation of the ISB-CGC platform <index.html>`_, and `FAQS <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/FAQ.html>`_.



I. Data Access and Google Cloud Project Setup
-----------------------------------------------

- ISB-CGC hosts both open-access and controlled-access cancer genomics data from the NCI.
      `About ISB-CGC Cloud-Hosted Datasets <Hosted-Data.html>`_
      

- To access controlled-access data, dbGaP authorization is required.

      `Accessing Controlled-Access Data and acquiring dbGaP authorization <Gaining-Access-To-Controlled-Access-Data.html>`_
      
- To work in GCP, you must first set up a GCP Project: 
      - A GCP project is required to make use of all of the data, tools, and Google Cloud functionality.
      - Do you have a Google identity already (e.g. a GMail account)? Your institutional email may be a Google identity (if your institution uses Google Apps), or you may have a personal GMail address.
      - If not, it only takes a minute to `create a google identity <https://accounts.google.com/signup/v2/webcreateaccount?dsh=308321458437252901&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount&flowName=GlifWebSignIn&flowEntry=SignUp#FirstName=&LastName=>`_.  You can even link a non-GMail account (eg. scientist@nih.gov) as a Google identity by `this <https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp&nogm=true>`_ method.
      - Create your own GCP project and take advantage of a one-time `$300 Google Credit <https://cloud.google.com/free/>`_.
      - If you have already used this one-time offer (or there is some other reason you cannot use it), please see the information here about how to request `ISB-CGC Cloud Credits <HowtoRequestCloudCredits.html>`_.
    
      
- `Registering the GCP project <Gaining-Access-To-Contolled-Access-Data.html#requirements-for-registering-a-google-cloud-project-service-account>`_
 
- `Enable Required Google Cloud APIs <https://cloud.google.com/apis/docs/getting-started#enabling_apis>`_
      
      
II. Accessing and Analyzing Data via BigQuery
-----------------------------------------------

 - BigQuery is Google’s native big data analysis tool. It is a serverless, highly scalable data warehouse tool that allows researchers to find meaningful insights from data using standard SQL queries CHEAPLY, and FAST!
 - ISB-CGC has leveraged this powerful tool and uploaded multiple cancer genomics datasets into BigQuery tables that are open to the public. `ISB-CGC Datasets in BigQuery <BigQuery/data_in_BQ.html>`_ and the always freshly updated `Data Release Notes and Future Plans <updates_and_releases/Data_Releases.html>`_. 
 - To obtain access to the ISB-CGC open access project tables in BigQuery, users can link these tables to your GCP project as described `here <progapi/bigqueryGUI/LinkingBigQueryToIsb-cgcProject.html>`_.
 - To obtain access to the ISB-CGC controlled access project tables in BigQuery, users can link these tables to your GCP project as described `here <progapi/bigqueryGUI/LinkingISB-CGCtoCABQ.html>`_.
 - ISB-CGC provides quickstart guides, tutorials and examples in both R and Jupyter notebooks for BigQuery in the  `Tutorials <TutorialsAndHow-ToGuides.html>`_ and `Community Notebooks <HowTos.html>`_ sections of the documentation page. 
 - Every month, ISB-CGC provides an example analysis of cancer genomics data using BigQuery in our `Query of the Month blog <QueryOfTheMonthClub.html>`_. 
 
 
III. Accessing and Analyzing Data Stored in Google Cloud Storage 
---------------------------------------------------------------


 - All open-access data on ISB-CGC are stored in a publically available GCS bucket (gs://isb-cgc-open).
 - All controlled-access data are stored in Google Cloud Storage (GCS) in their original form as obtained from the GDC. 
 - To access controlled data, users must first be authenticated by NIH (`via the ISB-CGC web-app <Gaining-Access-To-Contolled-Access-Data.html#interactive-access-to-controlled-data>`_). Upon successful authentication, user dbGaP authorization will be verified. These two steps are required before the user’s Google identity is added to the access control list (ACL) for the controlled data. At this time, this access must be renewed every 24 hours.
 - `Summary of programs, data types and data formats available <Hosted-Data.html>`_
 - Working with large-scale data hosted by the ISB-CGC in Google Cloud Storage requires some familiarity with tools such as the `Google Cloud SDK <https://cloud.google.com/sdk/>`_, `Google Compute Engine <https://cloud.google.com/compute/>`_, `Virtual Machines <https://en.wikipedia.org/wiki/Virtual_machine>`_ and `Docker <https://www.docker.com/why-docker#/VM>`_.
 
