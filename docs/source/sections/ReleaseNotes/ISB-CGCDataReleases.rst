############################
ISB-CGC Data Release Notes
############################

*August 2, 2021*

New study, case metadata, file metadata, clinical, project-level per-sample file, and protein abundance log2ratio (quant) tables added to isb-cgc-bq for PDC V1.21.

**BigQuery tables created**

- isb-cgc-bq.CBTTC_versioned.quant_phosphoproteome_pediatric_brain_cancer_pilot_study_pdc_V1_21
- isb-cgc-bq.CBTTC_versioned.quant_proteome_pediatric_brain_cancer_pilot_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.clinical_CPTAC3_other_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.clinical_proteogenomic_translational_research_centers_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_CPTAC2_other_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_CPTAC3_other_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_proteogenomic_translational_research_centers_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_acetylome_CPTAC_GBM_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_acetylome_CPTAC_LUAD_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_acetylome_CPTAC_UCEC_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_acetylome_prospective_breast_BI_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_glycoproteome_prospective_ovarian_JHU_N_linked_glycosite_containing_peptide_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_CPTAC_CCRCC_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_CPTAC_GBM_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_CPTAC_HNSCC_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_CPTAC_LUAD_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_CPTAC_UCEC_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_prospective_breast_BI_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_prospective_colon_PNNL_lumos_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_prospective_ovarian_PNNL_lumos_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_CCRCC_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_GBM_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_HNSCC_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_LUAD_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_UCEC_discovery_study_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_breast_BI_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_colon_PNNL_qeplus_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_ovarian_JHU_pdc_V1_21
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_ovarian_PNNL_qeplus_pdc_V1_21
- isb-cgc-bq.ICPC_versioned.quant_phosphoproteome_HBV_related_hepatocellular_carcinoma_pdc_V1_21
- isb-cgc-bq.ICPC_versioned.quant_phosphoproteome_proteogenomics_of_gastric_cancer_pdc_V1_21
- isb-cgc-bq.ICPC_versioned.quant_proteome_HBV_related_hepatocellular_carcinoma_pdc_V1_21
- isb-cgc-bq.ICPC_versioned.quant_proteome_proteogenomics_of_gastric_cancer_pdc_V1_21
- isb-cgc-bq.PDC_metadata_versioned.aliquot_to_case_mapping_V1_21
- isb-cgc-bq.PDC_metadata_versioned.case_metadata_V1_21
- isb-cgc-bq.PDC_metadata_versioned.file_associated_entity_mapping_V1_21
- isb-cgc-bq.PDC_metadata_versioned.file_metadata_V1_21
- isb-cgc-bq.PDC_metadata_versioned.gene_info_V1_21
- isb-cgc-bq.PDC_metadata_versioned.studies_V1_21
- isb-cgc-bq.TCGA_versioned.clinical_CPTAC_TCGA_pdc_V1_21
- isb-cgc-bq.TCGA_versioned.quant_phosphoproteome_TCGA_breast_cancer_pdc_V1_21
- isb-cgc-bq.TCGA_versioned.quant_phosphoproteome_TCGA_ovarian_PNNL_velos_qexactive_pdc_V1_21
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_breast_cancer_pdc_V1_21
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_ovarian_JHU_pdc_V1_21
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_ovarian_PNNL_pdc_V1_21


**BigQuery tables updated**

- isb-cgc-bq.CBTTC.quant_phosphoproteome_pediatric_brain_cancer_pilot_study_pdc_current
- isb-cgc-bq.CBTTC.quant_proteome_pediatric_brain_cancer_pilot_study_pdc_current
- isb-cgc-bq.CPTAC.clinical_CPTAC3_other_pdc_current
- isb-cgc-bq.CPTAC.clinical_proteogenomic_translational_research_centers_pdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_CPTAC2_other_pdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_CPTAC3_other_pdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_proteogenomic_translational_research_centers_pdc_current
- isb-cgc-bq.CPTAC.quant_acetylome_CPTAC_GBM_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_acetylome_CPTAC_LUAD_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_acetylome_CPTAC_UCEC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_acetylome_prospective_breast_BI_pdc_current
- isb-cgc-bq.CPTAC.quant_glycoproteome_prospective_ovarian_JHU_N_linked_glycosite_containing_peptide_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_CPTAC_CCRCC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_CPTAC_GBM_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_CPTAC_HNSCC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_CPTAC_LUAD_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_CPTAC_UCEC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_prospective_breast_BI_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_prospective_colon_PNNL_lumos_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_prospective_ovarian_PNNL_lumos_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_CCRCC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_GBM_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_HNSCC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_LUAD_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_UCEC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_breast_BI_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_colon_PNNL_qeplus_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_ovarian_JHU_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_ovarian_PNNL_qeplus_pdc_current
- isb-cgc-bq.ICPC.quant_phosphoproteome_HBV_related_hepatocellular_carcinoma_pdc_current
- isb-cgc-bq.ICPC.quant_phosphoproteome_proteogenomics_of_gastric_cancer_pdc_current
- isb-cgc-bq.ICPC.quant_proteome_HBV_related_hepatocellular_carcinoma_pdc_current
- isb-cgc-bq.ICPC.quant_proteome_proteogenomics_of_gastric_cancer_pdc_current
- isb-cgc-bq.PDC_metadata.aliquot_to_case_mapping_current
- isb-cgc-bq.PDC_metadata.case_metadata_current
- isb-cgc-bq.PDC_metadata.file_associated_entity_mapping_current
- isb-cgc-bq.PDC_metadata.file_metadata_current
- isb-cgc-bq.PDC_metadata.gene_info_current
- isb-cgc-bq.PDC_metadata.studies_current
- isb-cgc-bq.TCGA.clinical_CPTAC_TCGA_pdc_current
- isb-cgc-bq.TCGA.quant_phosphoproteome_TCGA_breast_cancer_pdc_current
- isb-cgc-bq.TCGA.quant_phosphoproteome_TCGA_ovarian_PNNL_velos_qexactive_pdc_current
- isb-cgc-bq.TCGA.quant_proteome_TCGA_breast_cancer_pdc_current
- isb-cgc-bq.TCGA.quant_proteome_TCGA_ovarian_JHU_pdc_current
- isb-cgc-bq.TCGA.quant_proteome_TCGA_ovarian_PNNL_pdc_current


*July 14, 2021*

Added release 28 miRNAseq isoform table for CPTAC

**BigQuery tables created**

- isb-cgc-bq.CPTAC_versioned.miRNAseq_isoform_hg38_gdc_r28
- isb-cgc-bq.CPTAC.miRNAseq_isoform_hg38_gdc_current

*June 21, 2021*

Updated the release 28 CPTAC miRNAseq tables to include the sample_type_name field

**BigQuery tables created**

- isb-cgc-bq.CPTAC_versioned.miRNAseq_hg38_gdc_r28_v2

**BigQuery tables updated**

- isb-cgc-bq.CPTAC.miRNAseq_hg38_gdc_current

*June 18, 2021*

New study, case metadata, file metadata, clinical, project-level per-sample file, and protein abundance log2ratio (quant) tables added to isb-cgc-bq for PDC V1.19.

**BigQuery tables created**

- isb-cgc-bq.CBTTC_versioned.quant_proteome_pediatric_brain_cancer_pilot_study_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.clinical_CPTAC2_other_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.clinical_CPTAC3_other_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.quant_glycoproteome_prospective_ovarian_JHU_N_linked_glycosite_containing_peptide_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_CCRCC_discovery_study_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_GBM_discovery_study_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_HNSCC_discovery_study_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_LUAD_discovery_study_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_UCEC_discovery_study_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_breast_BI_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_colon_PNNL_qeplus_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_ovarian_JHU_pdc_V1_19
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_ovarian_PNNL_qeplus_pdc_V1_19
- isb-cgc-bq.ICPC_versioned.quant_proteome_HBV_related_hepatocellular_carcinoma_pdc_V1_19
- isb-cgc-bq.ICPC_versioned.quant_proteome_proteogenomics_of_gastric_cancer_pdc_V1_19
- isb-cgc-bq.PDC_metadata_versioned.aliquot_to_case_mapping_V1_19
- isb-cgc-bq.PDC_metadata_versioned.case_metadata_V1_19
- isb-cgc-bq.PDC_metadata_versioned.file_associated_entity_mapping_V1_19
- isb-cgc-bq.PDC_metadata_versioned.file_metadata_V1_19
- isb-cgc-bq.PDC_metadata_versioned.gene_info_V1_19
- isb-cgc-bq.PDC_metadata_versioned.refseq_mapping_2021_03
- isb-cgc-bq.PDC_metadata_versioned.studies_V1_19
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_breast_cancer_pdc_V1_19
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_ovarian_JHU_pdc_V1_19
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_ovarian_PNNL_pdc_V1_19

**BigQuery tables updated**

- isb-cgc-bq.CBTTC.quant_proteome_pediatric_brain_cancer_pilot_study_pdc_current
- isb-cgc-bq.CPTAC.clinical_CPTAC2_other_pdc_current
- isb-cgc-bq.CPTAC.clinical_CPTAC3_other_pdc_current
- isb-cgc-bq.CPTAC.quant_glycoproteome_prospective_ovarian_JHU_N_linked_glycosite_containing_peptide_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_CCRCC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_GBM_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_HNSCC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_LUAD_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_UCEC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_breast_BI_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_colon_PNNL_qeplus_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_ovarian_JHU_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_ovarian_PNNL_qeplus_pdc_current
- isb-cgc-bq.ICPC.quant_proteome_HBV_related_hepatocellular_carcinoma_pdc_current
- isb-cgc-bq.ICPC.quant_proteome_proteogenomics_of_gastric_cancer_pdc_current
- isb-cgc-bq.PDC_metadata.aliquot_to_case_mapping_current
- isb-cgc-bq.PDC_metadata.case_metadata_current
- isb-cgc-bq.PDC_metadata.file_associated_entity_mapping_current
- isb-cgc-bq.PDC_metadata.file_metadata_current
- isb-cgc-bq.PDC_metadata.gene_info_current
- isb-cgc-bq.PDC_metadata.refseq_mapping_current
- isb-cgc-bq.PDC_metadata.studies_current
- isb-cgc-bq.TCGA.quant_proteome_TCGA_breast_cancer_pdc_current
- isb-cgc-bq.TCGA.quant_proteome_TCGA_ovarian_JHU_pdc_current
- isb-cgc-bq.TCGA.quant_proteome_TCGA_ovarian_PNNL_pdc_current

*June 10, 2021*

New study and project-level per sample file metadata tables added to isb-cgc-bq for PDC V1.17.

**BigQuery tables created**

- isb-cgc-bq.PDC_metadata_versioned.studies_V1_17
- isb-cgc-bq.CBTTC_versioned.per_sample_file_metadata_pediatric_brain_cancer_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_CPTAC_2_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_CPTAC2_other_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_CPTAC3_discovery_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_CPTAC3_other_pdc_V1_17
- isb-cgc-bq.GPRP_versioned.per_sample_file_metadata_georgetown_lung_cancer_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.per_sample_file_metadata_academia_sinica_LUAD_100_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.per_sample_file_metadata_HBV_related_hepatocellular_carcinoma_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.per_sample_file_metadata_human_early_onset_gastric_cancer_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.per_sample_file_metadata_oral_squamous_cell_carcinoma_pdc_V1_17
- isb-cgc-bq.Quant_Maps_Tissue_Biopsies_versioned.per_sample_file_metadata_pct_swath_kidney_pdc_V1_17
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_CPTAC_TCGA_pdc_V1_17
- isb-cgc-bq.PDC_metadata.studies_current
- isb-cgc-bq.CBTTC.per_sample_file_metadata_pediatric_brain_cancer_pdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_CPTAC_2_pdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_CPTAC2_other_pdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_CPTAC3_discovery_pdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_CPTAC3_other_pdc_current
- isb-cgc-bq.GPRP.per_sample_file_metadata_georgetown_lung_cancer_pdc_current
- isb-cgc-bq.ICPC.per_sample_file_metadata_academia_sinica_LUAD_100_pdc_current
- isb-cgc-bq.ICPC.per_sample_file_metadata_HBV_related_hepatocellular_carcinoma_pdc_current
- isb-cgc-bq.ICPC.per_sample_file_metadata_human_early_onset_gastric_cancer_pdc_current
- isb-cgc-bq.ICPC.per_sample_file_metadata_oral_squamous_cell_carcinoma_pdc_current
- isb-cgc-bq.Quant_Maps_Tissue_Biopsies.per_sample_file_metadata_pct_swath_kidney_pdc_current
- isb-cgc-bq.TCGA.per_sample_file_metadata_CPTAC_TCGA_pdc_current

*May 28, 2021*

New  per sample file metadata added to isb-cgc-bq for GDC release 29.

**BigQuery tables created**

- isb-cgc-bq.CMI_versioned.per_sample_file_metadata_hg38_gdc_r29
- isb-cgc-bq.CGCI_versioned.per_sample_file_metadata_hg38_gdc_r29
- isb-cgc-bq.HCMI_versioned.per_sample_file_metadata_hg38_gdc_r29
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_hg38_gdc_r29
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_hg38_gdc_r29
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_hg19_gdc_r29

