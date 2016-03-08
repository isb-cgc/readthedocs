save_cohort
###########
Creates and saves a cohort. Takes a JSON object in the request body to use as the cohort's filters. Authentication is required. Returns information about the saved cohort, including the number of patients and the number of samples in that cohort.

Request

HTTP request

POST https://api-dot-mvm-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/save_cohort``

Parameters

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	name,string,Required
	token,string,tbd


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

	adenocarcinoma_invasion[],list,tbd
	age_at_initial_pathologic_diagnosis[],list,tbd
	anatomic_neoplasm_subdivision[],list,tbd
	avg_percent_lymphocyte_infiltration[],list,tbd
	avg_percent_monocyte_infiltration[],list,tbd
	avg_percent_necrosis[],list,tbd
	avg_percent_neutrophil_infiltration[],list,tbd
	avg_percent_normal_cells[],list,tbd
	avg_percent_stromal_cells[],list,tbd
	avg_percent_tumor_cells[],list,tbd
	avg_percent_tumor_nuclei[],list,tbd
	batch_number[],list,tbd
	bcr[],list,tbd
	clinical_M[],list,tbd
	clinical_N[],list,tbd
	clinical_stage[],list,tbd
	clinical_T[],list,tbd
	colorectal_cancer[],list,tbd
	country[],list,tbd
	country_of_procurement[],list,tbd
	days_to_birth[],list,tbd
	days_to_collection[],list,tbd
	days_to_death[],list,tbd
	days_to_initial_pathologic_diagnosis[],list,tbd
	days_to_last_followup[],list,tbd
	days_to_submitted_specimen_dx[],list,tbd
	ethnicity[],list,tbd
	frozen_specimen_anatomic_site[],list,tbd
	gender[],list,tbd
	has_27k[],list,tbd
	has_450k[],list,tbd
	has_BCGSC_GA_RNASeq[],list,tbd
	has_BCGSC_HiSeq_RNASeq[],list,tbd
	has_GA_miRNASeq[],list,tbd
	has_HiSeq_miRnaSeq[],list,tbd
	has_Illumina_DNASeq[],list,tbd
	has_RPPA[],list,tbd
	has_SNP6[],list,tbd
	has_UNC_GA_RNASeq[],list,tbd
	has_UNC_HiSeq_RNASeq[],list,tbd
	height[],list,tbd
	histological_type[],list,tbd
	history_of_colon_polyps[],list,tbd
	history_of_neoadjuvant_treatment[],list,tbd
	history_of_prior_malignancy[],list,tbd
	hpv_calls[],list,tbd
	hpv_status[],list,tbd
	icd_10[],list,tbd
	icd_o_3_histology[],list,tbd
	icd_o_3_site[],list,tbd
	lymph_node_examined_count[],list,tbd
	lymphatic_invasion[],list,tbd
	lymphnodes_examined[],list,tbd
	lymphovascular_invasion_present[],list,tbd
	max_percent_lymphocyte_infiltration[],list,tbd
	max_percent_monocyte_infiltration[],list,tbd
	max_percent_necrosis[],list,tbd
	max_percent_neutrophil_infiltration[],list,tbd
	max_percent_normal_cells[],list,tbd
	max_percent_stromal_cells[],list,tbd
	max_percent_tumor_cells[],list,tbd
	max_percent_tumor_nuclei[],list,tbd
	menopause_status[],list,tbd
	min_percent_lymphocyte_infiltration[],list,tbd
	min_percent_monocyte_infiltration[],list,tbd
	min_percent_necrosis[],list,tbd
	min_percent_neutrophil_infiltration[],list,tbd
	min_percent_normal_cells[],list,tbd
	min_percent_stromal_cells[],list,tbd
	min_percent_tumor_cells[],list,tbd
	min_percent_tumor_nuclei[],list,tbd
	mononucleotide_and_dinucleotide_marker_panel_analysis_status[],list,tbd
	mononucleotide_marker_panel_analysis_status[],list,tbd
	neoplasm_histologic_grade[],list,tbd
	new_tumor_event_after_initial_treatment[],list,tbd
	number_of_lymphnodes_examined[],list,tbd
	number_of_lymphnodes_positive_by_he[],list,tbd
	ParticipantBarcode[],list,tbd
	pathologic_M[],list,tbd
	pathologic_N[],list,tbd
	pathologic_stage[],list,tbd
	pathologic_T[],list,tbd
	person_neoplasm_cancer_status[],list,tbd
	pregnancies[],list,tbd
	preservation_method[],list,tbd
	primary_neoplasm_melanoma_dx[],list,tbd
	primary_therapy_outcome_success[],list,tbd
	prior_dx[],list,tbd
	Project[],list,tbd
	psa_value[],list,tbd
	race[],list,tbd
	residual_tumor[],list,tbd
	SampleBarcode[],list,tbd
	SampleTypeCode[],list,tbd
	Study[],list,tbd
	tobacco_smoking_history[],list,tbd
	total_number_of_pregnancies[],list,tbd
	tumor_pathology[],list,tbd
	tumor_tissue_site[],list,tbd
	tumor_type[],list,tbd
	vital_status[],list,tbd
	weight[],list,tbd
	weiss_venous_invasion[],list,tbd
	year_of_initial_pathologic_diagnosis[],list,tbd


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

	comments, string, tbd
	email, string, tbd
	filters[], list, tbd
	filters[].name, string, tbd
	filters[].value, string, tbd
	id, string, tbd
	last_date_saved, string, tbd
	name, string, tbd
	num_patients, string, tbd
	num_samples, string, tbd
	parent_id, string, tbd
	perm, string, tbd
	source_notes, string, tbd
	source_type, string, tbd
