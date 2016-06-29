cohorts().googlegenomics()
###########################
Returns a list of Google Genomics dataset and readgroupset ids associated with all the samples in a specified cohort. Authentication is required. User must have either READER or OWNER permissions on the cohort.

**Example**::

	python isb_curl.py https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts/{COHORT ID}/googlegenomics

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v2/isb_cgc_api.cohorts.googlegenomics?cohort_id=COHORT%20ID%20HERE&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts/{cohort_id}/googlegenomics

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cohort_id,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "count": integer,
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

	count, integer, "Number of Google Genomics records returned."
	items[], list, "List of Google Genomics items."
	items[].GG_dataset_id, string, "Google Genomics dataset id for the sample."
	items[].GG_readgroupset_id, string, "Google Genomics readgroupset id for the sample."
	items[].SampleBarcode, string, "Sample barcode."
