save_cohort
###########
Creates and saves a cohort. Takes a JSON object in the request body to use as the cohort's filters. Authentication is required. Returns information about the saved cohort, including the number of patients and the number of samples in that cohort.

**Example**

$ python isb_curl.py "https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/save_cohort?name=BRCA-OV-cohort" -d '{"Study": ["BRCA", "OV"]}' -H "Content-Type: application/json"

**Request**

HTTP request

POST https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/save_cohort``

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	name,string,Required.
	token,string,Optional.


Request body

In the request body, supply a metadata resource:

.. code-block:: javascript

  {
    "adenocarcinoma_invasion": [string],
    "age_at_initial_pathologic_diagnosis": [string],
    "anatomic_neoplasm_subdivision": [string],
    "avg_percent_lymphocyte_infiltration": [number],
    "avg_percent_monocyte_infiltration": [number],
    "avg_percent_necrosis": [number],
    "avg_percent_neutrophil_infiltration": [number],
    "avg_percent_normal_cells": [number],
    "avg_percent_stromal_cells": [number],
    "avg_percent_tumor_cells": [number],
    "avg_percent_tumor_nuclei": [number],
    "batch_number": [string],
    "bcr": [string],
    "clinical_M": [string],
    "clinical_N": [string],
    "clinical_stage": [string],
    "clinical_T": [string],
    "colorectal_cancer": [string],
    "country": [string],
    "country_of_procurement": [string],
    "days_to_birth": [string],
    "days_to_collection": [string],
    "days_to_death": [string],
    "days_to_initial_pathologic_diagnosis": [string],
    "days_to_last_followup": [string],
    "days_to_submitted_specimen_dx": [string],
    "ethnicity": [string],
    "frozen_specimen_anatomic_site": [string],
    "gender": [string],
    "has_27k": [string],
    "has_450k": [string],
    "has_BCGSC_GA_RNASeq": [string],
    "has_BCGSC_HiSeq_RNASeq": [string],
    "has_GA_miRNASeq": [string],
    "has_HiSeq_miRnaSeq": [string],
    "has_Illumina_DNASeq": [string],
    "has_RPPA": [string],
    "has_SNP6": [string],
    "has_UNC_GA_RNASeq": [string],
    "has_UNC_HiSeq_RNASeq": [string],
    "height": [string],
    "histological_type": [string],
    "history_of_colon_polyps": [string],
    "history_of_neoadjuvant_treatment": [string],
    "history_of_prior_malignancy": [string],
    "hpv_calls": [string],
    "hpv_status": [string],
    "icd_10": [string],
    "icd_o_3_histology": [string],
    "icd_o_3_site": [string],
    "lymph_node_examined_count": [string],
    "lymphatic_invasion": [string],
    "lymphnodes_examined": [string],
    "lymphovascular_invasion_present": [string],
    "max_percent_lymphocyte_infiltration": [string],
    "max_percent_monocyte_infiltration": [string],
    "max_percent_necrosis": [string],
    "max_percent_neutrophil_infiltration": [string],
    "max_percent_normal_cells": [string],
    "max_percent_stromal_cells": [string],
    "max_percent_tumor_cells": [string],
    "max_percent_tumor_nuclei": [string],
    "menopause_status": [string],
    "min_percent_lymphocyte_infiltration": [string],
    "min_percent_monocyte_infiltration": [string],
    "min_percent_necrosis": [string],
    "min_percent_neutrophil_infiltration": [string],
    "min_percent_normal_cells": [string],
    "min_percent_stromal_cells": [string],
    "min_percent_tumor_cells": [string],
    "min_percent_tumor_nuclei": [string],
    "mononucleotide_and_dinucleotide_marker_panel_analysis_status": [string],
    "mononucleotide_marker_panel_analysis_status": [string],
    "neoplasm_histologic_grade": [string],
    "new_tumor_event_after_initial_treatment": [string],
    "number_of_lymphnodes_examined": [string],
    "number_of_lymphnodes_positive_by_he": [string],
    "ParticipantBarcode": [string],
    "pathologic_M": [string],
    "pathologic_N": [string],
    "pathologic_stage": [string],
    "pathologic_T": [string],
    "person_neoplasm_cancer_status": [string],
    "pregnancies": [string],
    "preservation_method": [string],
    "primary_neoplasm_melanoma_dx": [string],
    "primary_therapy_outcome_success": [string],
    "prior_dx": [string],
    "Project": [string],
    "psa_value": [number],
    "race": [string],
    "residual_tumor": [string],
    "SampleBarcode": [string],
    "SampleTypeCode": [string],
    "Study": [string],
    "tobacco_smoking_history": [string],
    "total_number_of_pregnancies": [string],
    "tumor_pathology": [string],
    "tumor_tissue_site": [string],
    "tumor_type": [string],
    "vital_status": [string],
    "weight": [string],
    "weiss_venous_invasion": [string],
    "year_of_initial_pathologic_diagnosis": [string]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	adenocarcinoma_invasion[],list,Optional.
	age_at_initial_pathologic_diagnosis[],list,Optional.
	anatomic_neoplasm_subdivision[],list,Optional.
	avg_percent_lymphocyte_infiltration[],list,Optional.
	avg_percent_monocyte_infiltration[],list,Optional.
	avg_percent_necrosis[],list,Optional.
	avg_percent_neutrophil_infiltration[],list,Optional.
	avg_percent_normal_cells[],list,Optional.
	avg_percent_stromal_cells[],list,Optional.
	avg_percent_tumor_cells[],list,Optional.
	avg_percent_tumor_nuclei[],list,Optional.
	batch_number[],list,Optional.
	bcr[],list,Optional.
	clinical_M[],list,Optional.
	clinical_N[],list,Optional.
	clinical_stage[],list,Optional.
	clinical_T[],list,Optional.
	colorectal_cancer[],list,Optional.
	country[],list,Optional.
	country_of_procurement[],list,Optional.
	days_to_birth[],list,Optional.
	days_to_collection[],list,Optional.
	days_to_death[],list,Optional.
	days_to_initial_pathologic_diagnosis[],list,Optional.
	days_to_last_followup[],list,Optional.
	days_to_submitted_specimen_dx[],list,Optional.
	ethnicity[],list,Optional.
	frozen_specimen_anatomic_site[],list,Optional.
	gender[],list,Optional.
	has_27k[],list,Optional.
	has_450k[],list,Optional.
	has_BCGSC_GA_RNASeq[],list,Optional.
	has_BCGSC_HiSeq_RNASeq[],list,Optional.
	has_GA_miRNASeq[],list,Optional.
	has_HiSeq_miRnaSeq[],list,Optional.
	has_Illumina_DNASeq[],list,Optional.
	has_RPPA[],list,Optional.
	has_SNP6[],list,Optional.
	has_UNC_GA_RNASeq[],list,Optional.
	has_UNC_HiSeq_RNASeq[],list,Optional.
	height[],list,Optional.
	histological_type[],list,Optional.
	history_of_colon_polyps[],list,Optional.
	history_of_neoadjuvant_treatment[],list,Optional.
	history_of_prior_malignancy[],list,Optional.
	hpv_calls[],list,Optional.
	hpv_status[],list,Optional.
	icd_10[],list,Optional.
	icd_o_3_histology[],list,Optional.
	icd_o_3_site[],list,Optional.
	lymph_node_examined_count[],list,Optional.
	lymphatic_invasion[],list,Optional.
	lymphnodes_examined[],list,Optional.
	lymphovascular_invasion_present[],list,Optional.
	max_percent_lymphocyte_infiltration[],list,Optional.
	max_percent_monocyte_infiltration[],list,Optional.
	max_percent_necrosis[],list,Optional.
	max_percent_neutrophil_infiltration[],list,Optional.
	max_percent_normal_cells[],list,Optional.
	max_percent_stromal_cells[],list,Optional.
	max_percent_tumor_cells[],list,Optional.
	max_percent_tumor_nuclei[],list,Optional.
	menopause_status[],list,Optional.
	min_percent_lymphocyte_infiltration[],list,Optional.
	min_percent_monocyte_infiltration[],list,Optional.
	min_percent_necrosis[],list,Optional.
	min_percent_neutrophil_infiltration[],list,Optional.
	min_percent_normal_cells[],list,Optional.
	min_percent_stromal_cells[],list,Optional.
	min_percent_tumor_cells[],list,Optional.
	min_percent_tumor_nuclei[],list,Optional.
	mononucleotide_and_dinucleotide_marker_panel_analysis_status[],list,Optional.
	mononucleotide_marker_panel_analysis_status[],list,Optional.
	neoplasm_histologic_grade[],list,Optional.
	new_tumor_event_after_initial_treatment[],list,Optional.
	number_of_lymphnodes_examined[],list,Optional.
	number_of_lymphnodes_positive_by_he[],list,Optional.
	ParticipantBarcode[],list,Optional.
	pathologic_M[],list,Optional.
	pathologic_N[],list,Optional.
	pathologic_stage[],list,Optional.
	pathologic_T[],list,Optional.
	person_neoplasm_cancer_status[],list,Optional.
	pregnancies[],list,Optional.
	preservation_method[],list,Optional.
	primary_neoplasm_melanoma_dx[],list,Optional.
	primary_therapy_outcome_success[],list,Optional.
	prior_dx[],list,Optional.
	Project[],list,Optional.
	psa_value[],list,Optional.
	race[],list,Optional.
	residual_tumor[],list,Optional.
	SampleBarcode[],list,Optional.
	SampleTypeCode[],list,Optional.
	Study[],list,Optional.
	tobacco_smoking_history[],list,Optional.
	total_number_of_pregnancies[],list,Optional.
	tumor_pathology[],list,Optional.
	tumor_tissue_site[],list,Optional.
	tumor_type[],list,Optional.
	vital_status[],list,Optional.
	weight[],list,Optional.
	weiss_venous_invasion[],list,Optional.
	year_of_initial_pathologic_diagnosis[],list,Optional.


Response

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "comments": string,
    "email": string,
    "filters": [
      {
        "name": string,
        "value": string
      }
    ],
    "id": string,
    "last_date_saved": string,
    "name": string,
    "num_patients": string,
    "num_samples": string,
    "parent_id": string,
    "perm": string,
    "source_notes": string,
    "source_type": string
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	comments, string, "Comments on the cohort."
	email, string, "Email of user."
	filters[], list, "List of filters applied to create cohort, if any."
	filters[].name, string, "Names of filtering parameters used to create the cohort."
	filters[].value, string, "Values of filtering parameters used to create the cohort."
	id, string, "Cohort id."
	last_date_saved, string, "Last date the cohort was saved."
	name, string, "Name of cohort."
	num_patients, string, "Number of unique participant barcodes in the cohort."
	num_samples, string, "Number of unique sample barcodes in the cohort."
	parent_id, string, "ID of the parent cohort this cohort was derived from, if any."
	perm, string, "User permissions on cohort: READER or OWNER."
	source_notes, string, "Notes on the source of the cohort."
	source_type, string, "Type of cohort source."