Current per sample file metadata tables updated to GDC release 29.

**BigQuery tables updated**

- isb-cgc-bq.CMI.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CGCI.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.HCMI.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.TCGA.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.TCGA.per_sample_file_metadata_hg19_gdc_current

*May 27, 2021*

New controlled-access VCF tables.

**BigQuery tables created**

- isb-cgc-cbq.VAREPOP_versioned.vcf_hg38_gdc_r24
- isb-cgc-cbq.VAREPOP.vcf_hg38_gdc_current
- isb-cgc-cbq.TCGA_versioned.vcf_hg38_gdc_r24
- isb-cgc-cbq.TCGA.vcf_hg38_gdc_current
- isb-cgc-cbq.ORGANOID_versioned.vcf_hg38_gdc_r24
- isb-cgc-cbq.ORGANOID.vcf_hg38_gdc_current
- isb-cgc-cbq.MMRF_versioned.vcf_hg38_gdc_r24
- isb-cgc-cbq.MMRF.vcf_hg38_gdc_current
- isb-cgc-cbq.HCMI_versioned.vcf_hg38_gdc_r24
- isb-cgc-cbq.HCMI.vcf_hg38_gdc_current
- isb-cgc-cbq.FM_versioned.vcf_hg38_gdc_r24
- isb-cgc-cbq.FM.vcf_hg38_gdc_current

*May 26, 2021*

New case metadata, file metadata, clinical, and quant data (for actylome, glycoproteome, phosphoproteome, and proteome) 
added to isb-cgc-bq from PDC V1.17.

**BigQuery tables created**

- isb-cgc-bq.CBTTC_versioned.clinical_diagnoses_pediatric_brain_cancer_pdc_V1_17
- isb-cgc-bq.CBTTC_versioned.clinical_pediatric_brain_cancer_pdc_V1_17
- isb-cgc-bq.CBTTC_versioned.quant_phosphoproteome_pediatric_brain_cancer_pilot_study_pdc_V1_17
- isb-cgc-bq.CBTTC_versioned.quant_proteome_pediatric_brain_cancer_pilot_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.clinical_CPTAC_2_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.clinical_CPTAC2_other_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.clinical_CPTAC3_discovery_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.clinical_CPTAC3_other_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_acetylome_CPTAC_GBM_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_acetylome_CPTAC_LUAD_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_acetylome_CPTAC_UCEC_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_acetylome_prospective_breast_BI_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_glycoproteome_prospective_ovarian_JHU_n_linked_glycosite_containing_peptide_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_CPTAC_CCRCC_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_CPTAC_GBM_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_CPTAC_HNSCC_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_CPTAC_LUAD_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_CPTAC_UCEC_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_prospective_breast_BI_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_prospective_colon_PNNL_lumos_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_phosphoproteome_prospective_ovarian_PNNL_lumos_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_CCRCC_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_GBM_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_HNSCC_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_LUAD_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_UCEC_discovery_study_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_breast_BI_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_colon_PNNL_qeplus_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_ovarian_JHU_pdc_V1_17
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_ovarian_PNNL_qeplus_pdc_V1_17
- isb-cgc-bq.GPRP_versioned.clinical_georgetown_lung_cancer_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.clinical_academia_sinica_LUAD_100_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.clinical_HBV_related_hepatocellular_carcinoma_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.clinical_human_early_onset_gastric_cancer_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.clinical_oral_squamous_cell_carcinoma_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.quant_phosphoproteome_HBV_related_hepatocellular_carcinoma_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.quant_phosphoproteome_proteogenomics_of_gastric_cancer_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.quant_proteome_HBV_related_hepatocellular_carcinoma_pdc_V1_17
- isb-cgc-bq.ICPC_versioned.quant_proteome_proteogenomics_of_gastric_cancer_pdc_V1_17
- isb-cgc-bq.PDC_metadata_versioned.aliquot_to_case_mapping_V1_17
- isb-cgc-bq.PDC_metadata_versioned.case_metadata_V1_17
- isb-cgc-bq.PDC_metadata_versioned.file_associated_entity_mapping_V1_17
- isb-cgc-bq.PDC_metadata_versioned.file_metadata_V1_17
- isb-cgc-bq.PDC_metadata_versioned.gene_info_V1_17
- isb-cgc-bq.PDC_metadata_versioned.refseq_mapping_2021_02
- isb-cgc-bq.Quant_Maps_Tissue_Biopsies_versioned.clinical_pct_swath_kidney_pdc_V1_17
- isb-cgc-bq.TCGA_versioned.clinical_CPTAC_TCGA_pdc_V1_17
- isb-cgc-bq.TCGA_versioned.quant_phosphoproteome_TCGA_breast_cancer_pdc_V1_17
- isb-cgc-bq.TCGA_versioned.quant_phosphoproteome_TCGA_ovarian_PNNL_velos_qexactive_pdc_V1_17
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_breast_cancer_pdc_V1_17
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_ovarian_JHU_pdc_V1_17
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_ovarian_PNNL_pdc_V1_17

- isb-cgc-bq.CBTTC.quant_phosphoproteome_pediatric_brain_cancer_pilot_study_pdc_current
- isb-cgc-bq.CPTAC.clinical_CPTAC2_other_pdc_current
- isb-cgc-bq.CPTAC.clinical_CPTAC3_other_pdc_current
- isb-cgc-bq.CPTAC.quant_acetylome_CPTAC_GBM_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_acetylome_CPTAC_LUAD_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_acetylome_CPTAC_UCEC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_acetylome_prospective_breast_BI_pdc_current
- isb-cgc-bq.CPTAC.quant_glycoproteome_prospective_ovarian_JHU_n_linked_glycosite_containing_peptide_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_CPTAC_CCRCC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_CPTAC_GBM_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_CPTAC_HNSCC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_CPTAC_LUAD_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_CPTAC_UCEC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_prospective_breast_BI_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_prospective_colon_PNNL_lumos_pdc_current
- isb-cgc-bq.CPTAC.quant_phosphoproteome_prospective_ovarian_PNNL_lumos_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_GBM_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_HNSCC_discovery_study_pdc_current
- isb-cgc-bq.ICPC.quant_phosphoproteome_HBV_related_hepatocellular_carcinoma_pdc_current
- isb-cgc-bq.ICPC.quant_phosphoproteome_proteogenomics_of_gastric_cancer_pdc_current
- isb-cgc-bq.PDC_metadata.gene_info_current
- isb-cgc-bq.PDC_metadata.refseq_mapping_current
- isb-cgc-bq.TCGA.quant_phosphoproteome_TCGA_breast_cancer_pdc_current
- isb-cgc-bq.TCGA.quant_phosphoproteome_TCGA_ovarian_PNNL_velos_qexactive_pdc_current

**BigQuery tables updated**

- isb-cgc-bq.CBTTC.clinical_diagnoses_pediatric_brain_cancer_pdc_current
- isb-cgc-bq.CBTTC.clinical_pediatric_brain_cancer_pdc_current
- isb-cgc-bq.CBTTC.quant_proteome_pediatric_brain_cancer_pilot_study_pdc_current
- isb-cgc-bq.CPTAC.clinical_CPTAC_2_pdc_current
- isb-cgc-bq.CPTAC.clinical_CPTAC3_discovery_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_CCRCC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_LUAD_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_UCEC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_breast_BI_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_colon_PNNL_qeplus_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_ovarian_JHU_pdc_current
- isb-cgc-bq.CPTAC.quant_proteome_prospective_ovarian_PNNL_qeplus_pdc_current
- isb-cgc-bq.GPRP.clinical_georgetown_lung_cancer_pdc_current
- isb-cgc-bq.ICPC.clinical_academia_sinica_LUAD_100_pdc_current
- isb-cgc-bq.ICPC.clinical_HBV_related_hepatocellular_carcinoma_pdc_current
- isb-cgc-bq.ICPC.clinical_human_early_onset_gastric_cancer_pdc_current
- isb-cgc-bq.ICPC.clinical_oral_squamous_cell_carcinoma_pdc_current
- isb-cgc-bq.ICPC.quant_proteome_HBV_related_hepatocellular_carcinoma_pdc_current
- isb-cgc-bq.ICPC.quant_proteome_proteogenomics_of_gastric_cancer_pdc_current
- isb-cgc-bq.PDC_metadata.aliquot_to_case_mapping_current
- isb-cgc-bq.PDC_metadata.case_metadata_current
- isb-cgc-bq.PDC_metadata.file_associated_entity_mapping_current
- isb-cgc-bq.PDC_metadata.file_metadata_current
- isb-cgc-bq.Quant_Maps_Tissue_Biopsies.clinical_pct_swath_kidney_pdc_current
- isb-cgc-bq.TCGA.clinical_CPTAC_TCGA_pdc_current
- isb-cgc-bq.TCGA.quant_proteome_TCGA_breast_cancer_pdc_current
- isb-cgc-bq.TCGA.quant_proteome_TCGA_ovarian_JHU_pdc_current
- isb-cgc-bq.TCGA.quant_proteome_TCGA_ovarian_PNNL_pdc_current

New CPTAC controlled-access VCF tables.

**BigQuery tables created**

- isb-cgc-cbq.CPTAC3_versioned.vcf_hg38_gdc_r24
- isb-cgc-cbq.CPTAC3.vcf_hg38_gdc_current
- isb-cgc-cbq.CPTAC2_versioned.vcf_hg38_gdc_r24
- isb-cgc-cbq.CPTAC2.vcf_hg38_gdc_current

*May 24, 2021*

New CPTAC RNA Seq table added to isb-cgc-bq for GDC release 28.

**BigQuery tables created**

- isb-cgc-bq.CPTAC_versioned.RNAseq_hg38_gdc_r28

**BigQuery tables updated**

- isb-cgc-bq.CPTAC.RNAseq_hg38_gdc_current

*May 21, 2021*

New clinical tables added to isb-cgc-bq for GDC release 29.

**BigQuery tables created**

- isb-cgc-bq.BEATAML1_0_versioned.clinical_gdc_r29
- isb-cgc-bq.CGCI_versioned.clinical_gdc_r29
- isb-cgc-bq.CGCI_versioned.clinical_diagnoses_gdc_r29
- isb-cgc-bq.CGCI_versioned.clinical_diagnoses_treatments_gdc_r29
- isb-cgc-bq.CGCI_versioned.clinical_follow_ups_gdc_r29
- isb-cgc-bq.CGCI_versioned.clinical_follow_ups_molecular_tests_gdc_r29
- isb-cgc-bq.CMI_versioned.clinical_gdc_r29
- isb-cgc-bq.CPTAC_versioned.clinical_gdc_r29
- isb-cgc-bq.CTSP_versioned.clinical_gdc_r29
- isb-cgc-bq.FM_versioned.clinical_gdc_r29
- isb-cgc-bq.GENIE_versioned.clinical_gdc_r29
- isb-cgc-bq.HCMI_versioned.clinical_gdc_r29
- isb-cgc-bq.HCMI_versioned.clinical_diagnoses_gdc_r29
- isb-cgc-bq.HCMI_versioned.clinical_diagnoses_treatments_gdc_r29
- isb-cgc-bq.HCMI_versioned.clinical_follow_ups_gdc_r29
- isb-cgc-bq.HCMI_versioned.clinical_follow_ups_molecular_tests_gdc_r29
- isb-cgc-bq.MMRF_versioned.clinical_gdc_r29
- isb-cgc-bq.MMRF_versioned.clinical_diagnoses_treatments_gdc_r29
- isb-cgc-bq.MMRF_versioned.clinical_family_histories_gdc_r29
- isb-cgc-bq.MMRF_versioned.clinical_follow_ups_gdc_r29
- isb-cgc-bq.MMRF_versioned.clinical_follow_ups_molecular_tests_gdc_r29
- isb-cgc-bq.NCICCR_versioned.clinical_gdc_r29
- isb-cgc-bq.OHSU_versioned.clinical_gdc_r29
- isb-cgc-bq.ORGANOID_versioned.clinical_gdc_r29
- isb-cgc-bq.TARGET_versioned.clinical_gdc_r29
- isb-cgc-bq.TCGA_versioned.clinical_gdc_r29
- isb-cgc-bq.TCGA_versioned.clinical_diagnoses_treatments_gdc_r29
- isb-cgc-bq.VAREPOP_versioned.clinical_gdc_r29
- isb-cgc-bq.VAREPOP_versioned.clinical_diagnoses_treatments_gdc_r29
- isb-cgc-bq.VAREPOP_versioned.clinical_family_histories_gdc_r29
- isb-cgc-bq.WCDT_versioned.clinical_gdc_r29

Current clinical tables updated to GDC release 29.

**BigQuery tables updated**

