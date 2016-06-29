***********************
Programmatic Interfaces
***********************

Programmatic access to molecular data and metadata within the ISB-CGC platform
uses a combination of ISB-CGC APIs and Google APIs, as illustrated by the
`block diagram <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/_images/new-block-three-p.png>`_
on the front page of this documentation.

* The ISB-CGC API provides programmatic access to data and metadata stored in CloudSQL.  This includes information describing TCGA patients and samples, data availability, user-created cohorts, *etc.*  This section of our documentation provides more details about using the ISB-CGC API.

* Native Google APIs are used for optimized, high-speed programmatic access to molecular data in BigQuery, Google Cloud Storage, or Google Genomics.  Code examples illustrating usage of these Google APIs are available in the `ISB-CGC code repositories on github <https://github.com/isb-cgc>`_.  Additional Google Cloud Platform `Documentation <https://cloud.google.com/docs/>`_ for some of the key technologies leveraged by the ISB-CGC platform can be found by following these links:

  + `BigQuery APIs & Reference <https://cloud.google.com/bigquery/docs/apis>`_
  + `Cloud Storage APIs & Reference <https://cloud.google.com/storage/docs/apis>`_
  + `Genomics API Overview <https://cloud.google.com/genomics/reference/>`_

ISB-CGC API
###########

The ISB-CGC API provides a REST interface to the ISB-CGC metadata stored in CloudSQL, 
and consists of several "endpoints", implemented using Google Cloud Endpoints.
Details about these APIs can be found here,
and examples illustrating the use of these endpoints from R and Python can be found in 
our `examples-R <https://github.com/isb-cgc/examples-R>`_ and
`examples-Python <https://github.com/isb-cgc/examples-Python/tree/master/python>`_ repositories.

Some example use-cases include:

* obtaining a list of patient identifiers based on a defined set of criteria;
* obtaining a list of sample identifiers, associated with a specific patient;
* obtaining a list of data files in Cloud Storage, associated with a specific sample;
* creating a cohort of patients and samples, based on a defined set of criteria;
* retrieving information about a previously saved cohort;

The Google
`APIs Explorer <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/>`_
can be used to see details about each endpoint, and also provides an interface to try it out through your web browser. 
Following the link in the previous sentence will take you to a page with a list of APIs, in which each
API consists of a set of functionally-related endpoints.  Together, these individual APIs form the **ISB-CGC API**.
Note that not all of these APIs are intended for direct use by end-users: 
some are intended for use only by the ISB-CGC Web-App.
In order to see the individual endpoints within a single API, click on the API name,
such as the `cohort API <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/cohort_api/v1/>`_.

Cohorts are the primary organizing principle for subsetting and working with the TCGA data.
A cohort is a list of samples and a list of patients.  (TCGA samples are identified using a
16-character "barcode" *eg* ``TCGA-B9-7268-01A``, 
while patients are identified using the 12-character prefix (*eg* ``TCGA-B9-7268``) of the sample barcode.
Other datasets such as CCLE may use other less standardized naming conventions).  Users may
create and share cohorts using the ISB-CGC web-app and then programmatically access these cohorts
using this API.

Authorization
=============

Some, but not all, of the endpoints require authorization.  This authorization is not related to
controlled-access data: these endpoints do not operate on or directly return any controlled data.
Instead, authorization is related to saving or retrieving cohorts because cohorts are *private* to 
the user who creates a cohort (and anyone the cohort owner chooses to share the cohort with).
Helper scripts, described below, are provided to access these endpoints from the command line.

**Note:** Prior to using any endpoints that require authorization, a user must have signed into the
`web application <https://isb-cgc.appspot.com/>`_ at least once.

Usage
=====

from Python
-----------

Step 1: User runs::

   $ python isb_auth.py

Script `source <https://github.com/isb-cgc/ISB-CGC-Webapp/blob/master/scripts/isb_auth.py>`_.

This starts an oauth flow, opening a browser tab and asking the user to log in with their google email address. Once authenticated, the user’s information, including access and refresh tokens, are written to their root directory in a file named ``.isb_credentials``. A ``--verbose`` flag displays the location and name of the file as well as the access and refresh tokens.

If a user is running this script via ssh, the ``--noauth_local_webserver`` flag will allow the user to obtain a verification code through their local browser.

Step 2: Once the credentials file is stored on the user's home directory, they can access any API requiring authentication with the command::

   $ python isb_curl.py {ENDPOINT_URL}

Script `source <https://github.com/isb-cgc/ISB-CGC-Webapp/blob/master/scripts/isb_curl.py>`_.

from R
------

*more details coming soon -- please see our examples-R repo*

Cohort API Details
==================

The Cohort API bundles the following cohort-related endpoints:

.. toctree::
   :maxdepth: 1

   progapi2/cohort_patients_samples_list.rst
   progapi2/cohorts_list.rst
   progapi2/datafilenamekey_list_from_cohort.rst
   progapi2/datafilenamekey_list_from_sample.rst
   progapi2/delete_cohort.rst
   progapi2/google_genomics_from_cohort.rst
   progapi2/google_genomics_from_sample.rst
   progapi2/patient_details.rst
   progapi2/preview_cohort.rst
   progapi2/sample_details.rst
   progapi2/save_cohort.rst


