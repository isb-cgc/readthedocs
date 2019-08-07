==========================
ISB-CGC Endpoints Tutorial
==========================




Programmatic access to molecular data and metadata within the ISB-CGC platform uses a combination of ISB-CGC APIs and Swagger UI documentation. 

The ISB-CGC API provides an interface to the ISB-CGC metadata stored in CloudSQL, and consists of several “endpoints”, implemented using Google Cloud Endpoints. Details about these endpoints can be found below. 

Some example use-cases include:


 - obtaining detailed metadata about a particular patient or sample;
 - creating (or retrieving a previously saved) cohort of patients and samples, based on a defined set of criteria;
 - retrieving a cohort's file manifest using the cohort ID;
 - retrieve a cohort's file manifest based on filters provided;
 - register, refresh, unregister a specified Google Cloud Project;



The Swagger UI(ADD PROD LINK) can be used to see details about each endpoint, and also provides a convenient interface to test an endpoint through your web browser. Following the link in the previous sentence will take you to a page with a list of APIs, in which each API consists of a set of functionally-related endpoints. Together, these individual APIs make up the ISB-CGC API. 


Cohorts are the primary organizing principle for sub setting and working with the TCGA data. A cohort is a list of samples and a list of patients. Users may create and share cohorts using the ISB-CGC web-app and then programmatically access these cohorts using the Swagger UI. (TCGA samples are identified using a 16-character “barcode” e.g. TCGA-B9-7268-01A, while patients are identified using the 12-character prefix, i.e. TCGA-B9-7268, of the sample barcode. Other datasets such as CCLE may use other less standardized naming conventions).



***************************
Get familiar with Swagger UI through the ISB-CGC demo
***************************


To get a better understanding of Swagger UI, let’s explore the Swagger ISB-CGC example. In the ISB-CGC example, the site is generated using Swagger UI.

 


.. image:: new_UI_display-pic
   :scale: 50
   :align: center 
   
   
   
The endpoints are grouped as follows:

 - cohorts
 - files
 - users
 
 

Authorize your request
======================


Before making any requests, you would normally authorize your session by clicking the Authorize button and completing the information required in the Authorization modal pictured below:



.. image:: Api-auth-page.PNG
   :scale: 50
   :align: center 
   
   
Make a Request
================

Now let’s make a request:

    Expand the  `POST samples endpoint <https://mvm-api-dot-isb-cgc.appspot.com/v4/swagger#/default/getSampleMetadataList>`_.

    Click Try it out.
   

.. image:: post-tryitout-button.PNG
   :scale: 50
   :align: center 
   
   
After you click Try it out, the example value in the Request Body field becomes editable.

In the sample barcode value field, change string to list of samples you wish you return information on. 

Click Execute


.. image:: post-tryitout-button.PNG
   :scale: 50
   :align: center 