- isb-cgc-bq.BEATAML1_0.clinical_gdc_current
- isb-cgc-bq.CGCI.clinical_gdc_current
- isb-cgc-bq.CGCI.clinical_diagnoses_gdc_current
- isb-cgc-bq.CGCI.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.CGCI.clinical_follow_ups_gdc_current
- isb-cgc-bq.CGCI.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq.CMI.clinical_gdc_current
- isb-cgc-bq.CPTAC.clinical_gdc_current
- isb-cgc-bq.CTSP.clinical_gdc_current
- isb-cgc-bq.FM.clinical_gdc_current
- isb-cgc-bq.GENIE.clinical_gdc_current
- isb-cgc-bq.HCMI.clinical_gdc_current
- isb-cgc-bq.HCMI.clinical_diagnoses_gdc_current
- isb-cgc-bq.HCMI.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.HCMI.clinical_follow_ups_gdc_current
- isb-cgc-bq.HCMI.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq.MMRF.clinical_gdc_current
- isb-cgc-bq.MMRF.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.MMRF.clinical_family_histories_gdc_current
- isb-cgc-bq.MMRF.clinical_follow_ups_gdc_current
- isb-cgc-bq.MMRF.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq.NCICCR.clinical_gdc_current
- isb-cgc-bq.OHSU.clinical_gdc_current
- isb-cgc-bq.ORGANOID.clinical_gdc_current
- isb-cgc-bq.TARGET.clinical_gdc_current
- isb-cgc-bq.TCGA.clinical_gdc_current
- isb-cgc-bq.TCGA.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.VAREPOP.clinical_gdc_current
- isb-cgc-bq.VAREPOP.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.VAREPOP.clinical_family_histories_gdc_current
- isb-cgc-bq.WCDT.clinical_gdc_current

*May 18, 2021*

New file metadata tables added to isb-cgc-bq for GDC release 29 and New GENCODE annotation tables.

**BigQuery tables created**

- isb-cgc-bq.GDC_case_file_metadata_versioned.GDCfileID_to_GCSurl_r29
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_legacy_r29
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_active_r29
- isb-cgc-bq.GDC_case_file_metadata_versioned.caseData_r29
- isb-cgc-bq.GDC_case_file_metadata_versioned.aliquot2caseIDmap_r29
- isb-cgc-bq.GDC_case_file_metadata_versioned.slide2caseIDmap_r29
- isb-cgc-bq.GENCODE_versioned.annotation_gtf_hg38_v38

**BigQuery tables updated**

- isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_legacy_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_active_current
- isb-cgc-bq.GDC_case_file_metadata.caseData_current
- isb-cgc-bq.GDC_case_file_metadata.aliquot2caseIDmap_current
- isb-cgc-bq.GDC_case_file_metadata.slide2caseIDmap_current
- isb-cgc-bq.GENCODE.annotation_gtf_hg38_current

*April 14, 2021*

New PDC Aliquot and Case Metadata tables.

**BigQuery tables created**

- isb-cgc-bq.PDC_metadata.aliquot_to_case_mapping_pdc_current
- isb-cgc-bq.PDC_metadata_versioned.aliquot_to_case_mapping_pdc_V1_11
- isb-cgc-bq.PDC_metadata.case_metadata_pdc_current
- isb-cgc-bq.PDC_metadata_versioned.case_metadata_pdc_V1_11

*April 2, 2021*

New GENCODE annotation tables.

**BigQuery tables created**

- isb-cgc-bq.GENCODE_versioned.annotation_gtf_hg38_v36
- isb-cgc-bq.GENCODE_versioned.annotation_gtf_hg38_v37

**BigQuery tables updated**

- isb-cgc-bq.GENCODE.annotation_gtf_hg38_current

*March 30, 2021*

New CPTAC miRNA expression tables.

**BigQuery tables created**

- isb-cgc-bq.CPTAC.miRNAseq_hg38_gdc_current
- isb-cgc-bq.CPTAC_versioned.miRNAseq_hg38_gdc_r28

*March 22, 2021*

New TARGET miRNA isoform expression tables.

**BigQuery tables created**

- isb-cgc-bq.TARGET_versioned.miRNAseq_isoform_hg38_gdc_r25

**BigQuery tables updated**

- isb-cgc-bq.TARGET.miRNAseq_isoform_hg38_gdc_current

*March 17, 2021*

New  HCMI RNA Seq table

**BigQuery tables created**

- isb-cgc-bq.HCMI_versioned.RNAseq_hg38_gdc_r28

**BigQuery tables updated**

- isb-cgc-bq.HCMI.RNAseq_hg38_gdc_current

*March 11, 2021*

New  HCMI Masked Somatic Mutation table

**BigQuery tables created**

- isb-cgc-bq.HCMI_versioned.masked_somatic_mutation_hg38_gdc_r28

**BigQuery tables updated**

- isb-cgc-bq.HCMI.masked_somatic_mutation_hg38_gdc_current

*March 5, 2021*

New file metadata, per sample file metadata, and clinical tables added to isb-cgc-bq for GDC release 28.

**BigQuery tables created**

- isb-cgc-bq.CMI_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.WCDT_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.GENIE_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.OHSU_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.FM_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.VAREPOP_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.CTSP_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.NCICCR_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.ORGANOID_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.MMRF_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.CGCI_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.HCMI_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.BEATAML1_0_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.TARGET_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_hg38_gdc_r28
- isb-cgc-bq.CCLE_versioned.per_sample_file_metadata_hg19_gdc_r28
- isb-cgc-bq.TARGET_versioned.per_sample_file_metadata_hg19_gdc_r28
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_hg19_gdc_r28
- isb-cgc-bq.GDC_case_file_metadata_versioned.GDCfileID_to_GCSurl_r28
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_legacy_r28
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_active_r28
- isb-cgc-bq.GDC_case_file_metadata_versioned.caseData_r28
- isb-cgc-bq.GDC_case_file_metadata_versioned.aliquot2caseIDmap_r28
- isb-cgc-bq.GDC_case_file_metadata_versioned.slide2caseIDmap_r28
- isb-cgc-bq.HCMI_versioned.clinical_follow_ups_molecular_tests_gdc_r28
- isb-cgc-bq.HCMI_versioned.clinical_diagnoses_treatments_gdc_r28
- isb-cgc-bq.HCMI_versioned.clinical_diagnoses_gdc_r28
- isb-cgc-bq.CPTAC_versioned.clinical_gdc_r28
- isb-cgc-bq.HCMI_versioned.clinical_gdc_r28
- isb-cgc-bq.CMI_versioned.clinical_gdc_r28
- isb-cgc-bq.HCMI_versioned.clinical_follow_ups_gdc_r28

Current file metadata, per sample file metadata, and clinical tables updated to GDC release 28.

**BigQuery tables updated**

- isb-cgc-bq.CMI.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.WCDT.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.GENIE.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.OHSU.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.FM.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.VAREPOP.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CTSP.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.NCICCR.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.ORGANOID.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.MMRF.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CGCI.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.BEATAML1_0.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.TARGET.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.TCGA.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CCLE.per_sample_file_metadata_hg19_gdc_current
- isb-cgc-bq.TARGET.per_sample_file_metadata_hg19_gdc_current
- isb-cgc-bq.TCGA.per_sample_file_metadata_hg19_gdc_current
- isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_legacy_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_active_current
- isb-cgc-bq.GDC_case_file_metadata.caseData_current
- isb-cgc-bq.GDC_case_file_metadata.aliquot2caseIDmap_current
- isb-cgc-bq.GDC_case_file_metadata.slide2caseIDmap_current
- isb-cgc-bq.HCMI.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq.HCMI.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.HCMI.clinical_diagnoses_gdc_current
- isb-cgc-bq.CPTAC.clinical_gdc_current
- isb-cgc-bq.HCMI.clinical_gdc_current
- isb-cgc-bq.CMI.clinical_gdc_current
- isb-cgc-bq.HCMI.clinical_follow_ups_gdc_current

*March 3, 2021*

PDC metadata

- isb-cgc-bq.PDC_metadata.file_associated_entity_mapping_current
- isb-cgc-bq.PDC_metadata_versioned.file_associated_entity_mapping_V1_9
- isb-cgc-bq.PDC_metadata.file_metadata_current
- isb-cgc-bq.PDC_metadata_versioned.file_metadata_V1_9

*February 25, 2021*

New TARGET miRNA-seq table

**BigQuery tables created**

- isb-cgc-bq.TARGET_versioned.miRNAseq_hg38_gdc_r25

**BigQuery tables updated**

- isb-cgc-bq.TARGET.miRNAseq_hg38_gdc_current

*February 18, 2021*

Pediatric Brain Cancer Pilot Study clinical data from PDC

- isb-cgc-bq.CBTTC.clinical_pediatric_brain_cancer_pdc_current
- isb-cgc-bq.CBTTC_versioned.clinical_pediatric_brain_cancer_pdc_V1_9
- isb-cgc-bq.CBTTC.clinical_diagnoses_pediatric_brain_cancer_pdc_current
- isb-cgc-bq.CBTTC_versioned.clinical_diagnoses_pediatric_brain_cancer_pdc_V1_9

Hepatitis B Virus (HBV) Related Hepatocellular Carcinoma clinical data from PDC

- isb-cgc-bq.ICPC.clinical_HBV_related_hepatocellular_carcinoma_pdc_current
- isb-cgc-bq.ICPC_versioned.clinical_HBV_related_hepatocellular_carcinoma_pdc_V1_9

Proteogenomics of Gastric Cancer Proteome clinical data from PDC

- isb-cgc-bq.ICPC.clinical_human_early_onset_gastric_cancer_pdc_current
- isb-cgc-bq.ICPC_versioned.clinical_human_early_onset_gastric_cancer_pdc_V1_9

Oral Squamous Cell Carcinoma clinical data from PDC

- isb-cgc-bq.ICPC.clinical_oral_squamous_cell_carcinoma_pdc_current
- isb-cgc-bq.ICPC_versioned.clinical_oral_squamous_cell_carcinoma_pdc_V1_9

Academia Sinica LUAD-100 clinical data from PDC

- isb-cgc-bq.ICPC.clinical_academia_sinica_LUAD_100_pdc_current
- isb-cgc-bq.ICPC_versioned.clinical_academia_sinica_LUAD_100_pdc_V1_9

Georgetown Lung Cancer Proteomics Study clinical data from PDC

- clinical_georgetown_lung_cancer_pdc_current
- clinical_georgetown_lung_cancer_pdc_V1_9

Quantitative digital maps of tissue biopsies clinical data from PDC

- isb-cgc-bq.Quant_Maps_Tissue_Biopsies.clinical_pct_swath_kidney_pdc_current
- isb-cgc-bq.Quant_Maps_Tissue_Biopsies_versioned.clinical_pct_swath_kidney_pdc_V1_9

CPTAC clincal data from PDC

- isb-cgc-bq.TCGA.clinical_CPTAC_TCGA_pdc_current
- isb-cgc-bq.TCGA_versioned.clinical_CPTAC_TCGA_pdc_V1_9
- isb-cgc-bq.CPTAC.clinical_CPTAC_2_pdc_current
- isb-cgc-bq.CPTAC_versioned.clinical_CPTAC_2_pdc_V1_9
- isb-cgc-bq.CPTAC.clinical_CPTAC3_discovery_pdc_current
- isb-cgc-bq.CPTAC_versioned.clinical_CPTAC3_discovery_pdc_V1_9

New CGCI and HCMI Masked Somatic Mutation tables

**BigQuery tables created**

- isb-cgc-bq.CGCI.masked_somatic_mutation_hg38_gdc_current
- isb-cgc-bq.CGCI_versioned.masked_somatic_mutation_hg38_gdc_r27
- isb-cgc-bq.HCMI_versioned.masked_somatic_mutation_hg38_gdc_r27

**BigQuery tables updated**

- isb-cgc-bq.HCMI.masked_somatic_mutation_hg38_gdc_current

*February 1, 2021*

New CTSP RNA Seq tables

**BigQuery tables created**

- isb-cgc-bq.CTSP.RNAseq_hg38_gdc_current
- isb-cgc-bq.CTSP_versioned.RNAseq_hg38_gdc_r23

*January 12, 2021*

New HCMI RNA Seq table

**BigQuery tables created**

- isb-cgc-bq.HCMI.RNAseq_hg38_gdc_r27

**BigQuery tables updated**

- isb-cgc-bq.HCMI.RNAseq_hg38_gdc_current

*January 4, 2021*

New TARGET RNA Seq tables

**BigQuery tables created**

- isb-cgc-bq.TARGET.RNAseq_hg38_gdc_current
- isb-cgc-bq.TARGET_versioned.RNAseq_hg38_gdc_r25
- isb-cgc-bq.TARGET_versioned.RNAseq_hg38_gdc_r26

*December 17, 2020*

New CPTAC Masked Somatic Mutation (MAF) tables.

**BigQuery tables created**

- isb-cgc-bq:CPTAC.masked_somatic_mutation_hg38_gdc_current
- isb-cgc-bq:CPTAC_versioned.masked_somatic_mutation_hg38_gdc_r25


*December 16, 2020*

New per sample file metadata tables added to isb-cgc-bq for GDC release 27.

**BigQuery tables created**

- isb-cgc-bq.CMI_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.WCDT_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.GENIE_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.OHSU_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.FM_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.VAREPOP_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.CTSP_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.NCICCR_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.ORGANOID_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.MMRF_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.CGCI_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.HCMI_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.BEATAML1_0_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.TARGET_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_hg38_gdc_r27
- isb-cgc-bq.CCLE_versioned.per_sample_file_metadata_hg19_gdc_r27
- isb-cgc-bq.TARGET_versioned.per_sample_file_metadata_hg19_gdc_r27
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_hg19_gdc_r27


