datafilenamekey_list_from_sample
################################
Takes a sample barcode as a required parameter and returns cloud storage paths to files associated with that sample.

Request

HTTP request

GET https://api-dot-isb-cgc.appspot.com/\_ah/api/cohort\_api/v1/datafilenamekey\_list\_from\_sample\``

Parameters

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	pipeline,string,Optional.
	platform,string,Optional.
	sample_barcode,string,Required.


Response

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "count": string,
    "datafilenamekeys": [string]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	count, string, "Number of data file cloud storage paths returned."
	datafilenamekeys[], list, "List of cloud storage file paths associated with each sample."
