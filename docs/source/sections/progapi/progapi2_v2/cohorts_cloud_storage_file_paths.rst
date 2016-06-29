cohorts().cloud_storage_file_paths()
#####################################
Takes a cohort id as a required parameter and returns cloud storage paths to files associated with all the samples in that cohort, up to a default limit of 10,000 files. Authentication is required. User must have READER or OWNER permissions on the cohort.

**Example**::

	python isb_curl.py https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts/{COHORT ID}/cloud_storage_file_paths

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v2/isb_cgc_api.cohorts.cloud_storage_file_paths?cohort_id=1&limit=10&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts/{cohort_id}/cloud_storage_file_paths

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cohort_id,string,"Required. "
	limit,string,"Optional. "
	pipeline,string,"Optional. "
	platform,string,"Optional. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "cloud_storage_file_paths": [string],
    "count": integer
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cloud_storage_file_paths[], list, "List of Google Cloud Storage paths of files associated with the cohort."
	count, integer, "Number of Google Cloud Storage paths returned for the cohort."
