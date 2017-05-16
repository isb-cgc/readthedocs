cases().get()
##############
Returns information about a specific case, including a list of samples and aliquots derived from this case. Takes a case barcode (of length 16, *eg* TARGET-51-PALFYG) as a required parameter. User does not need to be authenticated.

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_target_api/v3/cases/TARGET-10-DCC001

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_target_api/v3/isb_cgc_target_api.cases.get?case_barcode=TARGET-10-DCC001&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.cases().get(case_barcode='TARGET-10-DCC001').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_target_api/v3/cases/{case_barcode}

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	case_barcode,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "aliquots": [string],
    "clinical_data": {
      "age_at_diagnosis": integer,
      "case_barcode": string,
      "case_gdc_id": string,
      "days_to_birth": integer,
      "days_to_death": integer,
      "days_to_last_followup": integer,
      "days_to_last_known_alive": integer,
      "disease_code": string,
      "endpoint_type": string,
      "ethnicity": string,
      "event_free_survival": integer,
      "first_event": string,
      "gender": string,
      "program_name": string,
      "project_short_name": string,
      "protocol": string,
      "race": string,
      "sample_barcode": string,
      "sample_gdc_id": string,
      "sample_type": string,
      "summary_file_count": integer,
      "tumor_code": string,
      "vital_status": string,
      "wbc_at_diagnosis": number,
      "year_of_diagnosis": integer,
      "year_of_last_follow_up": integer
    },
    "samples": [string]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	aliquots[], list, "List of barcodes of aliquots taken from this patient."
	clinical_data, nested object, "The clinical data about the patient."
	clinical_data.age_at_diagnosis, integer, "Age at which a condition or disease was first diagnosed in years."
	clinical_data.case_barcode, string, "Case barcode."
	clinical_data.case_gdc_id, string, "The GDC assigned id for the case"
	clinical_data.days_to_birth, integer, "Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.days_to_death, integer, "Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.days_to_last_followup, integer, "Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.days_to_last_known_alive, integer, "The number of days between diagnosis and when the individual was last known to be alive."
	clinical_data.disease_code, string, "The short name for the type of disease"
	clinical_data.endpoint_type, string, "Which type of GDC Case API was used, either legacy or current"
	clinical_data.ethnicity, string, "The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories."
	clinical_data.event_free_survival, integer, "The length of time after primary treatment for a cancer ends that the patient remains free of certain complications or events."
	clinical_data.first_event, string, "The first event after the diagnosis of cancer."
	clinical_data.gender, string, "Text designations that identify gender."
	clinical_data.program_name, string, "Project name, e.g. 'TCGA'."
	clinical_data.project_short_name, string, "Tumor type abbreviation, e.g. 'BRCA'. "
	clinical_data.protocol, string, "A list detailed plans of scientific or medical experiments, treatments, or procedures."
	clinical_data.race, string, "The text for reporting information about race based on the Office of Management and Budget (OMB) categories."
	clinical_data.sample_barcode, string, "The barcode assigned by TCGA to a sample from a Participant."
	clinical_data.sample_gdc_id, string, "The GDC assigned id for the sample"
	clinical_data.sample_type, string, "The type of the sample tumor or normal tissue cell or blood sample provided by a participant."
	clinical_data.summary_file_count, integer, "The count of files associated with the sample"
	clinical_data.tumor_code, string, "Code representing the type of tumor."
	clinical_data.vital_status, string, "The survival state of the person registered on the protocol."
	clinical_data.wbc_at_diagnosis, number, "White blood cell range at diagnosis"
	clinical_data.year_of_diagnosis, integer, "Numeric value to represent the year of an individual's initial pathologic diagnosis of cancer."
	clinical_data.year_of_last_follow_up, integer, "Numeric value to represent the year of an individual's last follow up."
	samples[], list, "List of barcodes of samples taken from this patient."
