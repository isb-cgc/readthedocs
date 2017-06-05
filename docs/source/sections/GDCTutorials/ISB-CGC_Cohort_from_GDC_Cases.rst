Creating an ISB-CGC Cohort from a GDC Case JSON file
====================================================

This example is a little more difficult than the previous two since it involves a bit more extensive Python script and using the `ISB-CGC APIs <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/progapi/Programmatic-API.html>`__, however it is relatively straight-forward to understand.

Pre-requisites
==============
There are a couple of libraries that will make it much easier to use the ISB-CGC APIs (which are dervied from Google's APIs)

* `Google API Client Library for Python <https://developers.google.com/api-client-library/python/>`__

* If you don't install the Google API library, you'll need `oauth2client library (deprecated) <https://pypi.python.org/pypi/oauth2client>`__ or the `google_auth library <https://google-auth.readthedocs.io/en/latest/>`__

* The `Google API Explorer <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/>`__ can be of great help in understanding how to use the ISB-CGC APIs.

Creating the Cohort
===================

There are really only two steps to creating a cohort from the GDC case file:
 1) Parse the GDC case identifiers from the JSON file you downloaded from the GDC
 2) Pass the GDC case identifiers to the ISB-CGC cohorts.create() API endpoint along with a name for the cohort
 
We have a Python script in our` github repository <https://github.com/isb-cgc/examples-Python/tree/master/python>`__ that performs both of those tasks but we'll pull a couple of snippets to discuss here.

Parsing GDC JSON
++++++++++++++++

