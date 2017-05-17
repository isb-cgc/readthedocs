cohorts().preview()
####################
Takes a JSON object of filters in the request body and returns a "preview" of the cohort that would result from passing a similar request to the cohort **save** endpoint. This preview consists of two lists: the lists of case barcodes, and the list of sample barcodes. Authentication is not required.

**Example**::

	curl "https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_target_api/v3/cohorts/preview?program_short_name=TARGET-ALL-P2&program_short_name=TARGET-RT&age_at_diagnosis_lte=20"

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_target_api/v3/isb_cgc_target_api.cohorts.preview?resource=%257B%250A++%2522program_short_name%2522%253A+%250A++%255B%2522TARGET-ALL-P2%2522%252C%2522TARGET-RT%2522%250A++%255D%252C%250A++%2522age_at_diagnosis_lte%2522%253A+%252230%2522%250A%257D&/>`_ to see this endpoint in Google's API explorer.

**Python API Client Example**::

	from googleapiclient.discovery import build
	import httplib2

	def get_unauthorized_service():
		api = 'isb_cgc_target_api'
		version = 'v3'
		site = 'https://api-dot-isb-cgc.appspot.com'
		discovery_url = '%s/_ah/api/discovery/v1/apis/%s/%s/rest' % (site, api, version)
		return build(api, version, discoveryServiceUrl=discovery_url, http=httplib2.Http())

	service = get_unauthorized_service()
	body = {'program_short_name': ['TARGET-ALL-P2', 'TARGET-RT'], 'age_at_diagnosis_gte': 90}
	data = service.cohorts().preview(**body).execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_target_api/v3/cohorts/preview

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	age_at_diagnosis,integer,"Optional. "
	age_at_diagnosis_gte,integer,"Optional. "
	age_at_diagnosis_lte,integer,"Optional. "
	case_barcode,string,"Optional. "
	case_gdc_id,string,"Optional. "
	days_to_birth,integer,"Optional. "
	days_to_birth_gte,integer,"Optional. "
	days_to_birth_lte,integer,"Optional. "
	days_to_death,integer,"Optional. "
	days_to_death_gte,integer,"Optional. "
	days_to_death_lte,integer,"Optional. "
	days_to_last_followup,integer,"Optional. "
	days_to_last_followup_gte,integer,"Optional. "
	days_to_last_followup_lte,integer,"Optional. "
	days_to_last_known_alive,integer,"Optional. "
	days_to_last_known_alive_gte,integer,"Optional. "
	days_to_last_known_alive_lte,integer,"Optional. "
	disease_code,string,"Optional. "
	endpoint_type,string,"Optional. "
	ethnicity,string,"Optional. "
	event_free_survival,integer,"Optional. "
	event_free_survival_gte,integer,"Optional. "
	event_free_survival_lte,integer,"Optional. "
	first_event,string,"Optional. "
	gender,string,"Optional. "
	program_name,string,"Optional. "
	project_short_name,string,"Optional. "
	protocol,string,"Optional. "
	race,string,"Optional. "
	sample_barcode,string,"Optional. "
	sample_gdc_id,string,"Optional. "
	sample_type,string,"Optional. "
	summary_file_count,integer,"Optional. "
	summary_file_count_gte,integer,"Optional. "
	summary_file_count_lte,integer,"Optional. "
	tumor_code,string,"Optional. "
	vital_status,string,"Optional. "
	wbc_at_diagnosis,number,"Optional. "
	wbc_at_diagnosis_gte,number,"Optional. "
	wbc_at_diagnosis_lte,number,"Optional. "
	year_of_diagnosis,integer,"Optional. "
	year_of_diagnosis_gte,integer,"Optional. "
	year_of_diagnosis_lte,integer,"Optional. "
	year_of_last_follow_up,integer,"Optional. "
	year_of_last_follow_up_gte,integer,"Optional. "
	year_of_last_follow_up_lte,integer,"Optional. "


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
