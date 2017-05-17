cohorts().create()
###################
Creates and saves a cohort. Takes a JSON object in the request body to use as the cohort's filters. Authentication is required. Returns information about the saved cohort, including the number of cases and the number of samples in that cohort.

**Example**::

	python isb_curl.py "https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/cohorts/create?name={COHORT NAME}" -H "Content-Type: application/json" -d '{"program_short_name": ["TCGA-UCS", "TCGA-CESC"], "age_at_diagnosis_lte": 60}'

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_tcga_api/v3/isb_cgc_tcga_api.cohorts.create?name=COHORT%20NAME%20HERE&resource=%257B%250A++%2522Study%2522%253A+%250A++%255B%2522UCS%2522%250A++%255D%250A%257D&/>`_ to see this endpoint in Google's API explorer.

**Python API Client Example**::

	from googleapiclient.discovery import build
	from oauth2client.client import OAuth2WebServerFlow
	from oauth2client import tools
	from oauth2client.file import Storage
	import httplib2
	import os

	CLIENT_ID = '907668440978-0ol0griu70qkeb6k3gnn2vipfa5mgl60.apps.googleusercontent.com'
	CLIENT_SECRET = 'To_WJH7-1V-TofhNGcEqmEYi'
	EMAIL_SCOPE = 'https://www.googleapis.com/auth/userinfo.email'
	DEFAULT_STORAGE_FILE = os.path.join(os.path.expanduser('~'), '.isb_credentials')

	def get_credentials():
		oauth_flow_args = ['--noauth_local_webserver']
		storage = Storage(DEFAULT_STORAGE_FILE)
		credentials = storage.get()
		if not credentials or credentials.invalid:
			flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, EMAIL_SCOPE)
			flow.auth_uri = flow.auth_uri.rstrip('/') + '?approval_prompt=force'
			credentials = tools.run_flow(flow, storage, tools.argparser.parse_args(oauth_flow_args))
		return credentials

	def get_authorized_service():
		api = 'isb_cgc_tcga_api'
		version = 'v3'
		site = 'https://api-dot-isb-cgc.appspot.com'
		discovery_url = '%s/_ah/api/discovery/v1/apis/%s/%s/rest' % (site, api, version)
		credentials = get_credentials()
		http = credentials.authorize(httplib2.Http())
		if credentials.access_token_expired or credentials.invalid:
			credentials.refresh(http)
		authorized_service = build(api, version, discoveryServiceUrl=discovery_url, http=http)
		return authorized_service

	service = get_authorized_service()
	body = {'program_short_name': ['TCGA-BRCA', 'TCGA-UCS'], 'age_at_diagnosis_gte': 90}
	data = service.cohorts().create(name=name, body=body).execute()


**Request**

HTTP request::

	POST https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_tcga_api/v3/cohorts/create

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	name,string,"Required. "


Request body

In the request body, supply a metadata resource with the following properties:

.. code-block:: javascript

  {
    "age_at_diagnosis": [integer],
    "age_at_diagnosis_gte": integer,
    "age_at_diagnosis_lte": integer,
    "age_began_smoking_in_years": [integer],
    "age_began_smoking_in_years_gte": integer,
    "age_began_smoking_in_years_lte": integer,
    "anatomic_neoplasm_subdivision": [string],
    "avg_percent_lymphocyte_infiltration": [number],
    "avg_percent_lymphocyte_infiltration_gte": number,
    "avg_percent_lymphocyte_infiltration_lte": number,
    "avg_percent_monocyte_infiltration": [number],
    "avg_percent_monocyte_infiltration_gte": number,
    "avg_percent_monocyte_infiltration_lte": number,
    "avg_percent_necrosis": [number],
    "avg_percent_necrosis_gte": number,
    "avg_percent_necrosis_lte": number,
    "avg_percent_neutrophil_infiltration": [number],
    "avg_percent_neutrophil_infiltration_gte": number,
    "avg_percent_neutrophil_infiltration_lte": number,
    "avg_percent_normal_cells": [number],
    "avg_percent_normal_cells_gte": number,
    "avg_percent_normal_cells_lte": number,
    "avg_percent_stromal_cells": [number],
    "avg_percent_stromal_cells_gte": number,
    "avg_percent_stromal_cells_lte": number,
    "avg_percent_tumor_cells": [number],
    "avg_percent_tumor_cells_gte": number,
    "avg_percent_tumor_cells_lte": number,
    "avg_percent_tumor_nuclei": [number],
    "avg_percent_tumor_nuclei_gte": number,
    "avg_percent_tumor_nuclei_lte": number,
    "batch_number": [integer],
    "batch_number_gte": integer,
    "batch_number_lte": integer,
    "bcr": [string],
    "bmi": [number],
    "bmi_gte": number,
    "bmi_lte": number,
    "case_barcode": [string],
    "case_gdc_id": [string],
    "clinical_M": [string],
    "clinical_N": [string],
    "clinical_stage": [string],
    "clinical_T": [string],
    "colorectal_cancer": [string],
    "country": [string],
    "days_to_birth": [integer],
    "days_to_birth_gte": integer,
    "days_to_birth_lte": integer,
    "days_to_collection": [integer],
    "days_to_collection_gte": integer,
    "days_to_collection_lte": integer,
    "days_to_death": [integer],
    "days_to_death_gte": integer,
    "days_to_death_lte": integer,
    "days_to_initial_pathologic_diagnosis": [integer],
    "days_to_initial_pathologic_diagnosis_gte": integer,
    "days_to_initial_pathologic_diagnosis_lte": integer,
    "days_to_last_followup": [integer],
    "days_to_last_followup_gte": integer,
    "days_to_last_followup_lte": integer,
    "days_to_last_known_alive": [integer],
    "days_to_last_known_alive_gte": integer,
    "days_to_last_known_alive_lte": integer,
    "days_to_sample_procurement": [integer],
    "days_to_sample_procurement_gte": integer,
    "days_to_sample_procurement_lte": integer,
    "days_to_submitted_specimen_dx": [integer],
    "days_to_submitted_specimen_dx_gte": integer,
    "days_to_submitted_specimen_dx_lte": integer,
    "disease_code": [string],
    "endpoint_type": [string],
    "ethnicity": [string],
    "gender": [string],
    "gleason_score_combined": [integer],
    "gleason_score_combined_gte": integer,
    "gleason_score_combined_lte": integer,
    "h_pylori_infection": [string],
    "height": [integer],
    "height_gte": integer,
    "height_lte": integer,
    "histological_type": [string],
    "history_of_colon_polyps": [string],
    "history_of_neoadjuvant_treatment": [string],
    "hpv_calls": [string],
    "hpv_status": [string],
    "icd_10": [string],
    "icd_o_3_histology": [string],
    "icd_o_3_site": [string],
    "lymphatic_invasion": [string],
    "lymphnodes_examined": [string],
    "lymphovascular_invasion_present": [string],
    "max_percent_lymphocyte_infiltration": [number],
    "max_percent_lymphocyte_infiltration_gte": number,
    "max_percent_lymphocyte_infiltration_lte": number,
    "max_percent_monocyte_infiltration": [number],
    "max_percent_monocyte_infiltration_gte": number,
    "max_percent_monocyte_infiltration_lte": number,
    "max_percent_necrosis": [number],
    "max_percent_necrosis_gte": number,
    "max_percent_necrosis_lte": number,
    "max_percent_neutrophil_infiltration": [number],
    "max_percent_neutrophil_infiltration_gte": number,
    "max_percent_neutrophil_infiltration_lte": number,
    "max_percent_normal_cells": [number],
    "max_percent_normal_cells_gte": number,
    "max_percent_normal_cells_lte": number,
    "max_percent_stromal_cells": [number],
    "max_percent_stromal_cells_gte": number,
    "max_percent_stromal_cells_lte": number,
    "max_percent_tumor_cells": [number],
    "max_percent_tumor_cells_gte": number,
    "max_percent_tumor_cells_lte": number,
    "max_percent_tumor_nuclei": [number],
    "max_percent_tumor_nuclei_gte": number,
    "max_percent_tumor_nuclei_lte": number,
    "menopause_status": [string],
    "min_percent_lymphocyte_infiltration": [number],
    "min_percent_lymphocyte_infiltration_gte": number,
    "min_percent_lymphocyte_infiltration_lte": number,
    "min_percent_monocyte_infiltration": [number],
    "min_percent_monocyte_infiltration_gte": number,
    "min_percent_monocyte_infiltration_lte": number,
    "min_percent_necrosis": [number],
    "min_percent_necrosis_gte": number,
    "min_percent_necrosis_lte": number,
    "min_percent_neutrophil_infiltration": [number],
    "min_percent_neutrophil_infiltration_gte": number,
    "min_percent_neutrophil_infiltration_lte": number,
    "min_percent_normal_cells": [number],
    "min_percent_normal_cells_gte": number,
    "min_percent_normal_cells_lte": number,
    "min_percent_stromal_cells": [number],
    "min_percent_stromal_cells_gte": number,
    "min_percent_stromal_cells_lte": number,
    "min_percent_tumor_cells": [number],
    "min_percent_tumor_cells_gte": number,
    "min_percent_tumor_cells_lte": number,
    "min_percent_tumor_nuclei": [number],
    "min_percent_tumor_nuclei_gte": number,
    "min_percent_tumor_nuclei_lte": number,
    "mononucleotide_and_dinucleotide_marker_panel_analysis_status": [string],
    "neoplasm_histologic_grade": [string],
    "new_tumor_event_after_initial_treatment": [string],
    "num_portions": [integer],
    "num_portions_gte": integer,
    "num_portions_lte": integer,
    "num_slides": [integer],
    "num_slides_gte": integer,
    "num_slides_lte": integer,
    "number_of_lymphnodes_examined": [integer],
    "number_of_lymphnodes_examined_gte": integer,
    "number_of_lymphnodes_examined_lte": integer,
    "number_of_lymphnodes_positive_by_he": [integer],
    "number_of_lymphnodes_positive_by_he_gte": integer,
    "number_of_lymphnodes_positive_by_he_lte": integer,
    "number_pack_years_smoked": [integer],
    "number_pack_years_smoked_gte": integer,
    "number_pack_years_smoked_lte": integer,
    "other_dx": [string],
    "other_malignancy_anatomic_site": [string],
    "other_malignancy_histological_type": [string],
    "other_malignancy_type": [string],
    "pathologic_M": [string],
    "pathologic_N": [string],
    "pathologic_stage": [string],
    "pathologic_T": [string],
    "pathology_report_uuid": [string],
    "person_neoplasm_cancer_status": [string],
    "pregnancies": [string],
    "preservation_method": [string],
    "primary_neoplasm_melanoma_dx": [string],
    "primary_therapy_outcome_success": [string],
    "program_name": [string],
    "project_short_name": [string],
    "psa_value": [number],
    "psa_value_gte": number,
    "psa_value_lte": number,
    "race": [string],
    "residual_tumor": [string],
    "sample_barcode": [string],
    "sample_gdc_id": [string],
    "sample_type": [string],
    "stopped_smoking_year": [integer],
    "stopped_smoking_year_gte": integer,
    "stopped_smoking_year_lte": integer,
    "summary_file_count": [integer],
    "summary_file_count_gte": integer,
    "summary_file_count_lte": integer,
    "tobacco_smoking_history": [string],
    "tss_code": [string],
    "tumor_tissue_site": [string],
    "tumor_type": [string],
    "venous_invasion": [string],
    "vital_status": [string],
    "weight": [integer],
    "weight_gte": integer,
    "weight_lte": integer,
    "year_of_diagnosis": [integer],
    "year_of_diagnosis_gte": integer,
    "year_of_diagnosis_lte": integer,
    "year_of_tobacco_smoking_onset": [integer],
    "year_of_tobacco_smoking_onset_gte": integer,
    "year_of_tobacco_smoking_onset_lte": integer
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	age_at_diagnosis[],list,"Optional. "
	age_at_diagnosis_gte,integer,"Optional. "
	age_at_diagnosis_lte,integer,"Optional. "
	age_began_smoking_in_years[],list,"Optional. "
	age_began_smoking_in_years_gte,integer,"Optional. "
	age_began_smoking_in_years_lte,integer,"Optional. "
	anatomic_neoplasm_subdivision[],list,"Optional. Possible values include: 'Alveolar Ridge', 'Antrum/Distal', 'Ascending Colon', 'Base of tongue', 'Bilateral', 'Bladder - NOS', 'Body of Pancreas', 'Bronchial', 'Buccal Mucosa', 'Cardia/Proximal', 'Cecum', 'Descending Colon', 'Dome', 'Endometrium', 'Floor of mouth', 'Fundus uteri', 'Fundus/Body', 'Gastroesophageal Junction', 'Hard Palate', 'Head of Pancreas', 'Hepatic Flexure', 'Hypopharynx', 'L-Lower', 'L-Upper', 'Larynx', 'Left', 'Left Lower Inner Quadrant', 'Left Lower Outer Quadrant', 'Left Upper Inner Quadrant', 'Left Upper Outer Quadrant', 'Lip', 'Lower uterine segment/Isthmus uteri', 'Myometrium', 'Neck', 'Oral Cavity', 'Oral Tongue', 'Oropharynx', 'Other (please specify)', 'R-Lower', 'R-Middle', 'R-Upper', 'Rectosigmoid Junction', 'Rectum', 'Right', 'Right Lower Inner Quadrant', 'Right Lower Outer Quadrant', 'Right Upper Inner Quadrant', 'Right Upper Outer Quadrant', 'Sigmoid Colon', 'Splenic Flexure', 'Stomach (NOS)', 'Tail of Pancreas', 'Tonsil', 'Transverse Colon', 'Trigone', 'Unknown - Uterus NOS', 'Wall Anterior', 'Wall Lateral', 'Wall NOS', 'Wall Posterior'."
	avg_percent_lymphocyte_infiltration[],list,"Optional. "
	avg_percent_lymphocyte_infiltration_gte,number,"Optional. "
	avg_percent_lymphocyte_infiltration_lte,number,"Optional. "
	avg_percent_monocyte_infiltration[],list,"Optional. "
	avg_percent_monocyte_infiltration_gte,number,"Optional. "
	avg_percent_monocyte_infiltration_lte,number,"Optional. "
	avg_percent_necrosis[],list,"Optional. "
	avg_percent_necrosis_gte,number,"Optional. "
	avg_percent_necrosis_lte,number,"Optional. "
	avg_percent_neutrophil_infiltration[],list,"Optional. "
	avg_percent_neutrophil_infiltration_gte,number,"Optional. "
	avg_percent_neutrophil_infiltration_lte,number,"Optional. "
	avg_percent_normal_cells[],list,"Optional. "
	avg_percent_normal_cells_gte,number,"Optional. "
	avg_percent_normal_cells_lte,number,"Optional. "
	avg_percent_stromal_cells[],list,"Optional. "
	avg_percent_stromal_cells_gte,number,"Optional. "
	avg_percent_stromal_cells_lte,number,"Optional. "
	avg_percent_tumor_cells[],list,"Optional. "
	avg_percent_tumor_cells_gte,number,"Optional. "
	avg_percent_tumor_cells_lte,number,"Optional. "
	avg_percent_tumor_nuclei[],list,"Optional. "
	avg_percent_tumor_nuclei_gte,number,"Optional. "
	avg_percent_tumor_nuclei_lte,number,"Optional. "
	batch_number[],list,"Optional. "
	batch_number_gte,integer,"Optional. "
	batch_number_lte,integer,"Optional. "
	bcr[],list,"Optional. Possible values include: 'Nationwide Children's Hospital', 'Washington University'."
	bmi[],list,"Optional. "
	bmi_gte,number,"Optional. "
	bmi_lte,number,"Optional. "
	case_barcode[],list,"Optional. "
	case_gdc_id[],list,"Optional. "
	clinical_M[],list,"Optional. Possible values include: 'M0', 'M1', 'M1a', 'M1b', 'M1c', 'MX'."
	clinical_N[],list,"Optional. Possible values include: 'N0', 'N1', 'N2', 'N2a', 'N2b', 'N2c', 'N3', 'NX'."
	clinical_stage[],list,"Optional. Possible values include: 'Stage I', 'Stage IA', 'Stage IA1', 'Stage IA2', 'Stage IB', 'Stage IB1', 'Stage IB2', 'Stage IC', 'Stage II', 'Stage IIA', 'Stage IIA1', 'Stage IIA2', 'Stage IIB', 'Stage IIC', 'Stage III', 'Stage IIIA', 'Stage IIIB', 'Stage IIIC', 'Stage IIIC1', 'Stage IIIC2', 'Stage IS', 'Stage IV', 'Stage IVA', 'Stage IVB', 'Stage IVC'."
	clinical_T[],list,"Optional. Possible values include: 'T1', 'T1a', 'T1b', 'T1c', 'T2', 'T2a', 'T2b', 'T2c', 'T3', 'T3a', 'T3b', 'T4', 'T4a', 'T4b', 'T4c', 'T4d', 'T4e', 'TX'."
	colorectal_cancer[],list,"Optional. Possible values include: 'NO', 'YES'."
	country[],list,"Optional. Possible values include: 'Afghanistan', 'Algeria', 'American Samoa', 'Australia', 'Brazil', 'Bulgaria', 'Canada', 'Croatia', 'Czech Republic', 'France', 'Georgia', 'Germany', 'Hamburg/Germany', 'Israel', 'Italy', 'Korea', 'Korea South', 'Moldova', 'Netherlands', 'Nigeria', 'Ontario Canada', 'Ontario/Canada', 'Pakistan', 'Poland', 'Puerto Rico', 'Republic of Moldova', 'Romania', 'Russia', 'Sao Paulo', 'Singapore', 'Spain', 'Switzerland', 'Ukraine', 'United Kingdom', 'United States', 'Vietnam', 'Yemen'."
	days_to_birth[],list,"Optional. "
	days_to_birth_gte,integer,"Optional. "
	days_to_birth_lte,integer,"Optional. "
	days_to_collection[],list,"Optional. "
	days_to_collection_gte,integer,"Optional. "
	days_to_collection_lte,integer,"Optional. "
	days_to_death[],list,"Optional. "
	days_to_death_gte,integer,"Optional. "
	days_to_death_lte,integer,"Optional. "
	days_to_initial_pathologic_diagnosis[],list,"Optional. "
	days_to_initial_pathologic_diagnosis_gte,integer,"Optional. "
	days_to_initial_pathologic_diagnosis_lte,integer,"Optional. "
	days_to_last_followup[],list,"Optional. "
	days_to_last_followup_gte,integer,"Optional. "
	days_to_last_followup_lte,integer,"Optional. "
	days_to_last_known_alive[],list,"Optional. "
	days_to_last_known_alive_gte,integer,"Optional. "
	days_to_last_known_alive_lte,integer,"Optional. "
	days_to_sample_procurement[],list,"Optional. "
	days_to_sample_procurement_gte,integer,"Optional. "
	days_to_sample_procurement_lte,integer,"Optional. "
	days_to_submitted_specimen_dx[],list,"Optional. "
	days_to_submitted_specimen_dx_gte,integer,"Optional. "
	days_to_submitted_specimen_dx_lte,integer,"Optional. "
	disease_code[],list,"Optional. Possible values include: 'ACC', 'BLCA', 'BRCA', 'CESC', 'CHOL', 'COAD', 'DLBC', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP', 'LAML', 'LGG', 'LIHC', 'LUAD', 'LUSC', 'MESO', 'OV', 'PAAD', 'PCPG', 'PRAD', 'READ', 'SARC', 'SKCM', 'STAD', 'TGCT', 'THCA', 'THYM', 'UCEC', 'UCS', 'UVM'."
	endpoint_type[],list,"Optional. Possible values include: 'current', 'legacy'."
	ethnicity[],list,"Optional. Possible values include: 'HISPANIC OR LATINO', 'NOT HISPANIC OR LATINO'."
	gender[],list,"Optional. Possible values include: 'FEMALE', 'MALE'."
	gleason_score_combined[],list,"Optional. "
	gleason_score_combined_gte,integer,"Optional. "
	gleason_score_combined_lte,integer,"Optional. "
	h_pylori_infection[],list,"Optional. Possible values include: 'Current', 'Never', 'No', 'Yes'."
	height[],list,"Optional. "
	height_gte,integer,"Optional. "
	height_lte,integer,"Optional. "
	histological_type[],list,"Optional. "
	history_of_colon_polyps[],list,"Optional. Possible values include: 'NO', 'YES'."
	history_of_neoadjuvant_treatment[],list,"Optional. Possible values include: 'No', 'Yes', 'Yes, Pharmaceutical Treatment Prior to Resection', 'Yes, Radiation Prior to Resection'."
	hpv_calls[],list,"Optional. Possible values include: 'HPV16', 'HPV16;HPV18', 'HPV16;HPV18;HPV58', 'HPV16;HPV31', 'HPV16;HPV33', 'HPV16;HPV35', 'HPV16;HPV39', 'HPV16;HPV52', 'HPV16;HPV66', 'HPV18', 'HPV18;HPV31', 'HPV31', 'HPV33', 'HPV35', 'HPV39', 'HPV45', 'HPV51', 'HPV52', 'HPV56', 'HPV58', 'HPV59', 'HPV68', 'HPV73'."
	hpv_status[],list,"Optional. Possible values include: 'Indeterminate', 'Negative', 'Positive'."
	icd_10[],list,"Optional. "
	icd_o_3_histology[],list,"Optional. "
	icd_o_3_site[],list,"Optional. "
	lymphatic_invasion[],list,"Optional. Possible values include: 'NO', 'YES'."
	lymphnodes_examined[],list,"Optional. Possible values include: 'NO', 'YES'."
	lymphovascular_invasion_present[],list,"Optional. Possible values include: 'NO', 'YES'."
	max_percent_lymphocyte_infiltration[],list,"Optional. "
	max_percent_lymphocyte_infiltration_gte,number,"Optional. "
	max_percent_lymphocyte_infiltration_lte,number,"Optional. "
	max_percent_monocyte_infiltration[],list,"Optional. "
	max_percent_monocyte_infiltration_gte,number,"Optional. "
	max_percent_monocyte_infiltration_lte,number,"Optional. "
	max_percent_necrosis[],list,"Optional. "
	max_percent_necrosis_gte,number,"Optional. "
	max_percent_necrosis_lte,number,"Optional. "
	max_percent_neutrophil_infiltration[],list,"Optional. "
	max_percent_neutrophil_infiltration_gte,number,"Optional. "
	max_percent_neutrophil_infiltration_lte,number,"Optional. "
	max_percent_normal_cells[],list,"Optional. "
	max_percent_normal_cells_gte,number,"Optional. "
	max_percent_normal_cells_lte,number,"Optional. "
	max_percent_stromal_cells[],list,"Optional. "
	max_percent_stromal_cells_gte,number,"Optional. "
	max_percent_stromal_cells_lte,number,"Optional. "
	max_percent_tumor_cells[],list,"Optional. "
	max_percent_tumor_cells_gte,number,"Optional. "
	max_percent_tumor_cells_lte,number,"Optional. "
	max_percent_tumor_nuclei[],list,"Optional. "
	max_percent_tumor_nuclei_gte,number,"Optional. "
	max_percent_tumor_nuclei_lte,number,"Optional. "
	menopause_status[],list,"Optional. Possible values include: 'Indeterminate (neither Pre or Postmenopausal)', 'Peri (6-12 months since last menstrual period)', 'Post (prior bilateral ovariectomy OR >12 mo since LMP with no prior hysterectomy)', 'Pre (<6 months since LMP AND no prior bilateral ovariectomy AND not on estrogen replacement)'."
	min_percent_lymphocyte_infiltration[],list,"Optional. "
	min_percent_lymphocyte_infiltration_gte,number,"Optional. "
	min_percent_lymphocyte_infiltration_lte,number,"Optional. "
	min_percent_monocyte_infiltration[],list,"Optional. "
	min_percent_monocyte_infiltration_gte,number,"Optional. "
	min_percent_monocyte_infiltration_lte,number,"Optional. "
	min_percent_necrosis[],list,"Optional. "
	min_percent_necrosis_gte,number,"Optional. "
	min_percent_necrosis_lte,number,"Optional. "
	min_percent_neutrophil_infiltration[],list,"Optional. "
	min_percent_neutrophil_infiltration_gte,number,"Optional. "
	min_percent_neutrophil_infiltration_lte,number,"Optional. "
	min_percent_normal_cells[],list,"Optional. "
	min_percent_normal_cells_gte,number,"Optional. "
	min_percent_normal_cells_lte,number,"Optional. "
	min_percent_stromal_cells[],list,"Optional. "
	min_percent_stromal_cells_gte,number,"Optional. "
	min_percent_stromal_cells_lte,number,"Optional. "
	min_percent_tumor_cells[],list,"Optional. "
	min_percent_tumor_cells_gte,number,"Optional. "
	min_percent_tumor_cells_lte,number,"Optional. "
	min_percent_tumor_nuclei[],list,"Optional. "
	min_percent_tumor_nuclei_gte,number,"Optional. "
	min_percent_tumor_nuclei_lte,number,"Optional. "
	mononucleotide_and_dinucleotide_marker_panel_analysis_status[],list,"Optional. Possible values include: 'Indeterminate', 'MSI-H', 'MSI-L', 'MSS', 'Not Tested'."
	neoplasm_histologic_grade[],list,"Optional. Possible values include: 'G1', 'G2', 'G3', 'G4', 'GB', 'GX', 'High Grade', 'Low Grade'."
	new_tumor_event_after_initial_treatment[],list,"Optional. Possible values include: 'NO', 'YES'."
	num_portions[],list,"Optional. "
	num_portions_gte,integer,"Optional. "
	num_portions_lte,integer,"Optional. "
	num_slides[],list,"Optional. "
	num_slides_gte,integer,"Optional. "
	num_slides_lte,integer,"Optional. "
	number_of_lymphnodes_examined[],list,"Optional. "
	number_of_lymphnodes_examined_gte,integer,"Optional. "
	number_of_lymphnodes_examined_lte,integer,"Optional. "
	number_of_lymphnodes_positive_by_he[],list,"Optional. "
	number_of_lymphnodes_positive_by_he_gte,integer,"Optional. "
	number_of_lymphnodes_positive_by_he_lte,integer,"Optional. "
	number_pack_years_smoked[],list,"Optional. "
	number_pack_years_smoked_gte,integer,"Optional. "
	number_pack_years_smoked_lte,integer,"Optional. "
	other_dx[],list,"Optional. Possible values include: 'Both History of Synchronous/ Bilateral and Prior Malignancy', 'No', 'Yes, History of Prior Malignancy', 'Yes, History of Synchronous/Bilateral Malignancy'."
	other_malignancy_anatomic_site[],list,"Optional. "
	other_malignancy_histological_type[],list,"Optional. Possible values include: 'Adenocarcinoma, Not Otherwise Specified', 'Adenocarcinoma, Not Otherwise Specified, Adenocarcinoma, Not Otherwise Specified', 'Adenocarcinoma, Not Otherwise Specified, Colon Adenocarcinoma', 'Adenocarcinoma, Not Otherwise Specified, Kidney Clear Cell Renal Carcinoma', 'Adenocarcinoma, Not Otherwise Specified, Lung Acinar Adenocarcinoma', 'Adenocarcinoma, Not Otherwise Specified, Other, specify', 'Adenocarcinoma, Not Otherwise Specified, Other, specify, Other, specify', 'Adenocarcinoma, Not Otherwise Specified, Squamous Cell Carcinoma, Not Otherwise Specified', 'Adenosquamous', 'Astrocytoma', 'Basaloid Squamous Cell', 'Basaloid Squamous Cell, Adenocarcinoma, Not Otherwise Specified', 'Clear Cell Adenocarcinoma', 'Clear Cell Squamous Cell', 'Colon Adenocarcinoma', 'Colon Adenocarcinoma, Colon Adenocarcinoma', 'Colon Mucinous Adenocarcinoma', 'Endometrioid endometrial adenocarcinoma (Grade 1 or 2)', 'Endometrioid endometrial adenocarcinoma (Grade 3)', 'Head & Neck Squamous Cell Carcinoma', 'Hepatocellular Carcinoma', 'Kidney Clear Cell Renal Carcinoma', 'Kidney Clear Cell Renal Carcinoma, Kidney Clear Cell Renal Carcinoma', 'Kidney Clear Cell Renal Carcinoma, Kidney Clear Cell Renal Carcinoma, Other, specify', 'Kidney Clear Cell Renal Carcinoma, Kidney Papillary Renal Cell Carcinoma', 'Kidney Clear Cell Renal Carcinoma, Other, specify', 'Kidney Papillary Renal Cell Carcinoma', 'Kidney Papillary Renal Cell Carcinoma, Kidney Papillary Renal Cell Carcinoma', 'Kidney Papillary Renal Cell Carcinoma, Kidney Papillary Renal Cell Carcinoma, Adenocarcinoma, Not Otherwise Specified', 'Lung Adenocarcinoma Mixed Subtype', 'Lung Adenocarcinoma- Not Otherwise Specified (NOS)', 'Lung Adenocarcinoma- Not Otherwise Specified (NOS), Adenocarcinoma, Not Otherwise Specified', 'Lung Bronchioloalveolar Carcinoma Nonmucinous', 'Lung Clear Cell Squamous Cell Carcinoma', 'Lung Clear Cell Squamous Cell Carcinoma, Other, specify', 'Lung Papillary Adenocarcinoma', 'Lung Small Cell Squamous Cell Carcinoma', 'Other, specify', 'Other, specify, Adenocarcinoma, Not Otherwise Specified', 'Other, specify, Adenocarcinoma, Not Otherwise Specified, Other, specify', 'Other, specify, Basaloid Squamous Cell', 'Other, specify, Clear Cell Adenocarcinoma', 'Other, specify, Kidney Papillary Renal Cell Carcinoma', 'Other, specify, Kidney Papillary Renal Cell Carcinoma, Kidney Papillary Renal Cell Carcinoma', 'Other, specify, Lung Mucinous Adenocarcinoma', 'Other, specify, Other, specify', 'Other, specify, Other, specify, Kidney Papillary Renal Cell Carcinoma', 'Other, specify, Other, specify, Other, specify', 'Other, specify, Other, specify, Other, specify, Other, specify', 'Other, specify, Other, specify, Squamous Cell Carcinoma, Not Otherwise Specified', 'Other, specify, Squamous Cell Carcinoma, Not Otherwise Specified', 'Papillary Squamous Cell', 'Rectal Adenocarcinoma', 'Small Cell Squamous Cell', 'Squamous Cell Carcinoma, Not Otherwise Specified', 'Squamous Cell Carcinoma, Not Otherwise Specified, Basaloid Squamous Cell', 'Squamous Cell Carcinoma, Not Otherwise Specified, Kidney Papillary Renal Cell Carcinoma', 'Squamous Cell Carcinoma, Not Otherwise Specified, Lung Adenocarcinoma Mixed Subtype', 'Squamous Cell Carcinoma, Not Otherwise Specified, Other, specify', 'Squamous Cell Carcinoma, Not Otherwise Specified, Other, specify, Other, specify', 'Squamous Cell Carcinoma, Not Otherwise Specified, Squamous Cell Carcinoma, Not Otherwise Specified', 'Squamous Cell Carcinoma, Not Otherwise Specified, Squamous Cell Carcinoma, Not Otherwise Specified, Basaloid Squamous Cell', 'Thyroid Papillary Carcinoma - Classical/usual', 'Thyroid Papillary Carcinoma - Classical/usual, Adenocarcinoma, Not Otherwise Specified', 'Thyroid Papillary Carcinoma - Follicular (>= 99% follicular patterned)', 'Thyroid Papillary Carcinoma - Other, specify', 'Thyroid Papillary Carcinoma - Other, specify, Thyroid Papillary Carcinoma - Other, specify, Other, specify', 'Uterine serous endometrial adenocarcinoma'."
	other_malignancy_type[],list,"Optional. Possible values include: 'Prior Malignancy', 'Prior Malignancy, Prior Malignancy', 'Prior Malignancy, Prior Malignancy, Prior Malignancy', 'Prior Malignancy, Prior Malignancy, Prior Malignancy, Synchronous Malignancy', 'Prior Malignancy, Prior Malignancy, Synchronous Malignancy', 'Prior Malignancy, Synchronous Malignancy', 'Prior Malignancy, Synchronous Malignancy, Prior Malignancy', 'Synchronous Malignancy', 'Synchronous Malignancy, Prior Malignancy', 'Synchronous Malignancy, Prior Malignancy, Prior Malignancy, Prior Malignancy', 'Synchronous Malignancy, Prior Malignancy, Synchronous Malignancy', 'Synchronous Malignancy, Synchronous Malignancy', 'Synchronous Malignancy, Synchronous Malignancy, Prior Malignancy'."
	pathologic_M[],list,"Optional. Possible values include: 'cM0 (i+)', 'M0', 'M1', 'M1a', 'M1b', 'M1c', 'MX'."
	pathologic_N[],list,"Optional. Possible values include: 'N0', 'N0 (i+)', 'N0 (i-)', 'N0 (mol+)', 'N1', 'N1a', 'N1b', 'N1c', 'N1mi', 'N2', 'N2a', 'N2b', 'N2c', 'N3', 'N3a', 'N3b', 'N3c', 'NX'."
	pathologic_stage[],list,"Optional. Possible values include: 'I/II NOS', 'IS', 'Stage 0', 'Stage I', 'Stage IA', 'Stage IB', 'Stage II', 'Stage IIA', 'Stage IIB', 'Stage IIC', 'Stage III', 'Stage IIIA', 'Stage IIIB', 'Stage IIIC', 'Stage IV', 'Stage IVA', 'Stage IVB', 'Stage IVC', 'Stage X'."
	pathologic_T[],list,"Optional. Possible values include: 'T0', 'T1', 'T1a', 'T1a1', 'T1b', 'T1b1', 'T1b2', 'T1c', 'T2', 'T2a', 'T2a1', 'T2a2', 'T2b', 'T2c', 'T3', 'T3a', 'T3b', 'T3c', 'T4', 'T4a', 'T4b', 'T4c', 'T4d', 'T4e', 'Tis', 'TX'."
	pathology_report_uuid[],list,"Optional. "
	person_neoplasm_cancer_status[],list,"Optional. Possible values include: 'TUMOR FREE', 'WITH TUMOR'."
	pregnancies[],list,"Optional. Possible values include: '0', '1', '2', '3', '4+'."
	preservation_method[],list,"Optional. Possible values include: 'FFPE', 'frozen'."
	primary_neoplasm_melanoma_dx[],list,"Optional. Possible values include: 'NO', 'YES'."
	primary_therapy_outcome_success[],list,"Optional. Possible values include: 'Complete Remission/Response', 'No Measureable Tumor or Tumor Markers', 'Normalization of Tumor Markers, but Residual Tumor Mass', 'Partial Remission/Response', 'Persistent Disease', 'Progressive Disease', 'Stable Disease'."
	program_name[],list,"Optional. Possible values include: 'TCGA'."
	project_short_name[],list,"Optional. Possible values include: 'TCGA-ACC', 'TCGA-BLCA', 'TCGA-BRCA', 'TCGA-CESC', 'TCGA-CHOL', 'TCGA-COAD', 'TCGA-DLBC', 'TCGA-ESCA', 'TCGA-GBM', 'TCGA-HNSC', 'TCGA-KICH', 'TCGA-KIRC', 'TCGA-KIRP', 'TCGA-LAML', 'TCGA-LGG', 'TCGA-LIHC', 'TCGA-LUAD', 'TCGA-LUSC', 'TCGA-MESO', 'TCGA-OV', 'TCGA-PAAD', 'TCGA-PCPG', 'TCGA-PRAD', 'TCGA-READ', 'TCGA-SARC', 'TCGA-SKCM', 'TCGA-STAD', 'TCGA-TGCT', 'TCGA-THCA', 'TCGA-THYM', 'TCGA-UCEC', 'TCGA-UCS', 'TCGA-UVM'."
	psa_value[],list,"Optional. "
	psa_value_gte,number,"Optional. "
	psa_value_lte,number,"Optional. "
	race[],list,"Optional. Possible values include: 'AMERICAN INDIAN OR ALASKA NATIVE', 'ASIAN', 'BLACK OR AFRICAN AMERICAN', 'NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER', 'WHITE'."
	residual_tumor[],list,"Optional. Possible values include: 'R0', 'R1', 'R2', 'RX'."
	sample_barcode[],list,"Optional. "
	sample_gdc_id[],list,"Optional. "
	sample_type[],list,"Optional. Possible values include: '01', '02', '03', '05', '06', '07', '10', '11', '12', '14'."
	stopped_smoking_year[],list,"Optional. "
	stopped_smoking_year_gte,integer,"Optional. "
	stopped_smoking_year_lte,integer,"Optional. "
	summary_file_count[],list,"Optional. "
	summary_file_count_gte,integer,"Optional. "
	summary_file_count_lte,integer,"Optional. "
	tobacco_smoking_history[],list,"Optional. Possible values include: '1', '2', '3', '4', '5'."
	tss_code[],list,"Optional. "
	tumor_tissue_site[],list,"Optional. "
	tumor_type[],list,"Optional. Possible values include: 'Primary', 'Type 1', 'Type 2'."
	venous_invasion[],list,"Optional. Possible values include: 'NO', 'YES'."
	vital_status[],list,"Optional. Possible values include: 'Alive', 'Dead'."
	weight[],list,"Optional. "
	weight_gte,integer,"Optional. "
	weight_lte,integer,"Optional. "
	year_of_diagnosis[],list,"Optional. "
	year_of_diagnosis_gte,integer,"Optional. "
	year_of_diagnosis_lte,integer,"Optional. "
	year_of_tobacco_smoking_onset[],list,"Optional. "
	year_of_tobacco_smoking_onset_gte,integer,"Optional. "
	year_of_tobacco_smoking_onset_lte,integer,"Optional. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "case_count": integer,
    "filters": [
      {
        "name": string,
        "value": string
      }
    ],
    "id": string,
    "last_date_saved": string,
    "name": string,
    "sample_count": integer
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	case_count, integer, "Number of unique case barcodes in the cohort."
	filters[], list, "List of filters applied to create cohort, if any."
	filters[].name, string, "Names of filtering parameters used to create the cohort."
	filters[].value, string, "Values of filtering parameters used to create the cohort."
	id, string, "Cohort id."
	last_date_saved, string, "Last date the cohort was saved."
	name, string, "Name of cohort."
	sample_count, integer, "Number of unique sample barcodes in the cohort."
