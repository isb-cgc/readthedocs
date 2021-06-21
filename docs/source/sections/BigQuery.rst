
***********************
ISB-CGC BigQuery Tables
***********************

Google BigQuery (BQ) is a massively-parallel analytics engine ideal for working with tabular data. Leveraging the power of BigQuery, we have made the information scattered over tens of thousands of XML and tabular data files in legacy and active archives at the NCI GDC and PDC much more accessible in the form of open-access BigQuery tables. 

We have made the ability to explore and learn more about the ISB-CGC hosted BigQuery tables easy via an interactive BigQuery Table Search UI (https://isb-cgc.appspot.com/bq_meta_search/). Users can find tables of interest based on program, category, reference genome build, data type and free-form text search. 

Using SQL in the Google BigQuery Console, in Juypter notebooks or in R, users with Google Cloud Platform (GCP) projects can analyze patient, biospecimen, and molecular data for many cancer programs such as TCGA, TARGET, CCLE, GTEx from ISB-CGC's BigQuery tables. 

Note that dbGaP authorization is not required to access most tables. 

**Additional Support**

For more information about Google BigQuery, see the following Google support pages:

- `Google BigQuery documentation <https://cloud.google.com/bigquery/docs>`_

- `What is BigQuery? <https://cloud.google.com/bigquery/what-is-bigquery>`_


.. toctree::
   :hidden:
   :maxdepth: 1

   progapi/bigqueryGUI/HowToAccessBigQueryFromTheGoogleCloudPlatform
   BigQuery/ISBCGC-BQ-Projects
   progapi/bigqueryGUI/LinkingBigQueryToIsb-cgcProject
   progapi/bigqueryGUI/GettingStartedWithGoogleBigQuery
   BigQuery/VariantDataInBigQuery
   BigQuery/UserDefinedFunctions
   BigQuery/BigQueryUsageCosts

   
  
  




