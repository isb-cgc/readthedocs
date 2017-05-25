samples().get()
################
Given a sample barcode (of length 20-22, *eg* TARGET-51-PALFYG-01A), this endpoint returns all available "biospecimen" information about this sample, the associated case barcode, a list of associated aliquots, and a list of "data_details" blocks describing each of the data files associated with this sample

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_target_api/v3/samples/TARGET-10-DCC001-03A

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_target_api/v3/isb_cgc_target_api.samples.get?sample_barcode=TARGET-10-DCC001-03A&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.samples().get(sample_barcode='TARGET-10-DCC001-03A').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_target_api/v3/samples/{sample_barcode}

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

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "aliquots": [string],
    "biospecimen_data": {
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
    "case": string,
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
	biospecimen_data.age_at_diagnosis, integer, "Age at which a condition or disease was first diagnosed in years."
	biospecimen_data.case_barcode, string, "Case barcode."
	biospecimen_data.case_gdc_id, string, "The GDC assigned id for the case"
	biospecimen_data.days_to_birth, integer, "Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_death, integer, "Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_last_followup, integer, "Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_last_known_alive, integer, "The number of days between diagnosis and when the individual was last known to be alive."
	biospecimen_data.disease_code, string, "The short name for the type of disease"
	biospecimen_data.endpoint_type, string, "Which type of GDC Case API was used, either legacy or current"
	biospecimen_data.ethnicity, string, "The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories."
	biospecimen_data.event_free_survival, integer, "The length of time after primary treatment for a cancer ends that the patient remains free of certain complications or events."
	biospecimen_data.first_event, string, "The first event after the diagnosis of cancer."
	biospecimen_data.gender, string, "Text designations that identify gender."
	biospecimen_data.program_name, string, "Project name, e.g. 'TCGA'."
	biospecimen_data.project_short_name, string, "Tumor type abbreviation, e.g. 'BRCA'. "
	biospecimen_data.protocol, string, "A list detailed plans of scientific or medical experiments, treatments, or procedures."
	biospecimen_data.race, string, "The text for reporting information about race based on the Office of Management and Budget (OMB) categories."
	biospecimen_data.sample_barcode, string, "The barcode assigned by TCGA to a sample from a Participant."
	biospecimen_data.sample_gdc_id, string, "The GDC assigned id for the sample"
	biospecimen_data.sample_type, string, "The type of the sample tumor or normal tissue cell or blood sample provided by a participant."
	biospecimen_data.summary_file_count, integer, "The count of files associated with the sample"
	biospecimen_data.tumor_code, string, "Code representing the type of tumor."
	biospecimen_data.vital_status, string, "The survival state of the person registered on the protocol."
	biospecimen_data.wbc_at_diagnosis, number, "White blood cell range at diagnosis"
	biospecimen_data.year_of_diagnosis, integer, "Numeric value to represent the year of an individual's initial pathologic diagnosis of cancer."
	biospecimen_data.year_of_last_follow_up, integer, "Numeric value to represent the year of an individual's last follow up."
	case, string, "Case barcode."
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
