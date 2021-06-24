*********
Programs
*********
Uploading your own data is a way of creating custom groupings of the samples and/or cases that you are interested in analyzing further along with the data that is already preexisting in our system, using tools that are on the system. You may frequently reuse the data that was uploaded in multiple analyses. Creating a Program allows you to do this. If you have any existing Programs with data uploaded, they will appear here for you to view, edit and share.

Upload Program Data
####################

Selecting **Upload Program Data** from the **PROGRAMS** menu dropdown displays the **Register a Google Cloud Project** screen, or if you already have a registered Google Cloud Project, it will display the **Data Upload** screen. 

Or, from **Your Dashboard**, click on the **Upload Program Data** link in the **Saved Programs** panel at the bottom of the page. 

If you already have Programs created, they will be listed in the **Saved Programs** panel of your dashboard. Click on the **Saved Programs** link in that panel and this will take you to a page that displays the details of your existing Programs. Alternatively, to go directly to a given Program, click on its name and you will be taken to the program details page of that program.


Registering Cloud Storage Buckets and BigQuery Datasets
=======================================================


.. _registered:

Registering a Google Cloud Storage Bucket and a BigQuery Data Set is a prerequisite for using your own data in ISB-CGC. (Please note: The names of the buckets and data sets are case sensitive.)

**How To Register Buckets and Data sets**

Once you have created a bucket and a dataset in the Google Cloud Console of your Google Cloud Project, you will need to register them with your project name using the Web App.  

**Step 1**: Click on your user icon in the upper right or **Account Details** from the drop down menu under your name.


.. image:: Register_Step_1.png

**Step 2**: Click on the **View** button under **Google Cloud Projects**.


.. image:: Register_Step_2.png

**Step 3**: Click on the project you wish to use.  If you have not registered a project, follow the instructions `here`_.

.. _here: ../controlled-access/Controlled-data-GCP.html

.. image:: Register_Step_3.png

**Step 4**: Use the "Register Cloud Storage Bucket" or "Register BigQuery Dataset" links to add buckets and datasets as needed.


.. image:: Register_Step_4.png


Data Upload Page
================

A New Program
-------------
To start an entirely new program, users should click on the **A New Program** tab on the Data Upload screen.  This will bring up a form where a new program can be defined.  Users should fill out the required fields (Program Name, Project Name) and any optional fields (Program Description, Project Description) that would be helpful.  Clicking on the **Select File(S)** button will bring up a dialog to select the data file for upload. 

**NOTE:** You can upload multiple files in a single step.  The **Type** drop-down should be used to indicate what data type the file represents.  If the data type is one of the choices besides **Other**, the file will have to conform to the specifications below. For a more complete description of the options on this page, see the `Data Upload Page Components`_ section.

Files and File Formats
**********************

  .. _page:

The **Upload Program Data** uses a number of predefined file formats to get data into the system and make it available for use.  The **Other/Generic** file format is the most flexible.  This format assumes that the first row of the file contains the column headers and all subsequent rows contain data.  The remaining file formats are all matrix formats where the first column (or columns in some data types) contain identifiers like gene or miRNA name. The first row contains sample identifiers and the "cells" contain the actual data values.  Examples of the accepted matrix format files are shown below:

**NOTE:** For the matrix files, the text case matters for the required columns (lower case is different from upper case).  In addition, the ISB-CGC system will not validate any identifiers such as barcodes or gene names.  It is up to the user to make sure that uploaded data is correctly identified.


* DNA Methylation

  This is a simple matrix file.  The first column should have the header **Probe_ID**.  Sample barcodes should be the headers for all remaining columns.

  +-----------+-----------+----------+----------+
  | Probe_ID  | Barcode 1 | Barcode 2| Barcode N|
  +===========+===========+==========+==========+
  |Probe ID 1 | Value 1   | Value 2  | Value N  |
  +-----------+-----------+----------+----------+
  |Probe ID 2 | Value 1   | Value 2  | Value N  |
  +-----------+-----------+----------+----------+
  |Probe ID N | Value 1   | Value 2  | Value N  |
  +-----------+-----------+----------+----------+


* Gene Expression

  The Gene Expression matrix file has two required columns:
  
  * **Name**: This is the accession number for the gene. 
  * **Description**: This is the gene symbol for the gene.

  +------------+-------------+----------+-----------+-----------+
  | Name       | Description | Barcode 1| Barcode 2 |Barcode N  |
  +============+=============+==========+===========+===========+
  |Accession 1 | Gene name 1 |  Value 1 | Value 2   | Value N   |
  +------------+-------------+----------+-----------+-----------+
  |Accession 2 | Gene name 3 |  Value 1 | Value 2   | Value N   |
  +------------+-------------+----------+-----------+-----------+
  |Accession N | Gene name N |  Value 1 | Value 2   | Value N   |
  +------------+-------------+----------+-----------+-----------+


* microRNA

  There is one required and one optional column for microRNA:
  
  * **miRNA_ID**: This is generally the ID for the miRNA_ID; required.
  * **miRNA_name**: This can be used to provide alternative names for the miRNA; optional.  If not present, the BigQuery data table will have **null** in this column.
  
  +------------+-------------+----------+-----------+-----------+
  | miRNA_ID   | miRNA_name  | Barcode 1| Barcode 2 |Barcode N  |
  +============+=============+==========+===========+===========+
  |miRNA ID 1  | Alt name 1  |  Value 1 | Value 2   | Value N   |
  +------------+-------------+----------+-----------+-----------+
  |miRNA ID 2  | Alt name 2  |  Value 1 | Value 2   | Value N   |
  +------------+-------------+----------+-----------+-----------+
  |miRNA ID N  | Alt name N  |  Value 1 | Value 2   | Value N   |
  +------------+-------------+----------+-----------+-----------+


