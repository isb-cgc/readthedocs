*************
Release Notes
*************

*  **July 20, 2016**: `v1.6 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.6>`_
    
    **Known issues in Sprint 7**
    
    - The user can add same gene twice if two identical worksheets with different names are uploaded.
    - The Bar chart on the worksheet panel renders overlapping text.
    - User cannot delete whom you share cohort with from existing cohorts table.
    - Analysis Type : Seq peek Formatting Elongated.
    - The CCLE data in GUI is not parallel to the CCLE data in BigQuery.
    - If a user creates a cohort with sample type filter Cell Lines and CCLE the total number of samples count off by one.
    - Histological Type entries in create new cohort page on the user interface should match the Google BigQuery entries in terms of capitalization.
    - When a user sets a cohort as Color by feature for violin plot legend will remain cohort.
    - After 24 hour dbGaP authorization runs out the user is unable to re authenticate. (If you have this issue, please log out and log back in to be prompted with login link for dbGaP authorization.)

    **Issues resolved in Sprint 6**

    New Enhancements
    
    - Created ability in GUI to make cohorts based on presence of an HPV status.
    - Created ability in GUI to make cohorts based on BMI value.
    - In the details panel for existing cohort have a section that shows the ISB-CGC cohort_id.
    - Enhancements of GUI to view submenu item in different screen sizes and resolutions.
    - New version of IGV javascript installed.

    Bug Fixes

    - User can no longer add same filter to existing cohorts.
    - Optimized Security in the user interface.
    - If a user opens a shared cohort it will appear once on the dashboard.
    - Pathologic State Filter in create cohort Stage is displayed capitalized.
    - Filter counts with 0 value do list when editing a pre-existing cohort.
    - Filters for data type counting in left panel is working properly.
    - After 24 hour dbGaP authorization runs out the user is able to re authenticate.
    - User can not create new gene list without giving the gene list a name.


*  **July 6, 2016**: `v1.5 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.5>`_
    
    **Known issues in Sprint 6**
    
    - The user can add same gene twice if list to the same worksheet it they have different names.
    - The user can add same filter to existing cohorts.
    - The Bar chart on the worksheet panel renders overlapping text.
    - Cannot delete whom you share cohort with from existing cohorts table.
    - Analysis Type : Seqpeek Formatting Elongated.
    - The CCLE data in GUI is not parallel to the CCLE data in BigQuery.
    - If a user opens a shared cohort it will appear twice on the dashboard.
    - If a user creates a cohort with sample type filter Cell Lines and CCLE the total number of samples count are off by one.
    - Pathologic State Filter in create cohort Stage should be displayed capitalized.
    - Histological Type entries in create new cohort page on the user interface should match the Google BigQuery entries in terms of capitalization.
    - Filter counts with 0 value don't list when editing a pre-existing cohort.
    - Filters for data type counting in left panel currently is not working properly.

   
    **Issues resolved in Sprint 6**

    New Enhancements
    
    - A user can only select the cloud storage checkbox if he or she has been authenticated and authorized through the user details page. Otherwise the user can view the cloud storage checkbox but there will be a disabled cursor icon when the user hovers over in an attempt to select the checkbox.
    - The counts for the queries were refactored to match what was done for the APIs .
    - The Download File List as CSV was refactored to a maximum of 65,000 files at once.
    - Date formats on Workbooks, Cohort, Gene, and Variables list pages all reflect the same format.
    - The Last Updated columns to variable and gene lists were added to the user Dashboard

    Bug Fixes
    
    -  The user can now select a cohort in the color by feature section for the violin and the scatter plots in the worksheet section.
    - The Gene list variable used for analysis in the worksheet plot settings section is the exact gene as compared to a gene that contains the string.
    - The Comments button for both the workbook and the cohort section, when the user clicks the request multiple times within one second the user interface will not post duplicate comments in the comments section.
    - The user can now select gene HP in Create Gene list favorite page to be used for analysis. For worksheet analysis the user now has ability to select different genes once one already selected and utilized for analysis.
    - In the variable favorites table, the menu for a specific variable will no longer be cut off once a certain set of variables list are exceeded.
    - A 400 Error pop up window will no longer appear as the user transitions from the File List page to IGV browser page.
    - The Public Data Availability section will no longer display any cut off if the user drags data type to the left of the page away from the panel itself, in detail page of existing cohort or the create new cohort page.
    - When the user edits a cohort, details section will display which filter(s) were applied for each update.
    - Cloud storage path in CSV file download for GA/BCGSC and GA/UNC V2 platforms can now be viewed.
    - The menu bar will display existing list for variable favorites list, gene favorites list, cohorts, and workbooks with no cut off.
    - When the user has selected a variable for the y-axis, the chart will display the selected variable in the charts.
    - When the user clicks Save Changes when modifying an existing cohort the user can will no longer be spammed with multiple cohorts created at once when clicking the button multiple times within one second.
    - The Save cohort Endpoint default example for v1 now works properly.
    - For the cohort_list API endpoint v1 will now pull only the cohort_id you specified.


