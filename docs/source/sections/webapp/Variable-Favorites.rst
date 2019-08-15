
**********
Variables
**********
Creating a variable favorites list is a way of creating custom groupings of the samples and/or cases that you are interested in analyzing further. For example, you can create a variable favorites list that spans across multiple projects, only contains samples for which certain types of data are available, or focuses on specific phenotypic characteristics. A Variable Favorites list can be included in a workbook.

Create Variable Favorites List
##############################

To create a variable list from **Your Dashboard**, click on the **Create Variable Favorites** link which will display the **Create Variable Favorite** Page. 

Or, from the menu dropdown, select **Create Variables Favorite List** from the **VARIABLES** menu dropdown. 

To create a new Variable Favorite:

- Name your new favorite; you can create many favorites and use them later when working with workbooks.
- Clicking on a program (TCGA, CCLE, TARGET) will display relevant filters (attributes and features) under the **COMMON** tab.

  * Check the checkbox adjacent to each attribute or feature that you are interested in. They will display in the **Selected Variables** panel. (Note that checking these filters will also check the filters under the under programs, if it is on the list.)
- Click **Save As Favorite** to save the Variable list.

Common Filter List by Program 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   +-----------------------+------------------------------+---------------------+
   | TCGA Common  Filter   | CCLE Common  Filter List     | TARGET Common       |
   | List                  |                              | Filter List         |
   +=======================+==============================+=====================+
   | Year of Diagnosis     | Program                      | WBC at              |
   |                       |                              | Diagnosis           | 
   +-----------------------+------------------------------+---------------------+
   | Residual Tumor        | Project Short Name           | Year of Diagnosis   |
   +-----------------------+------------------------------+---------------------+
   | Neoplasm Histologic   | Disease Code                 | Event Free Survival |
   | Grade                 |                              |                     |
   +-----------------------+------------------------------+---------------------+
   | Disease Code          | Sample Type                  | Days to Last Follow |
   |                       |                              | Up                  |
   +-----------------------+------------------------------+---------------------+
   | Age at Diagnosis      | Gender                       | Gender              |
   +-----------------------+------------------------------+---------------------+
   | Vital Status          | Histology                    | Days to Last Known  |
   |                       |                              | Alive               |
   +-----------------------+------------------------------+---------------------+
   | Ethnicity             | Histological SubType         | Sample Type         |
   +-----------------------+------------------------------+---------------------+
   | Person Neoplasm       | Site Primary                 | Project Short Name  |
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
This filter allows the user to search by any clinical feature in a given program that is present in the most recent data uploaded for that program. 

User Uploaded Programs Filter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This filter allows you to select by filters that you have uploaded using the upload data functionality. It's separated by projects within your program, a drop down list will display the features that are associated.

Selected Filters Panel
^^^^^^^^^^^^^^^^^^^^^^
This is where the filters you have selected are shown on the right panel for clear verification of what has been selected for analysis. Clicking "Clear All" will remove all selected filters. 

Selected Filters Panel
----------------------
This panel displays any filters that have been used on the variable list or any of its ancestors. These cannot be modified and any additional filters applied to the cohorts will be deleted.


Manage Variable Favorites List
###############################

Selecting **Manage Variable Favorites List** from the **VARIABLES** menu dropdown displays the **Saved Variable Favorites** screen. This screen displays your saved Variables Favorites and allows you to edit or delete them, as well as start a new workbook using your favorite.

* Edit Button: Selecting this menu item make the filters panel appear. And filters selected will be additive to any filters that have already been selected. To return to the previous view, you much either save any selected filters, or choose to cancel adding any new filters.
* Delete Button: Selecting this button will delete you variable favorites list.
* Apply New Workbook button: Selecting this button will create a new workbook with the variable favorites list for analysis.

Editing a Variable Favorites List
=================================
Selecting the edit button from the variable list page or a specific variable details page, you are redirected to a page where you can add or remove filters from all programs on system and user uploaded data. You are also able to change the title of the variable favorite list from the feature. 

Deleting a Variable Favorites List
==================================
From the dashboard:
Click the arrow next to the variable favorites list a box will appear with the delete option. Confirm the deletion to permanently delete the list.

From within the variable favorites list: 
If you are viewing the variable favorites list you created, then you delete the cohort by clicking the delete button under the selected variables list.

Clicking on the **Create New Favorite** button will take you to the **Create Variable Favorite** screen.

Select Variables for a New Workbook
########################################

Selecting **Variables for a New Workbook** from the **VARIABLES** menu dropdown displays the **Data Source | Variables** screen. This screen allows you to create a new workbook with the selected variables.

- Click the **Create New Workbook With Selected Variables** button to create a new workbook using your selected variables.


