cohorts().get()
################
Returns information about a specific cohort the user has READER or OWNER permission on when given a cohort ID. Authentication is required.

**Example**::

	python isb_curl.py https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts/{COHORT ID}

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v2/isb_cgc_api.cohorts.get?cohort_id=1&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/cohorts/{cohort_id}

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cohort_id,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

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
    "patients": [string],
    "permission": string,
    "sample_count": integer,
    "samples": [string],
    "source_notes": string,
    "source_type": string
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	comments, string, "Comments on the cohort."
	email, string, "Email of user."
	filters[], list, "List of filters applied to create cohort, if any."
	filters[].name, string, "Names of filtering parameters used to create the cohort."
	filters[].value, string, "Values of filtering parameters used to create the cohort."
	id, string, "Cohort id."
	last_date_saved, string, "Last date the cohort was saved."
	name, string, "Name of the cohort"
	parent_id[], list, "List of id's of cohorts that this cohort was derived from, if any."
	patient_count, integer, "Total count of unique patient barcodes in the cohort."
	patients[], list, "List of patient barcodes in the cohort."
	permission, string, "User permissions on cohort: READER or OWNER."
	sample_count, integer, "Total count of unique sample barcodes in the cohort."
	samples[], list, "List of sample barcodes in the cohort."
	source_notes, string, "Notes on the source of the cohort."
	source_type, string, "Type of cohort source."
