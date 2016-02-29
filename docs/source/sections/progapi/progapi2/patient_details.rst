
patient_details 
###############

Returns information about a specific participant, including a list of samples and aliquots derived from this patient. Takes a participant barcode (of length 12, *eg* TCGA-B9-7268) as a required parameter. User does not need to be authenticated.

**Access control:** To call this method, you must have the following
roles:

-  None

Request

HTTP request

GET https://api-dot-isb-cgc.appspot.com/\_ah/api/cohort\_api/v1/patient\_details

Parameters

+-----------------------+-------------+--------------------------------------------------------------+
| **Parameter name**    | **Value**   | **Description**                                              |
+=======================+=============+==============================================================+
| **Path parameters**   |             |                                                              |
+-----------------------+-------------+--------------------------------------------------------------+
| patient\_barcode      | string      | Barcode of the patient to get information about. Required.   |
+-----------------------+-------------+--------------------------------------------------------------+

Response

If successful, this method returns a response body with the following
structure:

.. code-block:: javascript

	{
	  "kind": "cohort_api#cohortsItem",
	  "aliquots": [string],
	  "clinical_data": {
	    "ParticipantBarcode": string,
	    "Project": string,
	    "Study": string,
	    "age_at\initial_pathologic_diagnosis": string,
	    "anatomic_neoplasm_subdivision": string,
	    "batch_number": string,
	    "bcr": string,
	    "clinical_M": string,
	    "clinical_N": string,
	    "clinical_T": string,
	    "clinical_stage": string,
	    "colorectal_cancer": string,
	    "country": string,
	    "days_to_birth": string,
	    "days_to_initial_pathologic_diagnosis": string,
	    "days_to_last_followup": string,
	    "ethnicity": string,
	    "frozen_specimen_anatomic_site": string,
	    "gender": string,
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
	    "mononcleotide_and_dinucleotide_marker_panel_analysis_status": string,
	    "mononucleotide_marker_panel_analysis_status": string,
	    "neoplasm_histologic_grade": string,,
	    "new_tumor_event_after_initial_treatment": string,
	    "number_of_lymphnodes_examined": string,
	    "number_of_lymphnodes_positive_by_he": string,
	    "pathologic_M": string,
	    "pathologic_N": string,
	    "pathologic_T": string,
	    "pathologic_stage": string,
	    "person_neoplasm_cancer_status": string,
	    "pregnancies": string,
	    "primary_neoplasm_melanoma_dx": string,
	    "primary_therapy_outcome_success": string,
	    "prior_dx": string,
	    "race": string,
	    "residual_tumor": string,
	    "tobacco_smoking_history": string,
	    "tumor_tissue_site": string,
	    "tumor_type": string,
	    "vital_status": string,
	    "weiss_venous_invasion": string,
	    "year_of_initial_pathologic_diagnosis": string
	  },
	  "samples": [],
	}

