cohorts_list
############
Returns information about cohorts a user has either READER or OWNER permission on. Authentication is required. Optionally takes a cohort id as a parameter to only list information about one cohort.

**Example**::

	$ python isb_curl.py "https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/cohorts_list"

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/cohort_api/v1/cohort_api.cohort_endpoints.cohorts.list?/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/cohorts_list

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cohort_id,string,"Optional. "
	token,string,"Optional. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "count": string,
    "items": [
      {
        "comments": string,
        "email": string,
        "filters": [
          {
            "name": string,
            "value": string
          }
        ],
        "id": string,
        "last_date_saved": string,
        "name": string,
        "num_patients": string,
        "num_samples": string,
        "parent_id": [string],
        "perm": string,
        "source_notes": string,
        "source_type": string
      }
    ]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	count, string, "Number of cohorts returned. If no cohort_id is specified in the request, this will be the number of cohorts that the user has READER or OWNER permission on."
	items[], list, "List of cohorts."
	items[].comments, string, "Comments on the cohort."
	items[].email, string, "Email of user."
	items[].filters[], list, "List of filters applied to create cohort, if any."
	items[].filters[].name, string, "Names of filtering parameters used to create the cohort."
	items[].filters[].value, string, "Values of filtering parameters used to create the cohort."
	items[].id, string, "Cohort id."
	items[].last_date_saved, string, "Last date the cohort was saved."
	items[].name, string, "Name of cohort."
	items[].num_patients, string, "Number of unique participant barcodes in the cohort."
	items[].num_samples, string, "Number of unique sample barcodes in the cohort."
	items[].parent_id[], list, "ID of the parent cohort this cohort was derived from, if any."
	items[].perm, string, "User permissions on cohort: READER or OWNER."
	items[].source_notes, string, "Notes on the source of the cohort."
	items[].source_type, string, "Type of cohort source."
