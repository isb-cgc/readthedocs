*************
Release Notes
*************

*  **May 10, 2016**: `v1.3 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.3>`_
    **Known issues in Sprint 4**
    - A user can add same gene twice if identical gene list have different names.
    - The user can add same filter already selected to an existing cohort. 
    - The create new Cohort left filters number count does not re-populate as you select filters to match sample number count in clinical feature panel.
    - When a Bar chart renders overlapping text is displayed on the x-axis of the plot.
    - Cannot delete whom you share a cohort with from the existing cohorts table only from the details page of a cohort.
    - Analysis Type : Seq peek formatting is elongated when a user selects certain gene for analysis. Using the gene TP53 can reproduce this issue. 
    - The CCLE data in GUI currently does not parallel the CCLE data in BigQuery.
    - A user can add a duplicate gene to same gene favorites list in the create new gene list page.
    - By double clicking a gene name in the create new gene list page, the gene will expand but display a blank space.
    - A duplicate worksheet will display the color by feature variables twice in the drop down list.
    - A user currently cannot select a cohort in the color by feature section.
    - The Gene list drop down list used for analysis should be exact gene only.
    - The comments button for both workbook and cohort comments section, if the user is to click comment button multiple time within one second, this action will post a duplicate comment.
    - The last Update section should reflect any changes made to variable list, cohort, and gene list for their corresponding tables.
    - The user cannot select the gene HP in the Create Gene list favorite page.

   **Issues that are resolved in Sprint 4**

    New Enhancements
    
    - Data Use Certification Agreement link updated and the help link was removed. 
    - The Data Type section in the Create new Cohort page name change from MIRNA Sequencing to miRNA Sequencing and SNP CN to SNP Copy-Number. 
    - The number of patients is now dynamically displayed in the create new cohort page when selecting filters in the details panel.
    - The number of samples is now dynamically displayed in the create new cohort page when selecting filters in the details panel.
    - By default in the create new cohort page, you will have the TCGA data filter selected.
    - When creating a cohort, checking feature boxes will be throttled so as to avoid miss-represented data.
    - Tooltips were added to the Sample Type section in the clinical features panel.
    - Minor changes were made in personal details page.

   Bug Fixes
   
    - The Clinical Features Panel in the create new cohort page will no longer display BRCA even if unselected.
    - The last updated section in existing workbooks panel does update when changes are made to existing workbook.
    - Set operation Union patient number is working correctly.
    - Upon duplicating a cohort it will duplicate the selected filter(s) as well.
    - User is able  to download file list as csv for any cohort with any filter selected.
    - There is no legend cut off for violin plot or any other analysis type when the color by feature is set to Prior Diagnosis or any other variable. 
    - When user switches gene in plot settings the feature choices for that specification will refresh. 
    - The variable clinical search feature works properly when the user searches for clinical variables and then are used for analysis.


*  **April 27, 2016**: `v1.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.2>`_

    **Known issues in Sprint 3** 

    - Can add same gene twice if list has different names.
    - User can add same filter to existing cohorts.
    - Create new Cohort left filters (#) does not re-populate as you select filters to match sample # in clinical feature panel.
    - Clinical Features Panel in create new cohort page will still display BRCA even if unselected.
    - Last updated section in existing workbooks panel does not update when changes are made to existing workbook.
    - Bar chart renders overlapping text.
    - Set operation Union patient # off by one.
    - Legend Name cut off when name is too long.
    - Upon duplicating a cohort it duplicates the selected filter as well.
    - Cannot delete whom you share cohort with from existing cohorts table.
    - Unable to down file list as csv for any other cohort only selected filter CCLE.
    - Legend Cut Off for violin plot when color by feature set to Prior Diagnosis.
    - When user switches gene in plot settings the feature choices for that specification disappears.


    **Issues resolved in Sprint 3**

    New Enhancements

    - The comments section now has a max number of characters 1000 limit.
    - Link created to Extend controlled access period to 24-hours from the moment the link is clicked.

    Bug Fixes

    - A user can now click new worksheet multiple times within a few seconds and only produce one sheet.
    - The user must now add a new filter in an existing cohort to edit it the cohort.
    - The duplicate button for an existing cohort will only make one duplicate at a time.
    - Clicking 150+ selected filters will not create an error page.
    - Cancel button on Create new gene list page will send you to Gene list favorites table menu.
    - Violin plot : User can not add categorial value to y-axis.
    - If user edits an existing cohort, the old filter(s) will not be removed.
    - If a new worksheet is generated, the worksheet functionality is working properly.
    - User will get the ‘500: There was an error while handling your request. If you are trying to access a cohort please log out - and log back in. Sorry for the inconvenience.’  if the user is inactive for more in 15 minutes when trying to create/use existing cohort.
    - Clinical Feature Panel is displayed properly and reacts to filters being added/removed quickly.
    - The user must have text to add a comment.
    - All columns in file list table will be transferred/displayed when exported as csv file.


*  **April 14, 2016**: `v1.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.1>`_
    
    **Known issues in Sprint 2** 

    - If user clicks create in new worksheet too many times within a few seconds will create duplicate worksheets
    - Can add same gene twice if list has different names
    - Apply filters button work when no filter is selected in edit cohorts page
    - If user clicks create in new cohorts too many times within a few seconds will create duplicate cohorts
    - User can add same filter to existing cohorts
    - Clicking 150+ selected filters will create error page
    - Create new Cohort left filters (#) does not re-populate as you select filters to match sample # in clinical feature panel
    - Clinical Features Panel in create new cohort page will still display BRCA even if unselected
    - Cancel button on Create new gene list page will send you to Data Source | Gene Favorites page
    - Violin plot : User can add categorial value to y-axis
    - Last updated section in existing workbooks panel does not update when changes are made to existing workbook
    - If user edits an existing cohort the old filter(s) will be removed
    
    
    **Issues resolved in Sprint 2**

    New Enhancements
    
    - Tool tips added for disease code in create new cohort page
    - Disease in longname in tool tips the first letter is capitalized
    
    Bug Fixes
    
    - The user detail page will now display the correct date
    - The plot settings for a new worksheet are now working properly
    - Plot settings for duplicate worksheets are now working properly
    - The plot settings will now match the analysis type for  existing worksheet plot
    - The user can now edit existing cohort name
    - Set Operations : Intersection working properly
    - Set Operations : Union working properly
    - Set Operations : Complement is now working properly
    - User is now able to delete selected filters from selected filter panel in new cohort page using the blue X
    - Editing an existing variable favorites list will display previously selected variables
    - (Already in documentation) Green checkmark will appear for IGV link
    - Update plot button will now work on a duplicate worksheet(can be added with 3)
    - User can now delete all cohorts with the select all feature
    - Fixed bugs with Data Type Create new cohort generating errors
    - The user can now search for variable favorite with the miRNA feature
    - The user can now search for a variable favorite through the clinical search feature

*  **March 14, 2016**: `v1.0 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.0>`_
    - When working with a worksheet two plots will be generated occasionally.
    - Axis labels and tick values sometimes overlap and get cutoff.
    - Page elongated when Cubby Hole plot generated and there are lots of values in the y axis.

*  **December 23, 2015**: `v0.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.1>`_
    - Treemap graphs in cohort details and cohort creation pages will not apply its own filters to itself. For example, if you select a study, the study treemap graph will not update.
    - Cohort file list download not working.

* **December 3, 2015**: `v0.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.0>`_
    - First tagged release of the web-app

