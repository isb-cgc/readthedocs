samples().get()
################
Given a sample barcode (of length 16, *eg* TCGA-B9-7268-01A), this endpoint returns all available "biospecimen" information about this sample, the associated case barcode, a list of associated aliquots, and a list of "data_details" blocks describing each of the data files associated with this sample

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/samples/TCGA-ZH-A8Y6-1A

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_tcga_api/v3/isb_cgc_tcga_api.samples.get?sample_barcode=TCGA-ZH-A8Y6-01A&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.samples().get(sample_barcode='TCGA-W5-AA2R-01A').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/samples/{sample_barcode}

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
      "age_began_smoking_in_years": integer,
      "anatomic_neoplasm_subdivision": string,
      "avg_percent_lymphocyte_infiltration": number,
      "avg_percent_monocyte_infiltration": number,
      "avg_percent_necrosis": number,
      "avg_percent_neutrophil_infiltration": number,
      "avg_percent_normal_cells": number,
      "avg_percent_stromal_cells": number,
      "avg_percent_tumor_cells": number,
      "avg_percent_tumor_nuclei": number,
      "batch_number": integer,
      "bcr": string,
      "bmi": number,
      "case_barcode": string,
      "case_gdc_id": string,
      "clinical_M": string,
      "clinical_N": string,
      "clinical_stage": string,
      "clinical_T": string,
      "colorectal_cancer": string,
      "country": string,
      "days_to_birth": integer,
      "days_to_collection": integer,
      "days_to_death": integer,
      "days_to_initial_pathologic_diagnosis": integer,
      "days_to_last_followup": integer,
      "days_to_last_known_alive": integer,
      "days_to_sample_procurement": integer,
      "days_to_submitted_specimen_dx": integer,
      "disease_code": string,
      "endpoint_type": string,
      "ethnicity": string,
      "gender": string,
      "gleason_score_combined": integer,
      "h_pylori_infection": string,
      "height": integer,
      "histological_type": string,
      "history_of_colon_polyps": string,
      "history_of_neoadjuvant_treatment": string,
      "hpv_calls": string,
      "hpv_status": string,
      "icd_10": string,
      "icd_o_3_histology": string,
      "icd_o_3_site": string,
      "lymphatic_invasion": string,
      "lymphnodes_examined": string,
      "lymphovascular_invasion_present": string,
      "max_percent_lymphocyte_infiltration": number,
      "max_percent_monocyte_infiltration": number,
      "max_percent_necrosis": number,
      "max_percent_neutrophil_infiltration": number,
      "max_percent_normal_cells": number,
      "max_percent_stromal_cells": number,
      "max_percent_tumor_cells": number,
      "max_percent_tumor_nuclei": number,
      "menopause_status": string,
      "min_percent_lymphocyte_infiltration": number,
      "min_percent_monocyte_infiltration": number,
      "min_percent_necrosis": number,
      "min_percent_neutrophil_infiltration": number,
      "min_percent_normal_cells": number,
      "min_percent_stromal_cells": number,
      "min_percent_tumor_cells": number,
      "min_percent_tumor_nuclei": number,
      "mononucleotide_and_dinucleotide_marker_panel_analysis_status": string,
      "neoplasm_histologic_grade": string,
      "new_tumor_event_after_initial_treatment": string,
      "num_portions": integer,
      "num_slides": integer,
      "number_of_lymphnodes_examined": integer,
      "number_of_lymphnodes_positive_by_he": integer,
      "number_pack_years_smoked": integer,
      "other_dx": string,
      "other_malignancy_anatomic_site": string,
      "other_malignancy_histological_type": string,
      "other_malignancy_type": string,
      "pathologic_M": string,
      "pathologic_N": string,
      "pathologic_stage": string,
      "pathologic_T": string,
      "pathology_report_uuid": string,
      "person_neoplasm_cancer_status": string,
      "pregnancies": string,
      "preservation_method": string,
      "primary_neoplasm_melanoma_dx": string,
      "primary_therapy_outcome_success": string,
      "program_name": string,
      "project_short_name": string,
      "psa_value": number,
      "race": string,
      "residual_tumor": string,
      "sample_barcode": string,
      "sample_gdc_id": string,
      "sample_type": string,
      "stopped_smoking_year": integer,
      "summary_file_count": integer,
      "tobacco_smoking_history": string,
      "tss_code": string,
      "tumor_tissue_site": string,
      "tumor_type": string,
      "venous_invasion": string,
      "vital_status": string,
      "weight": integer,
      "year_of_diagnosis": integer,
      "year_of_tobacco_smoking_onset": integer
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
	biospecimen_data.age_began_smoking_in_years, integer, "Age began smoking cigarettes expressed in number of years since birth."
	biospecimen_data.anatomic_neoplasm_subdivision, string, "Text term to describe the spatial location, subdivisions and/or anatomic site name of a tumor."
	biospecimen_data.avg_percent_lymphocyte_infiltration, number, "Average in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_monocyte_infiltration, number, "Average in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_necrosis, number, "Average in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_neutrophil_infiltration, number, "Average in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_normal_cells, number, "Average in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_stromal_cells, number, "Average in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_tumor_cells, number, "Average in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_tumor_nuclei, number, "Average in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.batch_number, integer, "Groups samples by the batch they were processed in."
	biospecimen_data.bcr, string, "A TCGA center where samples are carefully catalogued, processed, quality-checked and stored along with participant clinical information."
	biospecimen_data.bmi, number, "Body Mass Index"
	biospecimen_data.case_barcode, string, "Case barcode."
	biospecimen_data.case_gdc_id, string, "The GDC assigned id for the case"
	biospecimen_data.clinical_M, string, "Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	biospecimen_data.clinical_N, string, "Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	biospecimen_data.clinical_stage, string, "Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis."
	biospecimen_data.clinical_T, string, "Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	biospecimen_data.colorectal_cancer, string, "Text term to signify whether a patient has been diagnosed with colorectal cancer."
	biospecimen_data.country, string, "Text to identify the name of the state, province, or country in which the sample was procured."
	biospecimen_data.days_to_birth, integer, "Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_collection, integer, "The number of days between diagnosis and tissue collection."
	biospecimen_data.days_to_death, integer, "Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_initial_pathologic_diagnosis, integer, "Numeric value to represent the day of an individual's initial pathologic diagnosis of cancer."
	biospecimen_data.days_to_last_followup, integer, "Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_last_known_alive, integer, "The number of days between diagnosis and when the individual was last known to be alive."
	biospecimen_data.days_to_sample_procurement, integer, "Indicates the days to sample procurement for the submitted sample in relation to the date of initial diagnosis"
	biospecimen_data.days_to_submitted_specimen_dx, integer, "Time interval from the date of diagnosis of the submitted sample to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.disease_code, string, "Text term referring to the cancer type"
	biospecimen_data.endpoint_type, string, "Which type of GDC Case API was used, either legacy or current"
	biospecimen_data.ethnicity, string, "The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories."
	biospecimen_data.gender, string, "Text designations that identify gender."
	biospecimen_data.gleason_score_combined, integer, "A numeric value obtained by adding the primary and secondary patterns (grades)."
	biospecimen_data.h_pylori_infection, string, "Text term to indicate the state of the diagnosis of an individual with Helicobacter pylori infection."
	biospecimen_data.height, integer, "The height of the patient in centimeters."
	biospecimen_data.histological_type, string, "Text term for the structural pattern of cancer cells used to define a microscopic diagnosis."
	biospecimen_data.history_of_colon_polyps, string, "Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report(s)."
	biospecimen_data.history_of_neoadjuvant_treatment, string, "Text term to describe the patient's history of neoadjuvant treatment and the kind of treatment given prior to resection of the tumor."
	biospecimen_data.hpv_calls, string, "Results of HPV tests."
	biospecimen_data.hpv_status, string, "Current HPV status."
	biospecimen_data.icd_10, string, "The tenth version of the International Classification of Disease (ICD)."
	biospecimen_data.icd_o_3_histology, string, "The third edition of the International Classification of Diseases for Oncology."
	biospecimen_data.icd_o_3_site, string, "The third edition of the International Classification of Diseases for Oncology."
	biospecimen_data.lymphatic_invasion, string, "A yes/no indicator to ask if malignant cells are present in small or thin-walled vessels suggesting lymphatic involvement."
	biospecimen_data.lymphnodes_examined, string, "A yes/no/unknown indicator whether a lymph node assessment was performed at the primary presentation of disease."
	biospecimen_data.lymphovascular_invasion_present, string, "A yes/no indicator to ask if large vessel (vascular) invasion or small, thin-walled (lymphatic) invasion was detected in a tumor specimen."
	biospecimen_data.max_percent_lymphocyte_infiltration, number, "Maximum in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_monocyte_infiltration, number, "Maximum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_necrosis, number, "Maximum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_neutrophil_infiltration, number, "Maximum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_normal_cells, number, "Maximum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_stromal_cells, number, "Maximum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_tumor_cells, number, "Maximum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_tumor_nuclei, number, "Maximum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.menopause_status, string, "Text term to signify the status of a woman's menopause, the permanent cessation of menses, usually defined by 6 to 12 months of amenorrhea."
	biospecimen_data.min_percent_lymphocyte_infiltration, number, "Minimum in the series of numeric values to represent the percentage of lymphcyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_monocyte_infiltration, number, "Minimum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_necrosis, number, "Minimum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_neutrophil_infiltration, number, "Minimum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_normal_cells, number, "Minimum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_stromal_cells, number, "Minimum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_tumor_cells, number, "Minimum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_tumor_nuclei, number, "Minimum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.mononucleotide_and_dinucleotide_marker_panel_analysis_status, string, "Text result of microsatellite instability (MSI) testing at using a mononucleotide and dinucleotide microsatellite panel."
	biospecimen_data.neoplasm_histologic_grade, string, "Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness."
	biospecimen_data.new_tumor_event_after_initial_treatment, string, "Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment."
	biospecimen_data.num_portions, integer, "The number of portions obtained from the sample"
	biospecimen_data.num_slides, integer, "The number of slides derived from the sample"
	biospecimen_data.number_of_lymphnodes_examined, integer, "The total number of lymph nodes removed and pathologically assessed for disease."
	biospecimen_data.number_of_lymphnodes_positive_by_he, integer, "Numeric value to signify the count of positive lymph nodes identified through hematoxylin and eosin (H&E) staining light microscopy."
	biospecimen_data.number_pack_years_smoked, integer, "Numeric computed value to represent lifetime tobacco exposure defined as number of cigarettes smoked per day x number of years smoked divided by 20."
	biospecimen_data.other_dx, string, "Text term to describe the patient's history of cancer diagnosis and the spatial location of any previous cancer occurrence."
	biospecimen_data.other_malignancy_anatomic_site, string, "Text term describe the anatomic site of the prior or synchronous malignancy."
	biospecimen_data.other_malignancy_histological_type, string, "Text term describe the histology and/or subtype of the prior or synchronous malignancy."
	biospecimen_data.other_malignancy_type, string, "The type, relative occurance to the current malignancy"
	biospecimen_data.pathologic_M, string, "Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the regional lymph nodes, using criteria established by the American Joint Committee on Cancer (AJCC)."
	biospecimen_data.pathologic_N, string, "The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cancer Staging Manual."
	biospecimen_data.pathologic_stage, string, "The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria."
	biospecimen_data.pathologic_T, string, "Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American Joint Committee on Cancer (AJCC)."
	biospecimen_data.pathology_report_uuid, string, "The UUID of th epathology report"
	biospecimen_data.person_neoplasm_cancer_status, string, "The state or condition of an individual's neoplasm at a particular point in time."
	biospecimen_data.pregnancies, string, "Value to describe the number of full-term pregnancies that a woman has experienced."
	biospecimen_data.preservation_method, string, "The method used to preserve the sample after it has been removed from a participant."
	biospecimen_data.primary_neoplasm_melanoma_dx, string, "Text indicator to signify whether a person had a primary diagnosis of melanoma."
	biospecimen_data.primary_therapy_outcome_success, string, "Measure of success."
	biospecimen_data.program_name, string, "Project name, e.g. 'TCGA'."
	biospecimen_data.project_short_name, string, "Tumor type abbreviation, e.g. 'BRCA'. "
	biospecimen_data.psa_value, number, "The lab value that represents the results of the most recent (post-operative) prostatic-specific antigen (PSA) in the blood."
	biospecimen_data.race, string, "The text for reporting information about race based on the Office of Management and Budget (OMB) categories."
	biospecimen_data.residual_tumor, string, "Text terms to describe the status of a tissue margin following surgical resection."
	biospecimen_data.sample_barcode, string, "The barcode assigned by TCGA to a sample from a Participant."
	biospecimen_data.sample_gdc_id, string, "The GDC assigned id for the sample"
	biospecimen_data.sample_type, string, "The type of the sample tumor or normal tissue cell or blood sample provided by a participant."
	biospecimen_data.stopped_smoking_year, integer, "The year in which the participant quit smoking."
	biospecimen_data.summary_file_count, integer, "The count of files associated with the sample"
	biospecimen_data.tobacco_smoking_history, string, "Category describing current smoking status and smoking history as self-reported by a patient."
	biospecimen_data.tss_code, string, "A TSS ID is an alphanumeric code that uniquely identifies a TSS and its associated study"
	biospecimen_data.tumor_tissue_site, string, "Text term that describes the anatomic site of the tumor or disease."
	biospecimen_data.tumor_type, string, "Text term to identify the morphologic subtype of papillary renal cell carcinoma."
	biospecimen_data.venous_invasion, string, "The result of an assessment using the Weiss histopathologic criteria."
	biospecimen_data.vital_status, string, "The survival state of the person registered on the protocol."
	biospecimen_data.weight, integer, "The weight of the patient measured in kilograms."
	biospecimen_data.year_of_diagnosis, integer, "Numeric value to represent the year of an individual's initial pathologic diagnosis of cancer."
	biospecimen_data.year_of_tobacco_smoking_onset, integer, "The year in which the participant began smoking."
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
=======
samples().get()
################
Given a sample barcode (of length 16, *eg* TCGA-B9-7268-01A), this endpoint returns all available "biospecimen" information about this sample, the associated patient barcode, a list of associated aliquots, and a list of "data_details" blocks describing each of the data files associated with this sample

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/samples/TCGA-ZH-A8Y6-1A

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v2/isb_cgc_api.samples.get?sample_barcode=TCGA-ZH-A8Y6-01A&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.samples().get(sample_barcode='TCGA-W5-AA2R-01A').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/samples/{sample_barcode}

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
    "aliquots": [string],
    "biospecimen_data": {
      "age_at_initial_pathologic_diagnosis": integer,
      "anatomic_neoplasm_subdivision": string,
      "avg_percent_lymphocyte_infiltration": number,
      "avg_percent_monocyte_infiltration": number,
      "avg_percent_necrosis": number,
      "avg_percent_neutrophil_infiltration": number,
      "avg_percent_normal_cells": number,
      "avg_percent_stromal_cells": number,
      "avg_percent_tumor_cells": number,
      "avg_percent_tumor_nuclei": number,
      "batch_number": integer,
      "bcr": string,
      "BMI": number,
      "clinical_M": string,
      "clinical_N": string,
      "clinical_stage": string,
      "clinical_T": string,
      "colorectal_cancer": string,
      "country": string,
      "days_to_birth": integer,
      "days_to_collection": integer,
      "days_to_death": integer,
      "days_to_initial_pathologic_diagnosis": integer,
      "days_to_last_followup": integer,
      "days_to_last_known_alive": integer,
      "days_to_submitted_specimen_dx": integer,
      "ethnicity": string,
      "frozen_specimen_anatomic_site": string,
      "gender": string,
      "gleason_score_combined": integer,
      "has_27k": boolean,
      "has_450k": boolean,
      "has_BCGSC_GA_RNASeq": boolean,
      "has_BCGSC_HiSeq_RNASeq": boolean,
      "has_GA_miRNASeq": boolean,
      "has_HiSeq_miRnaSeq": boolean,
      "has_Illumina_DNASeq": boolean,
      "has_RPPA": boolean,
      "has_SNP6": boolean,
      "has_UNC_GA_RNASeq": boolean,
      "has_UNC_HiSeq_RNASeq": boolean,
      "height": integer,
      "histological_type": string,
      "history_of_colon_polyps": string,
      "history_of_neoadjuvant_treatment": string,
      "history_of_prior_malignancy": string,
      "hpv_calls": string,
      "hpv_status": string,
      "icd_10": string,
      "icd_o_3_histology": string,
      "icd_o_3_site": string,
      "lymphatic_invasion": string,
      "lymphnodes_examined": string,
      "lymphovascular_invasion_present": string,
      "max_percent_lymphocyte_infiltration": number,
      "max_percent_monocyte_infiltration": number,
      "max_percent_necrosis": number,
      "max_percent_neutrophil_infiltration": number,
      "max_percent_normal_cells": number,
      "max_percent_stromal_cells": number,
      "max_percent_tumor_cells": number,
      "max_percent_tumor_nuclei": number,
      "menopause_status": string,
      "min_percent_lymphocyte_infiltration": number,
      "min_percent_monocyte_infiltration": number,
      "min_percent_necrosis": number,
      "min_percent_neutrophil_infiltration": number,
      "min_percent_normal_cells": number,
      "min_percent_stromal_cells": number,
      "min_percent_tumor_cells": number,
      "min_percent_tumor_nuclei": number,
      "mononucleotide_and_dinucleotide_marker_panel_analysis_status": string,
      "mononucleotide_marker_panel_analysis_status": string,
      "neoplasm_histologic_grade": string,
      "new_tumor_event_after_initial_treatment": string,
      "number_of_lymphnodes_examined": integer,
      "number_of_lymphnodes_positive_by_he": integer,
      "number_pack_years_smoked": integer,
      "ParticipantBarcode": string,
      "pathologic_M": string,
      "pathologic_N": string,
      "pathologic_stage": string,
      "pathologic_T": string,
      "person_neoplasm_cancer_status": string,
      "pregnancies": string,
      "primary_neoplasm_melanoma_dx": string,
      "primary_therapy_outcome_success": string,
      "prior_dx": string,
      "Project": string,
      "psa_value": number,
      "race": string,
      "residual_tumor": string,
      "SampleBarcode": string,
      "SampleTypeCode": string,
      "Study": string,
      "tobacco_smoking_history": string,
      "TSSCode": string,
      "tumor_tissue_site": string,
      "tumor_type": string,
      "vital_status": string,
      "weight": integer,
      "weiss_venous_invasion": string,
      "year_of_initial_pathologic_diagnosis": integer
    },
    "data_details": [
      {
        "cloud_storage_path": string,
        "DataCenterName": string,
        "DataCenterType": string,
        "DataFileName": string,
        "DataFileNameKey": string,
        "DatafileUploaded": string,
        "DataLevel": string,
        "Datatype": string,
        "GenomeReference": string,
        "GG_dataset_id": string,
        "GG_readgroupset_id": string,
        "Pipeline": string,
        "Platform": string,
        "platform_full_name": string,
        "Project": string,
        "Repository": string,
        "SampleBarcode": string,
        "SDRFFileName": string,
        "SecurityProtocol": string
      }
    ],
    "data_details_count": integer,
    "patient": string
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	aliquots[], list, "List of barcodes of aliquots taken from this participant."
	biospecimen_data, nested object, "Biospecimen data about the sample."
	biospecimen_data.age_at_initial_pathologic_diagnosis, integer, "Age at which a condition or disease was first diagnosed in years."
	biospecimen_data.anatomic_neoplasm_subdivision, string, "Text term to describe the spatial location, subdivisions and/or anatomic site name of a tumor."
	biospecimen_data.avg_percent_lymphocyte_infiltration, number, "Average in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_monocyte_infiltration, number, "Average in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_necrosis, number, "Average in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_neutrophil_infiltration, number, "Average in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_normal_cells, number, "Average in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_stromal_cells, number, "Average in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_tumor_cells, number, "Average in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_tumor_nuclei, number, "Average in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.batch_number, integer, "Groups samples by the batch they were processed in."
	biospecimen_data.bcr, string, "A TCGA center where samples are carefully catalogued, processed, quality-checked and stored along with participant clinical information."
	biospecimen_data.BMI, number, "Body Mass Index"
	biospecimen_data.clinical_M, string, "Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	biospecimen_data.clinical_N, string, "Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	biospecimen_data.clinical_stage, string, "Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis."
	biospecimen_data.clinical_T, string, "Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	biospecimen_data.colorectal_cancer, string, "Text term to signify whether a patient has been diagnosed with colorectal cancer."
	biospecimen_data.country, string, "Text to identify the name of the state, province, or country in which the sample was procured."
	biospecimen_data.days_to_birth, integer, "Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_collection, integer, ""
	biospecimen_data.days_to_death, integer, "Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_initial_pathologic_diagnosis, integer, "Numeric value to represent the day of an individual's initial pathologic diagnosis of cancer."
	biospecimen_data.days_to_last_followup, integer, "Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_last_known_alive, integer, ""
	biospecimen_data.days_to_submitted_specimen_dx, integer, "Time interval from the date of diagnosis of the submitted sample to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.ethnicity, string, "The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories."
	biospecimen_data.frozen_specimen_anatomic_site, string, "Text description of the origin and the anatomic site regarding the frozen biospecimen tumor tissue sample."
	biospecimen_data.gender, string, "Text designations that identify gender."
	biospecimen_data.gleason_score_combined, integer, ""
	biospecimen_data.has_27k, boolean, "Indicates if a sample has methylation data from the Illumina 27k platform. 'True', 'False', or 'None'."
	biospecimen_data.has_450k, boolean, "Indicates if a sample has methylation data from the Illumina 450k platform. 'True', 'False', or 'None'."
	biospecimen_data.has_BCGSC_GA_RNASeq, boolean, "Indicates if a sample has RNA sequencing data from the IlluminaGA platform and the BCGSC pipeline. 'True', 'False', or 'None'."
	biospecimen_data.has_BCGSC_HiSeq_RNASeq, boolean, "Indicates if a sample has RNA sequencing data from the IlluminaHiSeq platform and the BCGSC pipeline. 'True', 'False', or 'None'."
	biospecimen_data.has_GA_miRNASeq, boolean, "Indicates if a sample has microRNA data from the IlluminaGA platform. 'True', 'False', or 'None'."
	biospecimen_data.has_HiSeq_miRnaSeq, boolean, "Indicates if a sample has microRNA data from the IlluminaHiSeq platform. 'True', 'False', or 'None'."
	biospecimen_data.has_Illumina_DNASeq, boolean, "Indicates if a sample has gene sequencing data. 'True', 'False', or 'None'."
	biospecimen_data.has_RPPA, boolean, "Indicates if a sample has protein array data. 'True', 'False', or 'None'."
	biospecimen_data.has_SNP6, boolean, "Indicates if a sample has copy number data. 'True', 'False', or 'None'."
	biospecimen_data.has_UNC_GA_RNASeq, boolean, "Indicates if a sample has RNA sequencing data from the IlluminaGA platform and the UNC pipeline. 'True', 'False', or 'None'."
	biospecimen_data.has_UNC_HiSeq_RNASeq, boolean, "Indicates if a sample has RNA sequencing data from the IlluminaHiSeq platform and the UNC pipeline. 'True', 'False', or 'None'."
	biospecimen_data.height, integer, "The height of the patient in centimeters."
	biospecimen_data.histological_type, string, "Text term for the structural pattern of cancer cells used to define a microscopic diagnosis."
	biospecimen_data.history_of_colon_polyps, string, "Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report(s)."
	biospecimen_data.history_of_neoadjuvant_treatment, string, "Text term to describe the patient's history of neoadjuvant treatment and the kind of treatment given prior to resection of the tumor."
	biospecimen_data.history_of_prior_malignancy, string, "Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence."
	biospecimen_data.hpv_calls, string, "Results of HPV tests."
	biospecimen_data.hpv_status, string, "Current HPV status."
	biospecimen_data.icd_10, string, "The tenth version of the International Classification of Disease (ICD)."
	biospecimen_data.icd_o_3_histology, string, "The third edition of the International Classification of Diseases for Oncology."
	biospecimen_data.icd_o_3_site, string, "The third edition of the International Classification of Diseases for Oncology."
	biospecimen_data.lymphatic_invasion, string, "A yes/no indicator to ask if malignant cells are present in small or thin-walled vessels suggesting lymphatic involvement."
	biospecimen_data.lymphnodes_examined, string, "A yes/no/unknown indicator whether a lymph node assessment was performed at the primary presentation of disease."
	biospecimen_data.lymphovascular_invasion_present, string, "A yes/no indicator to ask if large vessel (vascular) invasion or small, thin-walled (lymphatic) invasion was detected in a tumor specimen."
	biospecimen_data.max_percent_lymphocyte_infiltration, number, "Maximum in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_monocyte_infiltration, number, "Maximum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_necrosis, number, "Maximum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_neutrophil_infiltration, number, "Maximum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_normal_cells, number, "Maximum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_stromal_cells, number, "Maximum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_tumor_cells, number, "Maximum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_tumor_nuclei, number, "Maximum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.menopause_status, string, "Text term to signify the status of a woman's menopause, the permanent cessation of menses, usually defined by 6 to 12 months of amenorrhea."
	biospecimen_data.min_percent_lymphocyte_infiltration, number, "Minimum in the series of numeric values to represent the percentage of lymphcyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_monocyte_infiltration, number, "Minimum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_necrosis, number, "Minimum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_neutrophil_infiltration, number, "Minimum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_normal_cells, number, "Minimum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_stromal_cells, number, "Minimum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_tumor_cells, number, "Minimum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_tumor_nuclei, number, "Minimum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.mononucleotide_and_dinucleotide_marker_panel_analysis_status, string, "Text result of microsatellite instability (MSI) testing at using a mononucleotide and dinucleotide microsatellite panel."
	biospecimen_data.mononucleotide_marker_panel_analysis_status, string, "Text result of microsatellite instability (MSI) testing using a mononucleotide microsatellite panel."
	biospecimen_data.neoplasm_histologic_grade, string, "Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness."
	biospecimen_data.new_tumor_event_after_initial_treatment, string, "Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment."
	biospecimen_data.number_of_lymphnodes_examined, integer, "The total number of lymph nodes removed and pathologically assessed for disease."
	biospecimen_data.number_of_lymphnodes_positive_by_he, integer, "Numeric value to signify the count of positive lymph nodes identified through hematoxylin and eosin (H&E) staining light microscopy."
	biospecimen_data.number_pack_years_smoked, integer, ""
	biospecimen_data.ParticipantBarcode, string, "Participant barcode."
	biospecimen_data.pathologic_M, string, "Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the regional lymph nodes, using criteria established by the American Joint Committee on Cancer (AJCC)."
	biospecimen_data.pathologic_N, string, "The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cancer Staging Manual."
	biospecimen_data.pathologic_stage, string, "The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria."
	biospecimen_data.pathologic_T, string, "Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American Joint Committee on Cancer (AJCC)."
	biospecimen_data.person_neoplasm_cancer_status, string, "The state or condition of an individual's neoplasm at a particular point in time."
	biospecimen_data.pregnancies, string, "Value to describe the number of full-term pregnancies that a woman has experienced."
	biospecimen_data.primary_neoplasm_melanoma_dx, string, "Text indicator to signify whether a person had a primary diagnosis of melanoma."
	biospecimen_data.primary_therapy_outcome_success, string, "Measure of success."
	biospecimen_data.prior_dx, string, "Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence."
	biospecimen_data.Project, string, "Project name, e.g. 'TCGA'."
	biospecimen_data.psa_value, number, "The lab value that represents the results of the most recent (post-operative) prostatic-specific antigen (PSA) in the blood."
	biospecimen_data.race, string, "The text for reporting information about race based on the Office of Management and Budget (OMB) categories."
	biospecimen_data.residual_tumor, string, "Text terms to describe the status of a tissue margin following surgical resection."
	biospecimen_data.SampleBarcode, string, "The barcode assigned by TCGA to a sample from a Participant."
	biospecimen_data.SampleTypeCode, string, "The type of the sample tumor or normal tissue cell or blood sample provided by a participant."
	biospecimen_data.Study, string, "Tumor type abbreviation, e.g. 'BRCA'. "
	biospecimen_data.tobacco_smoking_history, string, "Category describing current smoking status and smoking history as self-reported by a patient."
	biospecimen_data.TSSCode, string, ""
	biospecimen_data.tumor_tissue_site, string, "Text term that describes the anatomic site of the tumor or disease."
	biospecimen_data.tumor_type, string, "Text term to identify the morphologic subtype of papillary renal cell carcinoma."
	biospecimen_data.vital_status, string, "The survival state of the person registered on the protocol."
	biospecimen_data.weight, integer, "The weight of the patient measured in kilograms."
	biospecimen_data.weiss_venous_invasion, string, "The result of an assessment using the Weiss histopathologic criteria."
	biospecimen_data.year_of_initial_pathologic_diagnosis, integer, "Numeric value to represent the year of an individual's initial pathologic diagnosis of cancer."
	data_details[], list, "List of information about each file associated with the sample barcode."
	data_details[].cloud_storage_path, string, "Google Cloud Storage path to file."
	data_details[].DataCenterName, string, "Short name of the contributing data center, e.g. bcgsc.ca."
	data_details[].DataCenterType, string, "Abbreviation of the type of contributing data center, e.g. cgcc."
	data_details[].DataFileName, string, "Name of the datafile stored on the DCC file system."
	data_details[].DataFileNameKey, string, "Key into the ISB-CGC GCS bucket for this file."
	data_details[].DatafileUploaded, string, "Whether the file fit requirements to be uploaded into the project."
	data_details[].DataLevel, string, "Level of the type of data, depending on where it is stored in the DCC directory structure. Data levels are defined by TCGA DCC."
	data_details[].Datatype, string, "Data type, e.g. Complete Clinical Set, CNV (SNP Array), DNA Methylation, Expression-Protein, Fragment Analysis Results, miRNASeq, Protected Mutations, RNASeq, RNASeqV2, Somatic Mutations, TotalRNASeqV."
	data_details[].GenomeReference, string, "Allows a center to associate results with a specific genome build that was used as the basis for analysis, e.g. hg19 (GRCh37)"
	data_details[].Pipeline, string, "A combination of the center and the platform that can distinguish between two ways of performing the sequencing or assay for the same platform, e.g. bcgsc.ca__miRNASeq."
	data_details[].Platform, string, "A platform (within the scope of TCGA) is a vendor-specific technology for assaying or sequencing that could possibly be customized by a GSC or CGCC, e.g. IlluminaHiSeq_miRNASeq."
	data_details[].platform_full_name, string, "The full name of the sequencing platform used, e.g. Illumina HiSeq 2000, Ion Torrent PGM, AB SOLiD System 2.0."
	data_details[].Project, string, "The study for which the data was generated, e.g. TCGA."
	data_details[].Repository, string, "A storage location where files are deposited and made available, e.g. DCC, CGHub."
	data_details[].SampleBarcode, string, "Sample barcode."
	data_details[].SDRFFileName, string, "Name of SDRF file stored on the DCC file system, e.g. bcgsc.ca_KIRC.IlluminaHiSeq_miRNASeq.sdrf.txt"
	data_details[].SecurityProtocol, string, "An indication of the security protocol necessary to fulfill in order to access the data from the file, e.g. DBGap Protected Access, DBGap Open Access"
	data_details_count, integer, "Number of files associated with the sample barcode."
	patient, string, "Patient barcode."

