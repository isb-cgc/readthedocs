******************************
ISB-CGC BigQuery Table Search 
******************************

The ISB-CGC BigQuery Table Search UI ( `<https://isb-cgc.appspot.com/bq_meta_search//>`_) is a discovery tool that allows users to explore and search for ISB-CGC hosted BigQuery tables. It can be accessed directly from the ISB-CGC homepage (`<https://isb-cgc.org/>`_) as shown in red in the image below. 

**Note**: Users are not required to have a Google Cloud Platform (GCP) project or an account to learn more about the tables hosted by ISB-CGC.

.. image:: BigQueryTableSearchUI.png
   :align: center




Currently, ISB-CGC hosts over 300 open access BigQuery tables. Each table has been curated to include detailed table and field descriptions as well as table labels allowing users to search for BigQuery tables of interest using a free-form text search or via available filters. 



.. image:: BigQueryTableSearch-UI-homepage.png
   :scale: 25
   :align: center




Links to various helpful documentation pages are available, including Google BigQuery's documentation and ISB-CGC's Community Notebook repository which contains example use-cases on how to access BigQuery tables programmatically via Jupyter notebooks or R scripts.


.. image:: BigQueryTableSearch-Documentation.png
   :align: center


Filters
-------

The search filters consist of a combination of multi-select dropdown lists, checkboxes and free-form text fields. 

Selecting multiple items within a multi-select dropdown list or checkbox filter will perform a Boolean "AND" on those selections and bring back any data that match any of the selected items. For example, selecting Data Type BIOSPECIMEN and CLINICAL will display both biospecimen and clinical data.

Selecting multiple filters will perform a Boolean "OR" on those selections and bring back only data that fits all criteria. For example, selecting Data Type BIOSPECIMEN and Source of CCLE will only display CCLE biospecimen data.

Information about each filter is detailed below.

**Status**

We are committed to providing the most up-to-date information in our BigQuery tables but realize that at times researchers need to reference older versions of data. Each table is assigned a status based on the following criteria:

   * Tables with the most up-to-date available information are given a status of **current**
   * Tables with older versions of data are given a status of **archived**
   * Tables that have data that is no longer supported are **deprecated**
   
By default, the Status filter is set to Current.   
   
.. image:: Status-filter.png
   :align: center
   
   
**Categories**

The tables are grouped into four high-level categories: 

* Clinical Biospecimen Data : Patient case and sample information (includes clinical tables with patient demographic data, and                               biospecimen data with detailed sample information)

* File Metadata : Information about raw data files including Google Cloud Storage Paths (includes tables with information                       about files available at the GDC, including GCS paths, creation dates, sizes, etc.)

* Genomic Reference Database: Genomic information that can be used to cross-reference against processed-omics data tables                                   (examples include  COSMIC, ClinVar, cytoBand, dbSNP, Ensembl, Ensembl2Reactome)

* Processed-omics  Datasets: Processed data primarily from the GDC (i.e. raw data that has gone through GDC pipeline                                        processing e.g. gene expression, miRNA expression, copy number, somatic mutations, methylation)


Click on one or more checkboxes to select categories. 
Hovering the cursor over the information icon will display a short description of the category.

.. image:: Category-filter.png
   :align: center


**Reference Genome Build**

Filter for tables that contain data for hg19 or hg38. In a few cases, there are tables which contain information from both genome builds; for example, tables that include liftover coordinates between the reference builds. 

By default, the **Reference Genome** filter is set to ALL.  

.. image:: GenomeReference-filter.png
   :align: center


**Source**

Search through the sources of the data in our BigQuery tables by using the **Source** filter. Click the Source box to see the dropdown list and click on a source to select it. Additional sources can be selected by clicking in the Source box again. 


.. image:: Source-filter.png
   :align: center


**Data Type**

The **Data Type** filter also allows you to filter for data types of interest. Like Source, multiple Data Types can be selected.

.. image:: DataType-filter.png
   :align: center


**More Filters**

The **Show More Filters** button can be used to display **Dataset ID**, **Table ID**, **Table Description**, **Labels** and **Field Name** filters. These are free-form text fields; the user can type all or a portion of the name into the field to perform the query. For instance, for all datasets which have "alpha" in the name, type "alpha" into the field.

These fields are most useful for users already familiar with the BigQuery tables.


**Labels**

Each table was tagged with labels relating to the source, data type, reference genome build, status, and access. Users can search on any of these tags on the Labels filter field. Users can find the **Labels** search filter under the **Show More Filters** option. 

The labels for a table can be viewed when the blue plus sign (+) to the left of the table row is clicked. See the screen shot below.


Search Results
--------------

Each row will display the Dataset ID, Table ID, Status, Category, Source, Data Type, number of rows and Created Date of the table. 

Click on the column header to sort the displayed results by that column.

To further filter the results, use the **Search** box above the results, on the right-hand side. This is a free-form text field; the user can type all or a portion of the seach item into the field to perform the query. This searches all fields in the table.

To export the results of your search to a file in Comma Separated Values (CSV) format, click the **CSV Download** button.

Schema Description
++++++++++++++++++

For detailed table information, including full table ID, table description and field descriptions, click on the blue plus sign (+) on the left-hand side. Table labels (as described above) will also display.

.. image:: BigQueryTableSearchUI-descriptions.png
   :align: center

Table Preview
++++++++++++++

A few rows of the data in a BigQuery table can be viewed by clicking on the **Preview** button on the right-hand side. This feature allows the user to get a better idea of the contents and format of the data.


.. image:: BigQueryTableSearch-PreviewTableOption.png
   :align: center
 
 
Table Access
++++++++++++

For full-access to the tables including the ability to query the tables, please see the following ISB-CGC documentation pages:

`How to create a Google Cloud Platform (GCP) project <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/HowToGetStartedonISB-CGC.html/>`_ 

`How to link ISB-CGC BigQuery tables to your Google Cloud Platform (GCP) project <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/progapi/bigqueryGUI/LinkingBigQueryToIsb-cgcProject.html/>`_ 



