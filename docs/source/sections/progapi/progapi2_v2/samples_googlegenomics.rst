samples().googlegenomics()
###########################
Takes a sample barcode as a required parameter and returns the Google Genomics dataset id and readgroupset id associated with the sample, if any.

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/samples/CCLE-SU-DHL-5-RNA-08/googlegenomics

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v2/isb_cgc_api.samples.googlegenomics?sample_barcode=CCLE-SU-DHL-5-RNA-08&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.samples().googlegenomics(sample_barcode='CCLE-ACC-MESO-1-DNA-08').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/samples/{sample_barcode}/googlegenomics

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	sample_barcode,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "count": integer,
    "items": [
      {
        "GG_dataset_id": string,
        "GG_readgroupset_id": string,
        "SampleBarcode": string
      }
    ]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	count, integer, "Number of Google Genomics records returned."
	items[], list, "List of Google Genomics items."
	items[].GG_dataset_id, string, "Google Genomics dataset id for the sample."
	items[].GG_readgroupset_id, string, "Google Genomics readgroupset id for the sample."
	items[].SampleBarcode, string, "Sample barcode."
