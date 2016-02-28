
preview_cohort
##############

Takes a JSON object of
filters in the request body and previews the sample barcodes and participant barcodes in this new cohort. Authentication is not required. Example:

$ curl https:/api-dot-isb-cgc.appspot.com/\_ah/api/cohort\_api/v1/preview\_cohort -d '{"Study": "BRCA,OV"}' -H "Content-Type: application/json"

**Access control:** To call this method, you must have the following
roles:

-  None

Request

HTTP request

POST https://api-dot-isb-cgc.appspot.com/\_ah/api/cohort\_api/v1/preview\_cohort

Parameters

None

Request body

In the request body, supply a metadata resource:

.. code-block:: javascript

	{
		'adenocarcinoma_invasion ': string,
		'age_at_initial_pathologic_diagnosis ': string,
		'anatomic_neoplasm_subdivision ': string,
		'avg_percent_lymphocyte_infiltration ': float,
		'avg_percent_monocyte_infiltration ': float,
		'avg_percent_necrosis ': float,
		'avg_percent_neutrophil_infiltration ': float,
		'avg_percent_normal_cells ': float,
		'avg_percent_stromal_cells ': float,
		'avg_percent_tumor_cells ': float,
		'avg_percent_tumor_nuclei ': float,
		'batch_number ': integer,
		'bcr ': string,
		'clinical_M ': string,
		'clinical_N ': string,
		'clinical_stage ': string,
		'clinical_T ': string,
		'colorectal_cancer ': string,
		'country ': string,
		'country_of_procurement ': string,
		'days_to_birth ': integer,
		'days_to_collection ': integer,
		'days_to_death ': integer,
		'days_to_initial_pathologic_diagnosis ': integer,
		'days_to_last_followup ': integer,
		'days_to_submitted_specimen_dx ': integer,
		'Study ': string,
		'ethnicity ': string,
		'frozen_specimen_anatomic_site ': string,
		'gender ': string,
		'height ': integer,
		'histological_type ': string,
		'history_of_colon_polyps ': string,
		'history_of_neoadjuvant_treatment ': string,
		'history_of_prior_malignancy ': string,
		'hpv_calls ': string,
		'hpv_status ': string,
		'icd_10 ': string,
		'icd_o_3_histology ': string,
		'icd_o_3_site ': string,
		'lymph_node_examined_count ': integer,
		'lymphatic_invasion ': string,
		'lymphnodes_examined ': string,
		'lymphovascular_invasion_present ': string,
		'max_percent_lymphocyte_infiltration ': integer,
		'max_percent_monocyte_infiltration ': integer,
		'max_percent_necrosis ': integer,
		'max_percent_neutrophil_infiltration ': integer,
		'max_percent_normal_cells ': integer,
		'max_percent_stromal_cells ': integer,
		'max_percent_tumor_cells ': integer,
		'max_percent_tumor_nuclei ': integer,
		'menopause_status ': string,
		'min_percent_lymphocyte_infiltration ': integer,
		'min_percent_monocyte_infiltration ': integer,
		'min_percent_necrosis ': integer,
		'min_percent_neutrophil_infiltration ': integer,
		'min_percent_normal_cells ': integer,
		'min_percent_stromal_cells ': integer,
		'min_percent_tumor_cells ': integer,
		'min_percent_tumor_nuclei ': integer,
		'mononucleotide_and_dinucleotide_marker_panel_analysis_status': string,
		'mononucleotide_marker_panel_analysis_status ': string,
		'neoplasm_histologic_grade ': string,
		'new_tumor_event_after_initial_treatment ': string,
		'number_of_lymphnodes_examined ': integer,
		'number_of_lymphnodes_positive_by_he ': integer,
		'ParticipantBarcode ': string,
		'pathologic_M ': string,
		'pathologic_N ': string,
		'pathologic_stage ': string,
		'pathologic_T ': string,
		'person_neoplasm_cancer_status ': string,
		'pregnancies ': string,
		'preservation_method ': string,
		'primary_neoplasm_melanoma_dx ': string,
		'primary_therapy_outcome_success ': string,
		'prior_dx ': string,
		'Project ': string,
		'psa_value ': float,
		'race ': string,
		'residual_tumor ': string,
		'SampleBarcode ': string,
		'tobacco_smoking_history ': string,
		'total_number_of_pregnancies ': integer,
		'tumor_tissue_site ': string,
		'tumor_pathology ': string,
		'tumor_type ': string,
		'weiss_venous_invasion ': string,
		'vital_status ': string,
		'weight ': integer,
		'year_of_initial_pathologic_diagnosis ': string,
		'SampleTypeCode ': string,
		'has_Illumina_DNASeq ': string,
		'has_BCGSC_HiSeq_RNASeq ': string,
		'has_UNC_HiSeq_RNASeq ': string,
		'has_BCGSC_GA_RNASeq ': string,
		'has_UNC_GA_RNASeq ': string,
		'has_HiSeq_miRnaSeq ': string,
		'has_GA_miRNASeq ': string,
		'has_RPPA ': string,
		'has_SNP6 ': string,
		'has_27k ': string,
		'has_450k ': string
	}

