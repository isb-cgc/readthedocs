*****************
CPTAC Data Set
*****************

About the NCI Clinical Proteomic Tumor Analysis Consortium
------------------------------------------------------------
The `National Cancer Institute’s Clinical Proteomic Tumor Analysis Consortium <https://proteomics.cancer.gov/programs/cptac>`_ (CPTAC) is a national effort to accelerate the understanding of the molecular basis of cancer through the application of large-scale proteome and genome analysis or proteogenomics.

About the NCI Clinical Proteomic Tumor Analysis Consortium Data Set
---------------------------------------------------------------------

**From GDC**

CPTAC data obtained through the Genomic Data Commons (GDC) consists of whole-genome sequencing, whole-exome sequencing, RNA sequencing, and miRNA sequencing.  The program analyzed more than 700 cases. The GDC currently has controlled VCF, TSV, and BAM data available. The Project ID in the GDC Data Portal is `CPTAC-2 <https://portal.gdc.cancer.gov/projects/CPTAC-2>`_ and `CPTAC-3 <https://portal.gdc.cancer.gov/projects/CPTAC-3>`_.

For more information on the CPTAC data, please refer to these sites:

- `CPTAC-2 dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000892>`_
- `CPTAC-3 dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001287.v5.p4>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D&searchTableTab=files>`_

**From PDC**

ISB-CGC also has proteomic CPTAC data, obtained from the `Proteomics Data Commons (PDC) <https://pdc.cancer.gov/pdc/>`_ API. This includes clinical and protein expression data for breast, ovarian, colon, liver, lung, uterine and other cancers. 

The NCI CPTAC has generated a tremendous amount of valuable quantitative proteomics data derived from clinical cancer specimens and makes them publicly accessible to the community. We have imported the data into Google BigQuery, where they can be queried via SQL and easily joined with data tables from TCGA using the BigQuery interface or programmatically with the BigQuery API.

Which studies are available?

- CCRCC - Clear cell renal cell carcinoma
- GBM - glioblastoma multiforme
- HNSCC - Head and neck squamous cell carcinoma
- LUAD - lung adenocarcinoma
- UCEC - Uterine Corpus Endometrial Carcinoma
- Breast cancer
- Colon cancer
- Ovarian cancer

Most studies have both whole proteome as well as phosphoproteome. A few studies also have acetylome and glycoproteome data.

What processing of the raw data is available here?

- Most data have been processed by the original producers and presented in publications.
- The same raw data have been processed uniformly through the CPTAC Common Data Analysis Pipeline (CDAP).
- We provide here the results from the CDAP sourced from the PDC API.

Important considerations:

- All abundances are presented as log2 ratios as computed by the CDAP.
- Abundances are comparable within each study since the same reference was used within each study.
- However, different controls were used for different studies, and therefore extreme caution should be used when comparing abundance values between different studies.
- Some PDC datasets are embargoed, which means that the data may be examined prior to the end of the embargo period, but no manuscripts may be published until the embargo expires. Currently, ISB-CGC does not host any embargoed data in our BQ datasets.

Python Jupyter Notebooks showing examples of queries of PDC CPTAC data are available at:

* `How do I explore CPTAC protein abundances? <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_explore_CPTAC_protein_abundances.ipynb>`_

* `How do I compare protein and gene expression in CPTAC? <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_compare_protein_and_gene_expression_CPTAC.ipynb>`_

* `Compute correlations of protein and gene expression in CPTAC <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/Correlations_Protein_and_Gene_expression_CPTAC.ipynb>`_

* `Comparing protein expression from different pipelines - CPTAC <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/Comparing_protein_expression_from_different_pipelines_CPTAC.ipynb>`_
 

Accessing the NCI Clinical Proteomic Tumor Analysis Consortium Data on the Cloud
----------------------------------------------------------------------------------

Besides accessing the GDC files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the CPTAC files. Here is an example to find CPTAC-2 GDC files:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'CPTAC' and project_short_name = 'CPTAC-2'
  AND active.file_gdc_id = GCSurl.file_gdc_id
  
Here is an example to find CPTAC-3 GDC files:  

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'CPTAC' and project_short_name = 'CPTAC-3'
  AND active.file_gdc_id = GCSurl.file_gdc_id
  

Accessing the CPTAC Data in Google BigQuery
------------------------------------------------

ISB-CGC has GDC CPTAC data, such as clinical, RNA-Seq and somatic mutation, and PDC CPTAC data, such as clinical and protein expression, stored in Google BigQuery tables. 

Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with CPTAC2 and/or CPTAC3 selected for filter PROGRAM. 
To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The CPTAC tables are in project isb-cgc-bq. 

- Data set ``isb-cgc-bq.CPTAC`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.CPTAC_versioned`` contains previously released tables, as well as the most current table.

Note that some data are part of a CPTAC2 retrospective study of TCGA data. These tables are labeled as both program CPTAC2 and TCGA and can be found by filtering for either. The tables are in project isb-cgc-bq.

- Data set ``isb-cgc-bq.TCGA`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.TCGA_versioned`` contains previously released tables, as well as the most current table.

In addition, there are some tables with CPTAC data derived from the 2017 paper `Proteogenomics connects somatic mutations to signalling in breast cancer <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5102256/>`_. These are in data set ``isb-cgc.hg19_data_previews``. They are labeled with programs CPTAC2 and TCGA and source LIT (for literature).

To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.
Here is an example of a PDC CPTAC table viewed in the Google BigQuery console: `quant_acetylome_prospective_breast_BI_pdc_current <https://console.cloud.google.com/bigquery?p=isb-cgc-bq&d=CPTAC&t=quant_acetylome_prospective_breast_BI_pdc_current&page=table>`__