+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Property name**                                                                   | **Value**                 | **Description**                                                                                                                                                    |
+=====================================================================================+===========================+====================================================================================================================================================================+
| kind                                                                                | cohort\_api#cohortsItem   | The resource type.                                                                                                                                                 |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| aliquots[]                                                                          | list                      | List of barcodes of aliquots taken from this participant.                                                                                                          |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data                                                                      | nested object             | The clinical data about the participant.                                                                                                                           |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.ParticipantBarcode                                                   | string                    | Participant barcode.                                                                                                                                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.Project                                                              | string                    | Project name, .eg. “TCGA”.                                                                                                                                         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.Study                                                                | string                    | Tumor type abbreviation, e.g. “BRCA”.                                                                                                                              |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.age\_at\_initial\_pathologic\_diagnosis                              | string                    | Age at which a condition or disease was first diagnosed in years.                                                                                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.anatomic\_neoplasm\_subdivision                                      | string                    | Text term to describe the spatial location, subdivisions and/or anatomic site name of a tumor.                                                                     |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.batch\_number                                                        | string                    | Groups samples by the batch they were processed in.                                                                                                                |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.bcr                                                                  | string                    | Biospecimen core resource, e.g. "Nationwide Children's Hospital”, “Washington University".                                                                         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.clinical\_M                                                          | string                    | Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.                      |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.clinical\_N                                                          | string                    | Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.clinical\_T                                                          | string                    | Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.                                         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.clinical\_stage                                                      | string                    | Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis for cancer.   |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.colorectal\_cancer                                                   | string                    | Text term to signify whether a patient has been diagnosed with colorectal cancer.                                                                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.country                                                              | string                    | Text to identify the name of the state, province, or country in which the sample was procured.                                                                     |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.days\_to\_birth                                                      | string                    | Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days.                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.days\_to\_initial\_pathologic\_diagnosis                             | string                    | Numeric value to represent the day of an individual's initial pathologic diagnosis of cancer.                                                                      |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.days\_to\_last\_followup                                             | string                    | Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days.                              |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.ethnicity                                                            | string                    | The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories.                                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.frozen\_specimen\_anatomic\_site                                     | string                    | Text description of the origin and the anatomic site regarding the frozen biospecimen tumor tissue sample.                                                         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.gender                                                               | string                    | Text designations that identify gender.                                                                                                                            |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.histological\_type                                                   | string                    | Text term for the structural pattern of cancer cells used to define a microscopic diagnosis.                                                                       |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.history\_of\_colon\_polyps                                           | string                    | Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report(s).              |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.history\_of\_neoadjuvant\_treatment                                  | string                    | Text term to describe the patient's history of neoadjuvant treatment and the kind of treament given prior to resection of the tumor.                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.history\_of\_prior\_malignancy                                       | string                    | Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence.                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.hpv\_calls                                                           | string                    | Results of HPV tests.                                                                                                                                              |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.hpv\_status                                                          | string                    | Current HPV status.                                                                                                                                                |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.icd\_10                                                              | string                    | The tenth version of the International Classification of Disease (ICD).                                                                                            |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.icd\_o\_3\_histology                                                 | string                    | The third edition of the International Classification of Diseases for Oncology.                                                                                    |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.icd\_o\_3\_site                                                      | string                    | The third edition of the International Classification of Diseases for Oncology.                                                                                    |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.lymphatic\_invasion                                                  | string                    | A yes/no indicator to ask if malignant cells are present in small or thin-walled vessels suggesting lymphatic involvement.                                         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.lymphnodes\_examined                                                 | string                    | The yes/no/unknown indicator whether a lymph node assessment was performed at the primary presentation of disease.                                                 |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.lymphovascular\_invasion\_present                                    | string                    | The yes/no indicator to ask if large vessel (vascular) invasion or small, thin-walled (lymphatic) invasion was detected in a tumor specimen.                       |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.menopause\_status                                                    | string                    | Text term to signify the status of a woman's menopause, the permanent cessation of menses, usually defined by 6 to 12 months of amenorrhea.                        |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.mononucleotide\_and\_dinucleotide\_marker\_panel\_analysis\_status   | string                    | Text result of microsatellite instability (MSI) testing at using a mononucleotide and dinucleotide microsatellite panel.                                           |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.mononucleotide\_marker\_panel\_analysis\_status                      | string                    | Text result of microsatellite instability (MSI) testing using a mononucleotide microsatellite panel.                                                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.neoplasm\_histologic\_grade                                          | string                    | Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness.                                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.new\_tumor\_event\_after\_initial\_treatment                         | string                    | Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment.                                                          |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.number\_of\_lymphnodes\_examined                                     | string                    | The total number of lymph nodes removed and pathologically assessed for disease.                                                                                   |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.number\_of\_lymphnodes\_positive\_by\_he                             | string                    | Numeric value to signify the count of positive lymph nodes identified through hematoxylin and eosin (H&E) staining light microscopy.                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.pathologic\_M                                                        | string                    | Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the reg...           |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.pathologic\_N                                                        | string                    | The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cance...          |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.pathologic\_stage                                                    | string                    | The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria.                |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.pathologic\_T                                                        | string                    | Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American ...           |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.person\_neoplasm\_cancer\_status                                     | string                    | The state or condition of an individual's neoplasm at a particular point in time.                                                                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.pregnancies                                                          | string                    | Value to describe the number of full-term pregnancies that a woman has experienced.                                                                                |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.primary\_neoplasm\_melanoma\_dx                                      | string                    | Text indicator to signify whether a person had a primary diagnosis of melanoma.                                                                                    |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.primary\_therapy\_outcome\_success                                   | string                    | Measure of Success                                                                                                                                                 |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.prior\_dx                                                            | string                    | Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence.                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.race                                                                 | string                    | The text for reporting information about race based on the Office of Management and Budget (OMB) categories.                                                       |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.residual\_tumor                                                      | string                    | Text terms to describe the status of a tissue margin following surgical resection.                                                                                 |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.tobacco\_smoking\_history                                            | string                    | Category describing current smoking status and smoking history as self-reported by a patient.                                                                      |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.tumor\_tissue\_site                                                  | string                    | Text term that describes the anatomic site of the tumor or disease.                                                                                                |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.tumor\_type                                                          | string                    | Text term to identify the morphologic subtype of papillary renal cell carcinoma.                                                                                   |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.vital\_status                                                        | string                    | The survival state of the person registered on the protocol.                                                                                                       |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.weiss\_venous\_invasion                                              | string                    | The result of an assessment using the Weiss histopathologic criteria.                                                                                              |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.year\_of\_initial\_pathologic\_diagnosis                             | string                    | Numeric value to represent the year of an individual’s initial pathologic diagnosis of cancer.                                                                     |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| samples[]                                                                           | list                      | List of barcodes of samples taken from this participant.                                                                                                           |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

