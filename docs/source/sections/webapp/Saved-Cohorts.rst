********
Cohorts
********

Cohorts are a way of creating custom groupings of the samples and/or cases that you are interested in analyzing further. You may frequently reuse a cohort in multiple analyses. Creating a "saved cohort" allows you to do this. If you have any existing saved cohorts, they will display here for you to view, edit and share.

Create a New Cohort
###################

When you first log into the ISB-CGC Web App, the Create Cohort screen will be displayed. To get to it when you are on other screens, select **Create Cohort** from the **Cohorts** dropdown. If you are on the **Saved Cohorts** screen, you can click on the **New Cohort** button.

If you already have saved cohorts, they will be listed in the **Saved Cohorts** panel. Click on the **Saved Cohorts** link in that panel and a page with the details of your saved cohorts will display. Alternatively, to go directly to a given cohort, click on its name and the cohort details page of that cohort will display.

.. image:: CreateCohort.png
   :scale: 50
   :align: center


Using the list of data sets and filters on the left, you can select the attributes and features that interest you from ISB-CGC data. For a specific program, you can select data across nodes (GDC, PDC, IDC).

Select Program
===================

This panel in the top left of the screen allows you to pick the programs and user data sets that you want included in the cohort.

The drop down list will display the ISB-CGC programs that the Web App is currently supporting. Next to each progam, it will list the origin of this data (Genomics Data Commons (GDC), Proteomics Data Commons (PDC), Imaging Data Commons (IDC)).

To select more than one program for your cohort, after you **Select Filters** for a program, return to the **Select Program** drop down list. Select another program and then select filters for that program.  

Selected programs and filters will display in the **Selected Filters** section.

.. image:: SelectProgram.png
   :align: center

Select Filters
===================

When an ISB-CGC hosted data set is selected, appropriate filters will display under three tabs. All tabs are not available for all programs, but all programs will have some features available on the CASE tab.

  - The CASE tab displays clinical and demographic features applicable to the selected program.
  - The DATA tab displays data attributes (ex. Build, Data Type, Data Category, Experimental Strategy, File Type, Data Format, Platform, Access) applicable to the selected program.
  - The MOLECULAR tab is not currently in use.
  
On the CASE tab, expand the GDC, PDC or IDC headings to see the available filters. At that point, click on a filter name to see the selection values. For example, when you click on "Vital Status", it expands and provides a list containing "Alive" and "Dead" values you may choose. You may select multiple filters and multiple values.

On the DATA tab, click on a filter name to see the selection values.

Selected filters will display in the **Selected Filters** panel. The Data Set Details panel will update the Total Number of Cases and the Total Number of Samples based on the selected filters.

Individual selections within a filter group are "ORed" together, meaning if any of the conditions are met, they will be in the results.  On the other hand, filters are "ANDed" together, meaning that data must meet all filter criteria in order to be selected. There may be times where you have no cases and samples in the results, based on the combination of filters you have chosen.

 - If you use AND and do not see the data you are expecting in the filter, try OR instead. AND is a more restrictive criteria requiring all filters to be met; OR is less restrictive, requiring only one criteria to be met for the data to display.
 - You may want to consider adding the term "AND" or "OR" in your saved cohort title since the type of combination used in your cohort does not display in the filters list for a saved cohort.

.. image:: SelectFilter.png
   :align: center
          
Selected Filters Panel
----------------------

This panel displays the selected filters for the cohort. Filters are listed under the program name. If you click on the program name, the screen will change to display the information for that program.

Selecting an X beside a single filter will remove that filter. Selecting **Clear All** in the top right of the panel will remove all the filters.
Note that you cannot remove filters once the cohort has been saved. 

Program Details Panel
---------------------

This panel shows the **Total Number of Cases** and **Total Number of Samples** for the currently displayed data set based on the selected filters. If there is a small "timer" icon, the calculation is taking place; the results should appear soon.

Program Clinical Features Panel
-------------------------------

