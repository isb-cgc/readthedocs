cohorts().list()
#################
Returns information about cohorts a user has either READER or OWNER permission on. Authentication is required. Optionally takes a cohort id as a parameter to only list information about one cohort.

**Example**::

	$ python isb_curl.py https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v2/isb_cgc_api.cohorts.list?/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts

**Parameters**

None

**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "count": integer,
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
        "parent_id": [string],
        "patient_count": integer,
        "permission": string,
        "sample_count": integer,
        "source_notes": string,
        "source_type": string
      }
    ]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	count, integer, "Number of cohorts the user has OWNER or READER permission on."
	items[], list, "List of details about each cohort."
	items[].comments, string, "Comments on the cohort."
	items[].email, string, "Email of user."
	items[].filters[], list, "List of filters applied to create cohort, if any."
	items[].filters[].name, string, "Names of filtering parameters used to create the cohort."
	items[].filters[].value, string, "Values of filtering parameters used to create the cohort."
	items[].id, string, "Cohort id."
	items[].last_date_saved, string, "Last date the cohort was saved."
	items[].name, string, "Name of the cohort"
	items[].parent_id[], list, "List of id's of cohorts that this cohort was derived from, if any."
	items[].patient_count, integer, "Total count of unique patient barcodes in the cohort."
	items[].permission, string, "User permissions on cohort: READER or OWNER."
	items[].sample_count, integer, "Total count of unique sample barcodes in the cohort."
	items[].source_notes, string, "Notes on the source of the cohort."
	items[].source_type, string, "Type of cohort source."
