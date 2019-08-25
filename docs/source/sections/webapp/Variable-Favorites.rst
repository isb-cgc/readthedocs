
**********
Variables
**********
Creating a variable favorites list is a way of creating custom groupings of the samples and/or cases that you are interested in analyzing further. For example, you can create a variable favorites list that spans across multiple projects, only contains samples for which certain types of data are available, or focuses on specific phenotypic characteristics. A Variable Favorites list can be included in a workbook.

Create Variable Favorites List
##############################

To create a variable list from **Your Dashboard**, click on the **Create Variable Favorites** link which will display the **Create Variable Favorite** screen. 

Or, from the menu dropdown, select **Create Variables Favorite List** from the **VARIABLES** menu dropdown. 

To create a new Variable Favorite:

- Name your new favorite; you can create many favorites and use them later when working with workbooks.
  
- Select attributes and features for your variable list by performing one or more of these actions:

  - *Common Filter Selection* - Click on a program (TCGA, CCLE, TARGET) to display relevant filters (attributes and features) under the **COMMON** tab.
  
    * Check the checkbox adjacent to each feature that you are interested in. They will display in the **Selected Variables** panel. (Note that checking these filters will also check the filters under the under programs, if they are on that list.)
    
  - *Clinical Filter Feature Search* - Click on a program (TCGA, CCLE, TARGET) and then click the  **CLINICAL SEARCH** tab. This filter allows the user to search by any clinical feature in the selected program that is present in the most recent data uploaded for that program. 
  
    * Enter one or more characters in the **Feature Search** field. A list of features containing these characters displays. Select a feature from the list and it will display in the **Selected Variables** panel.
    
  - *Favorites Filter Selection* - Click on **FAVORITES** tab (in the same row as TCGA, CCLE and TARGET programs). This displays your existing Variable Favorite lists, and their component features. These features can now be selected for a new Variable Favorite list by checking the checkbox adjacent to each feature that you are interested in. They will display in the **Selected Variables** panel. 

  - *User Data Filter Search*- Click on **USER DATA** tab (in the same row as TCGA, CCLE and TARGET programs). This option allows you to select by filters that you have uploaded using the upload data functionality. It's separated by projects within your program; a drop down list will display the associated features.
  
- Verify that all your selected filters are displayed in the **Selected Variables** panel on the right-hand side. Clicking **Clear All** will remove all selected filters. 
  
- Click **Save As Favorite** to save the Variable list.

.. image:: Create_Variables.png
   :align: center


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


Manage Variable Favorites List
###############################

Selecting **Manage Variable Favorites List** from the **VARIABLES** menu dropdown displays the **Saved Variable Favorites** screen. This screen displays your saved Variables Favorites and allows you to edit or delete them, as well as start a new workbook using your favorite.

* Editing a Variable Favorites List - Clicking the **Edit** button displays the **Edit Variable Favorite** screen, which shows all filters in the selected variable list. Any variables selected will be added to any existing variables in the list. Variables can also be removed from the favorite list. The title of the variable favorite list can be changed. To return to the previous view, you must either save any selected filters, or choose to cancel adding any new filters.

* Deleting a Variable Favorites List - Clicking the Delete button will delete the variable list.

* Apply To New Workbook button - Clicking on the **Apply to New Workbook** button will take you to a screen where you can create a new workbook using your variable list.

Select Variables for a New Workbook
########################################

Selecting **Variables for a New Workbook** from the **VARIABLES** menu dropdown displays the **Data Source | Variables** screen. This screen allows you to create a new workbook with the selected variables.

- Click the **Create New Workbook With Selected Variables** button to create a new workbook using your selected variables.