This panel shows a list of images (called "treemaps") that give a high level breakdown of the selected samples for a 
handful of features (ex. Project Short Name, Disease Type, Gender, Tissue/Organ of Origin, Vital Status, etc.) for the currently displayed data set based on the selected filters. 

Mousing over an image shows the details of each specific section of the image and the number of samples associated with it.

Saving the Cohort
-----------------

Click the **Save as New Cohort** button when you are ready to save the cohort based on the filters you have set.  You will be asked for a cohort name and the selected filters will be displayed.  Enter the name and click the **Create Cohort** button. 

Manage Saved Cohorts
####################

Selecting **Manage Saved Cohorts** from the **Cohorts** menu dropdown displays the **Cohorts** screen, **Saved Cohorts** display. The number next to "Manage Saved Cohorts" indicates how many cohorts that you have saved.

.. image:: Cohorts-dropdown.png
   :align: center


The **Saved Cohorts** screen displays your saved cohorts and allows you to view, edit, delete and share them. 

* To view a cohort, click on the name of the cohort to display the cohort details. 
* To delete a cohort, check the checkbox next to the cohort, and click on the **Delete** button.
* To share a cohort, check the checkbox next to the cohort, and click on the **Share** button.

Cohort Details Screen
#####################

The cohort details screen displays the details of a specific cohort.  The title of the cohort is displayed at the top of the page.

.. image:: CreateDetails.png
   :align: center

The screen is divided into the following sections:

**Select Program**

This panel displays all the programs that are included in the cohort; click on the drop down to see them.

Changing the selected program will change what is displayed on the Select Filters, Program Details and Clinical Features Panels.

**Filters Panel**

This panel displays current filters on this cohort. Saved filters cannot be removed.

**Cohort Details Panel**

This panel displays the Internal ISB-CGC Cohort ID (the identifier you use to access this cohort through the `APIs <../progapi/progAPI-v4/Programmatic-Demo.html>`_), and the number of samples and cases in this cohort. The number of samples may be larger than the number of cases because some cases may have provided multiple samples. This panel also displays "Your Permissions" which can be either Owner or Reader, as well as Revision History.

**Select Filters Panel**

This panel displays the selected filters for the cohort. Filters are listed under the program name. If you click on the program name, the screen will change to display the information for that program.

**Program Details Panel**

This panel shows the **Total Number of Cases** and **Total Number of Samples** for the currently displayed program (selected from the Program drop down) based on the selected filters.

**Program Clinical Features Panel**

This panel shows a list of images (called "treemaps") that give a high level breakdown of the selected samples for a handful of features (ex. Project Short Name, Disease Type, Gender, Tissue/Organ of Origin, Vital Status, etc.) for the selected program. 

**Cohort Details Screen functions:**

Comment on a cohort
===================
Clicking the **Comments** button displays the Comments panel. Here anyone who can see this cohort (such as an owner or someone who has shared access to the cohort) can comment on it. Comments are shared with anyone who can view this cohort.  They are ordered by newest on the bottom.  Selecting the "X" on the Comments panel will close the panel.  

Delete a cohort
=================

Click the **Delete** button to delete the cohort. Confirm by clicking the second **Delete** button presented.

Share a cohort
==============

Clicking the **Share** button allows you to share the cohort in the Web App with users you select by entering the user's email. 

If the email address you entered is not registered with ISB-CGC, a message displays, "The following user emails could not be found; please ask them to log into the site first:(email entered)."

Cohort export to CSV
===================

Click the **CSV** button to download the cohort in CSV format. The file will contain a list of sample and cases IDs in the cohort.

Cohort export to BigQuery
=========================

Clicking the **BQ** button allows you to create a new table or append to an existing table. You must have a BigQuery data set with a Google Cloud Project on the registered Google Cloud Projects details page. 

If a user wants to export a cohort to their own premade table, it is required to have the following columns: 

