***************************************************
A guided tour of cancer data analysis using ISB-CGC
***************************************************

**Demo Use-Case**

We are interested in analyzing gene expression and protein abundance differences between two types of TCGA kidney cancers, Kidney Renal Clear Cell Carcinoma (KIRC) and Kidney Renal Papillary Carcinoma (KIRP). In this demo, we build our cohort of patients with these cancer types and extract their respective gene expression and protein abundance data all from Google BigQuery. We will demonstrate how to: 

- Identify tables of interest using ISB-CGC BigQuery Table Search UI 
- Navigate to tables and build queries in Google BigQuery Console directly from the ISB-CGC BigQuery Table Search page 
- Link to R notebooks in the Google AI Platform for data interrogation and plot visualization 
- Use Bioconductor packages designed for TCGA data on ISB-CGC BigQuery tables


1)	Navigate to the ISB-CGC homepage: https://isb-cgc.org and click on the BigQuery Table Search.

.. image:: ISB-homepage.png


2)	For this demo, we will search for ISB-CGC hosted BigQuery tables that contain information for TCGA gene expression, protein expression and clinical data. 

.. image:: BQTableSearch-demo.png

3)	We want to build a cohort of TCGA patients for which both gene expression and protein abundance data exists. Let’s search for TCGA in the Program filter and Clinical Data, Gene Expression, and Protein Expression in the Data Type filter. 

4)	We can preview the clinical table and see the table schema by clicking the (+) icon.

.. image:: BQTableSearch-TCGA.png

5)	We can navigate to the Google Cloud Platform (GCP) BigQuery Console by clicking on the “open” button under the table preview or on the “magnifying glass” icon on the right hand side of the Table Search row. 

.. image:: BQTableSearch-Open.png

