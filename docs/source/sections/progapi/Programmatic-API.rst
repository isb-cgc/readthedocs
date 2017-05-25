***********************
Programmatic Interfaces
***********************


..  code-block:: none

    The changes needed to support multiple programs have rendered the V1 and V2 APIs non-functional 
    and therefore users must migrage all API calls to the V3 version.  Note that this usually means 
    just a minor adjustment to the URL.  Also note that some of the examples in the github repository
    may still reference the V1 or V2 API.

Programmatic access to molecular data and metadata within the ISB-CGC platform
uses a combination of ISB-CGC APIs and Google APIs, as illustrated by the
`block diagram <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/_images/new-block-three-p.png>`_
on the front page of this documentation.

* The **ISB-CGC API** provides programmatic access to data and metadata stored in CloudSQL.  This includes information describing TCGA patients and samples, data availability, user-created cohorts, *etc.*  In this section of our documentation, you will find more details about using the ISB-CGC API.

* Native **Google APIs** are used for optimized, high-speed programmatic access to molecular data in BigQuery, Google Cloud Storage, or Google Genomics.  Code examples illustrating usage of these Google APIs are available in the ISB-CGC code `repositories <https://github.com/isb-cgc>`_ on github.  Additional `Google Cloud Platform Documentation <https://cloud.google.com/docs/>`_ for some of the key technologies leveraged by the ISB-CGC platform can be found by following these links:

  + `BigQuery APIs & Reference <https://cloud.google.com/bigquery/docs/apis>`_
  + `Cloud Storage APIs & Reference <https://cloud.google.com/storage/docs/apis>`_
  + `Genomics API Overview <https://cloud.google.com/genomics/reference/>`_

ISB-CGC API
###########

The **ISB-CGC API** provides an interface to the ISB-CGC metadata stored in CloudSQL,
and consists of several "endpoints", implemented using Google Cloud Endpoints.
Details about these endpoints can be found here,
and examples illustrating usage from R and Python can be found in
our `examples-R <https://github.com/isb-cgc/examples-R>`_ and
`examples-Python <https://github.com/isb-cgc/examples-Python/tree/master/python>`_ repositories on github.

Some example use-cases include:

* obtaining a list of *patient identifiers* based on a defined set of criteria;
* obtaining a list of *sample identifiers*, associated with a specific patient;
* obtaining detailed *metadata* about a particular patient or sample;
* creating (or retrieving a previously saved) *cohort* of patients and samples, based on a defined set of criteria;
* obtaining a list of *data files* in Cloud Storage, associated with a specific *sample*, *cohort*, *platform*, or *data-type* (or any combination thereof);

The `APIs Explorer <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/>`_
can be used to see details about each endpoint, and also provides a convenient interface
to test an endpoint through your web browser.
Following the link in the previous sentence will take you to a page with a list of APIs, in which each
API consists of a set of functionally-related endpoints.  Together, these individual APIs make up the **ISB-CGC API**.
In order to see the individual endpoints within a single API, click on the API name, such as the
`cohort API v1 <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/cohort_api/v1/>`_
or the just-released
`ISB-CGC API v2 <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/isb_cgc_api/v2/>`_.
(Note that not all of these APIs are intended for direct use by end-users:
some are intended for use only by the ISB-CGC Web-App, as described in the information on the 
first APIs Explorer page mentioned above.)

Cohorts are the primary organizing principle for subsetting and working with the TCGA data.
A cohort is a list of samples and a list of patients.
Users may create and share cohorts using the ISB-CGC web-app and then programmatically
access these cohorts using this API.
(TCGA samples are identified using a
16-character "barcode" *eg* ``TCGA-B9-7268-01A``,
while patients are identified using the 12-character prefix, *ie* ``TCGA-B9-7268``, of the sample barcode.
Other datasets such as CCLE may use other less standardized naming conventions).

Usage
=====

Endpoints are simple https GET or PUT requests, *eg*:

.. code-block:: none

        V3 TCGA - GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/cases/TCGA-B9-7268
        V3 TARGET - GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_target_api/v3/cases/TARGET-20-PABLDZ
        V3 CCLE - GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/cases/FU-OV-1
        
        V1 (deprecated) - GET https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/patient_details?patient_barcode=TCGA-B9-7268
        V2 (deprecated) - GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/patients/TCGA-B9-7268

The first three GET commands above illustrates the usage with the new program-specific V3 endpoints.  The V1 and V2 examples are presented so users can see the difference in calls and aid in the transition to V3.  

The url (without the "GET" command) can also be pasted directly into your browser, like
`this <https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/cases/TCGA-B9-7268>`_
or `this <https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/cases/FU-OV-1>`_.
Packages are available in most languages to allow you to easily perform https GET and PUT requests, such as the
`httr <https://cran.r-project.org/web/packages/httr/index.html>`_ package for R,
and the Python `requests <http://docs.python-requests.org/en/master/>`_ library.

In addition, the
`Google Python API Client Library <https://developers.google.com/api-client-library/python/>`_
can be used to build a service object which provides a functional interface to the resources defined by the API.
(Examples of this approach can be found in the examples-Python github repo, specifically the 
``api_test_service*.py`` scripts.)

