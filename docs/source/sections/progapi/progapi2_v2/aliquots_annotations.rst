aliquots().annotations()
#########################
Returns TCGA annotations about a specific aliquot, Takes a aliquot barcode (of length 28 *eg* TCGA-01-0628-11A-01D-0358-06) as a required parameter. User does not need to be authenticated.

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/aliquots/TCGA-01-0628-11A-01D-0358-06/annotations

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/isb_cgc_api/v2/isb_cgc_api.aliquots.annotations?aliquot_barcode=TCGA-01-0628-11A-01D-0358-06&/>`_ to see this endpoint in Google's API explorer.

**Python API Client Example**::

	from googleapiclient.discovery import build
	import httplib2

	def get_unauthorized_service():
		api = 'isb_cgc_api'
		version = 'v2'
		site = 'https://api-dot-isb-cgc.appspot.com'
		discovery_url = '%s/_ah/api/discovery/v1/apis/%s/%s/rest' % (site, api, version)
		return build(api, version, discoveryServiceUrl=discovery_url, http=httplib2.Http())

	service = get_unauthorized_service()
	data = service.aliquots().get(aliquot_barcode='TCGA-01-0628-11A-01D-0358-06').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/aliquots/{aliquot_barcode}/annotations

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	aliquot_barcode,string,"Required. "
	item_type_name,string,"Optional. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "count": integer,
    "items": [
      {
        "AliquotBarcode": string,
        "annotationCategoryId": integer,
        "annotationCategoryName": string,
        "annotationClassification": string,
        "annotationClassificationId": integer,
        "annotationId": integer,
        "annotationNoteText": string,
        "itemBarcode": string,
        "itemTypeId": integer,
        "itemTypeName": string,
        "ParticipantBarcode": string,
        "SampleBarcode": string,
        "Study": string
      }
    ]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	count, integer, "Number of annotations returned."
	items[], list, "List of annotation items."
	items[].AliquotBarcode, string, "Aliquot barcode."
	items[].annotationCategoryId, integer, ""
	items[].annotationCategoryName, string, "Annotation category name, e.g. 'Acceptable treatment for TCGA tumor'."
	items[].annotationClassification, string, "Annotation classification, .e.g 'CenterNotification', 'Notification', 'Observation', or 'Redaction'."
	items[].annotationClassificationId, integer, ""
	items[].annotationId, integer, ""
	items[].annotationNoteText, string, ""
	items[].itemBarcode, string, ""
	items[].itemTypeId, integer, ""
	items[].itemTypeName, string, "Item type, e.g. 'Patient', 'Aliquot', 'Analyte', 'Shipped Portion', 'Portion, 'Slide', or 'Sample'."
	items[].ParticipantBarcode, string, "Participant barcode."
	items[].SampleBarcode, string, "Sample barcode."
	items[].Study, string, "TCGA study, e.g. 'BRCA', 'OV', 'CESC'."
