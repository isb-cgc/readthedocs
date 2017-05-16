cohorts().cloud_storage_file_paths()
#####################################
Takes a cohort id as a required parameter and returns cloud storage paths to files associated with all the samples in that cohort, up to a default limit of 10,000 files. Authentication is required. User must have READER or OWNER permissions on the cohort.

**Example**::

	python isb_curl.py https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v3/cohorts/{COHORT ID}/cloud_storage_file_paths

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v3/isb_cgc_api.cohorts.cloud_storage_file_paths?cohort_id=1&limit=10&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.cohorts().cloud_storage_file_paths(cohort_id=1).execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v3/cohorts/{cohort_id}/cloud_storage_file_paths

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	analysis_workflow_type,string,"Optional. "
	cohort_id,string,"Required. "
	data_category,string,"Optional. "
	data_format,string,"Optional. "
	data_type,string,"Optional. "
	experimental_strategy,string,"Optional. "
	genomic_build,string,"Optional. "
	limit,string,"Optional. "
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
