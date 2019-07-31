cases().get_list()
##############
Given a list of case barcodes (*eg* ACC-MESO-1), returns information about them, including a list of samples and aliquots derived from this case. Takes a list of case barcodes (*eg* ACC-MESO-1) as a required data payload. User does not need to be authenticated.

**Example**::

	curl --data '{"case_barcodes": ["ACC-MESO-1","Saos-2"]}' https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/ccle/cases

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_ccle_api/v3/isb_cgc_ccle_api.cases.get_list&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.cases().get(body={"case_barcodes": ["Saos-2","ACC-MESO-1"]}).execute()


**Request**

HTTP request::

	POST https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/ccle/cases
{
  "case_barcodes": [
    "ACC-MESO-1",
    "Saos-2"
  ]
}

**Parameters**

.. csv-table::
    :header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	case_barcode,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure(CCLE does not have clinical data hence the clinical data would remain blank):

.. code-block:: javascript

  {
    "aliquots": [string],
    "clinical_data": {},
    "samples": [string],
    "sample_barcode": string
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	aliquots[], list, "List of barcodes of aliquots taken from this patient."
	clinical_data, nested object, "The clinical data about the patient."
	samples[], list, "List of barcodes of samples taken from this patient."