Current per sample file metadata tables updated to GDC release 27.

**BigQuery tables updated**

- isb-cgc-bq.CMI.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.WCDT.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.GENIE.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.OHSU.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.FM.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.VAREPOP.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CTSP.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.NCICCR.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.ORGANOID.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.MMRF.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CGCI.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.BEATAML1_0.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.TARGET.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.TCGA.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CCLE.per_sample_file_metadata_hg19_gdc_current
- isb-cgc-bq.TARGET.per_sample_file_metadata_hg19_gdc_current
- isb-cgc-bq.TCGA.per_sample_file_metadata_hg19_gdc_current

*December 14, 2020*

New GDC release 27 file metadata tables.

**BigQuery tables created**

- isb-cgc-bq.GDC_case_file_metadata_versioned.GDCfileID_to_GCSurl_r27
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_legacy_r27
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_active_r27
- isb-cgc-bq.GDC_case_file_metadata_versioned.caseData_r27
- isb-cgc-bq.GDC_case_file_metadata_versioned.aliquot2caseIDmap_r27
- isb-cgc-bq.GDC_case_file_metadata_versioned.slide2caseIDmap_r27

Current file metadata tables updated to GDC release 27.

**BigQuery tables updated**

- isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_legacy_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_active_current
- isb-cgc-bq.GDC_case_file_metadata.caseData_current
- isb-cgc-bq.GDC_case_file_metadata.aliquot2caseIDmap_current
- isb-cgc-bq.GDC_case_file_metadata.slide2caseIDmap_current

*December 9, 2020*

New CPTAC RNA Seq tables

**BigQuery tables created**

- isb-cgc-bq.CPTAC.RNAseq_hg38_gdc_current
- isb-cgc-bq.CPTAC_versioned.RNAseq_hg38_gdc_r25

*December 8, 2020*

CPTAC2, CPTAC3, TCGA quant proteome data from PDC, released Sept. 2020.

**BigQuery tables created**

- isb-cgc-bq.TCGA.quant_proteome_TCGA_ovarian_PNNL_pdc_current
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_ovarian_PNNL_pdc_2020_09
- isb-cgc-bq.TCGA.quant_proteome_TCGA_ovarian_JHU_pdc_current
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_ovarian_JHU_pdc_2020_09
- isb-cgc-bq.TCGA.quant_proteome_TCGA_breast_cancer_pdc_current
- isb-cgc-bq.TCGA_versioned.quant_proteome_TCGA_breast_cancer_pdc_2020_09
- isb-cgc-bq.CPTAC.quant_proteome_prospective_ovarian_PNNL_qeplus_pdc_current
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_ovarian_PNNL_qeplus_pdc_2020_09
- isb-cgc-bq.CPTAC.quant_proteome_prospective_ovarian_JHU_pdc_current
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_ovarian_JHU_pdc_2020_09
- isb-cgc-bq.CPTAC.quant_proteome_prospective_colon_PNNL_qeplus_pdc_current
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_colon_PNNL_qeplus_pdc_2020_09
- isb-cgc-bq.CPTAC.quant_proteome_prospective_breast_BI_pdc_current
- isb-cgc-bq.CPTAC_versioned.quant_proteome_prospective_breast_BI_pdc_2020_09
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_UCEC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_UCEC_discovery_study_pdc_2020_09
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_LUAD_discovery_study_pdc_current
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_LUAD_discovery_study_pdc_2020_09
- isb-cgc-bq.CPTAC.quant_proteome_CPTAC_CCRCC_discovery_study_pdc_current
- isb-cgc-bq.CPTAC_versioned.quant_proteome_CPTAC_CCRCC_discovery_study_pdc_2020_09

Pediatric Brain Cancer Pilot proteome study from PDC, released Sept. 2020.

- isb-cgc-bq.CBTTC.quant_proteome_pediatric_brain_cancer_pilot_study_pdc_current
- isb-cgc-bq.CBTTC_versioned.quant_proteome_pediatric_brain_cancer_pilot_study_pdc_2020_09

Hepatitis B Virus (HBV) Related Hepatocellular Carcinoma Proteome study, released Sept. 2020.

- isb-cgc-bq.ICPC.quant_proteome_HBV_related_hepatocellular_carcinoma_pdc_current
- isb-cgc-bq.ICPC_versioned.quant_proteome_HBV_related_hepatocellular_carcinoma_pdc_2020_09
 
Proteogenomics of Gastric Cancer Proteome study, released Sept. 2020.

- isb-cgc-bq.ICPC.quant_proteome_proteogenomics_of_gastric_cancer_pdc_current
- isb-cgc-bq.ICPC_versioned.quant_proteome_proteogenomics_of_gastric_cancer_pdc_2020_09

*December 2, 2020*

Clinical data tables released for GDC release 27.
Current clinical tables were updated to GDC release 27.

**BigQuery tables created and updated**

- isb-cgc-bq.MMRF.clinical_gdc_current
- isb-cgc-bq.MMRF_versioned.clinical_gdc_r27
- isb-cgc-bq.NCICCR.clinical_gdc_current
- isb-cgc-bq.NCICCR_versioned.clinical_gdc_r27
- isb-cgc-bq.OHSU.clinical_gdc_current
- isb-cgc-bq.OHSU_versioned.clinical_gdc_r27
- isb-cgc-bq.HCMI.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq.HCMI_versioned.clinical_follow_ups_molecular_tests_gdc_r27
- isb-cgc-bq.HCMI.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.HCMI_versioned.clinical_diagnoses_treatments_gdc_r27
- isb-cgc-bq.ORGANOID.clinical_gdc_current
- isb-cgc-bq.ORGANOID_versioned.clinical_gdc_r27
- isb-cgc-bq.CGCI.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.CGCI_versioned.clinical_diagnoses_treatments_gdc_r27
- isb-cgc-bq.MMRF.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.MMRF_versioned.clinical_diagnoses_treatments_gdc_r27
- isb-cgc-bq.MMRF.clinical_follow_ups_gdc_current
- isb-cgc-bq.MMRF_versioned.clinical_follow_ups_gdc_r27
- isb-cgc-bq.TCGA.clinical_gdc_current
- isb-cgc-bq.TCGA_versioned.clinical_gdc_r27
- isb-cgc-bq.TARGET.clinical_gdc_current
- isb-cgc-bq.TARGET_versioned.clinical_gdc_r27
- isb-cgc-bq.MMRF.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq.MMRF_versioned.clinical_follow_ups_molecular_tests_gdc_r27
- isb-cgc-bq.GENIE.clinical_gdc_current
- isb-cgc-bq.GENIE_versioned.clinical_gdc_r27
- isb-cgc-bq.VAREPOP.clinical_gdc_current
- isb-cgc-bq.VAREPOP_versioned.clinical_gdc_r27
- isb-cgc-bq.CTSP.clinical_gdc_current
- isb-cgc-bq.CTSP_versioned.clinical_gdc_r27
- isb-cgc-bq.CGCI.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq.CGCI_versioned.clinical_follow_ups_molecular_tests_gdc_r27
- isb-cgc-bq.VAREPOP.clinical_family_histories_gdc_current
- isb-cgc-bq.VAREPOP_versioned.clinical_family_histories_gdc_r27
- isb-cgc-bq.BEATAML1_0.clinical_gdc_current
- isb-cgc-bq.BEATAML1_0_versioned.clinical_gdc_r27
- isb-cgc-bq.MMRF.clinical_family_histories_gdc_current
- isb-cgc-bq.MMRF_versioned.clinical_family_histories_gdc_r27
- isb-cgc-bq.WCDT.clinical_gdc_current
- isb-cgc-bq.WCDT_versioned.clinical_gdc_r27
- isb-cgc-bq.VAREPOP.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.VAREPOP_versioned.clinical_diagnoses_treatments_gdc_r27
- isb-cgc-bq.HCMI.clinical_diagnoses_gdc_current
- isb-cgc-bq.HCMI_versioned.clinical_diagnoses_gdc_r27
- isb-cgc-bq.CGCI.clinical_diagnoses_gdc_current
- isb-cgc-bq.CGCI_versioned.clinical_diagnoses_gdc_r27
- isb-cgc-bq.CGCI.clinical_gdc_current
- isb-cgc-bq.CGCI_versioned.clinical_gdc_r27
- isb-cgc-bq.CGCI.clinical_follow_ups_gdc_current
- isb-cgc-bq.CGCI_versioned.clinical_follow_ups_gdc_r27
- isb-cgc-bq.TCGA.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq.TCGA_versioned.clinical_diagnoses_treatments_gdc_r27
- isb-cgc-bq.CPTAC.clinical_gdc_current
- isb-cgc-bq.CPTAC_versioned.clinical_gdc_r27
- isb-cgc-bq.HCMI.clinical_gdc_current
- isb-cgc-bq.HCMI_versioned.clinical_gdc_r27
- isb-cgc-bq.CMI.clinical_gdc_current
- isb-cgc-bq.CMI_versioned.clinical_gdc_r27
- isb-cgc-bq.FM.clinical_gdc_current
- isb-cgc-bq.FM_versioned.clinical_gdc_r27
- isb-cgc-bq.HCMI.clinical_follow_ups_gdc_current
- isb-cgc-bq.HCMI_versioned.clinical_follow_ups_gdc_r27

*November 16, 2020*

New TARGET controlled-access VCF tables.

**BigQuery tables created**

- isb-cgc-cbq.TARGET.vcf_hg38_gdc_current
- isb-cgc-cbq.TARGET_versioned.vcf_hg38_gdc_r22

*October 30, 2020*

RNA Seq data tables released for the WCDT program.

**BigQuery tables created**

- isb-cgc-bq:WCDT.RNAseq_hg38_gdc_current
- isb-cgc-bq:WCDT_versioned.RNAseq_hg38_gdc_r22

*October 23, 2020*

Clinical data tables released for GDC release 25 and 26.

**BigQuery tables created**

- isb-cgc-bq:BEATAML1_0_versioned.clinical_gdc_r25
- isb-cgc-bq:CGCI_versioned.clinical_gdc_r25
- isb-cgc-bq:CGCI_versioned.clinical_diagnoses_gdc_r25
- isb-cgc-bq:CGCI_versioned.clinical_diagnoses_treatments_gdc_r25
- isb-cgc-bq:CGCI_versioned.clinical_follow_ups_gdc_r25
- isb-cgc-bq:CGCI_versioned.clinical_follow_ups_molecular_tests_gdc_r25
- isb-cgc-bq:CPTAC_versioned.clinical_gdc_r25
- isb-cgc-bq:CTSP_versioned.clinical_gdc_r25
- isb-cgc-bq:FM_versioned.clinical_gdc_r25
- isb-cgc-bq:GENIE_versioned.clinical_gdc_r25
- isb-cgc-bq:HCMI_versioned.clinical_gdc_r25
- isb-cgc-bq:HCMI_versioned.clinical_diagnoses_gdc_r25
- isb-cgc-bq:HCMI_versioned.clinical_diagnoses_treatments_gdc_r25
- isb-cgc-bq:HCMI_versioned.clinical_follow_ups_gdc_r25
- isb-cgc-bq:HCMI_versioned.clinical_follow_ups_molecular_tests_gdc_r25
- isb-cgc-bq:MMRF_versioned.clinical_gdc_r25
- isb-cgc-bq:MMRF_versioned.clinical_diagnoses_treatments_gdc_r25
- isb-cgc-bq:MMRF_versioned.clinical_family_histories_gdc_r25
- isb-cgc-bq:MMRF_versioned.clinical_follow_ups_gdc_r25
- isb-cgc-bq:MMRF_versioned.clinical_follow_ups_molecular_tests_gdc_r25
- isb-cgc-bq:NCICCR_versioned.clinical_gdc_r25
- isb-cgc-bq:OHSU_versioned.clinical_gdc_r25
- isb-cgc-bq:ORGANOID_versioned.clinical_gdc_r25
- isb-cgc-bq:TARGET_versioned.clinical_gdc_r25
- isb-cgc-bq:TCGA_versioned.clinical_gdc_r25
- isb-cgc-bq:TCGA_versioned.clinical_diagnoses_treatments_gdc_r25
- isb-cgc-bq:VAREPOP_versioned.clinical_gdc_r25
- isb-cgc-bq:VAREPOP_versioned.clinical_diagnoses_treatments_gdc_r25
- isb-cgc-bq:VAREPOP_versioned.clinical_family_histories_gdc_r25
- isb-cgc-bq:WCDT_versioned.clinical_gdc_r25
- isb-cgc-bq:BEATAML1_0_versioned.clinical_gdc_r26
- isb-cgc-bq:CGCI_versioned.clinical_gdc_r26
- isb-cgc-bq:CGCI_versioned.clinical_diagnoses_gdc_r26
- isb-cgc-bq:CGCI_versioned.clinical_diagnoses_treatments_gdc_r26
- isb-cgc-bq:CGCI_versioned.clinical_follow_ups_gdc_r26
- isb-cgc-bq:CGCI_versioned.clinical_follow_ups_molecular_tests_gdc_r26
- isb-cgc-bq:CMI_versioned.clinical_gdc_r26
- isb-cgc-bq:CPTAC_versioned.clinical_gdc_r26
- isb-cgc-bq:CTSP_versioned.clinical_gdc_r26
- isb-cgc-bq:FM_versioned.clinical_gdc_r26
- isb-cgc-bq:GENIE_versioned.clinical_gdc_r26
- isb-cgc-bq:HCMI_versioned.clinical_gdc_r26
- isb-cgc-bq:HCMI_versioned.clinical_diagnoses_gdc_r26
- isb-cgc-bq:HCMI_versioned.clinical_diagnoses_treatments_gdc_r26
- isb-cgc-bq:HCMI_versioned.clinical_follow_ups_gdc_r26
- isb-cgc-bq:HCMI_versioned.clinical_follow_ups_molecular_tests_gdc_r26
- isb-cgc-bq:MMRF_versioned.clinical_gdc_r26
- isb-cgc-bq:MMRF_versioned.clinical_diagnoses_treatments_gdc_r26
- isb-cgc-bq:MMRF_versioned.clinical_family_histories_gdc_r26
- isb-cgc-bq:MMRF_versioned.clinical_follow_ups_gdc_r26
- isb-cgc-bq:MMRF_versioned.clinical_follow_ups_molecular_tests_gdc_r26
- isb-cgc-bq:NCICCR_versioned.clinical_gdc_r26
- isb-cgc-bq:MMRF_versioned.clinical_gdc_r26
- isb-cgc-bq:NCICCR_versioned.clinical_gdc_r26
- isb-cgc-bq:MMRF_versioned.clinical_gdc_r26
- isb-cgc-bq:NCICCR_versioned.clinical_gdc_r26
- isb-cgc-bq:MMRF_versioned.clinical_diagnoses_treatments_gdc_r26
- isb-cgc-bq:NCICCR_versioned.clinical_gdc_r26
- isb-cgc-bq:MMRF_versioned.clinical_diagnoses_treatments_gdc_r26
- isb-cgc-bq:NCICCR_versioned.clinical_family_histories_gdc_r26
- isb-cgc-bq:MMRF_versioned.clinical_gdc_r26
- isb-cgc-bq:CMI.clinical_gdc_current

