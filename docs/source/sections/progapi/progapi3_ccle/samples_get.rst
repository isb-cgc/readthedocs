samples().get()
################
Given a sample barcode (*eg* CCLE-ACC-MESO-1), this endpoint returns all available "biospecimen" information about this sample, the associated case barcode, a list of associated aliquots, and a list of "data_details" blocks describing each of the data files associated with this sample

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/ccle/samples/CCLE-LS1034

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_ccle_api/v3/isb_cgc_ccle_api.samples.get?sample_barcode=CCLE-LS1034&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.samples().get(sample_barcode='CCLE-LS1034').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_ccle_api/v3/ccle/samples/{sample_barcode}

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	analysis_workflow_type,string,"Optional. "
	data_category,string,"Optional. "
	data_format,string,"Optional. "
	data_type,string,"Optional. "
	endpoint_type,string,"Optional. "
	experimental_strategy,string,"Optional. "
	platform,string,"Optional. "
	sample_barcode,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure(CCLE does not have biospecimen data hence it would remain blank):

.. code-block:: javascript

  {
    "aliquots": [string],
    "biospecimen_data": {},
    "case_barcode": string,
    "case_gdc_id": string,
    "data_details": [
      {
        "access": string,
        "analysis_workflow_type": string,
        "data_category": string,
        "data_format": string,
        "data_type": string,
        "disease_code": string,
        "endpoint_type": string,
        "experimental_strategy": string,
        "file_gdc_id": string,
        "file_name": string,
        "file_name_key": string,
        "file_size": string,
        "index_file_name": string,
        "platform": string,
        "program_name": string,
        "project_short_name": string,
        "sample_barcode": string,
        "sample_gdc_id": string,
        "sample_type": string
      }
    ],
    "data_details_count": integer
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	aliquots[], list, "List of barcodes of aliquots taken from this participant."
	biospecimen_data, nested object, "Biospecimen data about the sample."
	case_barcode, string, "Case barcode."
    case_gdc_id, string, "Case gdc id."
	data_details[], list, "List of information about each file associated with the sample barcode."
	data_details[].access, string, "An indication of the security protocol necessary to fulfill in order to access the data from the file, e.g. open, controlled."
	data_details[].analysis_workflow_type, string, "The type of workflow used to generate the data file, e.g. 'BWA-aln', 'STAR 2-Pass', 'BWA with Mark Duplicates and Cocleaning'"
	data_details[].data_category, string, "The higher level categorization of the data_type in the file, e.g. 'Biospecimen', 'Clinical', 'Raw sequencing data', 'Simple nucleotide variation'"
	data_details[].data_format, string, "The format of the data file, e.g. 'BAM', 'BCR XML', 'TXT'"
	data_details[].data_type, string, "Data type stored in Google Cloud Storage, e.g. 'Clinical Supplement', 'Biospecimen Supplement', 'Aligned reads', 'Genotypes', 'Diagnostic image'"
	data_details[].disease_code, string, "The disease abbeviation, e.g. 'ACC', 'UVM', 'ALL', 'WT'"
	data_details[].endpoint_type, string, "The GDC files API the data file information was gottern from, e.g. 'legacy', 'current'"
	data_details[].experimental_strategy, string, "The sequencing, array or other strategy used to generate the data file, e.g. 'RNA-Seq', 'WGS', 'Genotyping array'"
	data_details[].file_gdc_id, string, "The GDC assigned id for the file"
	data_details[].file_name, string, "Name of the datafile stored on the GDC system."
	data_details[].file_name_key, string, "Google Cloud Storage path to file."
	data_details[].file_size, string, "The size of the file"
	data_details[].index_file_name, string, "For BAM files, the name of its index file"
	data_details[].platform, string, "The sequencing or array platform used, e.g. Illumina HiSeq, Ion Torrent PGM, Affymetrix SNP Array 6.0."
	data_details[].program_name, string, "The program for which the data was generated, e.g. 'CCLE', 'TARGET','TCGA'."
	data_details[].project_short_name, string, "The id of the project, e.g.  'CCLE-ACC', 'CCLE-UVM', 'TARGET-ALL-P1', ' TARGET-WT', 'TCGA-ACC', 'TCGA-UVM'"
	data_details[].sample_barcode, string, "Sample barcode."
	data_details[].sample_gdc_id, string, "The GDC assigned id for the sample"
	data_details[].sample_type, string, "The sample type, e.g. '01', '10', '11'"
	data_details_count, integer, "Number of files associated with the sample barcode."
