datafilenamekey_list_from_sample
################################
Takes a sample barcode as a required parameter and returns cloud storage paths to files associated with that sample.

**Example**::

	$ curl "https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/datafilenamekey_list_from_sample?sample_barcode=TCGA-ZH-A8Y6-01A&platform=Genome_Wide_SNP_6"

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/cohort_api/v1/cohort_api.cohort_endpoints.cohorts.datafilenamekey_list_from_sample?sample_barcode=TCGA-ZH-A8Y6-01A&platform=Genome_Wide_SNP_6&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/datafilenamekey_list_from_sample

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	pipeline,string,"Optional. "
	platform,string,"Optional. "
	sample_barcode,string,"Required. "


**Response**

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
