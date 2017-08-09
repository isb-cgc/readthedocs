cohorts().list()
#################
Returns information about cohorts a user has either READER or OWNER permission on. Authentication is required.

**Example**::

	$ python isb_curl.py https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v3/cohorts

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v3/isb_cgc_api.cohorts.list?/>`_ to see this endpoint in Google's API explorer.

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
	data = service.cohorts().list().execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v3/cohorts

**Parameters**

None

**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "count": integer,
    "items": [
      {
        "case_count": integer,
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
	items[].case_count, integer, "Total count of unique case barcodes in the cohort."
	items[].comments, string, "Comments on the cohort."
	items[].email, string, "Email of user."
	items[].filters[], list, "List of filters applied to create cohort, if any."
	items[].filters[].name, string, "Names of filtering parameters used to create the cohort."
	items[].filters[].value, string, "Values of filtering parameters used to create the cohort."
	items[].id, string, "Cohort id."
	items[].last_date_saved, string, "Last date the cohort was saved."
	items[].name, string, "Name of the cohort"
	items[].parent_id[], list, "List of id's of cohorts that this cohort was derived from, if any."
	items[].permission, string, "User permissions on cohort: READER or OWNER."
	items[].sample_count, integer, "Total count of unique sample barcodes in the cohort."
	items[].source_notes, string, "Notes on the source of the cohort."
	items[].source_type, string, "Type of cohort source."