*  **June 8, 2016**: `v1.4 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.4>`_
    
    **Known issues in Sprint 5**
    
    - The user can add same gene twice if list has different names.
    - The user can add same filter to existing cohorts.
    - In the Create new Cohort page, the left filters (#) does not re-populate as you select filters to match the sample number in clinical feature panel.
    - The bar chart renders overlapping text in the x-axis and y-axis for certain variables.
    - A user cannot delete whom you share a cohort with from the existing cohorts table.
    - On a worksheet with the Analysis Type : Seq peek, the formatting will display Elongated when the user selects a certain gene.
    - CCLE data in GUI is currently not parallel the CCLE data in BigQuery.
    - User currently cannot select a cohort in the color by feature section in a worksheet.
    - The Gene list used for analysis currently uses genes similar as to original gene and well as the specific gene added to list, in the plot settings menu.
    - The comments button for both workbooks/cohorts, if user clicks the comment button multiple times within one second will post duplicate comment.
    - User currently cannot select gene HP or gene’s with only two letters in the Create Gene list favorite page.
    - In Violin plot -  the user has no ability to select a different gene once one is already selected.
    - In the variable favorites table, the menu for a specific variable will be cut off once a certain set of variables list are exceeded.
    - A 400 Error pop up window will appear as the user transitions from the  File List page to  IGV browser page.
    - Public Data Availability section will be cut  is user drags data type title to the left of the page away from the panel itself,in detail page of existing cohort.
   
    **Issues resolved in Sprint 5**

    New Enhancements
    
    - Upgraded system from using Django 1.8 to Django 1.9.
    - A link to the google cloud platform has been added to the user details page. 
    - The TCGA filter is selected as the default project when creating a new cohort.
    - When the user clicks on the browser back button, the user will remain on the same worksheet that they were previously on.
    - When the user goes adds a new gene list, variable favorites list, and/or cohort from the worksheet data type panel, the button will display “Apply to Worksheet”.
    - The feedback/help section has been moved to the top of the page to provide the user a more convenient way to send us feedback.

    Bug Fixes
    
    - User can no longer add a duplicate gene to same gene favorites list. 
    - To edit a gene name the user must now delete and re-type the desired gene name. 
    - The functionality of a duplicate worksheet drop down menu reflects the same functionality of the original worksheet.
    - The Last Updated section reflects any changes made to the variable list, cohort list, and gene list in their corresponding tables.
    - The File list page now allows the user to add a maximum of five files to use in the IGV browser between all the pages in the file list table.
    - When a user hovers over clinical feature panel for Sample Type and Tumor Tissue Type the top row when hovered over the name is displayed clearly.
    - Order by Ascending/Descending is working properly for Existing Cohorts table page.
    - The user is now able to plot gene’s with a hyphen(-) in the gene name itself.
    - The user is now able to download a maximum of 85,000 files at a time, in the File List page for a selected cohort. 


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

    **Issues resolved in Sprint 4**

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