Current clinical tables were updated to GDC release 26.

**BigQuery tables updated**

- isb-cgc-bq:BEATAML1_0.clinical_gdc_current
- isb-cgc-bq:CGCI.clinical_gdc_current
- isb-cgc-bq:CGCI.clinical_diagnoses_gdc_current
- isb-cgc-bq:CGCI.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq:CGCI.clinical_follow_ups_gdc_current
- isb-cgc-bq:CGCI.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq:CPTAC.clinical_gdc_current
- isb-cgc-bq:CTSP.clinical_gdc_current
- isb-cgc-bq:FM.clinical_gdc_current
- isb-cgc-bq:GENIE.clinical_gdc_current
- isb-cgc-bq:HCMI.clinical_gdc_current
- isb-cgc-bq:HCMI.clinical_diagnoses_gdc_current
- isb-cgc-bq:HCMI.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq:HCMI.clinical_follow_ups_gdc_current
- isb-cgc-bq:HCMI.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq:MMRF.clinical_gdc_current
- isb-cgc-bq:MMRF.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq:MMRF.clinical_family_histories_gdc_current
- isb-cgc-bq:MMRF.clinical_follow_ups_gdc_current
- isb-cgc-bq:MMRF.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq:NCICCR.clinical_gdc_current
- isb-cgc-bq:MMRF.clinical_gdc_current
- isb-cgc-bq:NCICCR.clinical_gdc_current
- isb-cgc-bq:MMRF.clinical_gdc_current
- isb-cgc-bq:NCICCR.clinical_gdc_current
- isb-cgc-bq:MMRF.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq:NCICCR.clinical_gdc_current
- isb-cgc-bq:MMRF.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq:NCICCR.clinical_family_histories_gdc_current
- isb-cgc-bq:MMRF.clinical_gdc_current

RNA Seq data tables released for the CMI program.

**BigQuery tables created**

- isb-cgc-bq:CMI.RNAseq_hg38_gdc_current
- isb-cgc-bq:CMI_versioned.RNAseq_hg38_gdc_r26

*October 21, 2020*

RNA Seq data tables released for the CGCI program.

**BigQuery tables created**

- isb-cgc-bq:CGCI.RNAseq_hg38_gdc_current
- isb-cgc-bq:CGCI_versioned.RNAseq_hg38_gdc_r24

*October 15, 2020*

Current file metadata tables updated to GDC release 26.

**BigQuery tables updated**

- isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_legacy_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_active_current
- isb-cgc-bq.GDC_case_file_metadata.caseData_current
- isb-cgc-bq.GDC_case_file_metadata.aliquot2caseIDmap_current
- isb-cgc-bq.GDC_case_file_metadata.slide2caseIDmap_current

*October 14, 2020*

New GDC release 26 file metadata tables.

**BigQuery tables created**

- isb-cgc-bq.GDC_case_file_metadata_versioned.GDCfileID_to_GCSurl_r26
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_legacy_r26
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_active_r26
- isb-cgc-bq.GDC_case_file_metadata_versioned.caseData_r26
- isb-cgc-bq.GDC_case_file_metadata_versioned.aliquot2caseIDmap_r26
- isb-cgc-bq.GDC_case_file_metadata_versioned.slide2caseIDmap_r26

New per sample file metadata tables added to isb-cgc-bq for GDC release 26.

**BigQuery tables created**

- isb-cgc-bq.WCDT_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.GENIE_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.OHSU_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.FM_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.VAREPOP_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.CTSP_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.NCICCR_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.ORGANOID_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.MMRF_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.CGCI_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.HCMI_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.BEATAML1_0_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.TARGET_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.CCLE_versioned.per_sample_file_metadata_hg19_gdc_r26
- isb-cgc-bq.TARGET_versioned.per_sample_file_metadata_hg19_gdc_r26
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_hg19_gdc_r26
- isb-cgc-bq.CMI_versioned.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.CMI.per_sample_file_metadata_hg38_gdc_current

Current per sample file metadata tables updated to GDC release 26.

**BigQuery tables updated**

- isb-cgc-bq.WCDT.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.GENIE.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.OHSU.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.FM.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.VAREPOP.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CTSP.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.NCICCR.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.ORGANOID.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.MMRF.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CGCI.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.HCMI.per_sample_file_metadata_hg38_gdc_r26
- isb-cgc-bq.BEATAML1_0.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CPTAC.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.TARGET.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.TCGA.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq.CCLE.per_sample_file_metadata_hg19_gdc_current
- isb-cgc-bq.TARGET.per_sample_file_metadata_hg19_gdc_current
- isb-cgc-bq.TCGA.per_sample_file_metadata_hg19_gdc_current

*October 06, 2020*

New per sample file metadata tables added to isb-cgc-bq for GDC release 25.

**BigQuery tables created**

- isb-cgc-bq.WCDT_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.GENIE_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.OHSU_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.FM_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.VAREPOP_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.CTSP_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.NCICCR_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.ORGANOID_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.MMRF_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.CGCI_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.HCMI_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.BEATAML1_0_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.TARGET_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_hg38_gdc_r25
- isb-cgc-bq.CCLE_versioned.per_sample_file_metadata_hg19_gdc_r25
- isb-cgc-bq.TARGET_versioned.per_sample_file_metadata_hg19_gdc_r25
- isb-cgc-bq.TCGA_versioned.per_sample_file_metadata_hg19_gdc_r25

*October 02, 2020*

Open Somatic Mutation data tables released for the HCMI program.

**BigQuery tables created**

- isb-cgc-bq.HCMI.masked_somatic_mutation_hg38_gdc_current
- isb-cgc-bq.HCMI_versioned.masked_somatic_mutation_hg38_gdc_r23

The new COSMIC release v92 data is available in BigQuery.

**BigQuery tables created**

- isb-cgc-bq.COSMIC.ASCAT_purity_ploidy_grch37_current
- isb-cgc-bq.COSMIC.ASCAT_purity_ploidy_grch38_current
- isb-cgc-bq.COSMIC.breakpoints_grch37_current
- isb-cgc-bq.COSMIC.breakpoints_grch38_current
- isb-cgc-bq.COSMIC.cancer_gene_census_grch37_current
- isb-cgc-bq.COSMIC.cancer_gene_census_grch38_current
- isb-cgc-bq.COSMIC.cancer_gene_census_hallmarks_of_cancer_grch37_current
- isb-cgc-bq.COSMIC.cancer_gene_census_hallmarks_of_cancer_grch38_current
- isb-cgc-bq.COSMIC.classification_grch37_current
- isb-cgc-bq.COSMIC.classification_grch38_current
- isb-cgc-bq.COSMIC.complete_CNA_grch37_current
- isb-cgc-bq.COSMIC.complete_CNA_grch38_current
- isb-cgc-bq.COSMIC.complete_differential_methylation_grch37_current
- isb-cgc-bq.COSMIC.complete_differential_methylation_grch38_current
- isb-cgc-bq.COSMIC.complete_gene_expression_grch37_current
- isb-cgc-bq.COSMIC.complete_gene_expression_grch38_current
- isb-cgc-bq.COSMIC.complete_targeted_screens_mutant_grch37_current
- isb-cgc-bq.COSMIC.complete_targeted_screens_mutant_grch38_current
- isb-cgc-bq.COSMIC.fusion_grch37_current
- isb-cgc-bq.COSMIC.fusion_grch38_current
- isb-cgc-bq.COSMIC.genome_screens_mutant_grch37_current
- isb-cgc-bq.COSMIC.genome_screens_mutant_grch38_current
- isb-cgc-bq.COSMIC.HGNC_grch37_current
- isb-cgc-bq.COSMIC.HGNC_grch38_current
- isb-cgc-bq.COSMIC.mutant_census_grch37_current
- isb-cgc-bq.COSMIC.mutant_census_grch38_current
- isb-cgc-bq.COSMIC.mutant_grch37_current
- isb-cgc-bq.COSMIC.mutant_grch38_current
- isb-cgc-bq.COSMIC.mutation_tracking_grch37_current
- isb-cgc-bq.COSMIC.mutation_tracking_grch38_current
- isb-cgc-bq.COSMIC.NCV_grch37_current
- isb-cgc-bq.COSMIC.NCV_grch38_current
- isb-cgc-bq.COSMIC.resistance_mutations_grch37_current
- isb-cgc-bq.COSMIC.resistance_mutations_grch38_current
- isb-cgc-bq.COSMIC.sample_grch37_current
- isb-cgc-bq.COSMIC.sample_grch38_current
- isb-cgc-bq.COSMIC.structural_variants_grch37_current
- isb-cgc-bq.COSMIC.structural_variants_grch38_current
- isb-cgc-bq.COSMIC.transcripts_grch37_current
- isb-cgc-bq.COSMIC.transcripts_grch38_current
- isb-cgc-bq.COSMIC_versioned.ASCAT_purity_ploidy_grch37_v92
- isb-cgc-bq.COSMIC_versioned.ASCAT_purity_ploidy_grch38_v92
- isb-cgc-bq.COSMIC_versioned.breakpoints_grch37_v92
- isb-cgc-bq.COSMIC_versioned.breakpoints_grch38_v92
- isb-cgc-bq.COSMIC_versioned.cancer_gene_census_grch37_v92
- isb-cgc-bq.COSMIC_versioned.cancer_gene_census_grch38_v92
- isb-cgc-bq.COSMIC_versioned.cancer_gene_census_hallmarks_of_cancer_grch37_v92
- isb-cgc-bq.COSMIC_versioned.cancer_gene_census_hallmarks_of_cancer_grch38_v92
- isb-cgc-bq.COSMIC_versioned.classification_grch37_v92
- isb-cgc-bq.COSMIC_versioned.classification_grch38_v92
- isb-cgc-bq.COSMIC_versioned.complete_CNA_grch37_v92
- isb-cgc-bq.COSMIC_versioned.complete_CNA_grch38_v92
- isb-cgc-bq.COSMIC_versioned.complete_differential_methylation_grch37_v92
- isb-cgc-bq.COSMIC_versioned.complete_differential_methylation_grch38_v92
- isb-cgc-bq.COSMIC_versioned.complete_gene_expression_grch37_v92
- isb-cgc-bq.COSMIC_versioned.complete_gene_expression_grch38_v92
- isb-cgc-bq.COSMIC_versioned.complete_targeted_screens_mutant_grch37_v92
- isb-cgc-bq.COSMIC_versioned.complete_targeted_screens_mutant_grch38_v92
- isb-cgc-bq.COSMIC_versioned.fusion_grch37_v92
- isb-cgc-bq.COSMIC_versioned.fusion_grch38_v92
- isb-cgc-bq.COSMIC_versioned.genome_screens_mutant_grch37_v92
- isb-cgc-bq.COSMIC_versioned.genome_screens_mutant_grch38_v92
- isb-cgc-bq.COSMIC_versioned.HGNC_grch37_v92
- isb-cgc-bq.COSMIC_versioned.HGNC_grch38_v92
- isb-cgc-bq.COSMIC_versioned.mutant_census_grch37_v92
- isb-cgc-bq.COSMIC_versioned.mutant_census_grch38_v92
- isb-cgc-bq.COSMIC_versioned.mutant_grch37_v92
- isb-cgc-bq.COSMIC_versioned.mutant_grch38_v92
- isb-cgc-bq.COSMIC_versioned.mutation_tracking_grch37_v92
- isb-cgc-bq.COSMIC_versioned.mutation_tracking_grch38_v92
- isb-cgc-bq.COSMIC_versioned.NCV_grch37_v92
- isb-cgc-bq.COSMIC_versioned.NCV_grch38_v92
- isb-cgc-bq.COSMIC_versioned.resistance_mutations_grch37_v92
- isb-cgc-bq.COSMIC_versioned.resistance_mutations_grch38_v92
- isb-cgc-bq.COSMIC_versioned.sample_grch37_v92
- isb-cgc-bq.COSMIC_versioned.sample_grch38_v92
- isb-cgc-bq.COSMIC_versioned.structural_variants_grch37_v92
- isb-cgc-bq.COSMIC_versioned.structural_variants_grch38_v92
- isb-cgc-bq.COSMIC_versioned.transcripts_grch37_v92
- isb-cgc-bq.COSMIC_versioned.transcripts_grch38_v92

