******************************
Data Releases and Future Plans
******************************

Release Notes
#############

* June 25, 2018 : GDC data release 12 was posted on Wednesday, June 13, 2018
 - There is absolutely no change in the legacy archive data between DR11 and DR12
 - There is also no change in the total number of cases in either archive
 - The number of files in the current archive has increased from 329,165 to 356,381:
  - 67,220 files were removed
  - 94,436 files were added
 More details about the changes to the current archive of TCGA data:
 - Copy Number Variation | Genotyping Array | TXT files:
  - 22376 Copy Number Segment files replaced (ie removed and added)
  - 22376 Masked Copy Number Segment files replaced
 - Biospecimen | BCR XML files:
  - 11294 files replaced
 - Clinical | BCR XML files:
  - 11160 files removed / 11167 files added (ie 7 extra files)
 - Biospecimen | Diagnostic Slide | SVS files:
  - 11730 Slide Image files added
 - Biospecimen | BCR SSF XML files:
  - 10557 Biospecimen Supplement files added
 - Biospecimen | BCR Auxiliary XML files:
  - 2884 Biospecimen Supplement files added
 - Clinical | BCR OMF XML files:
  - 1051 Clinical Supplement files added
 - Biospecimen | BCR Biotab files:
  - 340 Biospecimen Supplement files added
 - Clinical | BCR Biotab files:
  - 226 Clinical Supplement files added
 - Simple Nucleotide Variation | WXS | VCF | Varscan2 files :
  - 1 Raw Simple Somatic Mutation file removed (2017-03-04)
  - 1 Annotated Somatic Mutation file removed (2017-06-17)
  - both for ESCA samples: TCGA-VR-A8ET-01A-11D-A403-09;TCGA-VR-A8ET-10B-01D-A403-09
 For TARGET data:
 - RNA-Seq data:
  - 3 BAM files and 9 Gene Expression Quantification files removed
  - sample barcodes: TARGET-30-PAKYZS-01A-01R, TARGET-30-PAMEZH-01A-01R, TARGET-30-PANRRW-01A-01R
 - Raw CGI Variant | WGS | Combined Nucleotide Variation | VCF files:
  - 435 files added

* June 4, 2018: metadata tables for GDC data release 11 are now available in BigQuery

* May 8, 2018: the gnomAD database (release 2.0.2, dated October 2017) is now available in BigQuery! **isb-cgc:genome_reference.gnomAD_20171003_GRCh37**

* April 30, 2018: recently released (2018-04-01) ClinVar VCFs are now available in BigQuery! two new tables (**ClinVar_20180401_GRCh37** and **ClinVar_20180401_GRCh38**) can be found in our genome_reference dataset; also available is dbSNP build 151 (announced 2018-04-24): **isb-cgc:genome_reference.dbSNP_b151_GRCh37p13_All** 

* February 22, 2018: a `genenames_mapping <https://bigquery.cloud.google.com/table/isb-cgc:genome_reference.genenames_mapping?pli=1&tab=schema>`_ table has been added to our numerous reference sources in BigQuery to simplify mapping between HGNC IDs, HGNC symbols, Entrez Gene IDs, Ensembl Gene IDs, Pubmed IDs, and RefSeq IDs!

* June 9, 2018: metadata tables for GDC data release 10 are now available in BigQuery

* May 8, 2018: release 85 of the COSMIC database is now available in BigQuery

* February 13, 2018: release 84 of the COSMIC database is now available in BigQuery

* December 19, 2017:  The ISB-CGC cohort metadata has been update to reflect the new and update TARGET gene expression data provided by the GDC in their data release 9. 

* December 6, 2017: the GDC release 9 included some updated and new TARGET gene expression data. The BigQuery table **isb-cgc:TARGET_hg38_data_v0.RNAseq_Gene_Expression** has been updated to reflect this. 

* November 7, 2017: release 83 of the COSMIC database is now available in BigQuery

* November 3, 2017: metadata tables for GDC data release 9 are now available in BigQuery

* October 30, 2017: the 'harmonized' hg38 TCGA VCF files (raw and annotated) are now available in the ISB-CGC controlled-data repository in Google Cloud Storage 

* August 30, 2017: hg38 TARGET VCF files (raw and annotated) are now available in the ISB-CGC controlled-data repository in Google Cloud Storage

* August 3, 2017: release 82 of the COSMIC database is  now available in BigQuery