.. code-block:: JSON

  {
        'fields': [
            {
                'name': 'cohort_id',
                'type': 'INTEGER',
                'mode': 'REQUIRED'
            },{
                'name': 'case_barcode',
                'type': 'STRING',
                'mode': 'REQUIRED'
            },{
                'name': 'sample_barcode',
                'type': 'STRING',
                'mode': 'REQUIRED'
            },{
                'name': 'project_short_name',
                'type': 'STRING',
                'mode': 'REQUIRED'
            },{
                'name': 'date_added',
                'type': 'TIMESTAMP',
                'mode': 'REQUIRED'
            },{
                'name': 'case_gdc_uuid',
                'type': 'STRING'
            }
        ]
    }
  
Note: You shouldn't ever set UUID to 'required' because sometimes a sample doesn't have a UUID, and the attempt to insert a 'null' will cause the cohort export to fail.
 


.. _file-browser-page:

View Files
============

Clicking the **View Files** button displays the **Cancer Data File Browser** screen with a list of data files associated with your current cohort.  

Cancer Data File Browser
#######################

The Cancer Data File Browser displays a listing of all files associated with the cohort, pathology reports and viewable images.

All Files
============

This list on the **All Files** tab includes all files which are stored on the Google Cloud, including both controlled access and open access data.

.. image:: CohortFileBrowser.png
   :align: center


You can use "Show", "Page", "Previous" and "Next" to navigate through the list.  The columns are sortable by selecting the column header.  You can select a subset of the default columns to show by using the "Choose Columns to Display" tool.

You can filter by full or partial Case Barcode on all tabs; click the CASE filter to expand it. To remove the search key word, click the "X" button adjacent to it. Filtering by Case Barcode updates the number to the right of all the other filters. 

You may also filter by program name, build (Hg38, Hg19), data type, data category, experimental strategy, data format, platform, node (GDC, PDC, IDC) and/or access.  Selecting a filter will update the associated list.  The numbers next to the filter refers to the number of files available for that filter.

Pathology Reports
=================

Click on the **Pathology Reports** tab to see a listing of all files containing Pathology Reports.

To download a pathology report, click on the File Name.

To download a list of pathology reports for this cohort, select the **CSV** button in the upper right corner. 


Viewing a Radiology Image
=========================

To find images associated with your cohort that can be viewed, click on the **Viewable Images** tab. Hovering over the Study Instance UID column and clicking on "Open in CHIF Viewer" will open the series Selection panel in a new tab using Osimis DICOM. (HINT: Using a smaller cohort will provide faster response in creating the list of files available.)

For a more detailed step-by-step process of Viewing Radiology Images using the Osimis DICOM viewer please go `here <OsimisWebViewer.html>`_.

Download File List as CSV
-------------------------

To download a list of files that are part of this cohort, select the **CSV** button in the upper right on the File Listing panel of the Cancer Data File Browser. 

The file contains the following information for each file:

* Case Barcode
* Sample Barcode
* Program
* Platform
* Experimental Strategy 
* Data Category
* Data Type
* Data Format
* Genomic Data Commons(GDC) File UUID
* Google Cloud Storage(GCS) location
* Genomic Data Commons(GDC) Index
* Index File Google Cloud Storage(GCS) location
* File Size
* Access Type (open or controlled access)


Export File List to BigQuery
----------------------------

To export the File List to BigQuery, select the **BQ** button on the Cancer Data File Browser.  You will need to have a Google Cloud Project and a BigQuery dataset to be able to export to BigQuery.  You can either make a new table or append to an existing table.  You can also give the table a unique name; if left blank, a name will be provided for the table.

The table will contain the following information (for each of the data type tabs):

* row
* cohort_id
* case_barcode
* sample_barcode
* project_short_name
* date_added
* build 
* gdc_file_uuid
* gdc_case_uuid
* platform 
* exp_strategy
* data_category
* data_type
* data_format
* cloud_storage_location
* file_size_bytes
* index_file_gdc_uuid
* index_file_cloud_storage_location

