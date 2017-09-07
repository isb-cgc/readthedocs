cohorts().create()
###################
Creates and saves a cohort. Takes a JSON object in the request body to use as the cohort's filters. Authentication is required. Returns information about the saved cohort, including the number of cases and the number of samples in that cohort.

**Example**::

	python isb_curl.py "https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_target_api/v3/cohorts/create?name={COHORT NAME}" -H "Content-Type: application/json" -d '{"program_short_name": ["TARGET-ALL-P2", "TARGET-RT"], "age_at_diagnosis_lte": 60}'

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_target_api/v3/isb_cgc_target_api.cohorts.create?name=COHORT%20NAME%20HERE&resource=%257B%250A++%2522Study%2522%253A+%250A++%255B%2522UCS%2522%250A++%255D%250A%257D&/>`_ to see this endpoint in Google's API explorer.

**Python API Client Example**::

	from googleapiclient.discovery import build
	from oauth2client.client import OAuth2WebServerFlow
	from oauth2client import tools
	from oauth2client.file import Storage
	import httplib2
	import os

	CLIENT_ID = '907668440978-0ol0griu70qkeb6k3gnn2vipfa5mgl60.apps.googleusercontent.com'
	CLIENT_SECRET = 'To_WJH7-1V-TofhNGcEqmEYi'
	EMAIL_SCOPE = 'https://www.googleapis.com/auth/userinfo.email'
	DEFAULT_STORAGE_FILE = os.path.join(os.path.expanduser('~'), '.isb_credentials')

	def get_credentials():
		oauth_flow_args = ['--noauth_local_webserver']
		storage = Storage(DEFAULT_STORAGE_FILE)
		credentials = storage.get()
		if not credentials or credentials.invalid:
			flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, EMAIL_SCOPE)
			flow.auth_uri = flow.auth_uri.rstrip('/') + '?approval_prompt=force'
			credentials = tools.run_flow(flow, storage, tools.argparser.parse_args(oauth_flow_args))
		return credentials

	def get_authorized_service():
		api = 'isb_cgc_target_api'
		version = 'v3'
		site = 'https://api-dot-isb-cgc.appspot.com'
		discovery_url = '%s/_ah/api/discovery/v1/apis/%s/%s/rest' % (site, api, version)
		credentials = get_credentials()
		http = credentials.authorize(httplib2.Http())
		if credentials.access_token_expired or credentials.invalid:
			credentials.refresh(http)
		authorized_service = build(api, version, discoveryServiceUrl=discovery_url, http=http)
		return authorized_service

	service = get_authorized_service()
	body = {'program_short_name': ['TARGET-ALL-P2', 'TARGET-RT'], 'age_at_diagnosis_gte': 90}
	data = service.cohorts().create(name=name, body=body).execute()


**Request**

HTTP request::

	POST https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_target_api/v3/cohorts/create

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	name,string,"Required. "


Request body

In the request body, supply a metadata resource with the following properties:

.. code-block:: javascript

  {
    "age_at_diagnosis": [integer],
    "age_at_diagnosis_gte": integer,
    "age_at_diagnosis_lte": integer,
    "case_barcode": [string],
    "case_gdc_id": [string],
    "days_to_birth": [integer],
    "days_to_birth_gte": integer,
    "days_to_birth_lte": integer,
    "days_to_death": [integer],
    "days_to_death_gte": integer,
    "days_to_death_lte": integer,
    "days_to_last_followup": [integer],
    "days_to_last_followup_gte": integer,
    "days_to_last_followup_lte": integer,
    "days_to_last_known_alive": [integer],
    "days_to_last_known_alive_gte": integer,
    "days_to_last_known_alive_lte": integer,
    "disease_code": [string],
    "endpoint_type": [string],
    "ethnicity": [string],
    "event_free_survival": [integer],
    "event_free_survival_gte": integer,
    "event_free_survival_lte": integer,
    "first_event": [string],
    "gender": [string],
    "program_name": [string],
    "project_short_name": [string],
    "protocol": [string],
    "race": [string],
    "sample_barcode": [string],
    "sample_gdc_id": [string],
    "sample_type": [string],
    "summary_file_count": [integer],
    "summary_file_count_gte": integer,
    "summary_file_count_lte": integer,
    "tumor_code": [string],
    "vital_status": [string],
    "wbc_at_diagnosis": [number],
    "wbc_at_diagnosis_gte": number,
    "wbc_at_diagnosis_lte": number,
    "year_of_diagnosis": [integer],
    "year_of_diagnosis_gte": integer,
    "year_of_diagnosis_lte": integer,
    "year_of_last_follow_up": [integer],
    "year_of_last_follow_up_gte": integer,
    "year_of_last_follow_up_lte": integer
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	age_at_diagnosis[],list,"Optional. "
	age_at_diagnosis_gte,integer,"Optional. "
	age_at_diagnosis_lte,integer,"Optional. "
	case_barcode[],list,"Optional. "
	case_gdc_id[],list,"Optional. "
	days_to_birth[],list,"Optional. "
	days_to_birth_gte,integer,"Optional. "
	days_to_birth_lte,integer,"Optional. "
	days_to_death[],list,"Optional. "
	days_to_death_gte,integer,"Optional. "
	days_to_death_lte,integer,"Optional. "
	days_to_last_followup[],list,"Optional. "
	days_to_last_followup_gte,integer,"Optional. "
	days_to_last_followup_lte,integer,"Optional. "
	days_to_last_known_alive[],list,"Optional. "
	days_to_last_known_alive_gte,integer,"Optional. "
	days_to_last_known_alive_lte,integer,"Optional. "
	disease_code[],list,"Optional. Possible values include: 'ALL', 'AML', 'CCSK', 'NBL', 'OS', 'RT', 'WT'."
	endpoint_type[],list,"Optional. Possible values include: 'current', 'legacy'."
	ethnicity[],list,"Optional. Possible values include: 'Hispanic or Latino', 'Not Hispanic or Latino'."
	event_free_survival[],list,"Optional. "
	event_free_survival_gte,integer,"Optional. "
	event_free_survival_lte,integer,"Optional. "
	first_event[],list,"Optional. Possible values include: 'Censored', 'Death', 'Death without remission', 'Event', 'Induction failure', 'Progression', 'Relapse', 'Second Malignant Neoplasm'."
	gender[],list,"Optional. Possible values include: 'Female', 'Male'."
	program_name[],list,"Optional. Possible values include: 'TARGET'."
	project_short_name[],list,"Optional. Possible values include: 'TARGET-ALL-P1', 'TARGET-ALL-P2', 'TARGET-AML', 'TARGET-CCSK', 'TARGET-NBL', 'TARGET-OS', 'TARGET-RT', 'TARGET-WT'."
	protocol[],list,"Optional. "
	race[],list,"Optional. Possible values include: 'American Indian or Alaska Native', 'Asian', 'Black or African American', 'Native Hawaiian or other Pacific Islander', 'Other', 'White'."
	sample_barcode[],list,"Optional. "
	sample_gdc_id[],list,"Optional. "
	sample_type[],list,"Optional. Possible values include: '01', '02', '03', '04', '06', '08', '09', '10', '11', '13', '14', '15', '20', '40', '41', '42', '50', '60'."
	summary_file_count[],list,"Optional. "
	summary_file_count_gte,integer,"Optional. "
	summary_file_count_lte,integer,"Optional. "
	tumor_code[],list,"Optional. Possible values include: '00', '10', '20', '21', '30', '40', '50', '51', '52'."
	vital_status[],list,"Optional. Possible values include: 'alive', 'dead'."
	wbc_at_diagnosis[],list,"Optional. "
	wbc_at_diagnosis_gte,number,"Optional. "
	wbc_at_diagnosis_lte,number,"Optional. "
	year_of_diagnosis[],list,"Optional. "
	year_of_diagnosis_gte,integer,"Optional. "
	year_of_diagnosis_lte,integer,"Optional. "
	year_of_last_follow_up[],list,"Optional. "
	year_of_last_follow_up_gte,integer,"Optional. "
	year_of_last_follow_up_lte,integer,"Optional. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "case_count": integer,
    "filters": [
      {
        "name": string,
        "value": string
      }
    ],
    "id": string,
    "last_date_saved": string,
    "name": string,
    "sample_count": integer
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	case_count, integer, "Number of unique case barcodes in the cohort."
	filters[], list, "List of filters applied to create cohort, if any."
	filters[].name, string, "Names of filtering parameters used to create the cohort."
	filters[].value, string, "Values of filtering parameters used to create the cohort."
	id, string, "Cohort id."
	last_date_saved, string, "Last date the cohort was saved."
	name, string, "Name of cohort."
	sample_count, integer, "Number of unique sample barcodes in the cohort."
