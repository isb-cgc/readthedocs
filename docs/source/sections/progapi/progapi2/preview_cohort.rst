preview_cohort
##############
Takes a JSON object of filters in the request body and returns a "preview" of the cohort that would result from passing a similar request to the cohort **save** endpoint. This preview consists of two lists: the lists of participant (aka patient) barcodes, and the list of sample barcodes. Authentication is not required.

**Example**::

	$ curl "https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/preview_cohort" -d '{"Study": ["BRCA", "OV"]}' -H "Content-Type: application/json"

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/cohort_api/v1/cohort_api.cohort_endpoints.cohorts.preview_cohort?_h=7&resource=%257B%250A++%2522Study%2522%253A+%250A++%255B%2522CESC%2522%250A++%255D%252C%250A++%2522age_at_initial_pathologic_diagnosis_lte%2522%253A+%252230%2522%250A%257D&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	POST https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/preview_cohort

**Parameters**

None

Request body

In the request body, supply a metadata resource with the following properties:

.. code-block:: javascript

  {
    "age_at_initial_pathologic_diagnosis": [string],
    "age_at_initial_pathologic_diagnosis_gte": string,
    "age_at_initial_pathologic_diagnosis_lte": string,
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
    "batch_number": [string],
    "bcr": [string],
    "clinical_M": [string],
    "clinical_N": [string],
    "clinical_stage": [string],
    "clinical_T": [string],
    "colorectal_cancer": [string],
    "country": [string],
    "days_to_birth": [string],
    "days_to_birth_gte": string,
    "days_to_birth_lte": string,
    "days_to_collection": [string],
    "days_to_collection_gte": string,
    "days_to_collection_lte": string,
    "days_to_death": [string],
    "days_to_death_gte": string,
    "days_to_death_lte": string,
    "days_to_initial_pathologic_diagnosis": [string],
    "days_to_initial_pathologic_diagnosis_gte": string,
    "days_to_initial_pathologic_diagnosis_lte": string,
    "days_to_last_followup": [string],
    "days_to_last_followup_gte": string,
    "days_to_last_followup_lte": string,
    "days_to_submitted_specimen_dx": [string],
    "days_to_submitted_specimen_dx_gte": string,
    "days_to_submitted_specimen_dx_lte": string,
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
    "height_gte": string,
    "height_lte": string,
    "histological_type": [string],
    "history_of_colon_polyps": [string],
    "history_of_neoadjuvant_treatment": [string],
    "history_of_prior_malignancy": [string],
    "hpv_calls": [string],
    "hpv_status": [string],
    "icd_10": [string],
    "icd_o_3_histology": [string],
    "icd_o_3_site": [string],
    "lymphatic_invasion": [string],
    "lymphnodes_examined": [string],
    "lymphovascular_invasion_present": [string],
    "max_percent_lymphocyte_infiltration": [string],
    "max_percent_lymphocyte_infiltration_gte": string,
    "max_percent_lymphocyte_infiltration_lte": string,
    "max_percent_monocyte_infiltration": [string],
    "max_percent_monocyte_infiltration_gte": string,
    "max_percent_monocyte_infiltration_lte": string,
    "max_percent_necrosis": [string],
    "max_percent_necrosis_gte": string,
    "max_percent_necrosis_lte": string,
    "max_percent_neutrophil_infiltration": [string],
    "max_percent_neutrophil_infiltration_gte": string,
    "max_percent_neutrophil_infiltration_lte": string,
    "max_percent_normal_cells": [string],
    "max_percent_normal_cells_gte": string,
    "max_percent_normal_cells_lte": string,
    "max_percent_stromal_cells": [string],
    "max_percent_stromal_cells_gte": string,
    "max_percent_stromal_cells_lte": string,
    "max_percent_tumor_cells": [string],
    "max_percent_tumor_cells_gte": string,
    "max_percent_tumor_cells_lte": string,
    "max_percent_tumor_nuclei": [string],
    "max_percent_tumor_nuclei_gte": string,
    "max_percent_tumor_nuclei_lte": string,
    "menopause_status": [string],
    "min_percent_lymphocyte_infiltration": [string],
    "min_percent_lymphocyte_infiltration_gte": string,
    "min_percent_lymphocyte_infiltration_lte": string,
    "min_percent_monocyte_infiltration": [string],
    "min_percent_monocyte_infiltration_gte": string,
    "min_percent_monocyte_infiltration_lte": string,
    "min_percent_necrosis": [string],
    "min_percent_necrosis_gte": string,
    "min_percent_necrosis_lte": string,
    "min_percent_neutrophil_infiltration": [string],
    "min_percent_neutrophil_infiltration_gte": string,
    "min_percent_neutrophil_infiltration_lte": string,
    "min_percent_normal_cells": [string],
    "min_percent_normal_cells_gte": string,
    "min_percent_normal_cells_lte": string,
    "min_percent_stromal_cells": [string],
    "min_percent_stromal_cells_gte": string,
    "min_percent_stromal_cells_lte": string,
    "min_percent_tumor_cells": [string],
    "min_percent_tumor_cells_gte": string,
    "min_percent_tumor_cells_lte": string,
    "min_percent_tumor_nuclei": [string],
    "min_percent_tumor_nuclei_gte": string,
    "min_percent_tumor_nuclei_lte": string,
    "mononucleotide_and_dinucleotide_marker_panel_analysis_status": [string],
    "mononucleotide_marker_panel_analysis_status": [string],
    "neoplasm_histologic_grade": [string],
    "new_tumor_event_after_initial_treatment": [string],
    "number_of_lymphnodes_examined": [string],
    "number_of_lymphnodes_examined_gte": string,
    "number_of_lymphnodes_examined_lte": string,
    "number_of_lymphnodes_positive_by_he": [string],
    "number_of_lymphnodes_positive_by_he_gte": string,
    "number_of_lymphnodes_positive_by_he_lte": string,
    "ParticipantBarcode": [string],
    "pathologic_M": [string],
    "pathologic_N": [string],
    "pathologic_stage": [string],
    "pathologic_T": [string],
    "person_neoplasm_cancer_status": [string],
    "pregnancies": [string],
    "primary_neoplasm_melanoma_dx": [string],
    "primary_therapy_outcome_success": [string],
    "prior_dx": [string],
    "Project": [string],
    "psa_value": [number],
    "psa_value_gte": number,
    "psa_value_lte": number,
    "race": [string],
    "residual_tumor": [string],
    "SampleBarcode": [string],
    "SampleTypeCode": [string],
    "Study": [string],
    "tobacco_smoking_history": [string],
    "tumor_tissue_site": [string],
    "tumor_type": [string],
    "vital_status": [string],
    "weight": [string],
    "weight_gte": string,
    "weight_lte": string,
    "weiss_venous_invasion": [string],
    "year_of_initial_pathologic_diagnosis": [string],
    "year_of_initial_pathologic_diagnosis_gte": string,
    "year_of_initial_pathologic_diagnosis_lte": string
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	age_at_initial_pathologic_diagnosis[],list,"Optional. "
	age_at_initial_pathologic_diagnosis_gte,string,"Optional. "
	age_at_initial_pathologic_diagnosis_lte,string,"Optional. "
	anatomic_neoplasm_subdivision[],list,"Optional. Possible values include: 'Alveolar Ridge', 'Antrum/Distal', 'Ascending Colon', 'Base of tongue', 'Bilateral', 'Bladder - NOS', 'Body of Pancreas', 'Bronchial', 'Buccal Mucosa', 'Cardia/Proximal', 'Cecum', 'Descending Colon', 'Dome', 'Endometrium', 'Floor of mouth', 'Fundus uteri', 'Fundus/Body', 'Gastroesophageal Junction', 'Hard Palate', 'Head of Pancreas', 'Hepatic Flexure', 'Hypopharynx', 'L-Lower', 'L-Upper', 'Larynx', 'Left', 'Left Lower Inner Quadrant', 'Left Lower Outer Quadrant', 'Left Upper Inner Quadrant', 'Left Upper Outer Quadrant', 'Lip', 'Lower uterine segment/ Isthmus uteri', 'Myometrium', 'Neck', 'Oral Cavity', 'Oral Tongue', 'Oropharynx', 'Other (please specify)', 'R-Lower', 'R-Middle', 'R-Upper', 'Rectosigmoid Junction', 'Rectum', 'Right', 'Right Lower Inner Quadrant', 'Right Lower Outer Quadrant', 'Right Upper Inner Quadrant', 'Right Upper Outer Quadrant', 'Sigmoid Colon', 'Splenic Flexure', 'Stomach (NOS)', 'Tail of Pancreas', 'Tonsil', 'Transverse Colon', 'Trigone', 'Wall Anterior', 'Wall Lateral', 'Wall NOS', 'Wall Posterior'."
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
	bcr[],list,"Optional. Possible values include: 'Nationwide Children's Hospital', 'Washington University'."
	clinical_M[],list,"Optional. Possible values include: 'M0', 'M1', 'M1a', 'M1b', 'M1c', 'MX'."
	clinical_N[],list,"Optional. Possible values include: 'N0', 'N1', 'N2', 'N2a', 'N2b', 'N2c', 'N3', 'NX'."
	clinical_stage[],list,"Optional. Possible values include: 'Stage I', 'Stage IA', 'Stage IA1', 'Stage IA2', 'Stage IB', 'Stage IB1', 'Stage IB2', 'Stage IC', 'Stage II', 'Stage IIA', 'Stage IIA1', 'Stage IIA2', 'Stage IIB', 'Stage IIC', 'Stage III', 'Stage IIIA', 'Stage IIIB', 'Stage IIIC', 'Stage IIIC1', 'Stage IIIC2', 'Stage IS', 'Stage IV', 'Stage IVA', 'Stage IVB', 'Stage IVC'."
	clinical_T[],list,"Optional. Possible values include: 'T1', 'T1a', 'T1b', 'T1c', 'T2', 'T2a', 'T2b', 'T2c', 'T3', 'T3a', 'T3b', 'T4', 'T4a', 'T4b', 'T4c', 'T4d', 'T4e', 'TX'."
	colorectal_cancer[],list,"Optional. Possible values include: 'NO', 'YES'."
	country[],list,"Optional. Possible values include: 'Afghanistan', 'Algeria', 'American Samoa', 'Australia', 'Brazil', 'Bulgaria', 'Canada', 'Croatia', 'Czech Republic', 'France', 'Georgia', 'Germany', 'Israel', 'Italy', 'Korea South', 'Moldova', 'Netherlands', 'Nigeria', 'Pakistan', 'Poland', 'Puerto Rico', 'Romania', 'Russia', 'Singapore', 'Spain', 'Switzerland', 'Ukraine', 'United Kingdom', 'United States', 'Vietnam', 'Yemen'."
	days_to_birth[],list,"Optional. "
	days_to_birth_gte,string,"Optional. "
	days_to_birth_lte,string,"Optional. "
	days_to_collection[],list,"Optional. "
	days_to_collection_gte,string,"Optional. "
	days_to_collection_lte,string,"Optional. "
	days_to_death[],list,"Optional. "
	days_to_death_gte,string,"Optional. "
	days_to_death_lte,string,"Optional. "
	days_to_initial_pathologic_diagnosis[],list,"Optional. "
	days_to_initial_pathologic_diagnosis_gte,string,"Optional. "
	days_to_initial_pathologic_diagnosis_lte,string,"Optional. "
	days_to_last_followup[],list,"Optional. "
	days_to_last_followup_gte,string,"Optional. "
	days_to_last_followup_lte,string,"Optional. "
	days_to_submitted_specimen_dx[],list,"Optional. "
	days_to_submitted_specimen_dx_gte,string,"Optional. "
	days_to_submitted_specimen_dx_lte,string,"Optional. "
	ethnicity[],list,"Optional. Possible values include: 'HISPANIC OR LATINO', 'NOT HISPANIC OR LATINO'."
	frozen_specimen_anatomic_site[],list,"Optional. Possible values include: 'Alveolar Ridge', 'Antrum', 'Ascending Colon', 'Base of Tongue', 'Brain', 'Brain; Supratentorial', 'Breast', 'Buccal mucosa', 'Cardia; Proximal', 'Cecum', 'Colon', 'Descending Colon', 'Floor of Mouth', 'Fundus of Stomach', 'Gastroesophageal Junction', 'Hard Palate', 'Hepatic Flexure', 'Hypopharynx', 'Larynx', 'Lip', 'Lymph Node(s) Axilla', 'Lymph Node(s) Cervical', 'Lymph Node(s) Inguinal', 'Lymph Node(s) Mesenteric', 'Lymph Node(s) Submandibular', 'Lymph node(s) Mediastinal', 'Oral Cavity', 'Oropharynx', 'Other', 'Popliteal fossa', 'Prostate', 'Rectosigmoid Junction', 'Rectum', 'Sigmoid Colon', 'Small Intestine', 'Soft Tissue', 'Spinal Cord', 'Splenic Flexure', 'Stomach', 'Testicle', 'Tongue', 'Tonsil', 'Transverse Colon', 'Unknown'."
	gender[],list,"Optional. Possible values include: 'FEMALE', 'MALE', 'NA'."
	has_27k[],list,"Optional. Possible values include: '1', '0', 'None'."
	has_450k[],list,"Optional. Possible values include: '1', '0', 'None'."
	has_BCGSC_GA_RNASeq[],list,"Optional. Possible values include: '1', '0', 'None'."
	has_BCGSC_HiSeq_RNASeq[],list,"Optional. Possible values include: '1', '0', 'None'."
	has_GA_miRNASeq[],list,"Optional. Possible values include: '1', '0', 'None'."
	has_HiSeq_miRnaSeq[],list,"Optional. Possible values include: '1', '0', 'None'."
	has_Illumina_DNASeq[],list,"Optional. Possible values include: '1', '0', 'None'."
	has_RPPA[],list,"Optional. Possible values include: '1', '0', 'None'."
	has_SNP6[],list,"Optional. Possible values include: '1', '0', 'None'."
	has_UNC_GA_RNASeq[],list,"Optional. Possible values include: '1', '0', 'None'."
	has_UNC_HiSeq_RNASeq[],list,"Optional. Possible values include: '1', '0', 'None'."
	height[],list,"Optional. "
	height_gte,string,"Optional. "
	height_lte,string,"Optional. "
	histological_type[],list,"Optional. "
	history_of_colon_polyps[],list,"Optional. Possible values include: 'NO', 'YES'."
	history_of_neoadjuvant_treatment[],list,"Optional. Possible values include: 'No', 'Yes', 'Yes, Pharmaceutical Treatment Prior to Resection', 'Yes, Radiation Prior to Resection'."
	history_of_prior_malignancy[],list,"Optional. "
	hpv_calls[],list,"Optional. Possible values include: 'HPV16', 'HPV16;HPV18', 'HPV16;HPV18;HPV58', 'HPV16;HPV31', 'HPV16;HPV33', 'HPV16;HPV35', 'HPV16;HPV39', 'HPV16;HPV52', 'HPV16;HPV66', 'HPV18', 'HPV18;HPV31', 'HPV31', 'HPV33', 'HPV35', 'HPV39', 'HPV45', 'HPV51', 'HPV52', 'HPV56', 'HPV58', 'HPV59', 'HPV68', 'HPV73'."
	hpv_status[],list,"Optional. Possible values include: 'Indeterminate', 'Negative', 'Positive'."
	icd_10[],list,"Optional. "
	icd_o_3_histology[],list,"Optional. "
	icd_o_3_site[],list,"Optional. "
	lymphatic_invasion[],list,"Optional. Possible values include: 'NO', 'YES'."
	lymphnodes_examined[],list,"Optional. Possible values include: 'NO', 'YES'."
	lymphovascular_invasion_present[],list,"Optional. Possible values include: 'NO', 'YES'."
	max_percent_lymphocyte_infiltration[],list,"Optional. "
	max_percent_lymphocyte_infiltration_gte,string,"Optional. "
	max_percent_lymphocyte_infiltration_lte,string,"Optional. "
	max_percent_monocyte_infiltration[],list,"Optional. "
	max_percent_monocyte_infiltration_gte,string,"Optional. "
	max_percent_monocyte_infiltration_lte,string,"Optional. "
	max_percent_necrosis[],list,"Optional. "
	max_percent_necrosis_gte,string,"Optional. "
	max_percent_necrosis_lte,string,"Optional. "
	max_percent_neutrophil_infiltration[],list,"Optional. "
	max_percent_neutrophil_infiltration_gte,string,"Optional. "
	max_percent_neutrophil_infiltration_lte,string,"Optional. "
	max_percent_normal_cells[],list,"Optional. "
	max_percent_normal_cells_gte,string,"Optional. "
	max_percent_normal_cells_lte,string,"Optional. "
	max_percent_stromal_cells[],list,"Optional. "
	max_percent_stromal_cells_gte,string,"Optional. "
	max_percent_stromal_cells_lte,string,"Optional. "
	max_percent_tumor_cells[],list,"Optional. "
	max_percent_tumor_cells_gte,string,"Optional. "
	max_percent_tumor_cells_lte,string,"Optional. "
	max_percent_tumor_nuclei[],list,"Optional. "
	max_percent_tumor_nuclei_gte,string,"Optional. "
	max_percent_tumor_nuclei_lte,string,"Optional. "
	menopause_status[],list,"Optional. Possible values include: 'Indeterminate (neither Pre or Postmenopausal)', 'Peri (6-12 months since last menstrual period)', 'Post (prior bilateral ovariectomy OR >12 mo since LMP with n', 'Pre (<6 months since LMP AND no prior bilateral ovariectomy'."
	min_percent_lymphocyte_infiltration[],list,"Optional. "
	min_percent_lymphocyte_infiltration_gte,string,"Optional. "
	min_percent_lymphocyte_infiltration_lte,string,"Optional. "
	min_percent_monocyte_infiltration[],list,"Optional. "
	min_percent_monocyte_infiltration_gte,string,"Optional. "
	min_percent_monocyte_infiltration_lte,string,"Optional. "
	min_percent_necrosis[],list,"Optional. "
	min_percent_necrosis_gte,string,"Optional. "
	min_percent_necrosis_lte,string,"Optional. "
	min_percent_neutrophil_infiltration[],list,"Optional. "
	min_percent_neutrophil_infiltration_gte,string,"Optional. "
	min_percent_neutrophil_infiltration_lte,string,"Optional. "
	min_percent_normal_cells[],list,"Optional. "
	min_percent_normal_cells_gte,string,"Optional. "
	min_percent_normal_cells_lte,string,"Optional. "
	min_percent_stromal_cells[],list,"Optional. "
	min_percent_stromal_cells_gte,string,"Optional. "
	min_percent_stromal_cells_lte,string,"Optional. "
	min_percent_tumor_cells[],list,"Optional. "
	min_percent_tumor_cells_gte,string,"Optional. "
	min_percent_tumor_cells_lte,string,"Optional. "
	min_percent_tumor_nuclei[],list,"Optional. "
	min_percent_tumor_nuclei_gte,string,"Optional. "
	min_percent_tumor_nuclei_lte,string,"Optional. "
	mononucleotide_and_dinucleotide_marker_panel_analysis_status[],list,"Optional. Possible values include: 'Indeterminate', 'MSI-H', 'MSI-L', 'MSS', 'Not Tested'."
	mononucleotide_marker_panel_analysis_status[],list,"Optional. "
	neoplasm_histologic_grade[],list,"Optional. Possible values include: 'G1', 'G2', 'G3', 'G4', 'GB', 'GX', 'High Grade', 'Low Grade'."
	new_tumor_event_after_initial_treatment[],list,"Optional. Possible values include: 'NO', 'YES'."
	number_of_lymphnodes_examined[],list,"Optional. "
	number_of_lymphnodes_examined_gte,string,"Optional. "
	number_of_lymphnodes_examined_lte,string,"Optional. "
	number_of_lymphnodes_positive_by_he[],list,"Optional. "
	number_of_lymphnodes_positive_by_he_gte,string,"Optional. "
	number_of_lymphnodes_positive_by_he_lte,string,"Optional. "
	ParticipantBarcode[],list,"Optional. "
	pathologic_M[],list,"Optional. Possible values include: 'M0', 'M1', 'M1a', 'M1b', 'M1c', 'MX', 'cM0 (i+)'."
	pathologic_N[],list,"Optional. Possible values include: 'N0', 'N0 (i+)', 'N0 (i-)', 'N0 (mol+)', 'N1', 'N1a', 'N1b', 'N1c', 'N1mi', 'N2', 'N2a', 'N2b', 'N2c', 'N3', 'N3a', 'N3b', 'N3c', 'NX'."
	pathologic_stage[],list,"Optional. Possible values include: 'I or II NOS', 'Stage 0', 'Stage I', 'Stage IA', 'Stage IB', 'Stage II', 'Stage IIA', 'Stage IIB', 'Stage IIC', 'Stage III', 'Stage IIIA', 'Stage IIIB', 'Stage IIIC', 'Stage IS', 'Stage IV', 'Stage IVA', 'Stage IVB', 'Stage IVC', 'Stage X'."
	pathologic_T[],list,"Optional. Possible values include: 'T0', 'T1', 'T1a', 'T1a1', 'T1b', 'T1b1', 'T1b2', 'T1c', 'T2', 'T2a', 'T2a1', 'T2a2', 'T2b', 'T2c', 'T3', 'T3a', 'T3b', 'T3c', 'T4', 'T4a', 'T4b', 'T4c', 'T4d', 'T4e', 'TX', 'Tis'."
	person_neoplasm_cancer_status[],list,"Optional. Possible values include: 'TUMOR FREE', 'WITH TUMOR'."
	pregnancies[],list,"Optional. Possible values include: '0', '1', '2', '3', '4+'."
	primary_neoplasm_melanoma_dx[],list,"Optional. Possible values include: 'NO', 'YES'."
	primary_therapy_outcome_success[],list,"Optional. Possible values include: 'Complete Remission/Response', 'No Measureable Tumor or Tumor Markers', 'Normalization of Tumor Markers, but Residual Tumor Mass', 'Partial Remission/Response', 'Persistent Disease', 'Progressive Disease', 'Stable Disease'."
	prior_dx[],list,"Optional. Possible values include: 'No', 'Yes', 'Yes, History of Prior Malignancy', 'Yes, History of Synchronous and or Bilateral Malignancy', 'Yes, History of Synchronous/Bilateral Malignancy'."
	Project[],list,"Optional. Possible values include: 'CCLE', 'TCGA'."
	psa_value[],list,"Optional. "
	psa_value_gte,number,"Optional. "
	psa_value_lte,number,"Optional. "
	race[],list,"Optional. Possible values include: 'AMERICAN INDIAN OR ALASKA NATIVE', 'ASIAN', 'BLACK OR AFRICAN AMERICAN', 'NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER', 'WHITE'."
	residual_tumor[],list,"Optional. Possible values include: 'R0', 'R1', 'R2', 'RX'."
	SampleBarcode[],list,"Optional. "
	SampleTypeCode[],list,"Optional. "
	Study[],list,"Optional. Possible values include: 'ACC', 'BLCA', 'BRCA', 'CESC', 'CHOL', 'COAD', 'DLBC', 'ESCA', 'GBM', 'HNSC', 'KICH', 'KIRC', 'KIRP', 'LAML', 'LCLL', 'LGG', 'LIHC', 'LUAD', 'LUSC', 'MESO', 'MM', 'OV', 'PAAD', 'PCPG', 'PRAD', 'READ', 'SARC', 'SKCM', 'STAD', 'TGCT', 'THCA', 'THYM', 'UCEC', 'UCS', 'UVM'."
	tobacco_smoking_history[],list,"Optional. Possible values include: 'Current Reformed Smoker, Duration Not Specified', 'Current reformed smoker for < or = 15 years', 'Current reformed smoker for > 15 years', 'Current smoker', 'Lifelong Non-smoker'."
	tumor_tissue_site[],list,"Optional. "
	tumor_type[],list,"Optional. Possible values include: 'Primary', 'Type 1', 'Type 2'."
	vital_status[],list,"Optional. Possible values include: 'Alive', 'Dead'."
	weight[],list,"Optional. "
	weight_gte,string,"Optional. "
	weight_lte,string,"Optional. "
	weiss_venous_invasion[],list,"Optional. "
	year_of_initial_pathologic_diagnosis[],list,"Optional. "
	year_of_initial_pathologic_diagnosis_gte,string,"Optional. "
	year_of_initial_pathologic_diagnosis_lte,string,"Optional. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "cohort_id": string,
    "patient_count": string,
    "patients": [string],
    "sample_count": string,
    "samples": [string]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cohort_id, string, "ID of the cohort."
	patient_count, string, "Total count of unique patient barcodes in the cohort."
	patients[], list, "List of patient barcodes."
	sample_count, string, "Total count of unique sample barcodes in the cohort."
	samples[], list, "List of sample barcodes."
