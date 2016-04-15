delete_cohort
#############
Deletes a cohort. User must have owner permissions on the cohort.

**Example**::

	$ python isb_curl.py "https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/delete_cohort?cohort_id={YOUR_COHORT_ID}" -d '{}'

**Request**

HTTP request::

	POST https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/delete_cohort

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
    "msg": string
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	msg, string, "Message indicating success or failure of cohort deletion."