* Protein Expression

  Protein Expression has three required columns:
  
  * **Protein_Name**: This is the name or symbol for the protein.
  * **Gene_Name**: This is the name of the gene associated with the protein.
  * **Gene_Id**: This is the accession number for the gene.
  
  +--------------+-------------+-----------+-----------+-----------+-----------+
  | Protein_name |  Gene_Name  | Gene_Id   | Barcode 1 |Barcode 2  |Barcode N  |
  +==============+=============+===========+===========+===========+===========+
  | Protein 1    | Gene Name 1 | Gene ID 1 | Value 1   | Value 2   | Value N   |
  +--------------+-------------+-----------+-----------+-----------+-----------+
  | Protein 2    | Gene Name 2 | Gene ID 2 | Value 1   | Value 2   | Value N   |
  +--------------+-------------+-----------+-----------+-----------+-----------+
  | Protein 3    | Gene Name 3 | Gene ID 3 | Value 1   | Value 2   | Value N   |
  +--------------+-------------+-----------+-----------+-----------+-----------+


* Other/Generic

  Files in Other/Generic format are not matrix files, but rather have the data in columns.  The order of the columns is very flexible, and the upload interface will allow users to define what kind of data is in each of the columns.  The only requirement is that one, and only one, of the columns should be sample barcodes.  In addition, all rows must have the same number of columns.  Any completely blank columns will be flagged and should be removed.  Any columns containing blank entries will have *null* used for the blanks in the BigQuery data table.

  **NOTE:** Currently, each Sample Barcode can only be represented once in a file.  Files with the same barcode on multiple rows will cause a failure.  If you have multiple data values for a single barcode (like gene expression values for multiple genes) you will either have to create a matrix file or upload multiple files using Other/Generic.



.. image:: MouseProject.PNG

Project description and file selection
**************************************

Clicking on the **Next** button brings up a form where users will select which bucket and BigQuery data set the file upload should use.  These buckets and data sets were registered_ according to the process above.  The **Platform** and **Pipeline** fields can contain any useful description a user wishes to provide.

.. image:: Mouse_bucket_and_dataset.png

Lastly, the user should click on the **Upload Data** button to start the process.  Users will first see a page with a message indicating their data is being processed.  Refresh the screen occasionally until either the final page is displayed or an error is shown indicating a problem with loading the file. Your data is being loaded into the BigQuery table you specified earlier for this data set.

.. image:: Mouse_processing.PNG

Correcting Data Uploaded As Other
*********************************
If your data does not fit into any of the existing pre-defined matrix formats, the *Other* data type will allow users to upload data that is in a tabular format.  In this format, the first row of the file is assumed to be the description of each of the columns and all subsequent rows are assumed to be data.  The system will attempt to define what kind of data are in each column; however this process may not always be correct and users must review the column data type assignments before proceeding.

In the example shown below, the automated process has identified two columns as potentially containing Sample Barcodes and has further misidentified a column containing decimal data (numeric float values) as containing categorical (text) data.  The user will need to correct both instances so there is only one Sample Barcode column and define the expression data as decimal.

.. image:: OtherExample.PNG

A New Project For An Existing Program
-------------------------------------
Adding a new project to an existing program follows the same steps as creating a new program.  However, instead of filling out the new program information fields, users should click on the **A New Project For An Existing Program** tab and select an existing program from the drop-down menu.  All other steps for describing and uploading the file will remain the same.

  .. image:: MouseExisting.png



Data Upload Page Components
***************************
This section describes the features found on the Data Upload page.

**Sharing User Uploaded Programs**

This will share the web view of your uploaded program with users you select by entering the users email. The user will receive an email
message with a link to your shared uploaded program explaining that you wanted to share a program with them and that you have invited
them to join. If the email address you entered in not registered in the database, you are prompted with a message saying, "The following user emails could not be found; please ask them to log into the site first:(email entered)."


**System Data Dictionary Link**

This link goes to the System Data Dictionary which is a comprehensive list of all clinical data fields and possible values.  This dictionary can be helpful in aligning metadata from the imported program to ISB-CGC data fields.


**High Level Data Files**

High level data files usually represent some level of data analysis as opposed to raw files.  High level files can be used in Workbooks and visualized alongside ISB-CGC data.

**Low Level Files for API Access**

Files uploaded as low-level files for API access will not be usable in the Web App, but rather will appear in the user's Google Storage Bucket.  This feature is intended for files like BAM or VCF files that contain more raw data.

**File Type**

This is the data type of the uploaded file.  Currently the allowed data types are:

* Gene Expression
* miRNA Expression
* Protein Expression
* Methylation
* Other

**File Format Requirements**

All files must be tab delimited and meet the formatting requirements described in `Files and File Formats`_.

.. image:: MouseProjectAnnotated.png

Saved Programs
##############

Selecting **Saved Programs** from the **PROGRAMS** menu dropdown displays the **Programs** screen, **SAVED PROGRAMS** tab. This screen displays your saved programs and allows you to edit or delete them, as well as start a new workbook using your favorite.

Clicking on the **Upload Data** button will take you to the **Register a Google Cloud Project** screen.


Public Programs
###############

Selecting **Public Program** from the **PROGRAMS** menu dropdown displays the **Programs** screen, **PUBLIC PROGRAMS** tab. This screen displays details about the public programs currently available in the Web App. It displays the number of projects, the ownership and the last date each program was updated.

Clicking the + adjacent to each program will display a list of all projects in the program, and their last updated dates.

