*******************
Saved Cohorts
*******************

Cohorts are a way of creating custom groupings of the samples and/or participants that you are 
interested in analyzing further.  You may frequently re-use a cohort in multiple analyses.  Creating a "saved cohort" allows you to do this.  If you have existing saved cohorts, they will be appear here for you to view, edit and share (see below for details).

Creating and saving a cohort
############################

To create a cohort from Your Dashboard, if you do not have a cohort created, click on the “Create Cohort” link in the "Saved Cohorts" panel at the bottom of the page. This will take you to the cohort creation page.

If you already have saved cohorts, they will be listed in the "Saved Cohorts" panel.  Click on the "Saved Cohorts" link in that panel and this will take you to a page that displays the details of your saved cohorts.  To create a new saved cohort, use the "Create New Cohort" button on the page listing your current saved cohorts.

Cohort Creation Page
====================

Using the provided list of filters on the left hand side, you can select the attributes and features
that you are interested in.
By clicking on a feature, the field will expand and provide you with additional filtering options.
For example, when you click on “Vital Status”, it expands and provides a list of “Alive”, “Dead”, and
“NA” as options to
choose from. Selecting one or more of these will cause the filter(s) to appear in the Selected Filters 
panel and visualizations on the page
will be updated to reflect that the current cohort that has been filtered by Vital Status. 
The numbers beside the selectable
filter values reflect the number of samples that have that attribute based on all other filters that 
have been selected.  Filters are "ANDed" together, meaning that selecting two filters means that the participants and samples are created based on both filters being executed.  There may be cases where you have 0 participants and samples, because the combination of filters you have chosen are ALL not present (AND function).

Cohort Filters
--------------
The panel on the left of the screen, with two tabs called "Donor" and "Data Type" allow you to apply filters to the cohorts your are creating.  Below are the details of each tab.

Donor Tab
^^^^^^^^^^^^^^^^^^^^^^^^

    * Public Projects
    * Public Studies (mouse over feature will display disease name if it is part of the TCGA dataset)
    * Vital Status
    * Gender
    * Age At Diagnosis
    * Sample Type Code
    * Tumor Tissue Site
    * Histological Type
    * Prior Diagnosis
    * Pathologic Stage
    * Tumor Status
    * New Tumor Event After Initial Treatment
    * Histological Grade
    * Residual Tumor
    * Tobacco Smoking History
    * ICD-10
    * ICD-O-3 Site
    * ICD-O-3 Histology

Data Type Tab
^^^^^^^^^^^^^^^^^^^^^^

    * DNA Sequencing
    * RNA Sequencing
    * MIRNA Sequencing
    * Protein
    * SNP CN
    * DNA Methylation

Save As New Cohort Button
^^^^^^^^^^^^^^^^^^^^^^^^^

Push this button if you wish to save the cohort based on the filters you have set.  You will be asked for a cohort name and the selected filters will be displayed.  Enter the name (any text) and push the "Create Cohort" button.

Selected Filters Panel
^^^^^^^^^^^^^^^^^^^^^^

This is where selected filters are shown so there is an easy way to see what filters have been selected.
If you have not saved the cohort yet, clicking on “Clear All” will remove all selected filters.  Also, if you have not saved the cohort yet, selecting an X beside a single filter will remove that filter.  If you have saved the filter, the X is not present as this function is disabled in saved cohorts.

Clinical Features Panel
^^^^^^^^^^^^^^^^^^^^^^^

This panel shows a list of images (called "treemaps") that give a high level breakdown of the selected samples for a 
handful of features:
* Study
* Vital Status
* Sample Type
* Tumor Tissue Site
* Gender
* Age at Initial Pathologic Diagnosis
By using the “Show More” button, you can see the last two tree maps.

Data Availability Panel
^^^^^^^^^^^^^^^^^^^^^^^

This panel shows a parallel sets graph of available data for the selected samples in the cohort. The large headers over
the vertical bars are data types. Each data type (vertical bar) is subdivided according to the different platforms
that were used to generate this type of data (with "NA" indicating samples for which this data type is not available).
Each sample in the current cohort is represented by a single line that "flows" horizontally from left to right,
crossing each vertical bar in the appropriate segment.
Hovering on a swatch between two vertical bars, you will see the number of samples that have data from those
two platforms. 
You can also reorder the vertical categories by dragging the headers left and right and reorder the
platforms by dragging the platform names up and down.

Operations on Cohorts
#####################

Set Operations
==============

You can create cohorts using set operations on the User Dashboard page.

To activate the set operations button, you must have at least one cohort selected in your "Cohorts" page. Upon clicking the “Set Operations”
button, a dialogue box will appear. Here you may do the following things:

* Enter in a name for the new cohort you’re about to create.
* Select a set operation.
* Edit cohorts to be used in the operation.
* Add A Cohort

The intersect and union operations can take any number of cohorts and in any order.
The complement operation requires that there be a base cohort, from which the other cohorts will be subtracted from.

The figure below shows what the results of the set operations will be (represented by I for Intersect, U for Union, and C for Complement).  There are two types of sets shown, those that overlap (on the left) and those that are nested (on the right).  For the last row (complement operations), the "Subtracted" area is removed from the "Base" area to result in the Complement (C). 

