aliquots().annotations()
#########################
Returns TCGA annotations about a specific aliquot, Takes an aliquot barcode (of length 28, *eg* TCGA-01-0628-11A-01D-0356-01) as a required parameter. User does not need to be authenticated.

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/aliquots/TCGA-01-0628-11A-01D-0358-06/annotations

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/isb_cgc_tcga_api/v3/isb_cgc_tcga_api.aliquots.annotations?aliquot_barcode=TCGA-01-0628-11A-01D-0358-06&/>`_ to see this endpoint in Google's API explorer.

**Python API Client Example**::

	from googleapiclient.discovery import build
	import httplib2

	def get_unauthorized_service():
		api = 'isb_cgc_tcga_api'
		version = 'v3'
		site = 'https://api-dot-isb-cgc.appspot.com'
		discovery_url = '%s/_ah/api/discovery/v1/apis/%s/%s/rest' % (site, api, version)
		return build(api, version, discoveryServiceUrl=discovery_url, http=httplib2.Http())

	service = get_unauthorized_service()
	data = service.aliquots().annotations(aliquot_barcode='TCGA-01-0628-11A-01D-0358-06').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/aliquots/{aliquot_barcode}/annotations

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	aliquot_barcode,string,"Required. "
	entity_type,string,"Optional. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "count": integer,
    "items": [
      {
        "aliquot_barcode": string,
        "annotation_gdc_id": string,
        "annotation_submitter_id": string,
        "case_barcode": string,
        "case_gdc_id": string,
        "category": string,
        "classification": string,
        "endpoint_type": string,
        "entity_barcode": string,
        "entity_gdc_id": string,
        "entity_type": string,
        "notes": string,
        "program_name": string,
        "project_short_name": string,
        "sample_barcode": string,
        "status": string
      }
    ]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	count, integer, "Number of annotations returned."
	items[], list, "List of annotation items."
	items[].aliquot_barcode, string, "Aliquot barcode."
	items[].annotation_gdc_id, string, "Id assigned by the GDC to the annotation"
	items[].annotation_submitter_id, string, "Id assigned to the annotation by the TCGA"
	items[].case_barcode, string, "Case barcode."
	items[].case_gdc_id, string, "Id assigned by the GDC to the case"
	items[].category, string, "Annotation category name, e.g. 'Acceptable treatment for TCGA tumor'."
	items[].classification, string, "Annotation classification, .e.g 'CenterNotification', 'Notification', 'Observation', or 'Redaction'."
	items[].endpoint_type, string, "Which type of GDC Annotation API was used, either legacy or current "
	items[].entity_barcode, string, "The TCGA barcode that the annottion is associated with"
	items[].entity_gdc_id, string, "Id assigned by the GDC to the entity"
	items[].entity_type, string, "Entity type, e.g. 'Case', 'Aliquot', 'Analyte', 'Portion'', 'Slide', or 'Sample'."
	items[].notes, string, "Notes on the annotation"
	items[].program_name, string, "The program name, e.g. 'TCGA' (the only program with annotations)"
	items[].project_short_name, string, "The project id, e.g. 'TCGA-BRCA', 'TCGA-OV'."
	items[].sample_barcode, string, "Sample barcode."
	items[].status, string, "Status of the annotation, e.g. 'Approved', 'Rescinded'"
