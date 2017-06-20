cohorts().get()
################
Returns information about a specific cohort the user has READER or OWNER permission on when given a cohort ID. Authentication is required.

**Example**::

	python isb_curl.py https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v3/cohorts/{COHORT ID}

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v3/isb_cgc_api.cohorts.get?cohort_id=1&/>`_ to see this endpoint in Google's API explorer.

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
		api = 'isb_cgc_api'
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
	data = service.cohorts().get(cohort_id=1).execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v3/cohorts/{cohort_id}

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cohort_id,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "case_count": integer,
    "cases": [string],
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
    "permission": string,
    "sample_count": integer,
    "samples": [string],
    "source_notes": string,
    "source_type": string
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	case_count, integer, "Total count of unique case barcodes in the cohort."
	cases[], list, "List of case barcodes in the cohort."
	comments, string, "Comments on the cohort."
	email, string, "Email of user."
	filters[], list, "List of filters applied to create cohort, if any."
	filters[].name, string, "Names of filtering parameters used to create the cohort."
	filters[].value, string, "Values of filtering parameters used to create the cohort."
	id, string, "Cohort id."
	last_date_saved, string, "Last date the cohort was saved."
	name, string, "Name of the cohort"
	parent_id[], list, "List of id's of cohorts that this cohort was derived from, if any."
	permission, string, "User permissions on cohort: READER or OWNER."
	sample_count, integer, "Total count of unique sample barcodes in the cohort."
	samples[], list, "List of sample barcodes in the cohort."
	source_notes, string, "Notes on the source of the cohort."
	source_type, string, "Type of cohort source."
