google_genomics_from_cohort
###########################
Returns a list of Google Genomics dataset and readgroupset ids associated with all the samples in a specified cohort. Authentication is required. User must have either READER or OWNER permissions on the cohort.

**Example**::

	$ python isb_curl.py "https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/google_genomics_from_cohort?cohort_id={YOUR_COHORT_ID}"

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/cohort_api/v1/cohort_api.cohort_endpoints.cohorts.google_genomics_from_cohort?cohort_id=1&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/google_genomics_from_cohort

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cohort_id,string,"Required. "
	token,string,"Optional. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "count": string,
    "items": [
      {
        "GG_dataset_id": string,
        "GG_readgroupset_id": string,
        "SampleBarcode": string
      }
    ]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	count, string, "Number of unique Google genomics datasets and readgroupsets associated with the sample(s)."
	items[], list, "List of Google genomics data associated with the sample(s)."
	items[].GG_dataset_id, string, "Google genomics dataset id associated with the sample barcode."
	items[].GG_readgroupset_id, string, "Google genomics readgroupset id associated with the sample barcode."
	items[].SampleBarcode, string, "Barcode of the sample."
