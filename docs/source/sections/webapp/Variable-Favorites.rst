
*******************
Variable Favorites
*******************
A variable Favorites list is a way of creating custom groupings of the samples and/or participants that you are interested in analyzing further. For example, you can create a variable favorites list that span across multiple projects, only contain samples for which certain types of data are available, or focus on specific phenotypic characteristics.

Creating and Saving a Variable Favorites List
##############################################
To create a variable list from the User Dashboard, click on the "Create Variable Favorite” link where you will be directed to the Create Variable Favorite Page. 

Variable Favorites List Creation page
======================================
Using the provided list of filters on the left hand side, you can select the attributes and features
that you are interested in.

By clicking on a program, the field will expand and provide you with additional filtering options in the Data Types section.
For example, when to select the TCGA tab you see a common filters section. The common filters section is shared across programs, so if the common filter is selected in one program it will be selected for all programs. 


Variable Favorites Filter 
--------------------------

Common Filter List by Program 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   +-----------------------+------------------------------+---------------------+
   | TCGA Common  Filter   | CCLE Common  Filter List     | TARGET Common       |
   | List                  |                              | Filter List         |
   +=======================+==============================+=====================+
   | Year of Diagnosis     | Gender                       | WBC at              |
   |                       |                              | Diagnosis           | 
   +-----------------------+------------------------------+---------------------+
   | Residual Tumor        | Disease Code                 | Year of Diagnosis   |
   +-----------------------+------------------------------+---------------------+
   | Neoplasm Histologic   | Sample Type                  | Event Free Survival |
   | Grade                 |                              |                     |
   +-----------------------+------------------------------+---------------------+
   | Disease Code          | Project Short Name           | Days to Last Follow |
   |                       |                              | Up                  |
   +-----------------------+------------------------------+---------------------+
   | Age at Diagnosis      | Site Primary                 | Gender              |
   +-----------------------+------------------------------+---------------------+
   | Vital Status          | Histology                    | Days to Last Known  |
   |                       |                              | Alive               |
   +-----------------------+------------------------------+---------------------+
   | Ethnicity             | Histological SubType         | Sample Type         |
   +-----------------------+------------------------------+---------------------+
   | Person Neoplasm       | Program                      | Project Short Name  |
   | Cancer Status         |                              |                     |
   +-----------------------+------------------------------+---------------------+
   | Sample Type           |                              | Disease Code        |
   +-----------------------+------------------------------+---------------------+
   | Menopause Status      |                              | Race                |
   +-----------------------+------------------------------+---------------------+
   | Histological Type     |                              | Days to Birth       |
   +-----------------------+------------------------------+---------------------+
   | BMI (Body Mass Index) |                              | Age at Diagnosis    |
   +-----------------------+------------------------------+---------------------+
   | Tobacco Smoking       |                              | Vital Status        |
   | History               |                              |                     |
   +-----------------------+------------------------------+---------------------+
   | Pathologic Stage      |                              | Days to Death       |
   +-----------------------+------------------------------+---------------------+  
   | HPV Status            |                              | Program             | 
   +-----------------------+------------------------------+---------------------+
   | Program               |                              | Ethnicity           |
   +-----------------------+------------------------------+---------------------+
   | Gender                |                              |                     |
   +-----------------------+------------------------------+---------------------+
   | Days to Last          |                              |                     |
   | Known Alive           |                              |                     |
   +-----------------------+------------------------------+---------------------+
   | Preservation Method   |                              |                     |
   +-----------------------+------------------------------+---------------------+
   | Project Short Name    |                              |                     |
   +-----------------------+------------------------------+---------------------+
   | Race                  |                              |                     |
   +-----------------------+------------------------------+---------------------+
   | Tumor Tissue Site     |                              |                     |
   +-----------------------+------------------------------+---------------------+


Favorites Filter
^^^^^^^^^^^^^^^^
This filter allows the user to add selected variables from existing variable Favorite list.

Clinical Filter Feature Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This filter allows the user to search by any clinical feature in a given program that is present in the most recent data upload for that program. 

User Uploaded Programs Filter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This filter allows you to select by filters that you have uploaded using the upload data functionality. It's seperated by projects within your program, a drop down list will display the features that are assocaited.

Selected Filters Panel
^^^^^^^^^^^^^^^^^^^^^^
This is where the filters you have selected are shown on the right panel for clear verification of what has been selected for analysis. Clicking "Clear All" will remove all selected filters. 


Editing a Variable Favorites List
=================================
**Details of variables favorites list edit page**

Main Menu
---------

* Edit Button: Selecting this menu item make the filters panel appear. And filters selected will be additive to any filters that have already been selected. To return to the previous view, you much either save any selected filters, or choose to cancel adding any new filters.
* Delete Button: Selecting this button will delete you variable favorites list.
* Apply New Workbook button: Selecting this button will create a new workbook with the variable favorites list for analysis.

Selected Filters Panel
----------------------
This panel displays any filters that have been used on the variable list or any of its ancestors. These cannot be modified and any additional filters applied to the cohorts will be deleted.

Deleting a Variable Favorites List
==================================
From the dashboard:
Click the arrow next to the variable favorites list a box will appear with the delete option. Confirm the deletion to permanently delete the list.

From within the variable favorites list: 
If you are viewing the variable favorites list you created, then you delete the cohort by clicking the delete button under the selected variables list.