Authorization
=============

Some, but not all, of the endpoints require authorization.  This authorization is *not* related to
controlled-access data: these endpoints do not operate on or directly return any controlled data.
Instead, authorization is related to saving or retrieving cohorts because cohorts are *private* to
the user who created the cohort (and anyone the cohort owner has chosen to share the cohort with).
Helper scripts, described below, are provided to access these endpoints from the command line.

**Note:** Prior to using any endpoints that require authorization, a user must have signed into the
`web application <https://isb-cgc.appspot.com/>`_ at least once.

Examples
========

from Python
-----------

**Step 1**: A python helper-script,
`isb_auth.py <https://github.com/isb-cgc/ISB-CGC-Webapp/blob/master/scripts/isb_auth.py>`_,
can be used to start the OAuth flow and store the users credentials in a file named ``~/.isb_credentials``

.. code-block:: none

   $ python isb_auth.py

This script will open a new tab in your browser and ask you to sign in with your google identity
(*eg* your gmail address).  The first time, you will also be asked to grant the ISB-CGC application
permission to see your email address.
Once authenticated, your access and refresh tokens are written to
``~/.isb_credentials``. You may use the ``--verbose`` flag when running this script
to see the contents and name of this file.

If you are running this script via ssh (or from Cloud Shell),
the ``--noauth_local_webserver`` flag will allow you to obtain a verification code through your local browser.

**Step 2**: Once you have a ``~/.isb_credentials`` file 
(either locally on your laptop, or on a GCE VM, or in Cloud Shell), 
you can access any API requiring authentication using another helper-script, 
`isb_curl.py <https://github.com/isb-cgc/ISB-CGC-Webapp/blob/master/scripts/isb_curl.py>`_

.. code-block:: none

   $ ## usage: python isb_curl.py {ENDPOINT_URL}
   $ python isb_curl.py https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts

from R
------

The `Examples-R <https://github.com/isb-cgc/examples-R>`_ (ISBCGCExamples) package contains a number of functions that "wrap" the http endpoints calls, making it easier to access your cohorts and query the database.
(Note that these wrappers are currently based on the *v1* endpoints and will soon be updated to 
use the *v2* endpoints.)

**Step 1**: After starting R, and loading the ISBCGCExamples, you can use the R helper script ``isb_init``
to go through the authentication process:

.. code-block:: none

   > library(ISBCGCExamples)
   > token <- isb_init()
   Use a local file to cache OAuth access credentials between R sessions?
   1: Yes
   2: No

   Selection: 1
   Waiting for authentication in browser...
   Press Esc/Ctrl + C to abort
   Authentication complete.

The ``isb_init`` function will open a new tab in your browser and ask you to sign in with your google
identity (*eg* your gmail address).  The first time, you will also be asked to grant the ISB-CGC
application permission to see your email address.
Once authenticated, your access and refresh tokens are written to your working directory in a 
file named ``.httr-oauth``.

**Step 2**: Using the endpoints

After authentication, any of the example endpoint functions can be used such as:

.. code-block:: none

   list_cohorts(token)

which returns a list of the user's previously created cohorts. 
Documentation for these functions can be found in the ISB-CGC github repo, 
`Examples-R <https://github.com/isb-cgc/examples-R>`_ under 'API Endpoints Interface'.

ISB-CGC API (v3)
=================

The endpoints have been reorganized to support the multiple programs that now have data in the ISB-CGC.  These endpoints are now organized into four different sections:  TCGA, CCLE, TARGET and common endpoints.
Details for each of these enpoints can be found below:

.. toctree::
   :maxdepth: 1
   
   progapi3_api/cohorts_cloud_storage_file_paths.rst
   progapi3_api/cohorts_delete.rst
   progapi3_api/cohorts_get.rst
   progapi3_api/cohorts_list.rst
   
   
**TCGA Endpoints**
 
 .. toctree::
    :maxdepth: 1
    
    progapi3_tcga/cohorts_preview.rst
    progapi3_tcga/cohorts_create.rst
    progapi3_tcga/cases_get.rst
    progapi3_tcga/samples_cloud_storage_file_paths.rst
    progapi3_tcga/samples_get.rst
    progapi3_tcga/users_get.rst
    progapi3_tcga/aliquots_annotations.rst
    progapi3_tcga/cases_annotations.rst
    progapi3_tcga/samples_annotations.rst
   
   
**TARGET Endpoints**
  
 .. toctree::
    :maxdepth: 1
    
    progapi3_target/cohorts_preview.rst
    progapi3_target/cohorts_create.rst
    progapi3_target/cases_get.rst
    progapi3_target/samples_cloud_storage_file_paths.rst
    progapi3_target/samples_get.rst
    progapi3_target/users_get.rst
    
    
**CCLE Endpoints**
  
 .. toctree::
    :maxdepth: 1
    
    progapi3_ccle/cohorts_preview.rst
    progapi3_ccle/cohorts_create.rst
    progapi3_ccle/cases_get.rst
    progapi3_ccle/samples_cloud_storage_file_paths.rst
    progapi3_ccle/samples_get.rst
    progapi3_ccle/users_get.rst


