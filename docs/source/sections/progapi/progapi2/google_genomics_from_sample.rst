google_genomics_from_sample
###########################
Takes a sample barcode as a required parameter and returns the Google Genomics dataset id and readgroupset id associated with the sample, if any.

**Example**::

	$ curl "https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/google_genomics_from_sample?sample_barcode=CCLE-SU-DHL-5-RNA-08"

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/cohort_api/v1/cohort_api.cohort_endpoints.cohorts.google_genomics_from_sample?sample_barcode=CCLE-SU-DHL-5-RNA-08&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/google_genomics_from_sample

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	sample_barcode,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "count": string,
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

	count, string, "Number of unique Google genomics datasets and readgroupsets associated with the sample(s)."
	items[], list, "List of Google genomics data associated with the sample(s)."
	items[].GG_dataset_id, string, "Google genomics dataset id associated with the sample barcode."
	items[].GG_readgroupset_id, string, "Google genomics readgroupset id associated with the sample barcode."
	items[].SampleBarcode, string, "Barcode of the sample."
