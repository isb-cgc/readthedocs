*******
Cohorts
*******

Cohorts are a way of creating custom groupings of the samples and/or participants that you are 
interested in analyzing further.
For example, you can create cohorts that span across multiple projects, only contain samples for
which certain types of data are avaialble, or focus on specific phenotypic characteristics.

Creating and saving a cohort
############################

To create a cohort from the User Dashboard, click on the “+ Create” button and select “New Cohort”. 
This will take you to the cohort creation page.

Cohort Creation Page
====================

Using the provided list of filters on the left hand side, you can select the attributes and features
that you are interested in.
By clicking on a feature, the field will expand and provide you with additional filtering options.
For example, when you click on “Vital Status”, it expands and provides a list of “Alive”, “Dead”, and
“None” as options to choose from. 
Selecting one or more of these will cause these filter(s) to appear in the Selected Filters 
panel and visualizations on the page
will be updated to reflect that the current cohort is the result of the specified filtering operations.
The numbers beside the selectable
filter values reflect the number of samples that have that attribute based on all other filters that 
have been selected.

Cohort Filters
--------------

Participant Filters List
^^^^^^^^^^^^^^^^^^^^^^^^

    * Project
    * Study
    * Vital Status
    * Gender
    * Age At Diagnosis
    * Sample Type Code
    * Tumor Tissue Site
    * Histological Type
    * Prior Diagnosis
    * Pathologic State
    * Tumor Status
    * New Tumor Event After Initial Treatment
    * Histological Grade
    * Residual Tumor
    * Tobacco Smoking History
    * ICD-10
    * ICD-O-3 Histology
    * ICD-O-3 Site

Data Type Filters List
^^^^^^^^^^^^^^^^^^^^^^

    * DNA-Sequence
    * RNA-Sequence
    * miRNA-Sequence
    * Protein
    * SNP Copy-Number
    * DNA Methylation

Selected Filters Panel
^^^^^^^^^^^^^^^^^^^^^^

This is where selected filters are shown so there is an easy way to see which filters have been selected.
Clicking on “Clear All” will remove all selected filters.

Clinical Features Panel
^^^^^^^^^^^^^^^^^^^^^^^

This panel shows a list of treemaps that give a high level breakdown of the selected samples for a 
handful of features:
* Disease Code
* Vital Status
* Sample Type
* Tumor Tissue Site
* Gender
* Age at Initial Pathologic Diagnosis
By using the “Show More” button, you can see two more treemaps that are currently available.

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

To activate the set operations button, you must have at least one cohort selected. Upon clicking the “Set Operations”
button, a dialogue box will appear. Here you may choose between the following actions:
* Enter the name for the new cohort to be created.
* Select a set operation.
* Select cohorts to be used in the operation.

The intersect and union operations can take any number of cohorts and in any order.
The complement operation requires that there be a base cohort, from which the other cohorts will be subtracted.
Click “OK” to complete the operation and create the new cohort.

Editing a Cohort
================

**Details of cohort edit page**

Main Menu
---------

* Add New Filters: Selecting this menu item make the filters panel appear. Any filters selected will be additive to any filters that have already been selected. To return to the previous view, you must either save the newly selected filters, or choose to cancel adding any new filters.
* Comments: Selecting “Comments” will cause the Comments panel to appear. Here anyone who can see this cohort can comment on it. Comments are shared with anyone who can view this cohort and ordered such that the newest comment is at the bottom.
* Make a Copy: Making a copy will create a copy of this cohort with the same list of samples and patients and make you the owner of the copy.
* Share with Others: A dialogue box appears and the user is prompted to select one or more other users who are registered in the system to share the cohort with. (This capability is also available on the User Dashboard page.)

Selected Filters Panel
----------------------

This panel displays any filters that have been used on the cohort or any of its ancestors. These cannot be modified and
any additional filters applied to this cohort will be appended to the list.

Details Panel
-------------

This panel displays the number of samples and participants in this cohort.  (The number of participants
and the number of samples may differ because a participant may have provided more than one sample.  In the 
TCGA dataset, most participants provided 2 samples.)
This panel also displays “Your Permissions” which can be either owner or reader.

Clinical Features Panel
-----------------------

This panel shows a list of treemaps that give a high level breakdown of the samples based on the following features:
* Disease Code
* Vital Status
* Sample Type
* Tumor Tissue Site
* Gender
* Age at Initial Pathologic Diagnosis

By using the “Show More” button, you can see two more treemaps available.

Data Availability Panel
-----------------------
This panel shows a parallel-sets graph of available data for the selected samples in the cohort. The large headers over
the vertical bars are data types. Each data-type line (vertical bar) is divided into segments representing the
different platforms (as necessary), and an additional "NA" segment for samples for which that type of data is not 
available.
The lines that flow horizontally represent individual samples. By
hovering on a horizontal segment between the first two bars, you will see the number of samples for which
both of those data types are available.
You can also reorder the vertical categories by dragging the headers left and right and reorder the
platforms by dragging the platform names up and down.

“View File List” takes you to a new page where you can view the file list associated with the current cohort.
The file list page provides a paginated list of files available for the samples in the cohort. Here, “available” refers
to files that have been uploaded to the ISB-CGC Google Cloud Project and that are open access data. You can use the
“Previous Page” and “Next Page” to show more values in the list.
You may filter on these files if you are only interested in a specific data type and platform. Selecting a filter will
update the list appropriately. The numbers next to the platform refers to the number of files available for that platform.
There is only one menu item available and that is the “Download File List as CSV”. Selecting this item will begin a
download process of all the files available for the cohort, taking into account the selected Platform filters. The file
contains the following information for each file:
* Sample Barcode
* Platform
* Pipeline
* Data Level
* File Path to the Cloud Storage Location

Commenting
----------
Any user who owns or has read-access to a cohort may comment on it. To open comments, use the menu button at the
top right and select “Comments”. A sidebar will appear on the right side and any previously created comments will be
shown.

On the bottom of the comments sidebar, you can create a new comment and save it. It should appear at the bottom of the
list of comments.

Deleting a cohort
=================

From the dashboard:
Select the cohorts that you wish to delete using the checkboxes next to the cohorts. When one or more are selected, the
delete button will be active and you can then proceed to delete them.

From within a cohort:
If you are viewing a cohort you created, then you can delete the cohort from the top right menu option.

Creating a Cohort from a Visualization
======================================

To create a cohort directly from a visualization, you must be in *plot selection* mode.  The current mode is indicated
by the crosshairs icon in the top right corner of the plot panel.  If it is blue, you are in *plot selection*
mode.  Click on the crosshairs icon to change the mode.

Once in plot selection mode, you can click and drag your cursor of the plot area to select the desired samples. For a
cubbyhole plot, you will have to select each cubby that you are interested in.

When your selection has been made, a small window will appear that contains a button labeled “Save as Cohort”. Click
on this when you are ready to create a new cohort.

Enter a name for you newly selected cohort and click the “Save” button.

Copying a cohort
================

Copying a cohort can only be done from the cohort details page of the cohort you want to copy.

When you are looking at the cohort you wish to copy, select the “Make A Copy” item from the top right menu.

This will take you to your copy of the cohort.

