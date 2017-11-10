cases().get()
##############
Returns information about a specific case, including a list of samples and aliquots derived from this case. Takes a case barcode (*eg* ACC-MESO-1) as a required parameter. User does not need to be authenticated.

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/cases/1034

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_ccle_api/v3/isb_cgc_ccle_api.cases.get?case_barcode=1034&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.cases().get(case_barcode='1034').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/cases/{case_barcode}

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
      "case_barcode": string,
      "case_gdc_id": string,
      "disease_code": string,
      "endpoint_type": string,
      "gender": string,
      "hist_subtype": string,
      "histology": string,
      "program_name": string,
      "project_short_name": string,
      "sample_barcode": string,
      "sample_gdc_id": string,
      "sample_type": string,
      "site_primary": string,
      "source": string,
      "summary_file_count": integer
    },
    "samples": [string]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	aliquots[], list, "List of barcodes of aliquots taken from this patient."
	clinical_data, nested object, "The clinical data about the patient."
	clinical_data.case_barcode, string, "Case barcode."
	clinical_data.case_gdc_id, string, "The GDC assigned id for the case"
	clinical_data.disease_code, string, "The short name for the type of disease"
	clinical_data.endpoint_type, string, "Which type of GDC Case API was used, either legacy or current"
	clinical_data.gender, string, "Text designations that identify gender."
	clinical_data.hist_subtype, string, "Text term for a more specific definition of the histology"
	clinical_data.histology, string, "Text term for the structural pattern of cancer cells used to define a microscopic diagnosis."
	clinical_data.program_name, string, "Project name, e.g. 'TCGA'."
	clinical_data.project_short_name, string, "Tumor type abbreviation, e.g. 'BRCA'. "
	clinical_data.sample_barcode, string, "The barcode assigned by TCGA to a sample from a Participant."
	clinical_data.sample_gdc_id, string, "The GDC assigned id for the sample"
	clinical_data.sample_type, string, "The type of the sample tumor or normal tissue cell or blood sample provided by a participant."
	clinical_data.site_primary, string, "Text term that describes the anatomic site of the tumor or disease."
	clinical_data.source, string, "The source institution the cell line was obtained from"
	clinical_data.summary_file_count, integer, "The count of files associated with the sample"
	samples[], list, "List of barcodes of samples taken from this patient."
