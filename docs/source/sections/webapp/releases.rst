*************
Release Notes
*************

*  **April 27, 2016**: `v1.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.2>`_

    **Known issues in this Sprint 3** 

    - Can add same gene twice if list has different names 1204
    - User can add same filter to existing cohorts 1206
    - Create new Cohort left filters (#) does not re-populate as you select filters to match sample # in clinical feature panel 1183
    - Clinical Features Panel in create new cohort page will still display BRCA even if unselected 1192
    - Last updated section in existing workbooks panel does not update when changes are made to existing workbook 1215
    - Bar chart renders overlapping text 1040
    - Set operation Union patient # off by one 1129
    - Legend Name cut off when name is too long 1134
    - Upon duplicating a cohort it duplicates the selected filter as well. 1209
    - Cannot delete whom you share cohort with from existing cohorts table 1228 
    - Unable to down file list as csv for any other cohort only selected filter CCLE 1246
    - Legend Cut Off for violin plot when color by feature set to Prior Diagnosis 1250
    - When user switches gene in plot settings the feature choices for that specification disappears 1252


    **Issues that are resolved in Sprint 3**

    New Enhancements

    - The comments section now has a max number of characters 1000 limit 1197
    - Link created to Extend controlled access period to 24-hours from the moment the link is clicked. 1217

    Bug Fixes

    - A user can now click new worksheet multiple times within a few seconds and only produce one sheet. 1178
    - The user must now add a new filter in an existing cohort to edit it the cohort. 1172
    - The duplicate button for an existing cohort will only make one duplicate at a time. 1213
    - Clicking 150+ selected filters will not create an error page. 1188
    - Cancel button on Create new gene list page will send you to Gene list favorites table menu. 1200
    - Violin plot : User can not add categorial value to y-axis. 1205
    - If user edits an existing cohort, the old filter(s) will not be removed. 1216
    - If a new worksheet is generated, the worksheet functionality is working properly. 1123
    - User will get the ‘500: There was an error while handling your request. If you are trying to access a cohort please log out - and log back in. Sorry for the inconvenience.’  if the user is inactive for more in 15 minutes when trying to create/use existing cohort 1186
    - Clinical Feature Panel is displayed properly and reacts to filters being added/removed quickly 1214
    - The user must have text to add a comment. 1223
    - All columns in file list table will be transferred/displayed when exported as csv file 1229


*  **April 14, 2016**: `v1.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.1>`_
    
    **Known issues in this Sprint 2** 

    - If user clicks create in new worksheet too many times within a few seconds will create duplicate worksheets 1178
    - Can add same gene twice if list has different names 1204
    - Apply filters button work when no filter is selected in edit cohorts page 1172
    - If user clicks create in new cohorts too many times within a few seconds will create duplicate cohorts 1213
    - User can add same filter to existing cohorts 1206
    - Clicking 150+ selected filters will create error page 1188
    - Create new Cohort left filters (#) does not re-populate as you select filters to match sample # in clinical feature panel 1183
    - Clinical Features Panel in create new cohort page will still display BRCA even if unselected 1192
    - Cancel button on Create new gene list page will send you to Data Source | Gene Favorites page 1200
    - Violin plot : User can add categorial value to y-axis 1205
    - Last updated section in existing workbooks panel does not update when changes are made to existing workbook 1215
    - If user edits an existing cohort the old filter(s) will be removed 1216
    
    
    **Issues that are resolved in Sprint 2**

    New Enhancements
    
    - Tool tips added for disease code in create new cohort page 132 1182
    - Disease in longname in tool tips the first letter is capitalized 1180
    
    Bug Fixes
    
    - The user detail page will now display the correct date 1064
    - The plot settings for a new worksheet are now working properly 1123
    - Plot settings for duplicate worksheets are now working properly 1124
    - The plot settings will now match the analysis type for  existing worksheet plot 1125
    - The user can now edit existing cohort name 1127
    - Set Operations : Intersection working properly 1128
    - Set Operations : Union working properly 1129
    - Set Operations : Complement is now working properly 1133
    - User is now able to delete selected filters from selected filter panel in new cohort page using the blue X 1138
    - Editing an existing variable favorites list will display previously selected variables 1143
    - (Already in documentation) Green checkmark will appear for IGV link 1166
    - Update plot button will now work on a duplicate worksheet(can be added with 3) 1171
    - User can now delete all cohorts with the select all feature 1185
    - Fixed bugs with Data Type Create new cohort generating errors 1191 1212
    - The user can now search for variable favorite with the miRNA feature 1201
    - The user can now search for a variable favorite through the clinical search feature 1202 

*  **March 14, 2016**: `v1.0 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.0>`_
    - When working with a worksheet two plots will be generated occasionally.
    - Axis labels and tick values sometimes overlap and get cutoff.
    - Page elongated when Cubby Hole plot generated and there are lots of values in the y axis.

*  **December 23, 2015**: `v0.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.1>`_
    - Treemap graphs in cohort details and cohort creation pages will not apply its own filters to itself. For example, if you select a study, the study treemap graph will not update.
    - Cohort file list download not working.

* **December 3, 2015**: `v0.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.0>`_
    - First tagged release of the web-app

