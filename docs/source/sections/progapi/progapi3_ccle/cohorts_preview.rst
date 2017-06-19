cohorts().preview()
####################
Takes a JSON object of filters in the request body and returns a "preview" of the cohort that would result from passing a similar request to the cohort **save** endpoint. This preview consists of two lists: the lists of case barcodes, and the list of sample barcodes. Authentication is not required.

**Example**::

	curl "https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/cohorts/preview?program_short_name=CCLE-BLCA&program_short_name=CCLE-LUSC&gender=Male"

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_ccle_api/v3/isb_cgc_ccle_api.cohorts.preview?resource=%257B%250A++%2522program_short_name%2522%253A+%250A++%255B%2522CCLE-BLCA%2522%252C%2522CCLE-LUSC%2522%250A++%255D%252C%250A++%2522age_at_initial_pathologic_diagnosis_lte%2522%253A+%252230%2522%250A%257D&/>`_ to see this endpoint in Google's API explorer.

**Python API Client Example**::

	from googleapiclient.discovery import build
	import httplib2

	def get_unauthorized_service():
		api = 'isb_cgc_ccle_api'
		version = 'v3'
		site = 'https://api-dot-isb-cgc.appspot.com'
		discovery_url = '%s/_ah/api/discovery/v1/apis/%s/%s/rest' % (site, api, version)
		return build(api, version, discoveryServiceUrl=discovery_url, http=httplib2.Http())

	service = get_unauthorized_service()
	body = {'program_short_name': ['CCLE-BLCA', 'CCLE-LUSC'], 'gender': Male}
	data = service.cohorts().preview(**body).execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/cohorts/preview

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	case_barcode,string,"Optional. "
	case_gdc_id,string,"Optional. "
	disease_code,string,"Optional. "
	endpoint_type,string,"Optional. "
	gender,string,"Optional. "
	hist_subtype,string,"Optional. "
	histology,string,"Optional. "
	program_name,string,"Optional. "
	project_short_name,string,"Optional. "
	sample_barcode,string,"Optional. "
	sample_gdc_id,string,"Optional. "
	sample_type,string,"Optional. "
	site_primary,string,"Optional. "
	source,string,"Optional. "
	summary_file_count,integer,"Optional. "
	summary_file_count_gte,integer,"Optional. "
	summary_file_count_lte,integer,"Optional. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "case_count": integer,
    "cases": [string],
    "sample_count": integer,
    "samples": [string]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	case_count, integer, "Number of cases in the cohort."
	cases[], list, "List of cases barcodes in the cohort."
	sample_count, integer, "Number of samples in the cohort."
	samples[], list, "List of sample barcodes in the cohort."
