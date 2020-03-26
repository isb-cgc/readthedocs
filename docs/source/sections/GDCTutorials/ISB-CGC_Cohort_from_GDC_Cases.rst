Creating an ISB-CGC Cohort from a GDC Case JSON file
====================================================

This example is a little more difficult than the previous two since it involves a bit more extensive Python script and using the `ISB-CGC APIs <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/progapi/Programmatic-API.html>`__, however it is relatively straight-forward to understand.

Pre-requisites
==============
There are a couple of libraries that will make it much easier to use the ISB-CGC APIs (which are derived from Google's APIs)

* `Google API Client Library for Python <https://developers.google.com/api-client-library/python/>`__

* If you don't install the Google API library, you'll need `oauth2client library (deprecated) <https://pypi.python.org/pypi/oauth2client>`__ or the `google_auth library <https://google-auth.readthedocs.io/en/latest/>`__

* The `Google API Explorer <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/>`__ can be of great help in understanding how to use the ISB-CGC APIs.

Creating the Cohort
===================

There are really only two steps to creating a cohort from the GDC case file:

1) Parse the GDC case identifiers from the JSON file you downloaded from the GDC
2) Pass the GDC case identifiers to the ISB-CGC cohorts.create() API endpoint along with a name for the cohort
 
We have a Python script in our github repository called `gdcCase2Cohort.py <https://github.com/isb-cgc/examples-Python/tree/master/python>`__ that performs both of those tasks but we'll pull a couple of snippets to discuss here.

Parsing GDC JSON
++++++++++++++++

.. code-block:: python

 def parseGDCCase(filename):
 	inputfile = open(filename,'r')
 	data = json.load(inputfile)
 	uuids = []
	
 	for entry in data:
 		uuids.append(entry['case_id'])
	
 	return uuids
  
  
This routine is actually very simple to understand.  It opens the JSON file and uses the Python json library to turn the file into a JSON object Python can use and then it loops through all of the cases in the file and parses out the case id for each.  The collected case IDs are then returned to the caller.

Using the create.cohorts API
++++++++++++++++++++++++++++

Creating the cohorts using the Google Python library involves a few steps:

* Authorize using your credentials
* Use the Google library to create an authorized service
* Format the GDC Case id list into a query for the APIs
* Use the authorized service to create the cohort
 
The first two steps (authorization and creating a service) have numerous examples in the ISB-CGC github repository and we won't repeat them here.
 
Formatting the case ID list is very straight forward:
 
.. code-block:: python
 
  query = {"case_gdc_id" : uuids}
  
Essentially you just need to assign the list of case IDs to the "case_gdc_id" key.  Then the authorized service, the name for the cohort and the constructed query are used to execute the query.  The returned data contains details about the new cohort, but no further action is needed from the user:

.. code-block:: python

  def cohortsCreate(service, name, query):
	try:
		data = service.cohorts().create(name=name, body=query).execute()
		return data
	except HttpError as exception:
		raise exception

If there have been no errors, the new cohort will be visible in both the cohorts.list() API endpoint and in the ISB-CGC Webapp

