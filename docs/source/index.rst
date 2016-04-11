.. ISB-CGC documentation master file, created by
   sphinx-quickstart on Sun Dec 20 11:20:02 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

*****************************
The ISB Cancer Genomics Cloud
*****************************

Welcome to the ISB-CGC Documentation on Read the Docs.

Here you will find information describing the features of the ISB-CGC platform, 
tips on how to use it, and details about the data that we are hosting on the 
Google Cloud Platform.

.. image:: new-block-three-p.png
   :scale: 100
   :align: center

The ISB-CGC aims to serve the needs of a broad range of cancer researchers ranging from 
scientists or clinicians who prefer to use an interactive web-based application to access 
and explore the rich TCGA dataset, to computational scientists who want to write their own 
custom scripts using languages such as R or Python, accessing the data through APIs, and 
to algorithm developers who wish to spin up thousands of virtual machines to analyze hundreds 
of terabytes of sequence data.

The table below describes the types of functions that can be performed in ISB-CGC and provides links to how to documentation on how to do those functions.

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Function                           |In GUI                                                                                                                                                                                      |With Command Line                                                                                                                                                 |
+===================================+============================================================================================================================================================================================+==================================================================================================================================================================+
|Work on the Google Cloud Platform  |- Google Console <www.cnn.com>                                                                                                                                                              |- Command line from local Linux machine                                                                                                                           |
|- Projects                         |                                                                                                                                                                                            |                                                                                                                                                                  |
|- ???                              |                                                                                                                                                                                            |                                                                                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Explore what data available        |- `Documentation <Hosted-Data.html>`_                                                                                                                                                       |- BigQuery `R and Python Tutorials </progapi/Tutorials.html>`_                                                                                                    |
|                                   |- `GUI </webapp/Saved-Cohorts.html>`_                                                                                                                                                       |- ISB-CGC `Endpoints </progapi/Programmatic-API.html>`_                                                                                                           |
|                                   |                                                                                                                                                                                            |- Google Genomics APIs `from cohort </progapi/progapi2/google_genomics_from_cohort.html>`_ or `from sample </progapi/progapi2/google_genomics_from_sample.html>`_ |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Understand detals of data          |- `Access TCGA controlled data </webapp/Gaining-Access-To-TCGA-Contolled-Access-Data.html>`_                                                                                                |- For data in BigQuery                                                                                                                                            |
|                                   |- `View File List <search.html?q=view+file+list>`_ in GUI                                                                                                                                   | - BigQuery `Command Line Tool <https://cloud.google.com/bigquery/bq-command-line-tool-quickstart>`_                                                              |
|                                   |- View Sequences with `IGV </webapp/IGV-Browser.html>`_                                                                                                                                     | - BigQuery `Command Line Tool <https://cloud.google.com/bigquery/bq-command-line-tool-quickstart>`_                                                              |
|                                   |- `Google BigQuery Web UI </progapi/bigqueryGUI/WalkthroughOfGoogleBigQuery.rst>`_                                                                                                          |- For data in Google Cloud Storage                                                                                                                                |
|                                   |- `Google API Explorer <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/>`_                                                             | - BigQuery `REST API <https://cloud.google.com/bigquery/bigquery-api-quickstart>`_                                                                               |
|                                   |                                                                                                                                                                                            | - Google `Cloud Storage JSON API <https://cloud.google.com/storage/docs/json_api/>`_                                                                             |
|                                   |                                                                                                                                                                                            | - Google Cloud Storage `gsutil <https://cloud.google.com/storage/docs/gsutil>`_                                                                                  |
|                                   |                                                                                                                                                                                            |- For data in Google Genomics                                                                                                                                     |
|                                   |                                                                                                                                                                                            | - `Google Genomics REST API <https://cloud.google.com/genomics/reference/rest/>`_                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Create cohorts of patients         |- `Create cohorts </webapp/Saved-Cohorts.html>`_                                                                                                                                            |- Use GUI saved cohorts in ISB-CGC `Endpoints </progapi/Programmatic-API.html>`_                                                                                  |
|                                   |- Cohorts `set operations <search.html?q=set+operations&check_keywords=yes&area=default>`_                                                                                                  |                                                                                                                                                                  |
|                                   |- Create a cohort from visualization (`background <search.html?q=Creating+a+Cohort+from+a+Visualization&check_keywords=yes&area=default'_ and `tool image <search.html?q=Selection+Icon>`_ |                                                                                                                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Add your data to the cloud         |                                                                                                                                                                                            |- blocks.                                                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Analyze your data with TCGA data   |                                                                                                                                                                                            |- blocks.                                                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|Run bioinformatics pipelines/tools |                                                                                                                                                                                            |- blocks.                                                                                                                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

This documentation is a work-in-progress, please let us know how we can improve 
it! feedback@isb-cgc.org 

-- the ISB-CGC team

Contents
########

.. toctree::
   :maxdepth: 1

   sections/About-ISB-CGC
   sections/Hosted-Data
   sections/Prog-APIs
   sections/Web-UI
   sections/FAQ
   sections/Support