..  data_details[].GG_dataset_id, string, "Google genomics dataset id."
..  data_details[].GG_readgroupset_id, string, "Google genomics readgroupset id."
=======
samples().get()
################
Given a sample barcode (of length 16, *eg* TCGA-B9-7268-01A), this endpoint returns all available "biospecimen" information about this sample, the associated case barcode, a list of associated aliquots, and a list of "data_details" blocks describing each of the data files associated with this sample

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/samples/TCGA-ZH-A8Y6-1A

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_tcga_api/v3/isb_cgc_tcga_api.samples.get?sample_barcode=TCGA-ZH-A8Y6-01A&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.samples().get(sample_barcode='TCGA-W5-AA2R-01A').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/samples/{sample_barcode}

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
      "age_began_smoking_in_years": integer,
      "anatomic_neoplasm_subdivision": string,
      "avg_percent_lymphocyte_infiltration": number,
      "avg_percent_monocyte_infiltration": number,
      "avg_percent_necrosis": number,
      "avg_percent_neutrophil_infiltration": number,
      "avg_percent_normal_cells": number,
      "avg_percent_stromal_cells": number,
      "avg_percent_tumor_cells": number,
      "avg_percent_tumor_nuclei": number,
      "batch_number": integer,
      "bcr": string,
      "bmi": number,
      "case_barcode": string,
      "case_gdc_id": string,
      "clinical_M": string,
      "clinical_N": string,
      "clinical_stage": string,
      "clinical_T": string,
      "colorectal_cancer": string,
      "country": string,
      "days_to_birth": integer,
      "days_to_collection": integer,
      "days_to_death": integer,
      "days_to_initial_pathologic_diagnosis": integer,
      "days_to_last_followup": integer,
      "days_to_last_known_alive": integer,
      "days_to_sample_procurement": integer,
      "days_to_submitted_specimen_dx": integer,
      "disease_code": string,
      "endpoint_type": string,
      "ethnicity": string,
      "gender": string,
      "gleason_score_combined": integer,
      "h_pylori_infection": string,
      "height": integer,
      "histological_type": string,
      "history_of_colon_polyps": string,
      "history_of_neoadjuvant_treatment": string,
      "hpv_calls": string,
      "hpv_status": string,
      "icd_10": string,
      "icd_o_3_histology": string,
      "icd_o_3_site": string,
      "lymphatic_invasion": string,
      "lymphnodes_examined": string,
      "lymphovascular_invasion_present": string,
      "max_percent_lymphocyte_infiltration": number,
      "max_percent_monocyte_infiltration": number,
      "max_percent_necrosis": number,
      "max_percent_neutrophil_infiltration": number,
      "max_percent_normal_cells": number,
      "max_percent_stromal_cells": number,
      "max_percent_tumor_cells": number,
      "max_percent_tumor_nuclei": number,
      "menopause_status": string,
      "min_percent_lymphocyte_infiltration": number,
      "min_percent_monocyte_infiltration": number,
      "min_percent_necrosis": number,
      "min_percent_neutrophil_infiltration": number,
      "min_percent_normal_cells": number,
      "min_percent_stromal_cells": number,
      "min_percent_tumor_cells": number,
      "min_percent_tumor_nuclei": number,
      "mononucleotide_and_dinucleotide_marker_panel_analysis_status": string,
      "neoplasm_histologic_grade": string,
      "new_tumor_event_after_initial_treatment": string,
      "num_portions": integer,
      "num_slides": integer,
      "number_of_lymphnodes_examined": integer,
      "number_of_lymphnodes_positive_by_he": integer,
      "number_pack_years_smoked": integer,
      "other_dx": string,
      "other_malignancy_anatomic_site": string,
      "other_malignancy_histological_type": string,
      "other_malignancy_type": string,
      "pathologic_M": string,
      "pathologic_N": string,
      "pathologic_stage": string,
      "pathologic_T": string,
      "pathology_report_uuid": string,
      "person_neoplasm_cancer_status": string,
      "pregnancies": string,
      "preservation_method": string,
      "primary_neoplasm_melanoma_dx": string,
      "primary_therapy_outcome_success": string,
      "program_name": string,
      "project_short_name": string,
      "psa_value": number,
      "race": string,
      "residual_tumor": string,
      "sample_barcode": string,
      "sample_gdc_id": string,
      "sample_type": string,
      "stopped_smoking_year": integer,
      "summary_file_count": integer,
      "tobacco_smoking_history": string,
      "tss_code": string,
      "tumor_tissue_site": string,
      "tumor_type": string,
      "venous_invasion": string,
      "vital_status": string,
      "weight": integer,
      "year_of_diagnosis": integer,
      "year_of_tobacco_smoking_onset": integer
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
	biospecimen_data.age_began_smoking_in_years, integer, "Age began smoking cigarettes expressed in number of years since birth."
	biospecimen_data.anatomic_neoplasm_subdivision, string, "Text term to describe the spatial location, subdivisions and/or anatomic site name of a tumor."
	biospecimen_data.avg_percent_lymphocyte_infiltration, number, "Average in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_monocyte_infiltration, number, "Average in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_necrosis, number, "Average in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_neutrophil_infiltration, number, "Average in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_normal_cells, number, "Average in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_stromal_cells, number, "Average in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_tumor_cells, number, "Average in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_tumor_nuclei, number, "Average in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.batch_number, integer, "Groups samples by the batch they were processed in."
	biospecimen_data.bcr, string, "A TCGA center where samples are carefully catalogued, processed, quality-checked and stored along with participant clinical information."
	biospecimen_data.bmi, number, "Body Mass Index"
	biospecimen_data.case_barcode, string, "Case barcode."
	biospecimen_data.case_gdc_id, string, "The GDC assigned id for the case"
	biospecimen_data.clinical_M, string, "Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	biospecimen_data.clinical_N, string, "Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	biospecimen_data.clinical_stage, string, "Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis."
	biospecimen_data.clinical_T, string, "Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	biospecimen_data.colorectal_cancer, string, "Text term to signify whether a patient has been diagnosed with colorectal cancer."
	biospecimen_data.country, string, "Text to identify the name of the state, province, or country in which the sample was procured."
	biospecimen_data.days_to_birth, integer, "Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_collection, integer, "The number of days between diagnosis and tissue collection."
	biospecimen_data.days_to_death, integer, "Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_initial_pathologic_diagnosis, integer, "Numeric value to represent the day of an individual's initial pathologic diagnosis of cancer."
	biospecimen_data.days_to_last_followup, integer, "Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.days_to_last_known_alive, integer, "The number of days between diagnosis and when the individual was last known to be alive."
	biospecimen_data.days_to_sample_procurement, integer, "Indicates the days to sample procurement for the submitted sample in relation to the date of initial diagnosis"
	biospecimen_data.days_to_submitted_specimen_dx, integer, "Time interval from the date of diagnosis of the submitted sample to the date of initial pathologic diagnosis, represented as a calculated number of days."
	biospecimen_data.disease_code, string, "Text term referring to the cancer type"
	biospecimen_data.endpoint_type, string, "Which type of GDC Case API was used, either legacy or current"
	biospecimen_data.ethnicity, string, "The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories."
	biospecimen_data.gender, string, "Text designations that identify gender."
	biospecimen_data.gleason_score_combined, integer, "A numeric value obtained by adding the primary and secondary patterns (grades)."
	biospecimen_data.h_pylori_infection, string, "Text term to indicate the state of the diagnosis of an individual with Helicobacter pylori infection."
	biospecimen_data.height, integer, "The height of the patient in centimeters."
	biospecimen_data.histological_type, string, "Text term for the structural pattern of cancer cells used to define a microscopic diagnosis."
	biospecimen_data.history_of_colon_polyps, string, "Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report(s)."
	biospecimen_data.history_of_neoadjuvant_treatment, string, "Text term to describe the patient's history of neoadjuvant treatment and the kind of treatment given prior to resection of the tumor."
	biospecimen_data.hpv_calls, string, "Results of HPV tests."
	biospecimen_data.hpv_status, string, "Current HPV status."
	biospecimen_data.icd_10, string, "The tenth version of the International Classification of Disease (ICD)."
	biospecimen_data.icd_o_3_histology, string, "The third edition of the International Classification of Diseases for Oncology."
	biospecimen_data.icd_o_3_site, string, "The third edition of the International Classification of Diseases for Oncology."
	biospecimen_data.lymphatic_invasion, string, "A yes/no indicator to ask if malignant cells are present in small or thin-walled vessels suggesting lymphatic involvement."
	biospecimen_data.lymphnodes_examined, string, "A yes/no/unknown indicator whether a lymph node assessment was performed at the primary presentation of disease."
	biospecimen_data.lymphovascular_invasion_present, string, "A yes/no indicator to ask if large vessel (vascular) invasion or small, thin-walled (lymphatic) invasion was detected in a tumor specimen."
	biospecimen_data.max_percent_lymphocyte_infiltration, number, "Maximum in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_monocyte_infiltration, number, "Maximum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_necrosis, number, "Maximum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_neutrophil_infiltration, number, "Maximum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_normal_cells, number, "Maximum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_stromal_cells, number, "Maximum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_tumor_cells, number, "Maximum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_tumor_nuclei, number, "Maximum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.menopause_status, string, "Text term to signify the status of a woman's menopause, the permanent cessation of menses, usually defined by 6 to 12 months of amenorrhea."
	biospecimen_data.min_percent_lymphocyte_infiltration, number, "Minimum in the series of numeric values to represent the percentage of lymphcyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_monocyte_infiltration, number, "Minimum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_necrosis, number, "Minimum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_neutrophil_infiltration, number, "Minimum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_normal_cells, number, "Minimum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_stromal_cells, number, "Minimum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_tumor_cells, number, "Minimum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_tumor_nuclei, number, "Minimum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.mononucleotide_and_dinucleotide_marker_panel_analysis_status, string, "Text result of microsatellite instability (MSI) testing at using a mononucleotide and dinucleotide microsatellite panel."
	biospecimen_data.neoplasm_histologic_grade, string, "Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness."
	biospecimen_data.new_tumor_event_after_initial_treatment, string, "Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment."
	biospecimen_data.num_portions, integer, "The number of portions obtained from the sample"
	biospecimen_data.num_slides, integer, "The number of slides derived from the sample"
	biospecimen_data.number_of_lymphnodes_examined, integer, "The total number of lymph nodes removed and pathologically assessed for disease."
	biospecimen_data.number_of_lymphnodes_positive_by_he, integer, "Numeric value to signify the count of positive lymph nodes identified through hematoxylin and eosin (H&E) staining light microscopy."
	biospecimen_data.number_pack_years_smoked, integer, "Numeric computed value to represent lifetime tobacco exposure defined as number of cigarettes smoked per day x number of years smoked divided by 20."
	biospecimen_data.other_dx, string, "Text term to describe the patient's history of cancer diagnosis and the spatial location of any previous cancer occurrence."
	biospecimen_data.other_malignancy_anatomic_site, string, "Text term describe the anatomic site of the prior or synchronous malignancy."
	biospecimen_data.other_malignancy_histological_type, string, "Text term describe the histology and/or subtype of the prior or synchronous malignancy."
	biospecimen_data.other_malignancy_type, string, "The type, relative occurance to the current malignancy"
	biospecimen_data.pathologic_M, string, "Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the regional lymph nodes, using criteria established by the American Joint Committee on Cancer (AJCC)."
	biospecimen_data.pathologic_N, string, "The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cancer Staging Manual."
	biospecimen_data.pathologic_stage, string, "The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria."
	biospecimen_data.pathologic_T, string, "Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American Joint Committee on Cancer (AJCC)."
	biospecimen_data.pathology_report_uuid, string, "The UUID of th epathology report"
	biospecimen_data.person_neoplasm_cancer_status, string, "The state or condition of an individual's neoplasm at a particular point in time."
	biospecimen_data.pregnancies, string, "Value to describe the number of full-term pregnancies that a woman has experienced."
	biospecimen_data.preservation_method, string, "The method used to preserve the sample after it has been removed from a participant."
	biospecimen_data.primary_neoplasm_melanoma_dx, string, "Text indicator to signify whether a person had a primary diagnosis of melanoma."
	biospecimen_data.primary_therapy_outcome_success, string, "Measure of success."
	biospecimen_data.program_name, string, "Project name, e.g. 'TCGA'."
	biospecimen_data.project_short_name, string, "Tumor type abbreviation, e.g. 'BRCA'. "
	biospecimen_data.psa_value, number, "The lab value that represents the results of the most recent (post-operative) prostatic-specific antigen (PSA) in the blood."
	biospecimen_data.race, string, "The text for reporting information about race based on the Office of Management and Budget (OMB) categories."
	biospecimen_data.residual_tumor, string, "Text terms to describe the status of a tissue margin following surgical resection."
	biospecimen_data.sample_barcode, string, "The barcode assigned by TCGA to a sample from a Participant."
	biospecimen_data.sample_gdc_id, string, "The GDC assigned id for the sample"
	biospecimen_data.sample_type, string, "The type of the sample tumor or normal tissue cell or blood sample provided by a participant."
	biospecimen_data.stopped_smoking_year, integer, "The year in which the participant quit smoking."
	biospecimen_data.summary_file_count, integer, "The count of files associated with the sample"
	biospecimen_data.tobacco_smoking_history, string, "Category describing current smoking status and smoking history as self-reported by a patient."
	biospecimen_data.tss_code, string, "A TSS ID is an alphanumeric code that uniquely identifies a TSS and its associated study"
	biospecimen_data.tumor_tissue_site, string, "Text term that describes the anatomic site of the tumor or disease."
	biospecimen_data.tumor_type, string, "Text term to identify the morphologic subtype of papillary renal cell carcinoma."
	biospecimen_data.venous_invasion, string, "The result of an assessment using the Weiss histopathologic criteria."
	biospecimen_data.vital_status, string, "The survival state of the person registered on the protocol."
	biospecimen_data.weight, integer, "The weight of the patient measured in kilograms."
	biospecimen_data.year_of_diagnosis, integer, "Numeric value to represent the year of an individual's initial pathologic diagnosis of cancer."
	biospecimen_data.year_of_tobacco_smoking_onset, integer, "The year in which the participant began smoking."
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