* June 30, 2017: hg19 and hg38 TARGET WXS, RNA-Seq, and miRNA-Seq BAM files are now available in the ISB-CGC controlled-data repository in Google Cloud Storage

* May 9, 2017: release 81 of the COSMIC database is now available in BigQuery

* May 5, 2017: a table mapping between UniProtKB accessions and identifiers has been added to our reference dataset: **isb-cgc:genome_reference.UniProtKB_idmapping**

* April 10, 2017: We have re-organized our TCGA clinical, biospecimen, and molecular data into new datasets in BigQuery -- please find them at `isb-cgc:TCGA_bioclin_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_bioclin_v0?pli=1>`_, `isb-cgc:TCGA_hg19_data_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_hg19_data_v0?pli=1>`_, and  `isb-cgc:TCGA_hg38_data_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_hg38_data_v0?pli=1>`_.  The hg19 data can also be found in the GDC's `legacy archive <https://portal.gdc.cancer.gov/legacy-archive/search/f>`_, while the hg38 data is available at the `GDC data portal <https://portal.gdc.cancer.gov/>`_.

* March 30, 2017: the 'harmonized' hg38 TCGA miRNA-Seq BAM files from the initial GDC data release are now available in the ISB-CGC controlled-data repository in Google Cloud Storage

* February 20, 2017: in collaboration with the Sanger Institute, the `COSMIC database <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/COSMIC_about.html>`_ is now available in BigQuery (registered users only)

* February 5, 2017: genomic coordinates (in GFF3 format) for human microRNAs added for miRBase v20 and v21 to the **isb-cgc:genome_reference** BigQuery dataset

* January 30, 2017: the final, unified "MC3" TCGA somatic mutations call set is available in the BigQuery **isb-cgc:hg19_data_previews** dataset (also `available on Synapse <https://www.synapse.org/#!Synapse:syn7214402/wiki/405297>`_)

* January 10, 2017: **miRBase_v20** table added to the **isb-cgc:genome_reference** BigQuery dataset

* January 4, 2017: Ensembl gene-set releases 75 (GRCh37) and 87 (GRCh38) are now also available in the **isb-cgc:genome_reference** BigQuery dataset.

* December 30, 2016: the 'harmonized' hg38 TCGA WXS BAM files and RNA-Seq BAM files from the initial GDC data release (1.0), as well as the legacy hg19 TCGA 'Level 2' Genome-Wide SNP6 array genotype files ('birdseed') files are now available in the ISB-CGC controlled-data repository in Google Cloud Storage

* November 16, 2016: TCGA proteomics data from the `CPTAC <https://cptac-data-portal.georgetown.edu/cptacPublic/>`_ (Phase II) is now available in `Google Cloud Storage <https://console.cloud.google.com/storage/browser/isb-cptac-open/Phase_II>`_

* November 14, 2016: TCGA radiology and tissue slide images are now available in Google Cloud Storage!  This includes radiology images (DICOM files) from the `Cancer Imaging Archive <http://www.cancerimagingarchive.net/>`_ (TCIA) and tissue slide images from the `NCI-GDC data portal <https://portal.gdc.cancer.gov/legacy-archive/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22files.data_type%22,%22value%22:%5B%22Tissue%20slide%20image%22%5D%7D%7D%5D%7D>`_ (SVS files).

* September 10, 2016: **GENCODE** versions 19, 22, 23, and 24 are all now available in the **isb-cgc:genome_reference** BigQuery dataset, with an updated and more complete schema -- note also that the naming convention is now **GENCODE_v19** rather than GENCODE_r19; also that v19 is the *last* version based on hg19/GRCh37, and all subsequent versions are based on hg38/GRCh38

* August 31, 2016: a table based on the latest liftOver hg19-to-hg38 chain files is available in the **isb-cgc:tcga_genome_reference** BigQuery dataset

* August 26, 2016: a set of tables based on running Picard over ~67,000 TCGA bam files in GCS have been added to the **isb-cgc:tcga_seq_metadata** BigQuery dataset: information contained in these tables includes bam-index stats, insert-size metrics, quality-distribution metrics, and quality-yield metrics -- these tables can be used in conjunction with the FastQC-based tables to look for bam and/or fastq data files that meet your analysis criteria

* August 21, 2016: new **miRBase_v21** table added to the **isb-cgc:genome_reference** BigQuery dataset

* August 20, 2016: updated **hg19** and **hg38** `Kaviar <http://db.systemsbiology.net/kaviar/>`_ tables added to the **isb-cgc:genome_reference** BigQuery dataset