*September 21, 2020*

Current file metadata tables updated to GDC release 25.

**BigQuery tables updated**

- isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_legacy_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_active_current
- isb-cgc-bq.GDC_case_file_metadata.caseData_current
- isb-cgc-bq.GDC_case_file_metadata.aliquot2caseIDmap_current
- isb-cgc-bq.GDC_case_file_metadata.slide2caseIDmap_current

*September 18, 2020*

New GDC release 25 file metadata tables.

**BigQuery tables created**

- isb-cgc-bq.GDC_case_file_metadata_versioned.GDCfileID_to_GCSurl_r25
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_legacy_r25
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_active_r25
- isb-cgc-bq.GDC_case_file_metadata_versioned.caseData_r25
- isb-cgc-bq.GDC_case_file_metadata_versioned.aliquot2caseIDmap_r25
- isb-cgc-bq.GDC_case_file_metadata_versioned.slide2caseIDmap_r25

*September 8, 2020*

Table generated as part of an analysis for a poster submitted to the ACM-BCB2020 conference. 

**BigQuery tables created**

- isb-cgc-bq.supplementary_tables.Abdilleh_etal_ACM_BCB_2020_TCGA_bioclin_v0_Clinical_UNPIVOT

*September 2, 2020*

New GENCODE data, version 34 and 35.

**BigQuery tables created**

- isb-cgc-bq.GENCODE_versioned.annotation_gtf_hg38_v34
- isb-cgc-bq.GENCODE_versioned.annotation_gtf_hg38_v35
- isb-cgc-bq.GENCODE.annotation_gtf_hg38_current


*August 28, 2020*

New GDC release 24 clinical tables.

**BigQuery tables created**

- isb-cgc-bq:BEATAML1_0.clinical_gdc_current
- isb-cgc-bq:BEATAML1_0_versioned.clinical_gdc_r24
- isb-cgc-bq:CGCI.clinical_diagnoses_gdc_current
- isb-cgc-bq:CGCI.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq:CGCI.clinical_follow_ups_gdc_current
- isb-cgc-bq:CGCI.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq:CGCI.clinical_gdc_current
- isb-cgc-bq:CGCI_versioned.clinical_diagnoses_gdc_r24
- isb-cgc-bq:CGCI_versioned.clinical_diagnoses_treatments_gdc_r24
- isb-cgc-bq:CGCI_versioned.clinical_follow_ups_gdc_r24
- isb-cgc-bq:CGCI_versioned.clinical_follow_ups_molecular_tests_gdc_r24
- isb-cgc-bq:CGCI_versioned.clinical_gdc_r24
- isb-cgc-bq:CPTAC.clinical_gdc_current
- isb-cgc-bq:CPTAC_versioned.clinical_gdc_r24
- isb-cgc-bq:CTSP.clinical_gdc_current
- isb-cgc-bq:CTSP_versioned.clinical_gdc_r24
- isb-cgc-bq:FM.clinical_gdc_current
- isb-cgc-bq:FM_versioned.clinical_gdc_r24
- isb-cgc-bq:GENIE.clinical_gdc_current
- isb-cgc-bq:GENIE_versioned.clinical_gdc_r24
- isb-cgc-bq:HCMI.clinical_diagnoses_gdc_current
- isb-cgc-bq:HCMI.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq:HCMI.clinical_follow_ups_gdc_current
- isb-cgc-bq:HCMI.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq:HCMI.clinical_gdc_current
- isb-cgc-bq:HCMI_versioned.clinical_diagnoses_gdc_r24
- isb-cgc-bq:HCMI_versioned.clinical_diagnoses_treatments_gdc_r24
- isb-cgc-bq:HCMI_versioned.clinical_follow_ups_gdc_r24
- isb-cgc-bq:HCMI_versioned.clinical_follow_ups_molecular_tests_gdc_r24
- isb-cgc-bq:HCMI_versioned.clinical_gdc_r24
- isb-cgc-bq:MMRF.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq:MMRF.clinical_family_histories_gdc_current
- isb-cgc-bq:MMRF.clinical_follow_ups_gdc_current
- isb-cgc-bq:MMRF.clinical_follow_ups_molecular_tests_gdc_current
- isb-cgc-bq:MMRF.clinical_gdc_current
- isb-cgc-bq:MMRF_versioned.clinical_diagnoses_treatments_gdc_r24
- isb-cgc-bq:MMRF_versioned.clinical_family_histories_gdc_r24
- isb-cgc-bq:MMRF_versioned.clinical_follow_ups_gdc_r24
- isb-cgc-bq:MMRF_versioned.clinical_follow_ups_molecular_tests_gdc_r24
- isb-cgc-bq:MMRF_versioned.clinical_gdc_r24
- isb-cgc-bq:NCICCR.clinical_gdc_current
- isb-cgc-bq:NCICCR_versioned.clinical_gdc_r24
- isb-cgc-bq:OHSU.clinical_gdc_current
- isb-cgc-bq:OHSU_versioned.clinical_gdc_r24
- isb-cgc-bq:ORGANOID.clinical_gdc_current
- isb-cgc-bq:ORGANOID_versioned.clinical_gdc_r24
- isb-cgc-bq:TARGET.clinical_gdc_current
- isb-cgc-bq:TARGET_versioned.clinical_gdc_r24
- isb-cgc-bq:TCGA.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq:TCGA.clinical_gdc_current
- isb-cgc-bq:TCGA_versioned.clinical_diagnoses_treatments_gdc_r24
- isb-cgc-bq:TCGA_versioned.clinical_gdc_r24
- isb-cgc-bq:VAREPOP.clinical_diagnoses_treatments_gdc_current
- isb-cgc-bq:VAREPOP.clinical_family_histories_gdc_current
- isb-cgc-bq:VAREPOP.clinical_gdc_current
- isb-cgc-bq:VAREPOP_versioned.clinical_diagnoses_treatments_gdc_r24
- isb-cgc-bq:VAREPOP_versioned.clinical_family_histories_gdc_r24
- isb-cgc-bq:VAREPOP_versioned.clinical_gdc_r24
- isb-cgc-bq:WCDT.clinical_gdc_current
- isb-cgc-bq:WCDT_versioned.clinical_gdc_r24


*July 23, 2020*

New TCGA controlled-access MAF tables.
New TARGET GDC release 22 RNAseq and miRNAseq tables.

**BigQuery tables created**

- isb-cgc-cbq:TCGA.maf_hg38_gdc_current
- isb-cgc-cbq:TCGA_versioned.maf_hg38_gdc_r14

- isb-cgc-bq:TARGET_versioned.miRNAseq_hg38_gdc_r22
- isb-cgc-bq:TARGET_versioned.RNAseq_hg38_gdc_r22
- isb-cgc-bq:TARGET.miRNAseq_hg38_gdc_current
- isb-cgc-bq:TARGET.RNAseq_hg38_gdc_current


*July 21, 2020*

New HCMI RNA seq table.

**BigQuery tables created**

- isb-cgc.HCMI.RNAseq_hg38_gdc_r23

*July 9, 2020*

New per sample file metadata tables added to isb-cgc-bq for GDC release 24.

**BigQuery tables created**

- isb-cgc-bq:BEATAML1_0.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:BEATAML1_0_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:TCGA.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:TCGA_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:TARGET.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:TARGET_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:GENIE.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:GENIE_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:CGCI.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:CGCI_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:CPTAC.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:CPTAC_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:CTSP.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:CTSP_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:FM.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:FM_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:HCMI.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:HCMI_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:MMRF.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:MMRF_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:NCICCR.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:NCICCR_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:OHSU.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:OHSU_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:ORGANOID.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:ORGANOID_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:VAREPOP.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:VAREPOP_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:WCDT.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:WCDT_versioned.per_sample_file_metadata_hg38_gdc_r24
- isb-cgc-bq:CCLE.per_sample_file_metadata_hg38_gdc_current
- isb-cgc-bq:CCLE_versioned.per_sample_file_metadata_hg38_gdc_r24

Existing GDC Release 24 file metadata tables in the isb-cgc project were copied to the isb-cgc-bq project.

**BigQuery tables created**

- isb-cgc-bq.GDC_case_file_metadata_versioned.slide2caseIDmap_r24
- isb-cgc-bq.GDC_case_file_metadata_versioned.GDCfileID_to_GCSurl_r24
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_legacy_r24
- isb-cgc-bq.GDC_case_file_metadata_versioned.fileData_active_r24
- isb-cgc-bq.GDC_case_file_metadata_versioned.caseData_r24
- isb-cgc-bq.GDC_case_file_metadata_versioned.aliquot2caseIDmap_r24
- isb-cgc-bq.GDC_case_file_metadata.slide2caseIDmap_current
- isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_legacy_current
- isb-cgc-bq.GDC_case_file_metadata.fileData_active_current
- isb-cgc-bq.GDC_case_file_metadata.caseData_current
- isb-cgc-bq.GDC_case_file_metadata.aliquot2caseIDmap_current


*June 16, 2020*

The new COSMIC release v91 data is available in BigQuery.

**BigQuery tables created**

- isb-cgc:COSMIC_v91_grch37.ASCAT_Purity_Ploidy
- isb-cgc:COSMIC_v91_grch37.Breakpoints
- isb-cgc:COSMIC_v91_grch37.Cancer_Gene_Census
- isb-cgc:COSMIC_v91_grch37.Complete_CNA
- isb-cgc:COSMIC_v91_grch37.Complete_Differential_Methylation
- isb-cgc:COSMIC_v91_grch37.Complete_Gene_Expression
- isb-cgc:COSMIC_v91_grch37.Complete_Targeted_Screens_Mutant
- isb-cgc:COSMIC_v91_grch37.Fusion
- isb-cgc:COSMIC_v91_grch37.Genome_Screens_Mutant
- isb-cgc:COSMIC_v91_grch37.HGNC
- isb-cgc:COSMIC_v91_grch37.Mutant
- isb-cgc:COSMIC_v91_grch37.Mutant_Census
- isb-cgc:COSMIC_v91_grch37.Mutation_Tracking
- isb-cgc:COSMIC_v91_grch37.NCV
- isb-cgc:COSMIC_v91_grch37.Resistance_Mutations
- isb-cgc:COSMIC_v91_grch37.Sample
- isb-cgc:COSMIC_v91_grch37.Structural_Variants
- isb-cgc:COSMIC_v91_grch37.Transcripts
- isb-cgc:COSMIC_v91_grch38.ASCAT_Purity_Ploidy
- isb-cgc:COSMIC_v91_grch38.Breakpoints
- isb-cgc:COSMIC_v91_grch38.Cancer_Gene_Census
- isb-cgc:COSMIC_v91_grch38.Classification
- isb-cgc:COSMIC_v91_grch38.Complete_CNA
- isb-cgc:COSMIC_v91_grch38.Complete_Differential_Methylation
- isb-cgc:COSMIC_v91_grch38.Complete_Gene_Expression
- isb-cgc:COSMIC_v91_grch38.Complete_Targeted_Screens_Mutant
- isb-cgc:COSMIC_v91_grch38.Fusion
- isb-cgc:COSMIC_v91_grch38.Genome_Screens_Mutant
- isb-cgc:COSMIC_v91_grch38.HGNC
- isb-cgc:COSMIC_v91_grch38.Mutant
- isb-cgc:COSMIC_v91_grch38.Mutant_Census
- isb-cgc:COSMIC_v91_grch38.Mutation_Tracking
- isb-cgc:COSMIC_v91_grch38.NCV
- isb-cgc:COSMIC_v91_grch38.Resistance_Mutations
- isb-cgc:COSMIC_v91_grch38.Sample
- isb-cgc:COSMIC_v91_grch38.Structural_Variants
- isb-cgc:COSMIC_v91_grch38.Transcripts

