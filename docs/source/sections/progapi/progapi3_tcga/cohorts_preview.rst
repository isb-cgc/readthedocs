cohorts().preview()
####################
Takes a JSON object of filters in the request body and returns a "preview" of the cohort that would result from passing a similar request to the cohort **save** endpoint. This preview consists of two lists: the lists of case barcodes, and the list of sample barcodes. Authentication is not required.

**Example**::

	curl "https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/cohorts/preview?program_short_name=TCGA-UCS&program_short_name=TCGA-CESC&age_at_diagnosis_lte=20"

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_tcga_api/v3/isb_cgc_tcga_api.cohorts.preview?resource=%257B%250A++%2522program_short_name%2522%253A+%250A++%255B%2522TCGA-BRCA%2522%252C%2522TCGA-UCS%2522%250A++%255D%252C%250A++%2522age_at_diagnosis_lte%2522%253A+%252230%2522%250A%257D&/>`_ to see this endpoint in Google's API explorer.

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
	body = {'program_short_name': ['TCGA-BRCA', 'TCGA-UCS'], 'age_at_diagnosis_gte': 90}
	data = service.cohorts().preview(**body).execute()


**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/cohorts/preview

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	age_at_diagnosis,integer,"Optional. "
	age_at_diagnosis_gte,integer,"Optional. "
	age_at_diagnosis_lte,integer,"Optional. "
	age_began_smoking_in_years,integer,"Optional. "
	age_began_smoking_in_years_gte,integer,"Optional. "
	age_began_smoking_in_years_lte,integer,"Optional. "
	anatomic_neoplasm_subdivision,string,"Optional. "
	avg_percent_lymphocyte_infiltration,number,"Optional. "
	avg_percent_lymphocyte_infiltration_gte,number,"Optional. "
	avg_percent_lymphocyte_infiltration_lte,number,"Optional. "
	avg_percent_monocyte_infiltration,number,"Optional. "
	avg_percent_monocyte_infiltration_gte,number,"Optional. "
	avg_percent_monocyte_infiltration_lte,number,"Optional. "
	avg_percent_necrosis,number,"Optional. "
	avg_percent_necrosis_gte,number,"Optional. "
	avg_percent_necrosis_lte,number,"Optional. "
	avg_percent_neutrophil_infiltration,number,"Optional. "
	avg_percent_neutrophil_infiltration_gte,number,"Optional. "
	avg_percent_neutrophil_infiltration_lte,number,"Optional. "
	avg_percent_normal_cells,number,"Optional. "
	avg_percent_normal_cells_gte,number,"Optional. "
	avg_percent_normal_cells_lte,number,"Optional. "
	avg_percent_stromal_cells,number,"Optional. "
	avg_percent_stromal_cells_gte,number,"Optional. "
	avg_percent_stromal_cells_lte,number,"Optional. "
	avg_percent_tumor_cells,number,"Optional. "
	avg_percent_tumor_cells_gte,number,"Optional. "
	avg_percent_tumor_cells_lte,number,"Optional. "
	avg_percent_tumor_nuclei,number,"Optional. "
	avg_percent_tumor_nuclei_gte,number,"Optional. "
	avg_percent_tumor_nuclei_lte,number,"Optional. "
	batch_number,integer,"Optional. "
	batch_number_gte,integer,"Optional. "
	batch_number_lte,integer,"Optional. "
	bcr,string,"Optional. "
	bmi,number,"Optional. "
	bmi_gte,number,"Optional. "
	bmi_lte,number,"Optional. "
	case_barcode,string,"Optional. "
	case_gdc_id,string,"Optional. "
	clinical_M,string,"Optional. "
	clinical_N,string,"Optional. "
	clinical_stage,string,"Optional. "
	clinical_T,string,"Optional. "
	colorectal_cancer,string,"Optional. "
	country,string,"Optional. "
	days_to_birth,integer,"Optional. "
	days_to_birth_gte,integer,"Optional. "
	days_to_birth_lte,integer,"Optional. "
	days_to_collection,integer,"Optional. "
	days_to_collection_gte,integer,"Optional. "
	days_to_collection_lte,integer,"Optional. "
	days_to_death,integer,"Optional. "
	days_to_death_gte,integer,"Optional. "
	days_to_death_lte,integer,"Optional. "
	days_to_initial_pathologic_diagnosis,integer,"Optional. "
	days_to_initial_pathologic_diagnosis_gte,integer,"Optional. "
	days_to_initial_pathologic_diagnosis_lte,integer,"Optional. "
	days_to_last_followup,integer,"Optional. "
	days_to_last_followup_gte,integer,"Optional. "
	days_to_last_followup_lte,integer,"Optional. "
	days_to_last_known_alive,integer,"Optional. "
	days_to_last_known_alive_gte,integer,"Optional. "
	days_to_last_known_alive_lte,integer,"Optional. "
	days_to_sample_procurement,integer,"Optional. "
	days_to_sample_procurement_gte,integer,"Optional. "
	days_to_sample_procurement_lte,integer,"Optional. "
	days_to_submitted_specimen_dx,integer,"Optional. "
	days_to_submitted_specimen_dx_gte,integer,"Optional. "
	days_to_submitted_specimen_dx_lte,integer,"Optional. "
	disease_code,string,"Optional. "
	endpoint_type,string,"Optional. "
	ethnicity,string,"Optional. "
	gender,string,"Optional. "
	gleason_score_combined,integer,"Optional. "
	gleason_score_combined_gte,integer,"Optional. "
	gleason_score_combined_lte,integer,"Optional. "
	h_pylori_infection,string,"Optional. "
	height,integer,"Optional. "
	height_gte,integer,"Optional. "
	height_lte,integer,"Optional. "
	histological_type,string,"Optional. "
	history_of_colon_polyps,string,"Optional. "
	history_of_neoadjuvant_treatment,string,"Optional. "
	hpv_calls,string,"Optional. "
	hpv_status,string,"Optional. "
	icd_10,string,"Optional. "
	icd_o_3_histology,string,"Optional. "
	icd_o_3_site,string,"Optional. "
	lymphatic_invasion,string,"Optional. "
	lymphnodes_examined,string,"Optional. "
	lymphovascular_invasion_present,string,"Optional. "
	max_percent_lymphocyte_infiltration,number,"Optional. "
	max_percent_lymphocyte_infiltration_gte,number,"Optional. "
	max_percent_lymphocyte_infiltration_lte,number,"Optional. "
	max_percent_monocyte_infiltration,number,"Optional. "
	max_percent_monocyte_infiltration_gte,number,"Optional. "
	max_percent_monocyte_infiltration_lte,number,"Optional. "
	max_percent_necrosis,number,"Optional. "
	max_percent_necrosis_gte,number,"Optional. "
	max_percent_necrosis_lte,number,"Optional. "
	max_percent_neutrophil_infiltration,number,"Optional. "
	max_percent_neutrophil_infiltration_gte,number,"Optional. "
	max_percent_neutrophil_infiltration_lte,number,"Optional. "
	max_percent_normal_cells,number,"Optional. "
	max_percent_normal_cells_gte,number,"Optional. "
	max_percent_normal_cells_lte,number,"Optional. "
	max_percent_stromal_cells,number,"Optional. "
	max_percent_stromal_cells_gte,number,"Optional. "
	max_percent_stromal_cells_lte,number,"Optional. "
	max_percent_tumor_cells,number,"Optional. "
	max_percent_tumor_cells_gte,number,"Optional. "
	max_percent_tumor_cells_lte,number,"Optional. "
	max_percent_tumor_nuclei,number,"Optional. "
	max_percent_tumor_nuclei_gte,number,"Optional. "
	max_percent_tumor_nuclei_lte,number,"Optional. "
	menopause_status,string,"Optional. "
	min_percent_lymphocyte_infiltration,number,"Optional. "
	min_percent_lymphocyte_infiltration_gte,number,"Optional. "
	min_percent_lymphocyte_infiltration_lte,number,"Optional. "
	min_percent_monocyte_infiltration,number,"Optional. "
	min_percent_monocyte_infiltration_gte,number,"Optional. "
	min_percent_monocyte_infiltration_lte,number,"Optional. "
	min_percent_necrosis,number,"Optional. "
	min_percent_necrosis_gte,number,"Optional. "
	min_percent_necrosis_lte,number,"Optional. "
	min_percent_neutrophil_infiltration,number,"Optional. "
	min_percent_neutrophil_infiltration_gte,number,"Optional. "
	min_percent_neutrophil_infiltration_lte,number,"Optional. "
	min_percent_normal_cells,number,"Optional. "
	min_percent_normal_cells_gte,number,"Optional. "
	min_percent_normal_cells_lte,number,"Optional. "
	min_percent_stromal_cells,number,"Optional. "
	min_percent_stromal_cells_gte,number,"Optional. "
	min_percent_stromal_cells_lte,number,"Optional. "
	min_percent_tumor_cells,number,"Optional. "
	min_percent_tumor_cells_gte,number,"Optional. "
	min_percent_tumor_cells_lte,number,"Optional. "
	min_percent_tumor_nuclei,number,"Optional. "
	min_percent_tumor_nuclei_gte,number,"Optional. "
	min_percent_tumor_nuclei_lte,number,"Optional. "
	mononucleotide_and_dinucleotide_marker_panel_analysis_status,string,"Optional. "
	neoplasm_histologic_grade,string,"Optional. "
	new_tumor_event_after_initial_treatment,string,"Optional. "
	num_portions,integer,"Optional. "
	num_portions_gte,integer,"Optional. "
	num_portions_lte,integer,"Optional. "
	num_slides,integer,"Optional. "
	num_slides_gte,integer,"Optional. "
	num_slides_lte,integer,"Optional. "
	number_of_lymphnodes_examined,integer,"Optional. "
	number_of_lymphnodes_examined_gte,integer,"Optional. "
	number_of_lymphnodes_examined_lte,integer,"Optional. "
	number_of_lymphnodes_positive_by_he,integer,"Optional. "
	number_of_lymphnodes_positive_by_he_gte,integer,"Optional. "
	number_of_lymphnodes_positive_by_he_lte,integer,"Optional. "
	number_pack_years_smoked,integer,"Optional. "
	number_pack_years_smoked_gte,integer,"Optional. "
	number_pack_years_smoked_lte,integer,"Optional. "
	other_dx,string,"Optional. "
	other_malignancy_anatomic_site,string,"Optional. "
	other_malignancy_histological_type,string,"Optional. "
	other_malignancy_type,string,"Optional. "
	pathologic_M,string,"Optional. "
	pathologic_N,string,"Optional. "
	pathologic_stage,string,"Optional. "
	pathologic_T,string,"Optional. "
	pathology_report_uuid,string,"Optional. "
	person_neoplasm_cancer_status,string,"Optional. "
	pregnancies,string,"Optional. "
	preservation_method,string,"Optional. "
	primary_neoplasm_melanoma_dx,string,"Optional. "
	primary_therapy_outcome_success,string,"Optional. "
	program_name,string,"Optional. "
	project_short_name,string,"Optional. "
	psa_value,number,"Optional. "
	psa_value_gte,number,"Optional. "
	psa_value_lte,number,"Optional. "
	race,string,"Optional. "
	residual_tumor,string,"Optional. "
	sample_barcode,string,"Optional. "
	sample_gdc_id,string,"Optional. "
	sample_type,string,"Optional. "
	stopped_smoking_year,integer,"Optional. "
	stopped_smoking_year_gte,integer,"Optional. "
	stopped_smoking_year_lte,integer,"Optional. "
	summary_file_count,integer,"Optional. "
	summary_file_count_gte,integer,"Optional. "
	summary_file_count_lte,integer,"Optional. "
	tobacco_smoking_history,string,"Optional. "
	tss_code,string,"Optional. "
	tumor_tissue_site,string,"Optional. "
	tumor_type,string,"Optional. "
	venous_invasion,string,"Optional. "
	vital_status,string,"Optional. "
	weight,integer,"Optional. "
	weight_gte,integer,"Optional. "
	weight_lte,integer,"Optional. "
	year_of_diagnosis,integer,"Optional. "
	year_of_diagnosis_gte,integer,"Optional. "
	year_of_diagnosis_lte,integer,"Optional. "
	year_of_tobacco_smoking_onset,integer,"Optional. "
	year_of_tobacco_smoking_onset_gte,integer,"Optional. "
	year_of_tobacco_smoking_onset_lte,integer,"Optional. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "case_count": integer,
    "cases": [string],
    "sample_count": integer,
    "samples": [string]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	case_count, integer, "Number of cases in the cohort."
	cases[], list, "List of cases barcodes in the cohort."
	sample_count, integer, "Number of samples in the cohort."
	samples[], list, "List of sample barcodes in the cohort."
