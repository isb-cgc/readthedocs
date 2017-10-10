cases().get()
##############
Returns information about a specific case, including a list of samples and aliquots derived from this case. Takes a case barcode (of length 12, *eg* TCGA-B9-7268) as a required parameter. User does not need to be authenticated.

**Example**::

	curl https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/cases/TCGA-ZH-A8Y6

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_tcga_api/v3/isb_cgc_tcga_api.cases.get?case_barcode=TCGA-ZH-A8Y6&/>`_ to see this endpoint in Google's API explorer.

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
	data = service.cases().get(case_barcode='TCGA-W5-AA2R').execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/cases/{case_barcode}

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
    "samples": [string]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	aliquots[], list, "List of barcodes of aliquots taken from this patient."
	clinical_data, nested object, "The clinical data about the patient."
	clinical_data.age_at_diagnosis, integer, "Age at which a condition or disease was first diagnosed in years."
	clinical_data.age_began_smoking_in_years, integer, "Age began smoking cigarettes expressed in number of years since birth."
	clinical_data.anatomic_neoplasm_subdivision, string, "Text term to describe the spatial location, subdivisions and/or anatomic site name of a tumor."
	clinical_data.avg_percent_lymphocyte_infiltration, number, "Average in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen."
	clinical_data.avg_percent_monocyte_infiltration, number, "Average in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	clinical_data.avg_percent_necrosis, number, "Average in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	clinical_data.avg_percent_neutrophil_infiltration, number, "Average in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	clinical_data.avg_percent_normal_cells, number, "Average in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	clinical_data.avg_percent_stromal_cells, number, "Average in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	clinical_data.avg_percent_tumor_cells, number, "Average in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	clinical_data.avg_percent_tumor_nuclei, number, "Average in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	clinical_data.batch_number, integer, "Groups samples by the batch they were processed in."
	clinical_data.bcr, string, "A TCGA center where samples are carefully catalogued, processed, quality-checked and stored along with participant clinical information."
	clinical_data.bmi, number, "Body Mass Index"
	clinical_data.case_barcode, string, "Case barcode."
	clinical_data.case_gdc_id, string, "The GDC assigned id for the case"
	clinical_data.clinical_M, string, "Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	clinical_data.clinical_N, string, "Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	clinical_data.clinical_stage, string, "Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis."
	clinical_data.clinical_T, string, "Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	clinical_data.colorectal_cancer, string, "Text term to signify whether a patient has been diagnosed with colorectal cancer."
	clinical_data.country, string, "Text to identify the name of the state, province, or country in which the sample was procured."
	clinical_data.days_to_birth, integer, "Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.days_to_collection, integer, "The number of days between diagnosis and tissue collection."
	clinical_data.days_to_death, integer, "Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.days_to_initial_pathologic_diagnosis, integer, "Numeric value to represent the day of an individual's initial pathologic diagnosis of cancer."
	clinical_data.days_to_last_followup, integer, "Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.days_to_last_known_alive, integer, "The number of days between diagnosis and when the individual was last known to be alive."
	clinical_data.days_to_sample_procurement, integer, "Indicates the days to sample procurement for the submitted sample in relation to the date of initial diagnosis"
	clinical_data.days_to_submitted_specimen_dx, integer, "Time interval from the date of diagnosis of the submitted sample to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.disease_code, string, "Text term referring to the cancer type"
	clinical_data.endpoint_type, string, "Which type of GDC Case API was used, either legacy or current"
	clinical_data.ethnicity, string, "The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories."
	clinical_data.gender, string, "Text designations that identify gender."
	clinical_data.gleason_score_combined, integer, "A numeric value obtained by adding the primary and secondary patterns (grades)."
	clinical_data.h_pylori_infection, string, "Text term to indicate the state of the diagnosis of an individual with Helicobacter pylori infection."
	clinical_data.height, integer, "The height of the patient in centimeters."
	clinical_data.histological_type, string, "Text term for the structural pattern of cancer cells used to define a microscopic diagnosis."
	clinical_data.history_of_colon_polyps, string, "Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report(s)."
	clinical_data.history_of_neoadjuvant_treatment, string, "Text term to describe the patient's history of neoadjuvant treatment and the kind of treatment given prior to resection of the tumor."
	clinical_data.hpv_calls, string, "Results of HPV tests."
	clinical_data.hpv_status, string, "Current HPV status."
	clinical_data.icd_10, string, "The tenth version of the International Classification of Disease (ICD)."
	clinical_data.icd_o_3_histology, string, "The third edition of the International Classification of Diseases for Oncology."
	clinical_data.icd_o_3_site, string, "The third edition of the International Classification of Diseases for Oncology."
	clinical_data.lymphatic_invasion, string, "A yes/no indicator to ask if malignant cells are present in small or thin-walled vessels suggesting lymphatic involvement."
	clinical_data.lymphnodes_examined, string, "A yes/no/unknown indicator whether a lymph node assessment was performed at the primary presentation of disease."
	clinical_data.lymphovascular_invasion_present, string, "A yes/no indicator to ask if large vessel (vascular) invasion or small, thin-walled (lymphatic) invasion was detected in a tumor specimen."
	clinical_data.max_percent_lymphocyte_infiltration, number, "Maximum in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen."
	clinical_data.max_percent_monocyte_infiltration, number, "Maximum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	clinical_data.max_percent_necrosis, number, "Maximum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	clinical_data.max_percent_neutrophil_infiltration, number, "Maximum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	clinical_data.max_percent_normal_cells, number, "Maximum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	clinical_data.max_percent_stromal_cells, number, "Maximum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	clinical_data.max_percent_tumor_cells, number, "Maximum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	clinical_data.max_percent_tumor_nuclei, number, "Maximum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	clinical_data.menopause_status, string, "Text term to signify the status of a woman's menopause, the permanent cessation of menses, usually defined by 6 to 12 months of amenorrhea."
	clinical_data.min_percent_lymphocyte_infiltration, number, "Minimum in the series of numeric values to represent the percentage of lymphcyte infiltration in a malignant tumor sample or specimen."
	clinical_data.min_percent_monocyte_infiltration, number, "Minimum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	clinical_data.min_percent_necrosis, number, "Minimum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	clinical_data.min_percent_neutrophil_infiltration, number, "Minimum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	clinical_data.min_percent_normal_cells, number, "Minimum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	clinical_data.min_percent_stromal_cells, number, "Minimum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	clinical_data.min_percent_tumor_cells, number, "Minimum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	clinical_data.min_percent_tumor_nuclei, number, "Minimum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	clinical_data.mononucleotide_and_dinucleotide_marker_panel_analysis_status, string, "Text result of microsatellite instability (MSI) testing at using a mononucleotide and dinucleotide microsatellite panel."
	clinical_data.neoplasm_histologic_grade, string, "Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness."
	clinical_data.new_tumor_event_after_initial_treatment, string, "Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment."
	clinical_data.num_portions, integer, "The number of portions obtained from the sample"
	clinical_data.num_slides, integer, "The number of slides derived from the sample"
	clinical_data.number_of_lymphnodes_examined, integer, "The total number of lymph nodes removed and pathologically assessed for disease."
	clinical_data.number_of_lymphnodes_positive_by_he, integer, "Numeric value to signify the count of positive lymph nodes identified through hematoxylin and eosin (H&E) staining light microscopy."
	clinical_data.number_pack_years_smoked, integer, "Numeric computed value to represent lifetime tobacco exposure defined as number of cigarettes smoked per day x number of years smoked divided by 20."
	clinical_data.other_dx, string, "Text term to describe the patient's history of cancer diagnosis and the spatial location of any previous cancer occurrence."
	clinical_data.other_malignancy_anatomic_site, string, "Text term describe the anatomic site of the prior or synchronous malignancy."
	clinical_data.other_malignancy_histological_type, string, "Text term describe the histology and/or subtype of the prior or synchronous malignancy."
	clinical_data.other_malignancy_type, string, "The type, relative occurance to the current malignancy"
	clinical_data.pathologic_M, string, "Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the regional lymph nodes, using criteria established by the American Joint Committee on Cancer (AJCC)."
	clinical_data.pathologic_N, string, "The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cancer Staging Manual."
	clinical_data.pathologic_stage, string, "The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria."
	clinical_data.pathologic_T, string, "Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American Joint Committee on Cancer (AJCC)."
	clinical_data.pathology_report_uuid, string, "The UUID of th epathology report"
	clinical_data.person_neoplasm_cancer_status, string, "The state or condition of an individual's neoplasm at a particular point in time."
	clinical_data.pregnancies, string, "Value to describe the number of full-term pregnancies that a woman has experienced."
	clinical_data.preservation_method, string, "The method used to preserve the sample after it has been removed from a participant."
	clinical_data.primary_neoplasm_melanoma_dx, string, "Text indicator to signify whether a person had a primary diagnosis of melanoma."
	clinical_data.primary_therapy_outcome_success, string, "Measure of success."
	clinical_data.program_name, string, "Project name, e.g. 'TCGA'."
	clinical_data.project_short_name, string, "Tumor type abbreviation, e.g. 'BRCA'. "
	clinical_data.psa_value, number, "The lab value that represents the results of the most recent (post-operative) prostatic-specific antigen (PSA) in the blood."
	clinical_data.race, string, "The text for reporting information about race based on the Office of Management and Budget (OMB) categories."
	clinical_data.residual_tumor, string, "Text terms to describe the status of a tissue margin following surgical resection."
	clinical_data.sample_barcode, string, "The barcode assigned by TCGA to a sample from a Participant."
	clinical_data.sample_gdc_id, string, "The GDC assigned id for the sample"
	clinical_data.sample_type, string, "The type of the sample tumor or normal tissue cell or blood sample provided by a participant."
	clinical_data.stopped_smoking_year, integer, "The year in which the participant quit smoking."
	clinical_data.summary_file_count, integer, "The count of files associated with the sample"
	clinical_data.tobacco_smoking_history, string, "Category describing current smoking status and smoking history as self-reported by a patient."
	clinical_data.tss_code, string, "A TSS ID is an alphanumeric code that uniquely identifies a TSS and its associated study"
	clinical_data.tumor_tissue_site, string, "Text term that describes the anatomic site of the tumor or disease."
	clinical_data.tumor_type, string, "Text term to identify the morphologic subtype of papillary renal cell carcinoma."
	clinical_data.venous_invasion, string, "The result of an assessment using the Weiss histopathologic criteria."
	clinical_data.vital_status, string, "The survival state of the person registered on the protocol."
	clinical_data.weight, integer, "The weight of the patient measured in kilograms."
	clinical_data.year_of_diagnosis, integer, "Numeric value to represent the year of an individual's initial pathologic diagnosis of cancer."
	clinical_data.year_of_tobacco_smoking_onset, integer, "The year in which the participant began smoking."
	samples[], list, "List of barcodes of samples taken from this patient."