.. image:: SetOperations.PNG
   :scale: 50
   :align: center

Click “Okay” to complete the set operation and create the new cohort.

Viewing and Editing a Cohort
============================

Once you have created a "Saved Cohort" you can view and edit it.  To view a cohort, select it by clicking on its name either from the "Saved Cohorts" panel on the main "Your Dashboard" page or on the "Cohorts" page listing all your saved cohorts.

Cohort Details Page
-------------------
When you have gone to your saved cohort page, you will be shown the details of the cohort on the "SAVED COHORTS" tab.  The "PUBLIC COHORTS" tab shows public cohorts that are commonly selected.  these can be used for a "New Workbook" and "Set Operations".

From the "SAVED COHORTS" tab you can:

* New Workbook: Pushing this button creates a New Workbook using the selected Cohorts
* Edit: Pushing this button makes the filters panel appear. And filters selected will be additive to any filters that have already been selected. To return to the previous view, you much either save any selected filters (with the "Save Changes" button), or choose to cancel adding any new filters (by clicking the "cancel" link).
* Comments: Pushing “Comments” will cause the Comments panel to appear. Here anyone who can see this cohort can comment on it. Comments are shared with anyone who can view this cohort.  They are ordered by newest on the bottom.  Selecting the "X" on the Comments panel will close the panel.  Any user who owns or has had a cohort shared with them can comment on it.
* Duplicate: Making a copy will create a copy of this cohort with the same list of samples and patients and make you the owner of the copy.
* Delete: Allows you to delete this cohort (if you confirm by clicking the second delete button presented)
* Share: A dialogue box appears and the user is prompted to select users that are registered in the system to share the cohort with.

Selected Filters Panel
----------------------

This panel displays any filters that have been used on the cohort or any of its ancestors. These cannot be modified and
any additional filters applied to this cohort will be appended to the list.

Details Panel
-------------

This panel displays the number of samples and participants in this cohort. These vary because some participants may have
provided multiple samples.
This panel also displays “Your Permissions” which can be either owner or reader, as well as revision history.

Clinical Features Panel
-----------------------

This panel shows a list of treemaps that give a high level break of the samples for a handful of features:

* Study
* Vital Status
* Sample Type
* Tumor Tissue Site
* Gender
* Age at Initial Pathologic Diagnosis

Data Availability Panel
-----------------------
This panel shows a parallel sets graph of available data for the selected samples in the cohort. The large headers over
the vertical bars are data types. Each data type is broken up into their different platforms and “NA” for samples that
do not have that data type. The bars that flow horizontally indicate the number of samples that have that data. By
hovering on a horizontal segment between the first two bars, you will see the number of data that have both those data
type platforms. You can also reorder the vertical categories by dragging the headers left and right and reorder the
platforms by dragging the platform names up and down.

.. _ViewFileList:

View File List
--------------
“View File List” takes you to a new page where you can view the file list associated to the cohort you are looking at.
The file list page provides a paginated list of files available with all samples in the cohort. Here, “available” refers
to files that have been uploaded to the ISB-CGC Google Cloud Project and that are open access data. You can use the
“Previous Page” and “Next Page” to show more values in the list.

You may filter on these files if you are only interested in a specific data type and platform. Selecting a filter will
update the list associated. The numbers next to the platform refers to the number of files available for that platform.
There is only one menu item available and that is the “Download File List as CSV”. Selecting this item will begin a
download process of all the files available for the cohort, taking into account the selected Platform filters. The file
contains the following information for each file:

* Sample Barcode
* Platform
* Pipeline
* Data Level
* File Path to the Cloud Storage Location

Viewing a Sequence
==================

When available, sequences in a cohort can be viewed using the IGV viewer.  To find those sequences that can be viewed with the IGV viewer, open a cohort and select the "View File List" link at the bottom of the "Public Data Availability" panel.  The files associated with your cohort will be shown, with the last column showing if there is a view of the sequence available through the IGV viewer (indicated by a checkmark and "Go to IGV").  Selecting that link will take you to the sequence view of the file, viewed in the IGV viewer.

Deleting a cohort
=================

From the "SAVED COHORTS" page:
Select the cohorts that you wish to delete using the checkboxes next to the cohorts. When one or more are selected, the
delete button will be active and you can then proceed to deleting them.

From within a cohort:
If you are viewing a cohort you created, then you can delete the cohort using the delete button on the menu.

Creating a Cohort from a Visualization
======================================

To create a cohort from a visualization, you must be in plot selection mode. If you are in plot selection mode, the
crosshairs icon in the top right corner of the plot panel should be blue. If it is not, click on it and it should turn
blue.

Once in plot selection mode, you can click and drag your cursor of the plot area to select the desired samples. For a
cubbyhole plot, you will have to select each cubby that you are interested in.

When your selection has been made, a small window should appear that contains a button labelled “Save as Cohort”. Click
on this when you are ready to create a new cohort.

Put in a name for you newly selected cohort and click the “Save” button.

Copying a cohort
================

Copying a cohort can only be done from the cohort details page of the cohort you want to copy.

When you are looking at the cohort you wish to copy, select Duplicate from the top menu.

This will take you to your copy of the cohort.
