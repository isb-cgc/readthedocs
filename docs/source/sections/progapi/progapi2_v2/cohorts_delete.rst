cohorts().delete()
###################
Deletes a cohort. User must have owner permissions on the cohort.

**Example**::

	python isb_curl.py https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts/{COHORT ID} -X DELETE

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v2/isb_cgc_api.cohorts.delete?cohort_id=COHORT%20ID%20HERE&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	DELETE https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts/{cohort_id}

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cohort_id,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "message": string
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	message, string, "Indicates success or failure of cohort deletion."
