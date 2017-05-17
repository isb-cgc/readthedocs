cohorts().create()
###################
Creates and saves a cohort. Takes a JSON object in the request body to use as the cohort's filters. Authentication is required. Returns information about the saved cohort, including the number of cases and the number of samples in that cohort.

**Example**::

	python isb_curl.py "https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/cohorts/create?name={COHORT NAME}" -H "Content-Type: application/json" -d '{"program_short_name": ["CCLE-BLCA", "CCLE-LUSC"], "gender": "Male"}'

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_ccle_api/v3/isb_cgc_ccle_api.cohorts.create?name=COHORT%20NAME%20HERE&resource=%257B%250A++%2522Study%2522%253A+%250A++%255B%2522UCS%2522%250A++%255D%250A%257D&/>`_ to see this endpoint in Google's API explorer.

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
		api = 'isb_cgc_ccle_api'
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
	body = {'program_short_name': ['CCLE-BLCA', 'CCLE-LUSC'], 'gender': 'Male'}
	data = service.cohorts().create(name=name, body=body).execute()


**Request**

HTTP request::

	POST https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/cohorts/create

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	name,string,"Required. "


Request body

In the request body, supply a metadata resource with the following properties:

.. code-block:: javascript

  {
    "case_barcode": [string],
    "case_gdc_id": [string],
    "disease_code": [string],
    "endpoint_type": [string],
    "gender": [string],
    "hist_subtype": [string],
    "histology": [string],
    "program_name": [string],
    "project_short_name": [string],
    "sample_barcode": [string],
    "sample_gdc_id": [string],
    "sample_type": [string],
    "site_primary": [string],
    "source": [string],
    "summary_file_count": [integer],
    "summary_file_count_gte": integer,
    "summary_file_count_lte": integer
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	case_barcode[],list,"Optional. "
	case_gdc_id[],list,"Optional. "
	disease_code[],list,"Optional. Possible values include: 'BLCA', 'BRCA', 'CESC', 'COAD', 'DLBC', 'ESCA', 'HNSC', 'KIRC', 'LCLL', 'LGG', 'LIHC', 'LUSC', 'MESO', 'MM', 'OV', 'PAAD', 'PRAD', 'SARC', 'SKCM', 'STAD', 'THCA', 'UCEC'."
	endpoint_type[],list,"Optional. Possible values include: 'legacy'."
	gender[],list,"Optional. Possible values include: 'F', 'M', 'U'."
	hist_subtype[],list,"Optional. Possible values include: 'acute_lymphoblastic_B_cell_leukaemia', 'acute_lymphoblastic_T_cell_leukaemia', 'acute_myeloid_leukaemia', 'adenocarcinoma', 'adult_T_cell_lymphoma-leukaemia', 'alveolar', 'anaplastic_carcinoma', 'anaplastic_large_cell_lymphoma', 'astrocytoma', 'astrocytoma_Grade_III', 'astrocytoma_Grade_IV', 'blast_phase_chronic_myeloid_leukaemia', 'Brenner_tumour', 'bronchioloalveolar_adenocarcinoma', 'Burkitt_lymphoma', 'B_cell_lymphoma_unspecified', 'carcinosarcoma-malignant_mesodermal_mixed_tumour', 'chronic_lymphocytic_leukaemia-small_lymphocytic_lymphoma', 'chronic_myeloid_leukaemia', 'clear_cell_carcinoma', 'clear_cell_renal_cell_carcinoma', 'dedifferentiated', 'diffuse_adenocarcinoma', 'diffuse_large_B_cell_lymphoma', 'ductal_carcinoma', 'embryonal', 'endometrioid_carcinoma', 'essential_thrombocythaemia', 'follicular_carcinoma', 'giant_cell_tumour', 'gliosarcoma', 'granulosa_cell_tumour', 'hepatoblastoma', 'hepatocellular_carcinoma', 'Hodgkin_lymphoma', 'intestinal_adenocarcinoma', 'large_cell_carcinoma', 'mantle_cell_lymphoma', 'medullary_carcinoma', 'metaplasia', 'metaplastic_carcinoma', 'mixed_adenosquamous_carcinoma', 'mixed_carcinoma', 'mucinous_carcinoma', 'mucoepidermoid_carcinoma', 'mycosis_fungoides-Sezary_syndrome', 'non_small_cell_carcinoma', 'NS', 'oligodendroglioma', 'papillary_carcinoma', 'papilloma', 'peripheral_T_cell_lymphoma_unspecified', 'plasma_cell_myeloma', 'renal_cell_carcinoma', 'serous_carcinoma', 'signet_ring_adenocarcinoma', 'small_cell_adenocarcinoma', 'small_cell_carcinoma', 'squamous_cell_carcinoma', 'transitional_cell_carcinoma', 'tubular_adenocarcinoma', 'undifferentiated_adenocarcinoma', 'undifferentiated_carcinoma'."
	histology[],list,"Optional. Possible values include: 'carcinoid-endocrine_tumour', 'carcinoma', 'chondrosarcoma', 'Ewings_sarcoma-peripheral_primitive_neuroectodermal_tumour', 'fibrosarcoma', 'giant_cell_tumour', 'glioma', 'haematopoietic_neoplasm', 'leiomyosarcoma', 'lymphoid_neoplasm', 'malignant_fibrous_histiocytoma-pleomorphic_sarcoma', 'malignant_melanoma', 'mesothelioma', 'neuroblastoma', 'osteosarcoma', 'other', 'primitive_neuroectodermal_tumour-medulloblastoma', 'rhabdoid_tumour', 'rhabdomyosarcoma', 'sarcoma', 'sex_cord-stromal_tumour'."
	program_name[],list,"Optional. Possible values include: 'CCLE'."
	project_short_name[],list,"Optional. Possible values include: 'CCLE-BLCA', 'CCLE-BRCA', 'CCLE-CESC', 'CCLE-COAD', 'CCLE-DLBC', 'CCLE-ESCA', 'CCLE-HNSC', 'CCLE-KIRC', 'CCLE-LCLL', 'CCLE-LGG', 'CCLE-LIHC', 'CCLE-LUSC', 'CCLE-MESO', 'CCLE-MM', 'CCLE-OV', 'CCLE-PAAD', 'CCLE-PRAD', 'CCLE-SARC', 'CCLE-SKCM', 'CCLE-STAD', 'CCLE-THCA', 'CCLE-UCEC'."
	sample_barcode[],list,"Optional. "
	sample_gdc_id[],list,"Optional. "
	sample_type[],list,"Optional. Possible values include: '13', '50'."
	site_primary[],list,"Optional. Possible values include: 'autonomic_ganglia', 'biliary_tract', 'bone', 'breast', 'central_nervous_system', 'endometrium', 'haematopoietic_and_lymphoid_tissue', 'kidney', 'large_intestine', 'liver', 'lung', 'oesophagus', 'ovary', 'pancreas', 'pleura', 'prostate', 'salivary_gland', 'skin', 'small_intestine', 'soft_tissue', 'stomach', 'thyroid', 'upper_aerodigestive_tract', 'urinary_tract'."
	source[],list,"Optional. Possible values include: 'Academic Lab', 'ATCC', 'DSMZ', 'ECACC', 'HSRRB', 'ICLC', 'KCLB', 'NCI/DCTD', 'RIKEN'."
	summary_file_count[],list,"Optional. "
	summary_file_count_gte,integer,"Optional. "
	summary_file_count_lte,integer,"Optional. "


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
