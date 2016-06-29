samples().cloud_storage_file_paths()
#####################################
Takes a sample barcode as a required parameter and returns cloud storage paths to files associated with that sample.

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/samples/TCGA-W5-AA2O-10A/cloud_storage_file_paths

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v2/isb_cgc_api.samples.cloud_storage_file_paths?sample_barcode=TCGA-ZH-A8Y6-01A&platform=Genome_Wide_SNP_6&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/samples/{sample_barcode}/cloud_storage_file_paths

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	pipeline,string,"Optional. "
	platform,string,"Optional. "
	sample_barcode,string,"Required. "


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

	cloud_storage_file_paths[], list, "List of Google Cloud Storage paths of files associated with the sample."
	count, integer, "Number of Google Cloud Storage paths returned for the sample."