* August 17, 2016: new **isb-cgc:GDC_metadata** BigQuery dataset containing metadata for both *legacy* and *current* files hosted at the `NCI-GDC <https://gdc.cancer.gov/>`_.

* July 28, 2016: new **isb-cgc:tcga_201607_beta** BigQuery dataset based on the *final* TCGA data upload from the DCC.  This dataset largely mirrors the previous **isb-cgc:tcga_20510_alpha** dataset and is now also supporting the ISB-CGC Web-App.  The curated TCGA cohort tables in the **isb-cgc:tcga_cohorts** BigQuery dataset have also been updated.

* June 24, 2016: an updated listing of all ISB-CGC hosted data in Google Cloud Storage (GCS) is now available in the **GCS_listing_24jun2016** table in the **isb-cgc:tcga_seq_metadata** dataset in BigQuery, in addition the **CGHub_Manifest_24jun2016** table contains the final CGHub Manifest prior to the transition of all data to the `Genomic Data Commons <https://portal.gdc.cancer.gov/>`_.

* June 18, 2016: new **GENCODE_r24** table added to the **isb-cgc:genome_reference** BigQuery dataset

* May 13, 2016: new **NCBI_Viral_Annotations_Taxid10239** table added to the **isb-cgc:genome_reference** BigQuery dataset

* May 9, 2016: new **Ensembl2Reactome** and **miRBase2Reactome** tables added to the **isb-cgc:genome_reference** BigQuery dataset

* May 3, 2016: new **isb-cgc:tcga_seq_metadata** BigQuery dataset contains metadata and FastQC metrics for thousands of TCGA DNA-seq and RNA-seq data files:
    * **CGHub_Manifest** table contains metadata for all TCGA files at CGHub as of April 27th, 2016
    * **GCS_listing_27apr2016** table contains metadata for all TCGA files hosted by ISB-CGC in GCS 
    * **RNAseq_FastQC** table contains metrics derived from FastQC runs on the RNAseq data files, including urls to the FastQC html reports that you can cut and paste directly into your browser
    * **WXS_FastQC** table contains metrics derived from FastQC runs on the exome DNAseq data files

* April 28, 2016: **GO_Ontology** and **GO_Annotations** tables added to the **isb-cgc:genome_reference** BigQuery dataset

* March 14, 2016: with the release of our **Web-App**, controlled-data is now accessible (programmatically) to users who have previously obtained dbGaP approval for TCGA data and go through the NIH authentication process built-in to the Web-App.

* February 26, 2016: new CCLE dataset in BigQuery **isb-cgc:ccle_201602_alpha** includes sample metadata, mutation calls, copy-number segments, and expression data (metadata includes full cloud-storage-path for world-readable BAM and SNP CEL files, and Genomics dataset- and readgroupset-ids for sequence data imported into Google Genomics)

* February 22, 2016: Kaviar database now available in the **isb-cgc:genome_reference** BigQuery dataset

* February 19, 2016: CCLE RNAseq and DNAseq bam files imported into **Google Genomics**

* January 10, 2016: **GENCODE_r19** and **miRBase_v20** tables added to the **isb-cgc:genome_reference** BigQuery dataset

* December 26, 2015: public release of new **isb-cgc:genome_reference** BigQuery dataset: the first table is based on the just-published **miRTarBase** release 6.1

* December 12, 2015: curated TCGA cohort lists available in **isb-cgc:tcga_cohorts** BigQuery dataset

* November 16, 2015: initial upload of data from CGHub into **Google Cloud Storage** (GCS) complete (not publicly released)

* November 2, 2015: first public release of TCGA open-access data in BigQuery tables
   * **isb-cgc:tcga_201510_alpha** dataset contains updated set of BigQuery tables, based on data available at the TCGA DCC as of October 2015
   * includes **Annotations** table with information about redacted samples, etc
   * **isb-cgc:platform_reference** contains annotation information for the Illumina DNA Methylation platform.

* October 4, 2015: complete data upload from TCGA DCC, including controlled-access data

* September 21, 2015: draft set of BigQuery tables (not publicly released)
   * **isb-cgc:tcga_201507_alpha** dataset containing clinical, biospecimen, somatic mutation calls and Level-3 TCGA data available at the TCGA DCC as of July 2015

Future Plans
############

We expect that our future plans will continually evolve based on user feedback, research priorities, 
and the dynamic nature of the Google Cloud Platform.  
Tell us what is important to you at feedback@isb-cgc.org