+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Parameter name**                                                   | **Value**   | **Description**                                                                                                                                              |
+======================================================================+=============+==============================================================================================================================================================+
| adenocarcinoma\_invasion                                             | string      |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| age\_at\_initial\_pathologic\_diagnosis                              | string      | Age at which a condition or disease was first diagnosed. (in years)                                                                                          |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| anatomic\_neoplasm\_subdivision                                      | string      | Text term to describe the spatial location, subdivisions and/or anatomic site name of a tumor.                                                               |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_lymphocyte\_infiltration                               | float       | Average in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen.                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_monocyte\_infiltration                                 | float       | Average in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen.                        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_necrosis                                               | float       | Average in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen.                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_neutrophil\_infiltration                               | float       | Average in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen.                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_normal\_cells                                          | float       | Average in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_stromal\_cells                                         | float       | Average in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen.                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_tumor\_cells                                           | float       | Average in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen.                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_tumor\_nuclei                                          | float       | Average in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| batch\_number                                                        | integer     | groups samples by the batch they were processed in                                                                                                           |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| bcr                                                                  | string      | A TCGA center where samples are carefully catalogued, processed, quality-checked and stored along with participant clinical information.                     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_M                                                          | string      | Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_N                                                          | string      | Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_stage                                                      | string      | Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis ...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_T                                                          | string      | Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| colorectal\_cancer                                                   | string      | Text term to signify whether a patient has been diagnosed with colorectal cancer.                                                                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| country                                                              | string      | Text to identify the name of the state, province, or country in which the sample was procured.                                                               |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| country\_of\_procurement                                             | string      | Text to identify the name of the state, province, or country in which the sample was procured.                                                               |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_birth                                                      | integer     | Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days.                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_collection                                                 | integer     |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_death                                                      | integer     | Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days.                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_initial\_pathologic\_diagnosis                             | integer     | Numeric value to represent the day of an individual's initial pathologic diagnosis of cancer.                                                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_last\_followup                                             | integer     | Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days.                        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_submitted\_specimen\_dx                                    | integer     | Time interval from the date of diagnosis of the submitted sample to the date of initial pathologic diagnosis, represented as a calculated number of d...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Study                                                                | string      | A disease study is the sum of results from all experiments for a specific cancer type (or tumor type) that TCGA is tasked to study. Within the projec...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ethnicity                                                            | string      | The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories.                                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| frozen\_specimen\_anatomic\_site                                     | string      | Text description of the origin and the anatomic site regarding the frozen biospecimen tumor tissue sample.                                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| gender                                                               | string      | Text designations that identify gender. Gender is described as the assemblage of properties that distinguish people on the basis of their societal ro...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| height                                                               | integer     | The height of the patient in centimeters.                                                                                                                    |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| histological\_type                                                   | string      | Text term for the structural pattern of cancer cells used to define a microscopic diagnosis.                                                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| history\_of\_colon\_polyps                                           | string      | Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report(s).        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| history\_of\_neoadjuvant\_treatment                                  | string      | Text term to describe the patient's history of neoadjuvant treatment and the kind of treament given prior to resection of the tumor.                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| history\_of\_prior\_malignancy                                       | string      | Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence.                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hpv\_calls                                                           | string      | Results of HPV tests                                                                                                                                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hpv\_status                                                          | string      | Current HPV status                                                                                                                                           |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| icd\_10                                                              | string      | The tenth version of the International Classification of Disease (ICD), published by the World Health Organization in 1992.\_A system of numbered cate...    |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| icd\_o\_3\_histology                                                 | string      | The third edition of the International Classification of Diseases for Oncology, published in 2000, used principally in tumor and cancer registries fo...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| icd\_o\_3\_site                                                      | string      | The third edition of the International Classification of Diseases for Oncology, published in 2000, used principally in tumor and cancer registries fo...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lymph\_node\_examined\_count                                         | integer     |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lymphatic\_invasion                                                  | string      | a yes/no indicator to ask if malignant cells are present in small or thin-walled vessels suggesting lymphatic involvement.                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lymphnodes\_examined                                                 | string      | the yes/no/unknown indicator whether a lymph node assessment was performed at the primary presentation of disease.                                           |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lymphovascular\_invasion\_present                                    | string      | the yes/no indicator to ask if large vessel (vascular) invasion or small, thin-walled (lymphatic) invasion was detected in a tumor specimen.                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_lymphocyte\_infiltration                               | integer     | Maximum in the series of numeric values to represent the percentage of lymphcyte infiltration in a malignant tumor sample or specimen.                       |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_monocyte\_infiltration                                 | integer     | Maximum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen.                        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_necrosis                                               | integer     | Maximum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen.                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_neutrophil\_infiltration                               | integer     | Maximum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen.                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_normal\_cells                                          | integer     | Maximum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_stromal\_cells                                         | integer     | Maximum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen.                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_tumor\_cells                                           | integer     | Maximum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen.                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_tumor\_nuclei                                          | integer     | Maximum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| menopause\_status                                                    | string      | Text term to signify the status of a woman's menopause, the permanent cessation of menses, usually defined by 6 to 12 months of amenorrhea.                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_lymphocyte\_infiltration                               | integer     | Minimum in the series of numeric values to represent the percentage of lymphcyte infiltration in a malignant tumor sample or specimen.                       |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_monocyte\_infiltration                                 | integer     | Minimum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen.                        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_necrosis                                               | integer     | Minimum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen.                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_neutrophil\_infiltration                               | integer     | Minimum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen.                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_normal\_cells                                          | integer     | Minimum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_stromal\_cells                                         | integer     | Minimum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen.                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_tumor\_cells                                           | integer     | Minimum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen.                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_tumor\_nuclei                                          | integer     | Minimum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| mononucleotide\_and\_dinucleotide\_marker\_panel\_analysis\_status   | string      | Text result of microsatellite instability (MSI) testing at using a mononucleotide and dinucleotide microsatellite panel.                                     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| mononucleotide\_marker\_panel\_analysis\_status                      | string      | Text result of microsatellite instability (MSI) testing using a mononucleotide microsatellite panel.                                                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| neoplasm\_histologic\_grade                                          | string      | Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness.                                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| new\_tumor\_event\_after\_initial\_treatment                         | string      | Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment.                                                    |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| number\_of\_lymphnodes\_examined                                     | integer     | the total number of lymph nodes removed and pathologically assessed for disease.                                                                             |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| number\_of\_lymphnodes\_positive\_by\_he                             | integer     | Numeric value to signify the count of positive lymph nodes identified through hematoxylin and eosin (H&E) staining light microscopy.                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ParticipantBarcode                                                   | string      | The barcode assigned by TCGA to the Participant                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pathologic\_M                                                        | string      | Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the reg...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pathologic\_N                                                        | string      | The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cance...    |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pathologic\_stage                                                    | string      | The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria.          |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pathologic\_T                                                        | string      | Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American ...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| person\_neoplasm\_cancer\_status                                     | string      | The state or condition of an individual's neoplasm at a particular point in time.                                                                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pregnancies                                                          | string      | Value to describe the number of full-term pregnancies that a woman has experienced.                                                                          |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| preservation\_method                                                 | string      |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| primary\_neoplasm\_melanoma\_dx                                      | string      | Text indicator to signify whether a person had a primary diagnosis of melanoma.                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| primary\_therapy\_outcome\_success                                   | string      | Measure of Success                                                                                                                                           |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| prior\_dx                                                            | string      | Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence                             |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Project                                                              | string      | The study for which the data was generated.                                                                                                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| psa\_value                                                           | float       | The lab value that represents the results of the most recent (post-operative) prostatic-specific antigen (PSA) in the blood.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| race                                                                 | string      | The text for reporting information about race based on the Office of Management and Budget (OMB) categories.                                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| residual\_tumor                                                      | string      | Text terms to describe the status of a tissue margin following surgical resection.                                                                           |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SampleBarcode                                                        | string      | The barcode assigned by TCGA to a sample from a Participant                                                                                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tobacco\_smoking\_history                                            | string      | Category describing current smoking status and smoking history as self-reported by a patient.                                                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| total\_number\_of\_pregnancies                                       | integer     |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tumor\_tissue\_site                                                  | string      | Text term that describes the anatomic site of the tumor or disease.                                                                                          |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tumor\_pathology                                                     | string      |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tumor\_type                                                          | string      | Text term to identify the morphologic subtype of papillary renal cell carcinoma.                                                                             |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| weiss\_venous\_invasion                                              | string      | The result of an assessment using the Weiss histopathologic criteria.                                                                                        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vital\_status                                                        | string      | the survival state of the person registered on the protocol.                                                                                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| weight                                                               | integer     | the weight of the patient measured in kilograms.                                                                                                             |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| year\_of\_initial\_pathologic\_diagnosis                             | string      | Numeric value to represent the year of an individual’s initial pathologic diagnosis of cancer.                                                               |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SampleTypeCode                                                       | string      | the type of the sample tumor or normal tissue cell or blood sample provided by a participant.                                                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_Illumina\_DNASeq                                                | string      | Indicates if a sample has gene sequencing data. “True”, “False”, or “None”.                                                                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_BCGSC\_HiSeq\_RNASeq                                            | string      | Indicates if a sample has RNA sequencing data from the IlluminaHiSeq platform and the BCGSC pipeline. “True”, “False”, or “None”.                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_UNC\_HiSeq\_RNASeq                                              | string      | Indicates if a sample has RNA sequencing data from the IlluminaHiSeq platform and the UNC pipeline. “True”, “False”, or “None”.                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_BCGSC\_GA\_RNASeq                                               | string      | Indicates if a sample has RNA sequencing data from the IlluminaGA platform and the BCGSC pipeline. “True”, “False”, or “None”.                               |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_UNC\_GA\_RNASeq                                                 | string      | Indicates if a sample has RNA sequencing data from the IlluminaGA platform and the UNC pipeline. “True”, “False”, or “None”.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_HiSeq\_miRnaSeq                                                 | string      | Indicates if a sample has microRNA data from the IlluminaHiSeq platform. “True”, “False”, or “None”.                                                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_GA\_miRNASeq                                                    | string      | Indicates if a sample has microRNA data from the IlluminaGA platform. “True”, “False”, or “None”.                                                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_RPPA                                                            | string      | Indicates if a sample has protein array data. “True”, “False”, or “None”.                                                                                    |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_SNP6                                                            | string      | Indicates if a sample has copy number data. “True”, “False”, or “None”.                                                                                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_27k                                                             | string      | Indicates if a sample has methylation data from the Illumina 27k platform. “True”, “False”, or “None”.                                                       |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_450k                                                            | string      | Indicates if a sample has methylation data from the Illumina 450k platform. “True”, “False”, or “None”.                                                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response

If successful, this method returns a response body with the following
structure:

.. code-block:: javascript

	{
	  "kind": "cohort_api#cohortsItem",
	  "patient_count": string,
	  "patients": [string],
	  "sample_count": string,
	  "samples": [string],
	}

+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
| **Property name**   | **Value**                 | **Description**                                                                                             |
+=====================+===========================+=============================================================================================================+
| kind                | cohort\_api#cohortsItem   | The resource type.                                                                                          |
+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
| patient_count       | string                    | Number of participants in this cohort.                                                                      |
+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
| patients[]          | list                      | List of participant barcodes in this cohort.                                                                |
+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
| sample_count        | string                    | Number of samples in this cohort.                                                                           |
+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
| samples[]           | list                      | List of sample barcodes in this cohort.                                                                     |
+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+