*June 09, 2020*

New GDC file ID to GCS url tables added to isb-cgc for GDC release 24.

**BigQuery tables created**

- isb-cgc:GDC_metadata.rel24_GDCfileID_to_GCSurl

*May 28, 2020*

New data set and RNA Sequence table derived data tables added to isb-cgc.

**BigQuery tables created**
 
- isb-cgc:TARGET.RNAseq_hg38_r22

*May 27, 2020*

PanCancer tables were added to the isb-cgc project. The Pan-Cancer Atlas tables include clinical, methylation, RPPA and copy number data.

**BigQuery tables created**

The following tables were created under the isb-cgc:pancer-altas data set:

- BarcodeMap
- clinical_PANCAN_patient_with_followup
- EBpp_AdjustPANCAN_IlluminaHiSeq_RNASeqV2_genExp
- Filtered_all_CNVR_data_by_gene
- Filtered_clinical_PANCAN_patient_with_followup
- Filtered_EBpp_AdjustPANCAN_IlluminaHiSeq_RNASeqV2_genExp
- Filtered_jhu_usc_edu_PANCAN_HumanMethylation27_betaValue_whitelisted
- Filtered_jhu_usc_edu_PANCAN_HumanMethylation450_betaValue_whitelisted
- Filtered_jhu_usc_edu_PANCAN_merged_HumanMethylation27_HumanMethylation450_betaValue_whitelisted
- Filtered_MC3_MAF_V5_one_per_tumor_sample
- Filtered_pancanMiRs_EBadjOnProtocolPlatformWithoutRepsWithUnCorrectMiRs_08_04_16
- Filtered_TCGA_RPPA_pancan_clean
- jhu_usc_edu_PANCAN_HumanMethylation27_betaValue_whitelisted
- jhu_usc_edu_PANCAN_HumanMethylation450_betaValue_whitelisted
- jhu_usc_edu_PANCAN_merged_HumanMethylation27_HumanMethylation450_betaValue_whitelisted
- merged_sample_quality_annotations
- pancanMiRs_EBadjOnProtocolPlatformWithoutRepsWithUnCorrectMiRs_08_04_16
- TCGA_CDR
- TCGA_RPPA_pancan_clean
- Whitelist_ParticipantBarcodes

GDC data release 24.0 was released on May 7, 2020.

**Updates to existing programs and projects**

- 110 new cases were released from the HNSCC cohort of CPTAC-3. This includes WXS, WGS, RNA-Seq and miRNA-Seq data.
 - Aliquot-level WXS MAFs are now available from the following projects: CPTAC-2 and CPTAC-3
 
**BigQuery tables created**

- isb-cgc:GDC_metadata.rel24_aliquot2caseIDmap
- isb-cgc:GDC_metadata.rel24_caseData
- isb-cgc:GDC_metadata.rel24_fileData_active
- isb-cgc:GDC_metadata.rel24_fileData_legacy
- isb-cgc:GDC_metadata.rel24_slide2caseIDmap

**New programs and projects available in Google Cloud Storage**

- New project released: CGCI-HTMCP-CC - HIV+ Tumor Molecular Characterization Project - Cervical Cancer
 - RNA-Seq: Alignments and gene expression levels
 - miRNA-Seq: Alignments and miRNA expression levels
 - WGS: Alignments
 - Targeted Sequencing: Alignments

New data sets and RNA Sequence tables derived data tables added to isb-cgc.

**BigQuery tables created**

- isb-cgc:BEATAML1_0.RNA_hg38_r19
 - isb-cgc:ORGANOID.RNA_hg38_r18

*May 8, 2020*

GDC data release 23.0 was posted on April 7, 2020.

**Updates to existing programs and projects**

- HCMI-CMDC Aliquot-level MAFs were released
- TARGET-ALL-P2 Aliquot-level MAFs were released
- TARGET-ALL-P3 Aliquot-level MAFs were released
- TARGET-AML Aliquot-level MAFs were released
- TARGET-NBL Aliquot-level MAFs were released
- TARGET-OS Aliquot-level MAFs were released
- TARGET-WT Aliquot-level MAFs were released
- All TCGA Projects Copy number segment and estimate files from SNP6 ASCAT were released
- TARGET-ALL-P2 Copy number segment and estimate files from SNP6 ASCAT were released
- TARGET-AML Copy number segment and estimate files from SNP6 ASCAT were released
- HCMI-CMDC RNA-seq data was released
- CGCI-BLGSP clinical data was updated
- HCMI-CMDC clinical data was updated
- WCDT-MCRPC clinical data was updated

**BigQuery tables created**

- isb-cgc:GDC_metadata.rel23_aliquot2caseIDmap
- isb-cgc:GDC_metadata.rel23_caseData
- isb-cgc:GDC_metadata.rel23_fileData_active
- isb-cgc:GDC_metadata.rel23_fileData_legacy
- isb-cgc:GDC_metadata.rel23_slide2caseIDmap
- isb-cgc:GDC_metadata.rel23_GDCfileID_to_GCSurl

*March 16, 2020*

GDC data release 22.0 was posted on January 16, 2020.

**New programs and projects available in Google Cloud Storage**

- WCDT-MCRPC (Genomic Characterization of Metastatic Castration Resistant Prostate Cancer), RNA-Seq and WGS Data included

**Updates to existing programs and projects**

- HCMI-CMDC new RNA-Seq, WXS, WGS data was released.
- CPTAC-3 new WXS, WGS, and RNA-Seq data and miRNA-Seq data for currently released cases was released

**BigQuery tables created**

- isb-cgc:GDC_metadata.rel22_aliquot2caseIDmap
- isb-cgc:GDC_metadata.rel22_caseData
- isb-cgc:GDC_metadata.rel22_fileData_active
- isb-cgc:GDC_metadata.rel22_fileData_legacy
- isb-cgc:GDC_metadata.rel22_slide2caseIDmap
- isb-cgc:GDC_metadata.rel22_GDCfileID_to_GCSurl

*January 11, 2020*

GDC data release 21.0 was posted on December 10, 2019.

**New programs and projects available in Google Cloud Storage**

- GENIE-MDA
- GENIE-VICC
- GENIE-DFCI
- GENIE-MSK
- GENIE-UHN
- GENIE-JHU
- GENIE-GRCC
- GENIE-NKI

**BigQuery tables created**

- isb-cgc:GDC_metadata.rel21_aliquot2caseIDmap
- isb-cgc:GDC_metadata.rel21_caseData
- isb-cgc:GDC_metadata.rel21_fileData_active
- isb-cgc:GDC_metadata.rel21_fileData_legacy
- isb-cgc:GDC_metadata.rel21_slide2caseIDmap

*December 20, 2019*

GDC data release 19.0 was posted on September 17, 2019.

GDC data release 19.1 was posted on November 6, 2019.

**New programs and projects available in Google Cloud Storage**

- BEATAML1.0-COHORT (Functional Genomic Landscape of Acute Myeloid Leukemia) WXS and RNA-Seq data was included. 
 
**Updates to existing programs and projects**

- TARGET-ALL-P1 new RNA-Seq data was released.
- TARGET-ALL-P2  new RNA-Seq, WXS, and miRNA-Seq data was released.
- TARGET-ALL-P3 new miRNA-Seq data was released.
- TARGET-AML new WXS and WGS data was released.
- TARGET-NBL new WXS and RNA-Seq data was released.
- TARGET-RT new WGS and RNA-Seq data was released.
- TARGET-WT new WGS, WXS, and RNA-Seq data was released.
- CGCI-BLGSP new WGS data was released. 
- TARGET-ALL-P3 new Pindel VCFs was released.
- MMRF new Pindel VCFs was released.
- HCMI new Pindel VCFs was released.
- CPTAC-3 new Pindel VCFs was released.
- Disease-specific staging properties for many projects released.

**BigQuery tables created**

- isb-cgc:GDC_metadata.rel19_aliquot2caseIDmap
- isb-cgc:GDC_metadata.rel19_caseData
- isb-cgc:GDC_metadata.rel19_fileData_active
- isb-cgc:GDC_metadata.rel19_fileData_legacy
- isb-cgc:GDC_metadata.rel19_slide2caseIDmap
	
GDC data release 18 was posted on July 8, 2019.

**New programs and projects available in Google Cloud Storage**

- ORGANOID-PANCREATIC (Pancreas Cancer Organoid Profiling)
- MMRF-COMMPASS (Multiple Myeloma CoMMpass Study)
- CGCI-BLGSP (Burkitt Lymphoma Genome Sequencing Project)
- TARGET-ALL-P1 (Acute Lymphoblastic Leukemia - Phase I)
- TARGET-ALL-P2 (Acute Lymphoblastic Leukemia - Phase II)

**Updates to existing programs and projects**

- TARGET-ALL-P3 new RNA-Seq data was released.
- TARGET-CCSK new RNA-Seq data was released.
- TARGET-OS new RNA-Seq data was released. 

**BigQuery tables created** 

- isb-cgc:GDC_metadata.rel18_aliquot2caseIDmap
- isb-cgc:GDC_metadata.rel18_caseData
- isb-cgc:GDC_metadata.rel18_fileData_active
- isb-cgc:GDC_metadata.rel18_fileData_legacy
- isb-cgc:GDC_metadata.rel18_slide2caseIDmap

*September 29, 2019*
	
GDC data release 17.0 was posted on June 5, 2019.

GDC data release 17.1 was posted on June 12, 2019.

**New programs and projects available in Google Cloud Storage**

- HCMI-CMDC 500 files,  2.8TB
- BEATAML1.0-CRENOLANIB 700 files,  3.6TB

**Updates to existing programs and projects**

- CPTAC-3 RNA-Seq - 7400 files, 16.6 TB
- TCGA ATAC-Seq - 820 files, 9.2 TB
- NCICCR-DLBCL RNA-Seq - 2900 files, 11.9 TB
- CTSP-DLBCL1 RNA-Seq - 250 files, .96TB
- Updates to TCGA clinical data
- Migrations of three properties across all projects from diagnosis to demographic (vital_status, days_to_birth, days_to_death)

**BigQuery tables created** 

- isb-cgc:GDC_metadata.rel17_aliquot2caseIDmap
- isb-cgc:GDC_metadata.rel17_caseData
- isb-cgc:GDC_metadata.rel17_fileData_active
- isb-cgc:GDC_metadata.rel17_fileData_legacy
- isb-cgc:GDC_metadata.rel17_slide2caseIDmap

*April 4, 2019*

GDC data release 16 was posted on March 26, 2019.

**New programs and projects available in Google Cloud Storage**

- CPTAC-3

**BigQuery tables created** 

- isb-cgc:GDC_metadata.rel16_aliquot2caseIDmap
- isb-cgc:GDC_metadata.rel16_caseData
- isb-cgc:GDC_metadata.rel16_fileData_active
- isb-cgc:GDC_metadata.rel16_fileData_legacy
- isb-cgc:GDC_metadata.rel16_slide2caseIDmap

*March 6, 2019*

GDC data release 15 was posted on February 20, 2019.

**New programs and projects available in Google Cloud Storage**

- TARGET-ALL-P3


**BigQuery tables created** 

- isb-cgc:GDC_metadata.rel15_aliquot2caseIDmap
- isb-cgc:GDC_metadata.rel15_caseData
- isb-cgc:GDC_metadata.rel15_fileData_current
- isb-cgc:GDC_metadata.rel15_fileData_legacy
- isb-cgc:GDC_metadata.rel15_slide2caseIDmap

*January 4, 2019*

GDC data release 14 was posted on December 18, 2018.

**New programs and projects available in Google Cloud Storage**

- FM-AD

**BigQuery tables created**

- isb-cgc:GDC_metadata.rel14_aliquot2caseIDmap
- isb-cgc:GDC_metadata.rel14_caseData
- isb-cgc:GDC_metadata.rel14_fileData_current
- isb-cgc:GDC_metadata.rel14_fileData_legacy
- isb-cgc:GDC_metadata.rel14_GDCfileID_to_GCSurl
- isb-cgc:GDC_metadata.rel14_GDCfileID_to_GCSurl_NEW
- isb-cgc:GDC_metadata.rel14_slide2caseIDmap
- isb-cgc:TCGA_hg38_data_v0.miRNAseq_Expression
- isb-cgc:TCGA_hg38_data_v0.miRNAseq_Isoform_Expression

*October 2, 2018*

GDC data release 13 was posted on September 27, 2018.

**New programs and projects available in Google Cloud Storage**

- VAREPOP-APOLLO
- CTSP-DLBCL1 
- NCICCR-DLBCL

**DR13**, active archive contains 428,543 files (DR12 contained 356,381 files)

- 116 files were removed: 88 VCF files, 24 BAM files, and 2 miRNA "mirnas.quantification" files and (corresponding) 2 miRNA "isoforms.quantification" files.
- 72278 files were added: 47248 BAI files, 23203 TBI files, 1287 BAM files, 504 SEG files, 36 SVS files.

*June 25, 2018:*

GDC data release 12 was posted on Wednesday, June 13, 2018.

