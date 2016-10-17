********************
Project Data Upload
********************

Uploading your own data is a way of creating custom groupings of the samples and/or participants that you are interested in analyzing further with the data that is already preexisting in our system. You may frequently re-use the data that was uploaded in multiple analyses. Creating a “Project” allows you to do this. If you have any existing Projects with data uploaded, they will appear here for you to view, edit and share (see below for details).

Creating and Saving a New Project
#################################
To create a new project from Your Dashboard, if you do not have a project created, click on the “Upload Project Data” link in the “Saved Projects” panel at the bottom of the page. This will take you to the Data Upload page.

If you already have Projects created, they will be listed in the “Saved Projects” panel. Click on the “Saved Projects” link in that panel and this will take you to a page that displays the details of your existing Projects. Alternatively, to go directly to a given Project, click on its name and you will be taken to the project details page of that project.

To create a new project, use the “Upload Project Data” link.


Registering Cloud Storage Buckets and BigQuery Datasets
=======================================================
You will need to have a BigQuery Dataset and a Google Cloud Storage bucket registered to you Google Cloud Project through the Google Project details page in the UI. (Please note: It is case sensitive.)


Data Upload Page
================

A New Project
-------------


A New Study For An Existing Project
------------------------------------


Data Upload
-----------

System Data Dictionary Link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

High Level Data Files
^^^^^^^^^^^^^^^^^^^^^

Low Level Files for API Access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Data Types That Can Be Uploaded
-----------------------------------------

* DNA Methylation
* Gene Expression
* microRNA
* Protein Expression
* Other

Review Files
-------------

On this page you select which Google Cloud Bucket and BigQuery dataset you upload your data to. 
The System Data Dictionary link can be found on this page as well for reference. 
You must label a platform and pipeline for the file(s) you choose to upload.  Selecting the Upload Data button will submit your files for processing. 

(Please Note: If you select Other for Data Type you will need to label each column of file with the proper type i.e Integer, decimal, categorical.)

Projects Page
=============

Saved Projects
--------------
Drop Down Arrow
^^^^^^^^^^^^^^^
* Edit
* Delete
* New Workbook

Plus Symbol(+)
^^^^^^^^^^^^^^^


Public Projects
----------------

Drop down Arrow
^^^^^^^^^^^^^^^^
* New Workbook

Plus Symbol(+)
^^^^^^^^^^^^^^

Upload Data Button
--------------------



Existing Projects Details Page
==============================

New Workbook Button
--------------------

Upload Data Button
-------------------

Edit Details Button
---------------------

Delete Button
-------------

Share Button
-------------

Studies Description Panel(s)
----------------------------

This section displays the description of the study added to the project if one was provided. The date of creation, number of files,and which cloud storage buckets and BigQuery Dataset each is associated to. The settings gear to the left of the Study name allows you to create a new Workbook with only the one study or delete the study. 
