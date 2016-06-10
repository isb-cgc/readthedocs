patient_details
###############
Returns information about a specific participant, including a list of samples and aliquots derived from this patient. Takes a participant barcode (of length 12, *eg* TCGA-B9-7268) as a required parameter. User does not need to be authenticated.

**Example**::

	curl "https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/patient_details?patient_barcode=TCGA-ZH-A8Y6"

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/cohort_api/v1/cohort_api.cohort_endpoints.cohorts.patient_details?patient_barcode=TCGA-ZH-A8Y6&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/patient_details

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	patient_barcode,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "aliquots": [string],
    "clinical_data": {
      "age_at_initial_pathologic_diagnosis": string,
      "anatomic_neoplasm_subdivision": string,
      "batch_number": string,
      "bcr": string,
      "clinical_M": string,
      "clinical_N": string,
      "clinical_stage": string,
      "clinical_T": string,
      "colorectal_cancer": string,
      "country": string,
      "days_to_birth": string,
      "days_to_death": string,
      "days_to_initial_pathologic_diagnosis": string,
      "days_to_last_followup": string,
      "days_to_submitted_specimen_dx": string,
      "ethnicity": string,
      "frozen_specimen_anatomic_site": string,
      "gender": string,
      "height": string,
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
      "menopause_status": string,
      "mononucleotide_and_dinucleotide_marker_panel_analysis_status": string,
      "mononucleotide_marker_panel_analysis_status": string,
      "neoplasm_histologic_grade": string,
      "new_tumor_event_after_initial_treatment": string,
      "number_of_lymphnodes_examined": string,
      "number_of_lymphnodes_positive_by_he": string,
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
      "Study": string,
      "tobacco_smoking_history": string,
      "tumor_tissue_site": string,
      "tumor_type": string,
      "vital_status": string,
      "weight": string,
      "weiss_venous_invasion": string,
      "year_of_initial_pathologic_diagnosis": string
    },
    "samples": [string]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	aliquots[], list, "List of barcodes of aliquots taken from this participant."
	clinical_data, nested object, "The clinical data about the participant."
	clinical_data.age_at_initial_pathologic_diagnosis, string, "Age at which a condition or disease was first diagnosed in years."
	clinical_data.anatomic_neoplasm_subdivision, string, "Text term to describe the spatial location, subdivisions and/or anatomic site name of a tumor."
	clinical_data.batch_number, string, "Groups samples by the batch they were processed in."
	clinical_data.bcr, string, "A TCGA center where samples are carefully catalogued, processed, quality-checked and stored along with participant clinical information."
	clinical_data.clinical_M, string, "Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	clinical_data.clinical_N, string, "Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	clinical_data.clinical_stage, string, "Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis."
	clinical_data.clinical_T, string, "Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment."
	clinical_data.colorectal_cancer, string, "Text term to signify whether a patient has been diagnosed with colorectal cancer."
	clinical_data.country, string, "Text to identify the name of the state, province, or country in which the sample was procured."
	clinical_data.days_to_birth, string, "Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.days_to_death, string, "Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.days_to_initial_pathologic_diagnosis, string, "Numeric value to represent the day of an individual's initial pathologic diagnosis of cancer."
	clinical_data.days_to_last_followup, string, "Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.days_to_submitted_specimen_dx, string, "Time interval from the date of diagnosis of the submitted sample to the date of initial pathologic diagnosis, represented as a calculated number of days."
	clinical_data.ethnicity, string, "The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories."
	clinical_data.frozen_specimen_anatomic_site, string, "Text description of the origin and the anatomic site regarding the frozen biospecimen tumor tissue sample."
	clinical_data.gender, string, "Text designations that identify gender."
	clinical_data.height, string, "The height of the patient in centimeters."
	clinical_data.histological_type, string, "Text term for the structural pattern of cancer cells used to define a microscopic diagnosis."
	clinical_data.history_of_colon_polyps, string, "Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report(s)."
	clinical_data.history_of_neoadjuvant_treatment, string, "Text term to describe the patient's history of neoadjuvant treatment and the kind of treatment given prior to resection of the tumor."
	clinical_data.history_of_prior_malignancy, string, "Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence."
	clinical_data.hpv_calls, string, "Results of HPV tests."
	clinical_data.hpv_status, string, "Current HPV status."
	clinical_data.icd_10, string, "The tenth version of the International Classification of Disease (ICD)."
	clinical_data.icd_o_3_histology, string, "The third edition of the International Classification of Diseases for Oncology."
	clinical_data.icd_o_3_site, string, "The third edition of the International Classification of Diseases for Oncology."
	clinical_data.lymphatic_invasion, string, "A yes/no indicator to ask if malignant cells are present in small or thin-walled vessels suggesting lymphatic involvement."
	clinical_data.lymphnodes_examined, string, "A yes/no/unknown indicator whether a lymph node assessment was performed at the primary presentation of disease."
	clinical_data.lymphovascular_invasion_present, string, "A yes/no indicator to ask if large vessel (vascular) invasion or small, thin-walled (lymphatic) invasion was detected in a tumor specimen."
	clinical_data.menopause_status, string, "Text term to signify the status of a woman's menopause, the permanent cessation of menses, usually defined by 6 to 12 months of amenorrhea."
	clinical_data.mononucleotide_and_dinucleotide_marker_panel_analysis_status, string, "Text result of microsatellite instability (MSI) testing at using a mononucleotide and dinucleotide microsatellite panel."
	clinical_data.mononucleotide_marker_panel_analysis_status, string, "Text result of microsatellite instability (MSI) testing using a mononucleotide microsatellite panel."
	clinical_data.neoplasm_histologic_grade, string, "Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness."
	clinical_data.new_tumor_event_after_initial_treatment, string, "Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment."
	clinical_data.number_of_lymphnodes_examined, string, "The total number of lymph nodes removed and pathologically assessed for disease."
	clinical_data.number_of_lymphnodes_positive_by_he, string, "Numeric value to signify the count of positive lymph nodes identified through hematoxylin and eosin (H&E) staining light microscopy."
	clinical_data.ParticipantBarcode, string, "Participant barcode."
	clinical_data.pathologic_M, string, "Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the regional lymph nodes, using criteria established by the American Joint Committee on Cancer (AJCC)."
	clinical_data.pathologic_N, string, "The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cancer Staging Manual."
	clinical_data.pathologic_stage, string, "The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria."
	clinical_data.pathologic_T, string, "Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American Joint Committee on Cancer (AJCC)."
	clinical_data.person_neoplasm_cancer_status, string, "The state or condition of an individual's neoplasm at a particular point in time."
	clinical_data.pregnancies, string, "Value to describe the number of full-term pregnancies that a woman has experienced."
	clinical_data.primary_neoplasm_melanoma_dx, string, "Text indicator to signify whether a person had a primary diagnosis of melanoma."
	clinical_data.primary_therapy_outcome_success, string, "Measure of success."
	clinical_data.prior_dx, string, "Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence."
	clinical_data.Project, string, "Project name, e.g. 'TCGA'."
	clinical_data.psa_value, number, "The lab value that represents the results of the most recent (post-operative) prostatic-specific antigen (PSA) in the blood."
	clinical_data.race, string, "The text for reporting information about race based on the Office of Management and Budget (OMB) categories."
	clinical_data.residual_tumor, string, "Text terms to describe the status of a tissue margin following surgical resection."
	clinical_data.Study, string, "Tumor type abbreviation, e.g. 'BRCA'. "
	clinical_data.tobacco_smoking_history, string, "Category describing current smoking status and smoking history as self-reported by a patient."
	clinical_data.tumor_tissue_site, string, "Text term that describes the anatomic site of the tumor or disease."
	clinical_data.tumor_type, string, "Text term to identify the morphologic subtype of papillary renal cell carcinoma."
	clinical_data.vital_status, string, "The survival state of the person registered on the protocol."
	clinical_data.weight, string, "The weight of the patient measured in kilograms."
	clinical_data.weiss_venous_invasion, string, "The result of an assessment using the Weiss histopathologic criteria."
	clinical_data.year_of_initial_pathologic_diagnosis, string, "Numeric value to represent the year of an individual's initial pathologic diagnosis of cancer."
	samples[], list, "List of barcodes of samples taken from this participant."