- There is absolutely no change in the legacy archive data between DR11 and DR12
- There is also no change in the total number of cases in either archive
- The number of files in the current archive has increased from 329,165 to 356,381:
 - 67,220 files were removed
 - 94,436 files were added

More details about the changes to the current archive of **TCGA** data:

Copy Number Variation | Genotyping Array | TXT files:

- 22376 Copy Number Segment files replaced (ie removed and added)
- 22376 Masked Copy Number Segment files replaced

Biospecimen | BCR XML files:

- 11294 files replaced

Clinical | BCR XML files:

- 11160 files removed / 11167 files added (ie 7 extra files)

Biospecimen | Diagnostic Slide | SVS files:

- 11730 Slide Image files added

Biospecimen | BCR SSF XML files:

- 10557 Biospecimen Supplement files added

Biospecimen | BCR Auxiliary XML files:

- 2884 Biospecimen Supplement files added

Clinical | BCR OMF XML files:

- 1051 Clinical Supplement files added

Biospecimen | BCR Biotab files:

- 340 Biospecimen Supplement files added

Clinical | BCR Biotab files:

- 226 Clinical Supplement files added

Simple Nucleotide Variation | WXS | VCF | Varscan2 files :

- 1 Raw Simple Somatic Mutation file removed (2017-03-04)
- 1 Annotated Somatic Mutation file removed (2017-06-17)

Both for ESCA samples: 

TCGA-VR-A8ET-01A-11D-A403-09;TCGA-VR-A8ET-10B-01D-A403-09

For **TARGET** data:
 
RNA-Seq data:

- 3 BAM files and 9 Gene Expression Quantification files removed
- Sample barcodes: TARGET-30-PAKYZS-01A-01R, TARGET-30-PAMEZH-01A-01R, TARGET-30-PANRRW-01A-01R
- Raw CGI Variant | WGS | Combined Nucleotide Variation | VCF files:435 files added

*June 4, 2018:*

The metadata tables for GDC data release 11 are now available in BigQuery.

*May 8, 2018:*

The gnomAD database (release 2.0.2, dated October 2017) is now available in BigQuery! **isb-cgc:genome_reference.gnomAD_20171003_GRCh37**.

*April 30, 2018:*

Recently released (2018-04-01) ClinVar VCFs are now available in BigQuery! Two new tables (**ClinVar_20180401_GRCh37** and **ClinVar_20180401_GRCh38**) can be found in our genome_reference dataset; also available is dbSNP build 151 (announced 2018-04-24): **isb-cgc:genome_reference.dbSNP_b151_GRCh37p13_All**. 

*February 22, 2018:*

A `genenames_mapping <https://bigquery.cloud.google.com/table/isb-cgc:genome_reference.genenames_mapping?pli=1&tab=schema>`_ table has been added to our numerous reference sources in BigQuery to simplify mapping between HGNC IDs, HGNC symbols, Entrez Gene IDs, Ensembl Gene IDs, Pubmed IDs, and RefSeq IDs!

*June 9, 2018:*

The metadata tables for GDC data release 10 are now available in BigQuery.

*May 8, 2018:*

The release 85 of the **COSMIC** database is now available in BigQuery.

*February 13, 2018:*

The release 84 of the **COSMIC** database is now available in BigQuery.

*December 19, 2017:* 

The ISB-CGC cohort metadata has been update to reflect the new and update TARGET gene expression data provided by the GDC in their data release 9.

*December 6, 2017:* 

The GDC release 9 included some updated and new TARGET gene expression data. The BigQuery table **isb-cgc:TARGET_hg38_data_v0.RNAseq_Gene_Expression** has been updated to reflect this.

*November 7, 2017:* 

The release 83 of the **COSMIC** database is now available in BigQuery.

*November 3, 2017:*

The metadata tables for GDC data release 9 are now available in BigQuery.

*October 30, 2017:* 

The 'harmonized' hg38 TCGA VCF files (raw and annotated) are now available in the ISB-CGC controlled-data repository in Google Cloud Storage.

*August 30, 2017:*

The hg38 TARGET VCF files (raw and annotated) are now available in the ISB-CGC controlled-data repository in Google Cloud Storage.


*August 3, 2017:*

Release 82 of the **COSMIC** database is  now available in BigQuery.


*June 30, 2017:* 

The genome sequence hg19 and hg38 TARGET WXS, RNA-Seq, and miRNA-Seq BAM files are now available in the ISB-CGC controlled-data repository in Google Cloud Storage.

*May 9, 2017:* 

Release 81 of the COSMIC database is now available in BigQuery.

*May 5, 2017:*

A table mapping between UniProtKB accessions and identifiers has been added to our reference dataset: **isb-cgc:genome_reference.UniProtKB_idmapping**.

*April 10, 2017:*

We have re-organized our TCGA clinical, biospecimen, and molecular data into new datasets in BigQuery.

Please find them below: 

- `isb-cgc:TCGA_bioclin_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_bioclin_v0?pli=1>`_
- `isb-cgc:TCGA_hg19_data_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_hg19_data_v0?pli=1>`_ 
- `isb-cgc:TCGA_hg38_data_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_hg38_data_v0?pli=1>`_ 

The hg19 data can also be found in the GDC's `legacy archive <https://portal.gdc.cancer.gov/legacy-archive/search/f>`_, while the hg38 data is available at the `GDC data portal <https://portal.gdc.cancer.gov/>`_.

*March 30, 2017:*

The 'harmonized' hg38 TCGA miRNA-Seq BAM files from the initial GDC data release are now available in the ISB-CGC controlled-data repository in Google Cloud Storage.

*February 20, 2017:*

In collaboration with the Sanger Institute, the `COSMIC database <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/COSMIC_about.html>`_ is now available in BigQuery (registered users only).

*February 5, 2017:* 

Genomic coordinates (in GFF3 format) for human microRNAs added for miRBase v20 and v21 to the **isb-cgc:genome_reference** BigQuery dataset.

*January 30, 2017:*

The final, unified "MC3" TCGA somatic mutations call set is available in the BigQuery. 
**isb-cgc:hg19_data_previews** dataset (also `available on Synapse <https://www.synapse.org/#!Synapse:syn7214402/wiki/405297>`_).


*January 10, 2017:*

**miRBase_v20** table added to the **isb-cgc:genome_reference** BigQuery dataset.

*January 4, 2017:* 

Ensembl gene-set releases 75 (GRCh37) and 87 (GRCh38) are now also available in the **isb-cgc:genome_reference** BigQuery dataset.

*December 30, 2016:*

The 'harmonized' hg38 TCGA WXS BAM files and RNA-Seq BAM files from the initial GDC data release (1.0), as well as the legacy hg19. TCGA 'Level 2' Genome-Wide SNP6 array genotype files ('birdseed') files are now available in the ISB-CGC controlled-data repository in Google Cloud Storage.

*November 14, 2016:*

TCGA radiology and tissue slide images are now available in Google Cloud Storage!  
This includes radiology images (DICOM files) from the `Cancer Imaging Archive <http://www.cancerimagingarchive.net/>`_ (TCIA) and tissue slide images from the `NCI-GDC data portal <https://portal.gdc.cancer.gov/legacy-archive/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22files.data_type%22,%22value%22:%5B%22Tissue%20slide%20image%22%5D%7D%7D%5D%7D>`_ (SVS files).

*November 16, 2016:*

TCGA proteomics data from the `CPTAC <https://cptac-data-portal.georgetown.edu/cptacPublic/>`_ (Phase II) is now available in `Google Cloud Storage <https://console.cloud.google.com/storage/browser/isb-cptac-open/Phase_II>`_.

*September 10, 2016:*

**GENCODE** versions 19, 22, 23, and 24 are all now available in the **isb-cgc:genome_reference** BigQuery dataset, with an updated and more complete schema. -- Note also that the naming convention is now **GENCODE_v19** rather than GENCODE_r19; also that v19 is the *last* version based on hg19/GRCh37, and all subsequent versions are based on hg38/GRCh38.

*August 31, 2016:*

A table based on the latest liftOver hg19-to-hg38 chain files is available in the **isb-cgc:tcga_genome_reference** BigQuery dataset.

*August 26, 2016:*

A set of tables based on running Picard over ~67,000 TCGA bam files in GCS have been added to the **isb-cgc:tcga_seq_metadata** BigQuery dataset: information contained in these tables includes bam-index stats, insert-size metrics, quality-distribution metrics, and quality-yield metrics -- these tables can be used in conjunction with the FastQC-based tables to look for bam and/or fastq data files that meet your analysis criteria.

*August 21, 2016:*

New **miRBase_v21** table added to the **isb-cgc:genome_reference** BigQuery dataset.

*August 20, 2016:*

Updated **hg19** and **hg38** `Kaviar <http://db.systemsbiology.net/kaviar/>`_ tables added to the **isb-cgc:genome_reference** BigQuery dataset.

*August 17, 2016:*

New **isb-cgc:GDC_metadata** BigQuery dataset containing metadata for both *legacy* and *current* files hosted at the `NCI-GDC <https://gdc.cancer.gov/>`_.

*July 28, 2016:* 

New **isb-cgc:tcga_201607_beta** BigQuery dataset based on the *final* TCGA data upload from the DCC.  This dataset largely mirrors the previous **isb-cgc:tcga_20510_alpha** dataset and is now also supporting the ISB-CGC Web-App.  The curated TCGA cohort tables in the **isb-cgc:tcga_cohorts** BigQuery dataset have also been updated.

*June 24, 2016:* 

An updated listing of all ISB-CGC hosted data in Google Cloud Storage (GCS) is now available in the **GCS_listing_24jun2016** table in the **isb-cgc:tcga_seq_metadata** dataset in BigQuery, in addition the **CGHub_Manifest_24jun2016** table contains the final CGHub Manifest prior to the transition of all data to the `Genomic Data Commons <https://portal.gdc.cancer.gov/>`_.

*June 18, 2016:*

New **GENCODE_r24** table added to the **isb-cgc:genome_reference** BigQuery dataset.

*May 13, 2016:*

New **NCBI_Viral_Annotations_Taxid10239** table added to the **isb-cgc:genome_reference** BigQuery dataset.

*May 9, 2016:* 

New **Ensembl2Reactome** and **miRBase2Reactome** tables added to the **isb-cgc:genome_reference** BigQuery dataset.

*May 3, 2016:*

New **isb-cgc:tcga_seq_metadata** BigQuery dataset contains metadata and FastQC metrics for thousands of TCGA DNA-seq and RNA-seq data files:
- **CGHub_Manifest** table contains metadata for all TCGA files at CGHub as of April 27th, 2016
- **GCS_listing_27apr2016** table contains metadata for all TCGA files hosted by ISB-CGC in GCS 
- **RNAseq_FastQC** table contains metrics derived from FastQC runs on the RNAseq data files, including urls to the FastQC html reports that you can cut and paste directly into your browser
- **WXS_FastQC** table contains metrics derived from FastQC runs on the exome DNAseq data files

*April 28, 2016*

**GO_Ontology** and **GO_Annotations** tables added to the **isb-cgc:genome_reference** BigQuery dataset.

*March 14, 2016*

With the release of our **Web-App**, controlled-data is now accessible (programmatically) to users who have previously obtained dbGaP approval for TCGA data and go through the NIH authentication process built-in to the Web-App.

*February 26, 2016*

New CCLE dataset in BigQuery **isb-cgc:ccle_201602_alpha** includes sample metadata, mutation calls, copy-number segments, and expression data (metadata includes full cloud-storage-path for world-readable BAM and SNP CEL files, and Genomics dataset- and readgroupset-ids for sequence data imported into Google Genomics).

*February 22, 2016*

Kaviar database now available in the **isb-cgc:genome_reference** BigQuery dataset.

*February 19, 2016*

CCLE RNAseq and DNAseq bam files imported into **Google Genomics**.

*January 10, 2016*

**GENCODE_r19** and **miRBase_v20** tables added to the **isb-cgc:genome_reference** BigQuery dataset.

*December 26, 2015*

Public release of new **isb-cgc:genome_reference** BigQuery dataset: the first table is based on the just-published **miRTarBase** release 6.1.

*December, 12, 2015*

Curated TCGA cohort lists available in **isb-cgc:tcga_cohorts** BigQuery dataset.

*December 3, 2015*

Version `v0.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.0>`_.

First tagged release of the web-app.

*November 16, 2015*

Initial upload of data from CGHub into **Google Cloud Storage** (GCS) complete (not publicly released).

*November 2, 2015*

First public release of TCGA open-access data in BigQuery tables.

- **isb-cgc:tcga_201510_alpha** dataset contains updated set of BigQuery tables, based on data available at the TCGA DCC as of October 2015
- Includes **Annotations** table with information about redacted samples, etc
- **isb-cgc:platform_reference** contains annotation information for the Illumina DNA Methylation platform

*October 4, 2015*

Complete data upload from TCGA DCC, including controlled-access data

*September 21, 2015* 

Draft set of BigQuery tables (not publicly released)

- **isb-cgc:tcga_201507_alpha** dataset containing clinical, biospecimen, somatic mutation calls and Level-3 TCGA data available at the TCGA DCC as of July 2015
