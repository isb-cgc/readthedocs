#############################
ISB-CGC Web App Release Notes
#############################

*July 19, 2021* 

- The Warning Notice about accessing a government website that should pop up when ISB-CGC is accessed was missing. It has been reinstated.
- There was an issue loading the Variable selection page. This has been fixed.
- On the Create and Edit Variable screens, the data set/programs tabs have been changed to a drop down.
- In some cases when creating a cohort with multiple programs, the Data Set Clinical Features panel was not displaying the appropriate information. This has been corrected.
- The system now logs when users refresh their 24 hour access at DCF so that this can be monitored.


*June 24, 2021* 

**New Features** 

- The Citations link on the top-level menu has been replaced with a Publications link. The page now includes ISB-CGC publications and posters, as well as citations.
- Enhance the Cohort Builder UI and Cohort Details UI so that additional node based GDC and PDC Programs can be selected and edited. The Programs now available are:

  - GDC
  
    - TCGA
    - TARGET
    - CCLE
    - BEATAML1.0
    - FM
    - MMRF
    - OHSU
    
  - PDC
 
    - Georgetown Proteomics (GPRP) 
- On the Cohort Builder, replace the Selected Filters panel with the Cohort Filters panel. This panel displays all selected filters for all selected Programs.

*April 13, 2021* 

**New Features** 

- On the home page, the title in each box is now clickable and will bring the user to that function. 
- A Citations link has been added to the top level menu. Papers which reference ISB-CGC are listed.
- In the Cancer Data File Browser, when viewing a cohort that only has HG19 data, the Build filter will automatically be set to HG19.

**Bug Fixes**

- Fixed the following issues in the Cancer Data File Browser:

   - When selecting Build of HG19 and Data Format of Zip, incorrect results were displayed.
   - When selecting Build of HG19 and Program of TCGA, the incorrect number of entries was displayed under the File Listing.
   - When selecting Build of HG19 and Data Format of Raw sequencing data, the number of entries displayed under the File Listing was off by one.

*February 22, 2021* 

**New Features** 

- In the Cohort Builder (via filters), there is a new option to hide filter attributes with zero counts.
- In the Cancer Data File Browser - Pathology Image Viewer, Pathology Report Viewer and Radiology Image Viewer, login is no longer required.
- A survey link has been added to the ISB-CGC home page.
- On the home page, the icons next to the title in each box are now clickable and will bring the user to that function. 
- Security update.

**Bug Fixes**

- In the Cancer Data File Browser - Radiology Image Viewer, error handing for records with missing disease code or project short name has been added.
- In the Cancer Data File Browser, the display of the 'Next' button for paginations has been fixed.
- In the Cohort Builder (via filters), inaccurate filter and sample counts for numeric range type filters (e.g. Age at diagnosis) were corrected.

*December 8, 2020* 

**New Features** 

- In the Cancer Data File Browser, BEATAML1.0 has been added as a choice under filter Program Name. It has also been added to the Cohort Builder/Data Explorer.
- On the ISB-CGC home page, a Contact Us page has been added under the Help dropdown menu item.
- On the ISB-CGC home page, a step by step guide called **How to Discover Cancer Data through ISB-CGC** has been added.
- There is a registration maximum of six programs/datasets to a service account implementation from the DCF.
- Bootstrap library upgraded from version 3.3.1 to 3.4.1.

**Known Issues**

- Work is underway to rework our cohort creation page to better display images associated with samples.
- The user data upload feature will return an error message stating, "Error submitting response : Could not connect to data upload server."
- Analysis Type: Seq peek Formatting is Elongated on occasion.
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.


*August 19, 2020* 

**New Features**  

- ISB-CGC has a new home page, which prominently features ISB-CGC Data Browsers and Resources.
- A Cancer Data File Browser is now available directly from the ISB-CGC home page. It is similar to the existing File Browser within the Web App, except:

  * Sign in is not needed.
  * It is not dependent on cohorts built through the Web App.
  * Output can be downloaded to CSV. To download to Google Storage Buckets or Google BigQuery tables, the user must sign in.
  * Program filter has been added.

- The ISB-CGC home page includes a Programmatic API section. The Launch functionality includes links to:
  
  * ISB-CGC API;
  * Tutorials for Workflow on Google Cloud;
  * Comparison of Workflow Languages.
   
- All NA filters have been renamed to None in both the File Browser page and the Cohort Builder page.

- User details page has been modified to include more icons and buttons. The essential functionality and contents are not modified.


**Known Issues**

- Work is underway to rework our cohort creation page to better display images associated with samples.
- The user data upload feature will return an error message stating, "Error submitting response : Could not connect to data upload server."
- Analysis Type: Seq peek Formatting is Elongated on occasion.
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.


*July 23, 2020* 

**New Features** 

- To increase system speed when filtering cohorts, switched metadata counting to use Apache Solr (instead of MySQL).
- The WebApp is now performing its data retrieval and counts on ISB-CGC Google BigQuery tables which are based on the latest GDC data release. This means that you will see current data, but that the same queries in the WebApp could produce different results if they were run during different time periods, when the WebApp was based on different GDC data releases.
- On the Create Cohorts – Filters page, on the left-hand filter panel, display the number of cases available for each filter, instead of the number of samples.
- Within the Cohort Details page, on the Current Filters panel, when there are more filters than what fits on the initial screen, display the selected cohort filters in a gradient (fade-away) overlay instead of a clipped design.
- The video tutorials have been moved to the ISB-CGC YouTube channel.

**Bug Fixes**

- Clicking on the X on an existing cohort filter token in the Selected Filter panel did not delete the existing cohort filter token. (This issue was caused by a jQuery update.) It has now been fixed.
- When a user tried to register for controlled access for 12 or more programs, this caused an error from Data Commons Framework (DCF) to occur. This was fixed by limiting the number of controlled access programs that a user could register for at one time to six.

**Known Issues**

- The Program filter is listing 'NA' as an option. 
- Work is underway to rework our cohort creation page to better display images associated with samples.
- The user data upload feature will return an error message stating, "Error submitting response : Could not connect to data upload server."
- Analysis Type: Seq peek Formatting is Elongated on occasion.
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.


*May 27, 2020* 

**New Features**

- Modify the opt-in (subscription) form to have an "Ask me later" option.

- Provide a link (https://isb-cgc.appspot.com/opt_in/form_reg_user/) to the opt-in page. The link will first prompt the user to login with their google ID (if they are not already logged in). After the login, the feedback page will open.

**Bug Fixes**

- When writing and saving a comment in the cohort details or worksheet sections, the system displayed underlying code (such as escape characters) along with the text entered in the Comments panel. This has been corrected.

- Some data results were not displaying when working with OncoGrid due to it being unable to handle the amount of data being processed. This has been fixed.

- All plotting components under the Plot settings should be disabled when user views a shared workbook; however, 'Plot by' and 'Plot as Log' were not. This has been fixed.

- On analysis plots for workbooks, sometimes the y-axis tick marks would overlap the y-axis label when using the zoom out feature. This has been fixed. 

- On the Create Cohorts - Filters page, when using the program TARGET with the filter Days to Birth, the Total Number of Cases and Total Number of Samples were not displaying. Also, the Save As New Cohort button was disabled. This has been corrected.

**Known Issues**

- Work is underway to rework our cohort creation page to better display images associated with samples.
- The user data upload feature will return an error message stating, "Error submitting response : Could not connect to data upload server."
- Analysis Type: Seq peek Formatting is Elongated on occasion.
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.

*April 16, 2020* 

**New Features**

- The Cohort Creation by Filter builder is now accessible without having to log in to ISB-CGC.
- The Cohort, Workbooks, and Gene and Variable Favorites lists are now paginated to display 10 to 15 records at a time.
- The 'To complete this analysis' section on the workbook creation page has changed from a checklist to an interactive tool. After each step is completed, its icon changes from an orange arrow to a green checkmark.
- A link 'Learn more about our available Analyses' was added next to the Analysis Type selection field. Clicking on this link opens up a screen with a detailed explanation of all the analysis options. 

**Bug Fixes**

- On the File Browser, the search by CASE filter on the Radiology Images tab has been fixed. 
- 'How to Cite Us' text on the Home page has been updated to reflect the entire ISB-CGC platform. 
- When using a workbook, if you completely zoomed out of a plot, the chart was being reduced to half of the screen. This has been corrected.

**Known Issues**

- Work is underway to rework our cohort creation page to better display images associated with samples.
- The workbook zoom-out feature will cause text overlap in the y-axis panel of analysis.
- The user data upload feature will return an error message stating, "Error submitting response : Could not connect to data upload server."
- Analysis Type: Seq peek Formatting is Elongated on occasion.
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.


*March 11, 2020* 

**New Features**

- An Opt-in page was created for the user to sign up for ISB-CGC announcements.

**Bug Fixes**

- When working with the ISB-CGC API DELETE/cohorts/{cohort_id}, only able to delete cohorts owned by authenticated user.

**Known Issues**

- Analysis Type: Seq peek Formatting is Elongated on occasion.
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.
- Work is underway to rework our cohort creation page to better display images associated with samples.

*January 30, 2020* 

The following datasets (open and controlled access) have been added to the ISB-CGC for service account registration:

 1. Genomics Evidence Neoplasia Information Exchange (GENIE)
 2. The Pancreas Cancer Organoid Profiling (ORGANOID)
 3. The Multiple Myeloma CoMMpass Study (MMRF)
 4. Burkitt Lymphoma Genome Sequencing Project (CGCI)
 5. Acute Lymphoblastic Leukemia - Phase I (TARGET-ALL-P1)
 6. Acute Lymphoblastic Leukemia - Phase II (TARGET-ALL-P2)
 7. Functional Genomic Landscape of Acute Myeloid Leukemia (BEATAML1.0-COHORT)
 
**New Features**

- The File Browser is enabled to define cancer names under the Disease Code filter in the left panel.

**Bug Fixes**

- The Cohorts share button is now enabled from the cohorts list page.
- The Cohort builder - filters, when using Pathologic Stage filter, the filters display in the correct format.
- Add a gene & miRNA variable favorite list from menu bar selection is now enabled. 


*November 26, 2019* `v1.21 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.21>`_

**New Features**

APIs

- Endpoint GET/data/available/registration lists all possible open and controlled programs available for registration with a service account. 
- Endpoint GET/data/available/cohorts list all possible programs and projects available to use to make a cohort of the data available. 

**Known Issues**

- Analysis Type: Seq peek Formatting is Elongated on occasion.
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.
- Work is underway to rework our cohort creation page to better display images associated with samples.

*August 27, 2019* `v1.20 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.20>`_

The following datasets (open and controlled access) have been added to the ISB-CGC for service account registration:

 1. The Human Cancer Models Initiative (HCMI)
 2. The Functional Genomic Landscape of Acute Myeloid Leukemia (BEATAML1.0)
 
**New Features**
 
- ISB-CGC APIs have been updated to a Swagger user interface as well as Google Endpoints OpenAPI, now known as APIsv4.

**Known Issues**

- Analysis Type: Seq peek Formatting is Elongated on occasion
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.
- Work is underway to rework our cohort creation page to better display images associated with samples.

*July 18, 2019* `v3.19 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.19>`_

The following datasets (open and controlled access) have been added to the ISB-CGC for service account registration:

 1. The Clinical Proteomic Tumor Analysis Consortium (CPTAC)

**New Features**

Workbooks

- Edit plot settings feature provides the ability to plot by either cases or samples barcode count for a bar chart, histogram, scatter plot, violin plot, and cubby hole plot analyses.
- Detailed information provided by dbGaP for every program available when registering a Google service account. 

**Known Issues**

- Analysis Type: Seq peek Formatting is Elongated on occasion
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.
- Work is underway to rework our cohort creation page to better display images associated with samples.

*April 25, 2019* `v3.18 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.18>`_
 
The following datasets (open and controlled access) have been added to the ISB-CGC for service account registration:

 1. The National Cancer Institute Center for Cancer Research (NCICCR)
 2. Foundation Medicine (FM)
 3. Clinical Trial Sequencing Project (CTSP)
 4. Veterans Research for Precision Oncology Program (VAREPOP) 
 5. Acute Lymphoblastic Leukemia - Phase III (TARGET-ALL-P3)
  
**Enhancements** 

- When working with Oncogrid, OncoPrint, or a SeqPeek plot on a workbook, you will receive an automated list of genes ready for analysis.
- When on an additional workbook, text has been added to guide the user to select edit plot settings to choose a gene/miRNA/variable filter and cohort to used in the selected analysis.
- The Workbook comments section has been reformatted to better align with analysis displayed.
- On the cohort creation - filter page, the filters have been updated in the left filter panel to specify the count type displayed (samples).

**Bug Fixes**

- Clicking on a legend entry to toggle the display of the data points on a scatter or violin plot will now work correctly, even if the legend text has a space.
- Plotting with sample type filter on a workbook will now display counts correctly.
- When working with the color by feature on either a Scatter plot or a Violin plot, the numerical values are now displayed as a color-gradient legend.
- When using a workbook with OncoGrid analysis you are now able to plot using genomic build hg19.
- When using a workbook with a Cubby Hole plot analysis text is no longer cut off when using sample type or residual tumor as a filter.

**Known Issues**

- Analysis Type: Seq peek Formatting is Elongated on occasion
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.
- Work is underway to rework our cohort creation page to better display images associated with samples.


*March 8, 2019* `v3.17 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.17>`_

**Enhancements**

- When working with a workbook many overall enhancements of user functionality have been improved. 
- Cubby hole plot analysis has been reformatted to better suit the end user by now allowing resizing and scrolling through the cubby hole plot analysis.
- You are now able to work on a workbook via fullscreen for added comfort. 
- You are also now able to download plot data for Bar charts, Histogram charts, Scatter plots, Violin plot charts, and Cubby hole plots as a CSV file.
- `OncoGrid <https://github.com/oncojs/oncogrid>`_ has been added as an analysis option when working with a workbook. 
- On the File Browser section you are now able to use full screen on all image viewers. 
- On the register/adjust a service account page, we’ve clarified the notification message if a key or role is found associated to a service account. 

**Bug Fixes**

- When using a workbook you will no longer see text overlap when working on a violin/scatter plot with the color by feature sample type as filter option.
- When working on the Pathology images viewer you will no longer see text overlap on the top right hand side of viewer.

**Known Issues**

- Analysis Type: Seq peek Formatting is Elongated on occasion
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.
- Work is underway to rework our cohort creation page to better display images associated with samples.

*January 22, 2019* `v3.16 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.16>`_

**Enhancements**
  
- On the Gene list creation page, you can now upload line separated and tab separated gene lists to be used for analysis.
- We have made some updates to the workbooks plotting section.
- You are now able to redraw to the original plot after any changes.
- Plots are now able to be saved as a .SVG, .PNG, or .JSON file.
  
**Bug Fixes**
  
- On the cohort creation using the barcode upload feature, the table page list feature now is now displayed properly. 
- If you have not linked to the Data Commons Framework at all you are able to unregister a Google Cloud Project. If you are not linked to the Data Commons Framework, but others in the Google Cloud project are, only they will be able to unregister the GCP.  
 
**Known Issues**

- Analysis Type: Seq peek Formatting is Elongated on occasion
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.
- Work is underway to rework our cohort creation page to better display images associated with samples.

*December 5, 2018* `v3.15 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.15>`_
 
**Enhancements**
 
- The ISB-CGC homepage has been updated to provide Funding and Partnership information, and the About Us section is now hidden by default. 
- An introduction video has been added to the videos tutorials section. This video covers the user interface, BigQuery and using the API endpoints. 
- Funding information has been updated on the ISB-CGC homepage.
- On the Register/Adjust a service account page all spacing issues have been addressed. 
- On the Register/Adjust a service account pages you are now returned more detailed information. You will be returned verification results for all users on the Google Cloud Project, datasets permissions verification, registered service account verification results, and all service accounts verification results. 
- On the File Browser page, when working with on a cohort with CCLE data included for genomic build hg38 you are displayed a notification message for CSV export button. 
- On the File Browser a new column has been added for File Size for all tabs. 
- When exporting a large cohort on the File Browser page you are returned a notification message stating cohort export is underway to check BigQuery in a few minutes. 
- On the File Browser you are now able to view/download/print Pathology Reports in pdf format. 
- On the Pathology Images viewer, the GDC has released multiple versions of slide barcodes. To handle this we now sort the pathology image files by UUID. 
- On the the File Browser for Radiology Images, ISB-CGC has upgraded the viewer to run OHIF for better performance times and views. 
  
**Bug Fixes**
 
- When working on the File Browser export to BigQuery/Google Cloud Storage entering an invalid name will disable the export feature, even after toggling between datasets. 
- When on a Workbook, using an OncoPrint analysis using certain genes with no gene positions will return correct error message stating no internal feature ID was found.
- Certain gene names which symbol ‘_’ included will now return data points when working with a Workbook. 
  
**Known Issues**
 
- Analysis Type: Seq peek Formatting is Elongated on occasion
- If the user shares a Cohort, neither the owner nor the person who was granted access to the Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcode error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated with them.
- Sharing a workbook with someone else will cause the analysis to reset.
- Work is underway to rework our cohort creation page to better display images associated with samples.

*September 20, 2018* `v3.14 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.14>`_
 
**Enhancements**
  
- When on the File browser page, the case barcode column is included when downloading the file manifest CSV format option. 
- You will now need to log into the Data Commons Framework to be able to access controlled data. 
  
**Bug Fixes**
 
- API endpoint cohort.creation will no longer include NULL values in sample counts when cohort is created. 
- On the File Browser tab using filter option NA will now return all entries associated to it. 
- Program TCGA and TARGET have new miRNA based on the GDC release 11 is now available in Google BigQuery and for plotting.
  
**Known Issues**
  
- Analysis Type: Seq peek Formatting is Elongated on occasion 
- If the user shares a Cohort, neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly. 
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL. 
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcodes error message and unable to upload all the barcodes. 
- On the File Browser page for Diagnostic images there is no GDC file UUID associated to them. 
- Sharing a workbook with someone else will cause the analysis to reset. 
- When using a workbook, a gene with symbol “_” will produce a error message saying, “There was an error retrieving plot data. Please try again.” 
- Work is underway to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.

*July 31, 2018* `v3.13 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.13>`_

**Enhancements**
 
- When working on the File Browser you now have the ability to search by case barcode all on tabs(Pathology Images, Radiology Images, IGV Browser, All Files). 
- On the File Browser page for the Pathology Images tab, you can now also filter by Disease Code, Data Format, and Data Type. For the Radiology Images, a disease code was added. 
- On the File Browser page, you now have the ability to hide the filters and expand the file list to full width. 
- On the File Browser page, if you download the file manifest using the export CSV feature, you will see newly updated file paths. The older paths are still in existence but will be deleted within the next month. 
- On the File Browser page if you use a cohort with CCLE data present, switch to build hg38 and attempt to export you will return a notification no CCLE data will be present for build hg38. 
- On the homepage, we have added a carousel scrolling feature for all how-to videos for easy access. 
- A description has been added to all video tutorials. 
- The menu bar text variable favorites have been updated to be undifferentiated. 
  
**Bug Fixes**
 
- When creating a cohort using the filter selection option, if the filter options selected add up to zero the save cohort button will be disabled. 
- A workbook with user upload data and public data e.g TCGA data will plot any analyses.
- For the export to GCS and BigQuery feature the export button will now disable when an invalid name is given. 
- On a registered Google Cloud Project detail page, datasets can no longer be duplicated within a project, and bucket names are globally unique (across all projects).
  
**Known Issues**
  
- Analysis Type: Seq peek Formatting is Elongated on occasion 
- If the user shares a Cohort, neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort. 
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly. 
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL. 
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcodes error message and unable to upload all the barcodes. 
- API endpoint cohort.creation will include NULL values in sample counts when the cohort is created. 
- On the File Browser page for Diagnostic images, there is no GDC file UUID associated to them.
- Sharing a workbook with someone else will cause the analysis to reset.
- When downloading the CSV file for Radiology Images tab on the File Browser page you will noticed there are no samples barcodes associated to Radiology Images. ISB-CGC will add a case barocde to the CSV file export table in the next release. 
- Work is underway to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.

*June 18, 2018* `v3.12 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.12>`_

**Enhancements**
  
- The ISB-CGC has enabled OncoPrint visualization tool for germline mutations (codebase obtained with permission from cBioPortal) as another Workbook analysis tool. For more information please go `here. <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/Workbooks.html#creating-and-saving-a-workbook>`_
- You are now able to view Radiology Images from TCIA data through the File Browser using the Osimis viewer. For more information please go here `here. <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/OsimisWebViewer.html>`_
- Two new videos have been added to our video tutorials section. You can now learn how to sign up with a Google account and how to make a gene list easily. For more information please go here. `here <https://isb-cgc.appspot.com/videotutorials/>`_
- The Dashboard has been upgraded to include a collapse feature for all panels (workbooks and cohorts are opened by default) and a direct link to the File Browser has been added to the Cohorts panel. 
- Under cohort creation by filters, the Molecular tab for TCGA data has been upgraded to combine multiple gene mutation filters. Filters can be combined using AND (requires all filters to be met for the data to be filtered) or OR (at least one criteria needs to be met for the data to be displayed). 
- The CSV download, Export to BigQuery, and Export to GCS feature has been added to the IGV Browser, Pathology Images, and the Radiology Images tab on the File Browser. 
- On the File Browser All files tab the clinical filter now displays the accurate count available for analysis. 
- The File Browser has been upgraded to now include the option of which columns to display and the ability to jump to any page. 
- The site menu has been improved to allow faster load times and better overall performance. Please Note that Workbooks must now be created from a data source (Cohorts, Variable lists, Gene & miRNA lists) or from the Workbook list page.
 
**Bug Fixes**
  
- When working on Firefox browser a violin plot will display the data plotted correctly when working on a Worksheet.
- A cohort with user uploaded data present and public data present in our system e.g TCGA data, the cohort details page for the selected filters panel will sort the filters by their appropriate program. 
- On the cohort creation - barcode upload page the 'Samples' and 'Cases' column headers were sometimes swapped. This has been corrected. 
- When trying to reload a stored Seq-Peek plot from a Workbook the previous gene selection is stored and the plot will automatically be loaded. 
- On the File Browser IGV Browser tab when switching genomic builds the view column selection option will be disabled.
 
**Known Issues**
  
- Analysis Type: Seq peek Formatting is Elongated on occasion 
- If the user shares a Cohort, neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL. 
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcodes error message and unable to upload all the barcodes. 
- API endpoint cohort.creation will include NULL values in sample counts when cohort is created. 
- Duplicate entries can be entered for the register a dataset and the register a bucket on the Google cloud project details page. 
- On the File Browser page for Diagnostic images there is no GDC file UUID associated to them. 
- Sharing a workbook with someone else will cause the analysis to reset.
- A Workbook using a cohort that has user uploaded data and public TCGA data present will not return data for any analysis. 
- Work is underway to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.

*May 3, 2018* `v3.11 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.11>`_
 
**Enhancements**
 
- The export to BigQuery feature has been enhanced to include faster processing time for larger cohorts with e.g 30,000 > samples and 65,000 > file records.
- You are now able to export cohort and cohort file manifests to a Google Cloud Storage using either .JSON or .CSV format from the cohort details page and from the File Browser page. 
- We have enhanced our instructions associated with buttons to further provide directions to the end-users. 
- On the File Browser page it is now possible to change how many entries are displayed at a time, as well as sort columns by clicking on the column header.
- Google Cloud Project membership is now automatically updated every six hours. If you are adding someone new to the project they will be able to use the project after six hours maximum without someone having to log in and manually refresh the project.
 
**Bug Fixes**
 
- You can no longer share a cohort with yourself (email currently logged into) and cause the file browser page to disable.  
- DNA methylation has been re-enabled to be used with hg38 and hg19 data when working with workbooks and plotting. 
- Sharing inputs have had their security restrictions tightened. This also includes the registering a service account page. 
- On the File Browser page when downloading the file manifest via the CSV button you are no longer able to re-select the CSV button while the file is building. 
- On the File Browser tab if you toggle between entries pages on the All Files tab it will not affect the IGV tab or Pathology Images tab entries counts display. 
- On the File Browser page you can now freely toggle between entries pages with no errors displayed. 
- On the File Browser page selecting filters from the left hand side while exploring pages will no longer crash and require you to back or refresh the page to fix. 
 
**Known Issues**
 
- Analysis Type: Seq peek Formatting is Elongated on occasion
- If the user shares a Cohort, neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL. 
- When working on Firefox browser a violin plot does not display the data plotted correctly when working on a Worksheet. 
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcodes error message and unable to upload all the barcodes. 
- API endpoint cohort.creation will include NULL values in sample counts when cohort is created. 
- Duplicate entries can be entered for the register a dataset and the register a bucket on the Google cloud project details page.
- A cohort with user uploaded data present and public data present in our system e.g TCGA data, the cohort details page for the selected filters panel does not properly display the filters selected. 
- On the File Browser page for Diagnostic images there is no GDC file UUID associated to them.
- Work is underway to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.

*April 2, 2018* `v3.10 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.10>`_
 
**Enhancements**

- When working with the File List table you can now Export the cohort file list to BigQuery for later analysis.
- When registering or adjusting a service account to use controlled data, the page will no longer briefly appear as if no datasets had been selected. This should reduce confusion. 
- Selecting the refresh project button from a registered Google Cloud Project details page will leave you on the details page rather than redirecting you to the registered Google cloud project list table page.
- On the cohort creation page, using the barcode upload page, the valid/invalid entries table can now be sorted by on any column with either ascending/descending order. 
- Removing someone from the IAM and Admin list does not remove them from the web-app automatically. If the removed user still has the GCP present in their webapp interface attempting to register or refresh a service account will remove the GCP from the web app, and a display message informing them they are no longer a member of the project will be seen.
- When working with any tables that can be sorted on smaller screens, there is no longer any text overlap in the table columns.
- Character restrictions has been relaxed, you can now use characters such as []{}(); for entity names and descriptions. 

**Bug Fixes**
 
- SeqPeek and CNVR can only be plotted with TCGA data, but if a cohort contains no TCGA samples the SeqPeek analysis will now return an error message saying, “The chosen cohorts do not contain samples from programs with Gene Mutation data.” 
- API endpoint samples.get can now be used to return data for all three programs.
- On the adjust service account page, when attempting to remove the service account from being able to access controlled data, and then immediately trying to add the service account back to controlled data, the system will require you to verify the service account’s users again. 

**Known Issues**
 
- Analysis Type: Seq peek Formatting is Elongated on occasion 
- If the user shares a Cohort, neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort. 
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly. 
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL. 
- When working on Firefox browser a violin plot does not display the data plotted correctly when working on a Worksheet. 
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcodes error message and unable to upload all the barcodes.
- On the cohort File List Browser page, while you are downloading CSV files, other filters can be selected.
- Work is underway to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.

*February 28, 2018* `v3.9 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.9>`_
 
**Enhancements**
 
- On the register a Google Cloud Project you now can only register the project ID. Registering the project name or project number will now result in an error message. Additionally, the GCP Project Name and ID will now both display on the GCP detail and list pages, and refreshing a GCP Project in the Web Application will update the Name if it was changed in the GCP console.
- For cohort creation via sets of barcodes, the barcode set (pasted in the text box or uploaded as a file) can now be a simple list of sample or case barcodes separated by newlines, commas, or tabs; the program listing is no longer needed, and you don’t need to supply the barcodes in a distinct columnar format.. The previous 3-column format will continue to work as well.
- On a worksheet, if no table is being searched the BQ table(s) used panel becomes inactive.
 
**Bug Fixes**
 
- When editing the name of a cohort the cancel feature is now working properly.
- When working on a worksheet the SeqPeek feature will now work with all genes.
- All genes can be plotted on a worksheet when working with a histogram.
- When registered Service Accounts for controlled data, the Adjust/Register can only be clicked once.
- When working with SeqPeek, the BQ table(s) used panel will now refresh every time even if no new data is plotted. 
- When a user is removed from their Google project the user interface doesn’t remove the project from their list. Instead, the individual removed will receive error messages saying they are no longer on the project if they try to refresh the project or register the service account. 
- On a registered Google Cloud Project page, the refresh button will now properly add and remove users from the project if they are added or removed from the IAM and Admin list on the Google console. 
- When working on the Internet Explorer you can again create a cohort using the filter creation page. 
- When using the dbGaP eRA authentication you will now be logged out at 24 hours instead of 16 hours. 
- For cohort creation when uploading a large set of barcodes you will no longer return a 400 bad request error.
 
**Known Issues**
 
- Analysis Type: Seq peek Formatting is Elongated on occasion 
- If the user shares a Cohort, neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort. 
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL. 
- When working on Firefox browser a violin plot does not display the data plotted correctly when working on a Worksheet. 
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcodes error message and unable to upload all the barcodes. 
- SeqPeek and CNVR can only be plotted with TCGA data, but if a cohort contains no TCGA samples the SeqPeek analysis will still search the TCGA BigQuery tables
- API endpoint samples.get currently down and will return a 503 error for all three programs. 
- On the File Browser page, while you are downloading CSV files, other filters can be selected. 
- Work is underway to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.

*February 1, 2018* `v3.8 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.8>`_

**Enhancements**
 
- We have enabled DNA methylation data to be used when plotting with genomic build hg38.
- The cohort view files page has been updated to File Browser. The File Browser page also now has new filters data level, data type, disease code, data format, and experimental strategy. A time stamp has also been added to the CSV file that can be downloaded.
- The IGV browser and caMicroscope are now more clearly defined and separated on the File Browser page.
- When uploading a set of barcodes to create a cohort the error message has been redefined to direct someone to the instructions.
 
**Bug Fixes**
 
- You can now plot DNA methylation data using genomic build hg19 when working on a worksheet.
- When registering a service account to controlled data you will no longer receive an error message when certain Google managed service accounts are also on the IAM and Admin page.
- On a worksheet, if you add new cohorts to a worksheet with pre-existing cohorts. Now the older and newly added cohorts are present on the worksheet for analysis.
- When working with a worksheet you are now able to plot gene names that contain periods.

**Known Issues**

- You cannot make a cohort using the cohort creation filter option on an Internet Explorer browser.
- Analysis Type: Seq peek Formatting Elongated on occasion.
- If the user shares a Cohort neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort. 
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a Worksheet, then tries to implement the log scale it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When working on Firefox browser a violin plot does not display the data plotted correctly when working on a Worksheet.
- When uploading TARGET files using the cohort barcode creation feature from the GDC you may get an invalid barcodes error message and unable to upload all the barcodes.
- SeqPeek can only be plotted with TCGA data, but if a cohort contains no TCGA samples the SeqPeek analysis will still search the TCGA BigQuery tables.
- API endpoint samples.get currently down and will return a 503 error for all three programs.
- Currently unable to use TARGET data with the IGV browser to view .bam files. 
- When editing the name of a cohort the cancel feature is not working properly. 
- When working on a worksheet the SeqPeek feature is currently not working with certain genes.
- Certain genes will produce a blank chart with no data on a worksheet when working with a histogram.
- Work is underway to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.

*December 20, 2017* `v3.7 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.7>`_
 
**Enhancements**

- Using the 'View Files' page you can now view TCGA pathology images using caMicroscope! 
- After logging into dbGaP you are now redirected to the user details page.  
- Due to recent updates with Google, we have implemented new security requirements when working with the service accounts and attempting the access the controlled data. For more information about new requirements please go `here <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/Gaining-Access-To-Contolled-Access-Data.html#requirements-for-registering-a-google-cloud-project-service-account>`_. 

**Bug Fixes**
 
- You will no longer experience a 502 error when trying to create a new variable favorite list if you have uploaded a lot of your own data using the user data upload feature.
 
**Known Issues**
 
- Analysis Type: Seq Peek formatting elongated on occasion 
- If the user shares a Cohort neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort. 
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
- When a user duplicates a Worksheet, then tries to implement the log scale it will not function properly. 
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL. 
- When working on Firefox browser a violin plot does not display the data plotted correctly when working on a Worksheet. 
- When working on a workbook if you add new cohorts to the worksheet the pre-existing cohorts will be de-selected from the worksheet.
- If you have uploaded a lot of data using the User Data Upload feature, it is likely you will experience 502 error page when attempting to create a new variable favorite list. 
- When uploading TARGET files using the cohort barcode creation feature from the GDC you may get an invalid barcodes error message and unable to upload all the barcodes.
- Work is underway to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.

*November 20, 2017* `v3.6 <https://github.com/isb-cgc/ISB-CGC-WebApp/releases/tag/3.6>`_
 
**Enhancements**
 
- You can now send a cohort you have created in the web application to a new BigQuery dataset or append an existing table. 
- The cohort creation by uploading barcodes feature has been extended to include .JSON and .TSV files from the Genomic Data Commons data portal. 
- Created a new API endpoint to be used to return a GCS object URL given a GDC file identifier also known as a UUID.
- Updated the registered Google Cloud Project to clearly state if the project’s service accounts are active or not.
- You can now enter special characters into the comments section for workbooks and cohorts e.g URL 
- On the register a service account page the Compute Engine default service account is automatically added to the enter service ID text box.
- When creating a new cohort we have implemented a text saying, “Creating cohort...” for instances when creating a new cohort takes a little longer than usual.
- We have significantly sped up loading times for the cohorts detail and cohorts table list page for users who have 50 + cohorts which caused slow loading time.
 
**Bug Fixes**
 
- A duplication of the exact cohort will no longer happen when you select the confirmation multiple times while the page is loading working with Set Operations. 
- On the cohort details, you can no longer select the clinical feature panel and edit filters without selecting the edit button first. 
- On the cohort creation page, you can use the clinical feature panel to select filters when working with the User data upload tab.

**Known Issues**
 
- Analysis Type: Seq peek Formatting Elongated on occasion 
- If the user shares a Cohort neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort. 
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
- When a user duplicates a Worksheet, then tries to implement the log scale it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When working on Firefox browser a violin plot does not display the data plotted correctly when working on a Worksheet. 
- When working on a workbook if you add new cohorts to the worksheet the pre-existing cohorts will be de-selected from the worksheet. 
- If you have uploaded a lot of data using the User Data Upload feature, it is likely you will experience 502 error page when attempting to create a new variable favorite list. 
- When working with the API endpoints the sample.get for all three programs will return a 503 internal server error.

*October 13, 2017* `v3.5 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.5>`_
 
**Enhancements**
 
- You can now upload sample and case identifiers from programs TCGA, CCLE and TARGET to create a cohort. 
- We have begun to allow the addition/removal of a service account with a new button instead of the user having to re-register the service account every time.
- For the Set Operations feature when working with cohorts has been enhanced and has become easier to work with. 
- For the Set Operation Complement feature you will now create a cohort faster than before.
- You will now be displayed mouse over text when working with the New Workbook, Delete, Set Operations, and Share button on the Cohorts list details page. 
- The About Us link in the top left of the page has been re-named to Homepage. 

**Bug Fixes**
 
- All bam files for the TARGET program are available to be used with the IGV browser. 
- On the Cohort creation page, you can now select a filter for your Cohort by selecting an option from the Clinical Feature graphs using Histological Type for program CCLE. 

**Known Issues**
 
- Analysis Type: Seq peek Formatting Elongated on occasion 
- If the user shares a Cohort neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
- When a user duplicates a Worksheet, then tries to implement the log scale it will not function properly. 
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations. 
- The mouse-over feature is currently disabled for program TARGET with disease code ALL. 
- When working on Firefox browser a violin plot does not display the data plotted correctly when working on a Worksheet. 
- We need to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.

*September 21,2017* `v3.4 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.4>`_
 
**Enhancements**
 
- When plotting, certain values will now be displayed as categorical when before it was displayed as a numerical value e.g Tobacco Smoking History.
- The Homepage has been updated to incorporate links for TARGET and CCLE programs.
- The extended list of programs and projects on the new User Uploaded Data creation page is now displayed in alphabetical order.
- On the user details page you are now shown a confirmation box when you attempt to unlink the NIH identity account associated to the Google Identity you originally logged in with. 
- When working with Workbooks you are now shown a table on the top right hand side of Worksheet which shows what BigQuery tables the information being displayed is from. 
- On the Cohort creation page you can now select a filter for your Cohort by selecting an option from the Clinical Features graphs. 
- On the user details page, if you attempt to associate you Google Identity to an NIH Identity that is already registered in the system to another Google Account you are given a yellow error message stating which email the NIH Identity is already associated to. 

**Bug Fixes**

- When working with Workbooks the log scale graphing option will be saved when a user comes back to the Worksheet at another time. 
- On the existing Cohorts table list page, the confirmation delete ‘blue x’ button will now remove a selected Cohort if you select another option e.g Set Operation.
- The Google Cloud Project details page refresh wheel and delete icon are now working properly for service accounts.
- The Cloud Project details page now lists the authorized datasets active with an associated service account. 
- When deleting a User Uploaded program you are now sent to the existing programs list page if you delete the program. If you delete the project you stay on the program details page. 
- The ownership of a Variable list, Gene and miRNa list, and User Uploaded Programs are now verified. This means you can no longer view any existing in system if you are not the original creator.
- A confirmation on the Register a Service Account page has been implemented for service accounts when the user attempts to register. 
- On the Cohort creation when toggling between the tabs for the different programs, you now cannot switch tabs until the tab on display is loaded. 
- We need to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.

**Known Issues**
 
- Analysis Type : Seq peek Formatting Elongated on occasion 
- If the user shares a Cohort neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort. 
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
- When a user duplicates a Worksheet, then tries to implement the log scale it will not function properly.
- The set operation for existing Cohorts complement is behaving exceptionally slow. 
- A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations. 
- The mouse over feature is currently disabled for program TARGET with disease code ALL.
- A very small amount of bam files for program TARGET currently have the wrong file name and cannot be used with the IGV browser. 
- When working on Firefox browser a violin plot does not display the data plotted correctly when working on a Worksheet. 

*August 23, 2017* `v3.3 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.3>`_
 
**Enhancements**
 
- Users with NIH-approved access can now view and analyze TARGET (Therapeutically Applicable Research To Generate Effective Treatments) controlled data using service accounts and also on the IGV browser. 
- You will be returned a more detailed error message when invalid characters are used with user data uploading titles.
- On the File list page you will be allowed to select only one genomic build at a time for clarity on which build will be used by the IGV browser.
- When attempting to duplicate the registration of your Google Cloud Project you are given an error message saying, “A Google Cloud Project with the id xxx-xxx-xxxx already exists.”
- If you attempt to register a service account with the same datasets it already has activated, you will be given an error message saying, “Service account xxxxxxxxxxxx-compute@developer.gserviceaccount.com already exists with these datasets, and so does not need to be registered.”
- The Data Use Certification and Agreement covering your access to all controlled data has been added to the user details page in the interface.
- The CCLE user.get API endpoint has been removed from the system due to the fact we do not currently host any controlled CCLE data.
- The format of CSV file downloaded with Download IDs button from the cohort details page has been changed to display the case and sample barcodes as two separate columns.
- From the User uploaded program detail page, you can now edit the project name and description by selecting the gear option.
 
**Bug Fixes**
 
- When creating a large cohort you are no longer returned a red error message.
- The sharing feature for Workbooks, Cohorts, and User Uploaded Programs has been re-activated. You must enter a valid email address that is present in the system to share the workbook, cohort, or user uploaded program. If they are not present in our system please feel free to invite them to the `ISB-CGC website <https://isb-cgc.appspot.com/>`_.
- When working with a new worksheet or a duplicate worksheet with workbooks for categorical features e.g bar chart, you can no longer select the log option. The log option only applies to numerical options.
- When working with workbooks, selecting the Delete button multiple times will no longer result in an error, and instead return you to the Workbooks list page after successful deletion of the Workbook.
- Users can plot user uploaded data when working with workbooks when using variables and cohorts from the same files that were uploaded.
- The cohort.list API endpoint will display the correct cases count for cohorts listed.
- The Download File List as CSV on the File List page will download the correct information when genomic build hg38 is selected. 
- You are no longer able to add XSS-vulnerable characters to the edit section for user uploaded data.
- An improved error message is displayed when attempting to register a Google Project you are not associated with. 
- Making a new Gene and miRNA set from a Workbook will no longer result in lowercase gene and miRNA names. 
- The TCGA Sample.get API endpoint will no longer return a response with sample ID duplicates.

**Known Issues**
 
- Analysis Type : Seq peek Formatting Elongated on occasion
- If the user shares a cohort neither the owner nor the person who was granted access to cohort will receive a confirmation email when sharing a cohort.
- CCLE data cannot be plotted when working with workbooks. ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
- When a user duplicates a worksheet, then tries to implement the log scale it will not function properly. 
- On the existing cohorts table list page, the confirmation delete ‘blue x’ button does not remove selected cohort if you select another option e.g Set Operation. The same issue can be found in reverse if you select the ‘blue x’ on the confirmation page for set operation you can then select the delete button and see the cohort on the confirmation panel.
- When working with working with workbooks the log option is not working properly for the plot settings. 
- The set operation for existing cohorts complement is behaving exceptionally slow. 
- A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations.
- When plotting, certain values will be displayed as numerical when it should be a categorical value e.g Tobacco Smoking History.
- The mouse over feature is currently disabled for program TARGET with disease code ALL. 

*July 31, 2017* `v3.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.2>`_

**Enhancements**

- You will be returned a more detailed error message when using invalid characters when working with user data uploading titles. 
- On the File list page you will are allowed to select only one genomic build at a time for better clarification of which build you will view on the IGV browser.

**Bug Fixes**

- When working with Swap Values button on a worksheet, the log option selected for either axis is now carried over as well when the swap values button is selected. 
- On the IGV browser when working with TCGA data build hg38 the interface will no longer return a No feature found with name “efgr” at the bottom of the IGV browser page. 
- When working with the cohort.create API endpoint you have the ability to create a large cohort with the barcode filter without a timeout error. 
- When creating a cohort with the cohort.create API endpoint you can view the list of barcodes from the cohort details page in the ISB-CGC user interface irrelevant of size. 
- When working with the create a new variable favorites list page, you can now create a variable list using the USER DATA tab. 

**Known Issues**

- The sharing feature for Workbooks, Cohorts, and User Uploaded Programs is currently disabled
- Analysis Type : Seq peek Formatting Elongated on occasion 
- The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
- Cannot plot any data if you use a CCLE data cohort on a worksheet. 
- On the existing cohorts table list page, the confirmation delete ‘blue x’ button does not remove selected cohort if you select another option e.g Set Operation. The same issue can be found in reverse if you select the ‘blue x’ on the confirmation page for set operation you can then select the delete button and see the cohort on the confirmation panel.
- The set operation for existing cohorts complement is behaving exceptionally slow. 
- A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations.
- When working with a new worksheet or a duplicate worksheet with workbooks for categorical features e.g bar chart you can select the log option. The log option only applies to numerical options.
- When working with workbooks, if you select the delete confirmation button multiple times while the page is loading you will be sent to an error page. 
- You currently cannot plot user uploaded data when working with workbooks.
- When plotting, certain values will be displayed as numerical when it should be a categorical value e.g Tobacco Smoking History. 
- The mouse over feature is currently disabled for program TARGET with disease code ALL.
- The cohort.list API endpoint will display the incorrect cases count for cohort listed.
- The Download File List as CSV on the File List page downloads the wrong information when genomic build hg38 is selected. 
- You are currently able to add non-whitelist characters to edit section for user uploaded data.
- You are returned a vague error message on the register a Google Cloud Project page when attempting to register a Google Project you are not associated to.
- The samples and cases filters have not been removed from the cohort.list API endpoint and are visible as a possible filter.
- The user.get CCLE program API endpoint will return a 503 internal server error.
- When creating large cohort you will be given a red error message saying, “There was an error saving your cohort; it may not have been saved correctly.” 

*June 14, 2017* `v3.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.1>`_

**Known Issues**
 
- Analysis Type : Seq peek Formatting Elongated on occasion 
- The CCLE data in the Webapp is not exactly the same as the CCLE data in BigQuery. 
- Users cannot plot any data from a CCLE cohort on a worksheet.
- In the Webapp, the log scale on graphs does not function properly for duplicated worksheets. 
- On the existing cohorts table list page, the confirmation delete ‘blue x’ button does not remove selected cohort if you select another option e.g Set Operation. The same issue can be found in reverse if you select the ‘blue x’ on the confirmation page for set operation you can then select the delete button and see the cohort on the confirmation panel.
- Swap values is not working properly for the plot settings. 
- The set operation for existing cohorts complement is behaving exceptionally slow. 
- A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations.
- When working with a new worksheet or a duplicate worksheet with workbooks for categorical features e.g bar chart you can select the log option. The log option only applies to numerical options. 
- When working with workbooks, if you select the delete confirmation button multiple times while the page is loading you will be sent to an error page. 
- You currently cannot plot user uploaded data when working with workbooks. 
- When plotting, certain values will be displayed as numerical when it should be a categorical value e.g Tobacco Smoking History.
- On the IGV browser when working with TCGA data build hg38 you get a No feature found with name “efgr” at the bottom of the iGV browser page. 
- On the cohort creation page for TCGA data the filters disease code and project short name NA is an option which is not a valid disease.
- The mouse over feature is currently disabled for program TARGET with disease code ALL.
- The sharing feature for Workbooks, Cohorts, and User Uploaded Programs is currently disabled. 
- A number of TCGA and CCLE case IDs shown below will have been removed from all cohorts since they are no longer available from NCI’s Genomics Data Commons, and ISB-CGC is trying to mirror that data as closely as possible.
 
 - TCGA cases:
TCGA-33-4579, TCGA-35-3621, TCGA-66-2746, TCGA-66-2747, TCGA-66-2750, TCGA-66-2751, TCGA-66-2752, TCGA-AN-A0FE, TCGA-AN-A0FG, TCGA-BH-A0B2, TCGA-BR-4186, TCGA-BR-4190, TCGA-BR-4194, TCGA-BR-4195, TCGA-BR-4196, TCGA-BR-4197, TCGA-BR-4199, TCGA-BR-4200, TCGA-BR-4205, TCGA-BR-4259, TCGA-BR-4260, TCGA-BR-4261, TCGA-BR-4263, TCGA-BR-4264, TCGA-BR-4265, TCGA-BR-4266, TCGA-BR-4270, TCGA-BR-4271, TCGA-BR-4272, TCGA-BR-4273, TCGA-BR-4274, TCGA-BR-4276, TCGA-BR-4277, TCGA-BR-4278, TCGA-BR-4281, TCGA-BR-4282, TCGA-BR-4283, TCGA-BR-4284, TCGA-BR-4285, TCGA-BR-4286, TCGA-BR-4288, TCGA-BR-4291, TCGA-BR-4298, TCGA-BR-4375, TCGA-BR-4376, TCGA-DM-A286, TCGA-E2-A1IP, TCGA-F4-6857, TCGA-GN-A261, TCGA-O2-A5IC, TCGA-PN-A8M9

- CCLE cases:
LS123, LS1034

- The number of cases and samples when viewed in the User Interface as compared to the BigQuery tables vary across all three projects (TCGA, TARGET, and CCLE). This is because the user interface reflects the data available at the Genomic Data Commons, whereas data in BigQuery reflects either data at the original TCGA data coordinating center supplemented with Genomic Data Commons Data (for TCGA and CCLE), or for TARGET, data received from the TARGET data coordinating center, not the Genomic Data Commons.
- We have removed Google Genomics functionality from the user interface. You will still be able to access CCLE open access data in Google Genomics from the command line. We are open to adding Google Genomics controlled data back into the user interface if you have a use case for it. Also we are restructuring the handling of multiple Programs of data. Please feel free to provide `feedback <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_. 
- For TARGET data the clinical and Gene Expression files themselves are available in the system.

**Enhancements**

- You will be returned a more detailed error message when uploading your own user data.
- On the Data Availability section on the cohort details page now displays the HG38 somatic mutation information for program TCGA.
  
**Bug Fixes**
   
- There is now a 2000 character limit for the workbook title section. 
- When selecting the cohort link to complete analysis section on a worksheet will send you to the existing cohort list table page. 
- Latency issues when working with the cohort creation page have been resolved.
- When working with TCGA data the IGV browser will not give you a 401 or a 404 error. 
- The mouse over feature will display the long name for disease code and project short name for all programs.
- On the cohort creation page you can now filter with the HG38 somatic mutation data by gene for program TCGA using the Molecular tab. 
- On the IGV Browser when working with TCGA genomic build hg38 you will no longer get a 404 error. 
- On the cohort creation page when working with User Data tab, the left filter panel sorts the other filter. 
- Cohorts created with API specific filters are now accessible to access by their cohort details page. 
- You are now able to plot miRNA data with genomic build hg38 for TARGET data. 
   
*May 25, 2017* `v3.0 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.0>`_

In collaboration with the GDC we now have TARGET pediatric cancer data available for analysis in the user interface. You are now able to create cohorts and plot analysis with information from TARGET, TCGA, and CCLE data. 
 
In addition, we have replaced the previous APIs with a new version that supports the new user interface.
 
We have also released the analyzed data types that are based on genome build GRCh38 for TCGA and TARGET data. GRCh37 (HG19) is also still available for TCGA, TARGET, and CCLE datasets.

Workbooks, cohorts, and variables favorites list created before the data structure migration will still be available for analysis and have been labeled as legacy and version 1. If you have difficulty using version 1 workbooks, please contact us

**Known Issues**

- Analysis Type : Seq peek Formatting Elongated on occasion 
- The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
- If the user shares a cohort neither the owner nor the person who was granted access to cohort will receive a confirmation email. 
- Cannot plot any data if you use a CCLE data cohort on a worksheet.
- When a user duplicates a worksheet, then tries to implement the log scale it will not function properly. 
- On the existing cohorts table list page, the confirmation delete ‘blue x’ button does not remove selected cohort if you select another option e.g Set Operation. The same issue can be found in reverse if you select the ‘blue x’ on the confirmation page for set operation you can then select the delete button and see the cohort on the confirmation panel. 
- On the cohort view files page there are capitalization bugs on the Platform filter.
- Swap values is not working properly for the plot settings. 
- The set operation for existing cohorts complement is behaving exceptionally slow. 
- A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations.
- When working with a new worksheet or a duplicate worksheet with workbooks for categorical features e.g bar chart you can select the log option. The log option only applies to numerical options. 
- When working with workbooks, if you select the delete confirmation button multiple times while the page is loading you will be sent to an error page.
- When working on a scatter plot the Tobacco Smoking being used as the Legend is displayed in numerical values when it should be displayed as categorical values.
- The character limit for a workbook title name is currently inactive, if you exceed the possible limit you will be sent to an error page.
- You currently cannot plot user uploaded data when working with workbooks. 
- Selecting cohort from worksheet “To Complete Analysis” section will send you to a 400 Bad Request error.
- You will experience latency issues when working with the create a new cohort page. 
- When plotting, certain values will be displayed as numerical when it should be a categorical value e.g Tobacco Smoking History.
- The Data File Availability Panel for program CCLE in currently inactive when on the cohort details page and also editing a cohort with CCLE data. 
- On the File List page you currently unable to access the bam files for the IGV Browser associated to build hg38 when working with TCGA data.
- A number of TCGA and CCLE case IDs shown below will have been removed from all cohorts since they are no longer available from NCI’s Genomics Data Commons, and ISB-CGC is trying to mirror that data as much as possible.
 - TCGA cases:
TCGA-33-4579, TCGA-35-3621, TCGA-66-2746, TCGA-66-2747, TCGA-66-2750, TCGA-66-2751, TCGA-66-2752, TCGA-AN-A0FE, TCGA-AN-A0FG, TCGA-BH-A0B2, TCGA-BR-4186, TCGA-BR-4190, TCGA-BR-4194, TCGA-BR-4195, TCGA-BR-4196, TCGA-BR-4197, TCGA-BR-4199, TCGA-BR-4200, TCGA-BR-4205, TCGA-BR-4259, TCGA-BR-4260, TCGA-BR-4261, TCGA-BR-4263, TCGA-BR-4264, TCGA-BR-4265, TCGA-BR-4266, TCGA-BR-4270, TCGA-BR-4271, TCGA-BR-4272, TCGA-BR-4273, TCGA-BR-4274, TCGA-BR-4276, TCGA-BR-4277, TCGA-BR-4278, TCGA-BR-4281, TCGA-BR-4282, TCGA-BR-4283, TCGA-BR-4284, TCGA-BR-4285, TCGA-BR-4286, TCGA-BR-4288, TCGA-BR-4291, TCGA-BR-4298, TCGA-BR-4375, TCGA-BR-4376, TCGA-DM-A286, TCGA-E2-A1IP, TCGA-F4-6857, TCGA-GN-A261, TCGA-O2-A5IC, TCGA-PN-A8M9
 - CCLE cases:
LS123, LS1034
- The number of cases and samples when viewed in the User Interface as compared to the BigQuery tables vary across all three projects (TCGA, TARGET, and CCLE). This is because the user interface reflects the data available at the Genomic Data Commons, whereas data in BigQuery reflects either (for TCGA and CCLE) data at the original TCGA data coordinating center supplemented with Genomic Data Commons Data, or for TARGET, data received from the TARGET data coordinating center, not the Genomic Data Commons.
- We have removed Google Genomics functionality from the user interface. You will still be able to access CCLE open access data in Google Genomics from the command line. We are open to adding Google Genomics controlled data back into the user interface if you have a use case for it. Also we are restructuring the handling of multiple Programs of data. Please feel free to provide `feedback <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_. 
- For TARGET data the clinical and Gene Expression files themselves are available in the system. The bam files will be available soon! 

**Enhancements**

- You will be returned a more detailed error message when uploading your own user data. 
- The user interface now displays the same nomenclature as the Genomic Data Commons (GDC).

**Bug Fixes**

- The user data upload is enabled and users can now upload their own datasets and create cohorts using existing programs and newly uploaded data by the user.
- You can now have multiple Google Cloud Projects associated to your account and use only one bucket and dataset on one project with no interference. 

*April 12, 2017* `v1.15 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.15>`_

**Known Issues**

- We are currently having issues viewing bam files using the IGV browser for TCGA and CCLE data. We are working to fix the issue and it should be resolved as soon as possible.

*February 26, 2017* `v1.14 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.14>`_

**Known Issues**
  
- Analysis Type : Seq peek Formatting Elongated 
- The CCLE data in GUI is not parallel to the CCLE data in BigQuery.
- If the user shares a cohort neither the owner nor the person who was granted access to cohort will receive a confirmation email.
- Cannot plot any data if you use a CCLE data cohort on a worksheet. 
- When a user duplicates a worksheet, then tries to implement the log scale it will not function properly. 
- On the existing cohorts table list page, the confirmation delete ‘blue x’ button does not remove selected cohort if you select another option e.g Set Operation. The same issue can be found in reverse if you select the ‘blue x’ on the confirmation page for set operation you can then select the delete button and see the cohort on the confirmation panel. 
- On the cohort view files page there are capitalization bugs on the Platform filter. 
- Swap values is not working properly for the plot settings. 
- The set operation for existing cohorts complement is behaving exceptionally slow. 
- A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations. 
- When working with a new worksheet or a duplicate worksheet with workbooks for categorical features e.g bar chart you can select the log option. The log option only applies to numerical options. 
- If multiple Google Cloud Projects are registered through the user interface, it is advised to to add Google buckets and BigQuery datasets to both projects currently. 
- When working with workbooks, if you select the delete confirmation button multiple times while the page is loading you will be sent to an error page. 
- When working on a scatter plot the Tobacco Smoking being used as the Legend is displayed in numerical values when it should be displayed as categorical values. 
- The character limit for a workbook title name is currently inactive, if you exceed the possible limit you will be sent to an error page. 
- We have removed Google Genomics functionality from the user interface. You will still be able to access CCLE open access data in Google Genomics from the command line. We are open to adding Google Genomics controlled data back into the user interface if you have a use case for it. Also we are restructuring the handling of multiple Programs of data. Please feel free to provide `feedback <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_. 
- There will be a reduced number of releases and features over the next month (or so) while we do some rework required for enabling the distribution of additional data sets and types copied from the NCI-GDC. The new data type is TARGET data, and different analyzed data types are based on the hg38 genome builds. Stay tuned in likely the early part of 2017.
- User data uploads are currently disabled. Any projects you have previously uploaded will continue to be available in your Saved Projects list, and you can continue to work with them, but new data cannot be added at this time. We are working on bringing this function up again, please stay tuned.

**Bug Fixes**
  
- User will no longer be sent to the Social Network Login page when trying to login. If this occurs, please feel free to send ISB-CGC feedback using this link `feedback <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_.

*November 30, 2016* `v1.13 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.13>`_

**Known Issues**
  
- Analysis Type : Seq peek Formatting Elongated 
- The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
- User will occasionally be sent to the Social Network Login page when trying to login. If this occurs, please go the the home page of the Web Application and try again. 
- If the user shares a cohort they do not receive a confirmation email. 
- Cannot plot any data if you use CCLE data cohort on a worksheet. 
- When a user duplicates a worksheet, then tries to implement the log scale it will not function properly. 
- If a researcher leaves the workbooks inactive the page freezes. 
- On the existing cohort list page for the delete button, select the blue x does nothing. It should be disabled. 
- On the cohort view files page there are capitalization bugs on the Platform filter. 
- Swap values is not working properly for the plot settings. 
- Some plot setting are saved or retrieved when working with worksheets. 
- The set operation for existing cohorts intersection is behaving exceptionally slow.
- We have removed Google Genomics functionality from the user interface. You will still be able to access CCLE open access data in Google Genomics from the command line. We are open to adding Google Genomics controlled data back into the user interface if you have a use case for it. Also we are restructuring the handling of multiple Programs of data. Please feel free to provide `here <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_. 
- There will be a reduced number of releases and features over the next month (or so) while we do some rework required for enabling the distribution of additional data sets and types copied from the NCI-GDC. The new data type is TARGET data, and different analyzed data types are based on the hg38 genome builds. Stay tuned in likely the early part of 2017.

**Bug Fixes**
  
- The user can no longer see BCGSC expression as an option when plotting genes if user does not select center filter on worksheet. 
- Worksheets added to an existing workbook now behave the same as the original worksheet.
- Cohort set operations no longer performing exceptionally slow.
  
*November 16, 2016* `v1.12 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.12>`_

**Known Issues**
  
- Analysis Type : Seq peek Formatting is Elongated 
- The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
- User will occasionally be sent to the Social Network Login page when trying to login. If this occurs, please go the the home page of the Web Application and try again. 
- If the user shares a cohort they do not receive a confirmation email. 
- Cannot plot any data if you use CCLE data cohort on a worksheet. 
- When a user duplicates a worksheet, then tries to implement the log scale it will not function properly. 
- If a researcher leaves the workbooks inactive the page freezes. 
- On the existing cohort list page for the delete button, selecting the blue x does nothing. It will be be disabled in a future release. 
- On the cohort view files page there are capitalization bugs on the Platform filter. 
- Swap values is not working properly for the plot settings. 
- Some plot setting are saved or retrieved when working with worksheets. 
- Worksheets added to an existing workbook behave differently than the original worksheet. 
- The user can see BCGSC expression as an option when plotting genes if user does not select center filter on worksheet. 
- The set operation for existing cohorts intersection is behaving exceptionally slow. 
- We are removing Google Genomics from the user interface. You will still be able to access CCLE open access data in Google Genomics from the command line. We are open to adding Google Genomics controlled data back into the user interface if you have a use case for it. Please feel free to provide `feedback <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_.

**Enhancements**
  
- A warning will be displayed if the user is trying to plot with required data missing e.g. must select an analysis, gene or variable, and a cohort to create a plot. 
- On the project details page user will be sent to upload new study in existing project tab when they select upload data. 
- When the user plots a graph with NA values, you will be returned a notification stating no valid data was found. 
- There is no longer text overlapping on the Cloud Hosted Datasets readthedocs page in the documentation. 
  
**Bug Fixes**
  
- The user can no longer add the same gene symbol twice if list to the same worksheet even if they have given their list different names. 
- When the user selects multiple cohorts for color by feature for scatter plot all cohorts selected display on the graph. 
- On the existing cohorts table for public cohorts, the new workbook and set operations buttons are now active. 
- For all analysis types the x-axis and y-axis with certain variables text will no longer overlap and is displayed clearly. 
- The upload data button is disabled on the review files page when no buckets or datasets are associated. 
- Someone with multiple eRA accounts will be no longer have issues when trying to access controlled data. 
  
*November 2, 2016* `v1.11 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.11>`_

**Known Issues**

- The user can add same gene twice if list to the same worksheet it they have different names. 
- Analysis Type : Seq peek Formatting Elongated 
- The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
- If a user creates a cohort with sample type filter Cell Lines and CCLE the total number of samples count off by one. 
- User will occasionally be sent to the Social Network Login page when trying to login. If this occurs, please go the the home page of the Web Application and try again. 
- If the user shares a cohort they do not receive a confirmation email. 
- When the user selects multiple cohorts for color by feature for scatter plot they do not display in chart. 
- Cannot plot any data if you use CCLE data cohort on a worksheet. 
- When the user plots a graph with NA values the UI returns a blank graph. 
- When a user duplicates a worksheet, then tries to implement the log scale it will not function properly. 
- If a researcher leaves the workbooks inactive the page freezes. 
- On the existing cohort list page for the delete button, selecting the blue x does nothing. It should be disabled. 
- On the cohort view files page capitalization bugs on the Platform filter. 
- Swap values is not working properly for the plot settings. 
- Some plot settings are saved or retrieved when working with worksheets. 
- On the existing cohorts table for public cohorts, the new workbook and set operations buttons are currently inactive. 
- Worksheets added to an existing workbook behave differently than the original worksheet.

**Enhancements**

- Introduce user data upload functionality see documentation `here <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/program_data_upload.html>`_.
- More fluid zoom feature when working with analysis worksheets. 
- Case Sensitivity is now maintained in creating and displaying Workbook names throughout the entire User Interface. 
- You can now create a new cohort from the menu bar. 
- Variables menu bar is displayed similar to the rest of the favorites variables. 
- On the dashboard, all create new buttons/links are identical. 
- Owner of what is shared either a workbook or a cohort is able to remove multiple viewers. Viewers are also able to remove themselves. 
- Removed BCGSC gene expression from the UI gene specification selection for plot analysis. 

**Bug Fixes**

- X or Y- Axis for text no longer overlaps on worksheet for any analysis type, except for violin plot. 
- The Legend is no longer displayed elongated when you use multiple cohort for color by feature for violin plot. 
- miRNA_expression_values_fixed table in dataset 2016_07_09_tcga_data_open reflect only hg19.mirbase20 files. 
- You are now able to duplicate a workbook that has been shared with you by someone else. 
- Added pseudo-counts to the mosaic plots on the create new cohort page. This allows you to be sure of always being able to see (and select) the smallest contributors in these mosaics. 
- Removing the filter from the filter confirmation from the create new cohort page, this will remove it from the rest of filter selections. 
- Select the “check-all” feature on the create new cohort page will no longer cause duplicates on the selected filters panel. 
- Create cohort from plot selection now works with all analysis types. 
- Data inconsistencies between the create new cohort histogram filter and the most recent BigQuery datasets has been addressed and resolved.

*September 21, 2016* `v1.10 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.10>`_

**Enhancements**
  
- Text in confirmation box of a duplication of a workbook has been enhanced. 
- On the registered Google Cloud Projects page, icon has been added for the user to go directly to the Google Cloud Console page if desired. 
- When the a Service Account is removed from the Access Control List, the project owner is sent an email with an explanation as to why the account was removed. 
- IGV File List page displays of which page user is browsing. 

**Bug Fixes**

- For a Cubby hole plot the x - axis name can be seen clearly. 
- On a duplicate worksheet when working with gene specifications, user is able to select between all options multiple times. 
- Page becomes elongated when the user builds a Cubby Hole plot. 
- The selected variables for the plot setting on a worksheet are saved after the user leaves the workbook. 
- When registering a Google Cloud Project the user is displayed the list of emails associated to the GCP only once. 

**Known Issues**
  
- The user can add same gene twice if list to the same worksheet it they have different names. 
- The Bar chart on the worksheet panel renders overlapping text. 
- Analysis Type : Seq peek Formatting Elongated 
- The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
- If a user creates a cohort with sample type filter Cell Lines and CCLE the total number of samples count off by one. 
- User will occasionally be sent to the Social Network Login page when trying to login. If this occurs, please go the the home page of the Web Application and try again. 
- If the user shares a cohort they do not receive a confirmation email.
- The Legend is displayed elongated when you use multiple cohort for color by feature for violin plot.
- When the user selects multiple cohorts for color by feature for scatter plot they do not display in chart. 
- Cannot plot any data if you use CCLE data cohort on a worksheet. 
- When the user plots a graph with NA values the UI returns a blank graph. 
- When a user duplicates a worksheet, then tries to implement the log scale it will not function properly. 
- There are duplicate rows in the molecular data table in BigQuery. 

*September 7, 2016* `v1.9 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.9>`_

**Enhancements**
  
- Dictionary mapping feature types to units for use in plot displays added to worksheets. 
- The user now has the option to make the axis logarithmic if the plot can display continuous numerical data for eg. mRNA expression levels. 
- The NIH username entry is now case insensitive for dbGaP authorization.
- The mouse over feature works when the user has created a long workbook name on the existing workbooks table page.
- The mouse over functionality was added to the worksheet name within a workbook. 

**Bug Fixes**
  
- The order by ascending or descending feature is now working properly for the existing workbooks table page.
- Tobacco Smoking History filter in the create cohort page displays the filters in descriptive values.
- The user can now select all existing cohorts when on the add cohort(s) to worksheet page.
- The gene specification selection on the worksheet page is now working properly.
- When a user shares a workbook with someone the person who received viewer access to the workbook is sent a confirmation email. If the person who shared the workbook then deletes the workbook before it's opened, then the person clicks the invitation link the person is sent to the unknown invitation page. The button to go back to the Dashboard page appears like this, "Your Dashboard"
- The user is sent an email when the Service Account is removed the Access controlled list for having a user associated to the project who is not dbGaP authorized.

**Known Issues**

- The user can add same gene twice if list to the same worksheet it they have different names.
- The Bar chart on the worksheet panel renders overlapping text.
- Analysis Type : Seq peek Formatting Elongated 
- The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
- If a user creates a cohort with sample type filter Cell Lines and CCLE the total number of samples count off by one.
- User will occasionally be sent to the Social Network Login page when trying to login. If this occurs, please go the the home page of the Web Application and try again.
- Page becomes elongated when the user builds a Cubby Hole plot. 
- X-axis name cut off for cubby hole plot when x-axis has only 3 criteria.
- If the user shares a cohort they do not receive a confirmation email.
- The Legend is displayed elongated when you use multiple cohort for color by feature for violin plot.
- When the user selects multiple cohorts for color by feature for scatter plot they do not display in chart.
- When the user creates a duplicate worksheet,the bar chart with a gene with specification protein can freeze when selecting an option for the Select Feature.
- Cannot plot any data if you use CCLE data cohort on a worksheet.
- When the user plots a graph with NA values the UI returns a blank graph.
- When a user duplicates a worksheet, some functionality related to plotting will not function properly on the duplicate worksheet. 

*August 24, 2016* `v1.8 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.8>`_
  
**Known Issues**
  
- The user can add same gene twice if list to the same worksheet it they have different names. 
- The Bar chart on the worksheet panel renders overlapping text. 
- Analysis Type : Seq peek Formatting Elongated.
- The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
- If a user creates a cohort with sample type filter Cell Lines and CCLE the total number of samples count off by one. 
- User will occasionally be sent to the Social Network Login page when trying to login. If this occurs, please go the the home page of the Web Application and try again. 
- Page becomes elongated when the user builds a Cubby Hole plot. 
- X-axis name cut off for cubby hole plot when x-axis has only 3 criteria. 
- When the user shares a cohort they do not receive a confirmation email. 
- User will be spammed with email every one minute when their service account is removed from the ACL control list. To stop this, please either delete your service account from the ISB-CGC interface, or remove the GCP project member(s) who is (are) not authorized to access the controlled data set. (see documentation `here <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/Gaining-Access-To-Contolled-Access-Data.html>`_). We are planning to reduce the frequency of the notification emails to once per day. 
- The Legend is displayed elongated when you use multiple cohort for color by feature for violin plot. 
- When the user selects multiple cohorts for color by feature for scatter plot they do not display in chart. 
- When the user creates a duplicate worksheet,the bar chart with a gene with specification protein can freeze when selecting an option for the Select Feature. 
- When a user shares a workbook with someone the person who received viewer access to the workbook is sent a confirmation email. If the person who shared the workbook then deletes the workbook before it's opened, then the person clicks the invitation link the person is sent to the unknown invitation page. The button to go back to the Dashboard page appears like this, "Your Dashboard{" 
- Cannot plot any data if you use CCLE data cohort on a worksheet. 

**Enhancements**

- When the researcher is on the Register Service Account page, after they have submitted the Service Account associated to their Google Cloud Project a table that shows who is authorized will be prompted.
- There is now a column that says “Has NIH Identity”, before it said, “Has eRA Commons”. 
- When the researcher creates a new cohort with more than 20 filters chosen the URL exceeds the limit of 2K characters and this affects the count for the Details panel. Therefore the user is now prompted with an alert box that will say, “You have selected too many filters. The current counts shown will not be accurate until one or more filter options are removed.” if this is ever the case. 
- In the user details page, if the researcher has not registered a Google Cloud Project it will say, “Register a Google Cloud Project” on the link. 

**Bug Fixes**

- The researcher can now delete whom they share cohort with from existing cohorts table. 
- After 24-hours of use, a dbGaP authorized user can re-authenticate through the link provided in the user details page.
- The variable favorites list table page can now support a long title for the variable list.
- The filter name will appear aligned in the verification panel when the filter is name too long for the create in cohort filter confirmation selection on the create new cohort page. 
- Grouped Data Type filter counts (Methylation, RNA Seq, miRNA Seq) now behave like the other count groups. The counts will behave as grouped values. 
- The user can no longer select a categorical variable for selection for Histogram plot. 
- The Filter token displays are now shown in 'readable' names when working with cohort filters.
- Controlled access BAM files are now viewable viewable in the IGV browser after the user has authorized their credentials. 
- The user can now unlink an eRA commons account from their Google Identity in the user detail page. 
- The violin plot was inconsistently failing. We have updated the JavaScript, therefore the Violin plot no longer fail. 

*August 10, 2016* `v1.7 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.7>`_
  
**New Features**
  
- The researcher can now create a cohort of participants and samples based on the presence of a gene mutation in a specified gene. Look for the new “Molecular” tab when you are creating a cohort.
- The bioinformatics programmer now has the ability to associate their Google Cloud Project’s Service Account. This allows the researcher to run computational pipelines from Google Virtual Machines using TCGA Controlled data (e.g. BAM files) for seven days before they have to reauthorize. For more information please select `here <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/Gaining-Access-To-Contolled-Access-Data.html>`_.

**Known Issues**
  
- The user can add same gene twice if list to the same worksheet it they have different names.
- The Bar chart on the worksheet panel renders overlapping text. 
- Cannot delete whom you share cohort with from existing cohorts table. 
- Analysis Type : Seq peek Formatting Elongated
- The CCLE data in GUI is not exactly coordinated the CCLE data in BigQuery. 
- If a user creates a cohort with sample type filter Cell Lines and CCLE the total number of samples count is off by one. 
- After 24-hours of use, a dbGaP authorized user has to logout and then log back in to be prompted with NIH login link to re-access controlled data. 
- User will occasionally be sent to the Social Network Login page when trying to login. If this occurs, please go the the home page of the Web Application and try again.
- Page becomes elongated when the user builds a Cubby Hole plot. 
- X-axis name cut off for Cubby Hole plot when x-axis has only 3 criteria. 
- When the user shares a cohort they do not receive a confirmation email. 
- When a name is too long for variable favorites list table, the Last Updated” column will appear cut off. 
- Filter name will appear off the verification panel when the filter is name too long for the create in cohort filter selection. 
- Grouped Data Type filter counts (Methylation, RNA Seq, miRNA Seq) don't behave like other count groups. The counts behave as though the values were for distinct categories. 
- User will be spammed with email every one minute when their service account is removed from the ACL control list. To stop this, please either delete your service account from the ISB-CGC interface, or remove the GCP project member(s) who is (are) not authorized to access the controlled data set. (see documentation here). We are planning to reduce the frequency of the notification emails to once per day.
- The user can select a categorical variable for selection for Histogram plot, and will return a graph with no data. 
- The Legend is displayed elongated when you use multiple cohort for color by feature for violin plot.
- When the user selects multiple cohorts for color by feature for scatter plot they do not display in chart.
- When the user creates a duplicate worksheet,the bar chart with a gene with specification protein can freeze when selecting an option for the Select Feature. 
   
**Enhancements**
  
- The user now has the option to select all or deselect all possible filters for any tab that has more than 10 possible options in the create new cohort page. 
- The user can now set all existing tables by either ascending or descending order. 
- The cohort_id has been added to the detail cohort page. This allows the user to reference a desired cohort with ease in the API endpoints. 
- When creating a new cohort, the user is given the full description for sample type in the selected filters panel.
  
**Bug Fixes**
  
- Histological Type entries in create new cohort page on the user interface now match the Google BigQuery entries in terms of capitalization. 
- Filters for data type counts in left panel currently is now working properly. 
- When a user sets a cohort as Color by feature for violin plot legend will be set to cohort. Then when the user sets another color by feature it will update the legend.
- The user can no longer make a gene list without selecting a gene first. 
- The user can now list the Last Modified section for the existing cohort table by either ascending or descending order.
- In the create new cohort page for the data type tab, the user can now select either True or False for DNA Sequencing, Protein, and SNP Copy Number filters. 
- When the user edits a new cohort and sets the edited cohort to return zero samples, the user will be prompted to select different set of filters.

*July 20, 2016* `v1.6 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.6>`_
  
**Known Issues**
  
- The user can add same gene twice if two identical worksheets with different names are uploaded.
- The Bar chart on the worksheet panel renders overlapping text.
- User cannot delete whom you share cohort with from existing cohorts table.
- Analysis Type : Seq peek Formatting Elongated.
- The CCLE data in GUI is not parallel to the CCLE data in BigQuery.
- If a user creates a cohort with sample type filter Cell Lines and CCLE the total number of samples count off by one.
- Histological Type entries in create new cohort page on the user interface should match the Google BigQuery entries in terms of capitalization.
- When a user sets a cohort as Color by feature for violin plot legend will remain cohort.
- After 24 hour dbGaP authorization runs out the user is unable to re authenticate. (If you have this issue, please log out and log back in to be prompted with login link for dbGaP authorization.)

**Enhancements**
  
- Created ability in GUI to make cohorts based on presence of an HPV status.
- Created ability in GUI to make cohorts based on BMI value.
- In the details panel for existing cohort have a section that shows the ISB-CGC cohort_id.
- Enhancements of GUI to view submenu item in different screen sizes and resolutions.
- New version of IGV javascript installed.

**Bug Fixes**

- User can no longer add same filter to existing cohorts.
- Optimized Security in the user interface.
- If a user opens a shared cohort it will appear once on the dashboard.
- Pathologic State Filter in create cohort Stage is displayed capitalized.
- Filter counts with 0 value do list when editing a pre-existing cohort.
- Filters for data type counting in left panel is working properly.
- After 24 hour dbGaP authorization runs out the user is able to re authenticate.
- User can not create new gene list without giving the gene list a name.

*July 6, 2016* `v1.5 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.5>`_
  
**Known Issues**
  
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

**Enhancements**
  
- A user can only select the cloud storage checkbox if he or she has been authenticated and authorized through the user details page. Otherwise the user can view the cloud storage checkbox but there will be a disabled cursor icon when the user hovers over in an attempt to select the checkbox.
- The counts for the queries were refactored to match what was done for the APIs .
- The Download File List as CSV was refactored to a maximum of 65,000 files at once.
- Date formats on Workbooks, Cohort, Gene, and Variables list pages all reflect the same format.
- The Last Updated columns to variable and gene lists were added to the user Dashboard

**Bug Fixes**

- The user can now select a cohort in the color by feature section for the violin and the scatter plots in the worksheet section.
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

*June 8, 2016* `v1.4 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.4>`_
  
**Known Issues**
  
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
- In Violin plot - the user has no ability to select a different gene once one is already selected.
- In the variable favorites table, the menu for a specific variable will be cut off once a certain set of variables list are exceeded.
- A 400 Error pop up window will appear as the user transitions from the File List page to IGV browser page.
- Public Data Availability section will be cut is user drags data type title to the left of the page away from the panel itself,in detail page of existing cohort.
 
**Enhancements**
  
- Upgraded system from using Django 1.8 to Django 1.9.
- A link to the google cloud platform has been added to the user details page. 
- The TCGA filter is selected as the default project when creating a new cohort.
- When the user clicks on the browser back button, the user will remain on the same worksheet that they were previously on.
- When the user goes adds a new gene list, variable favorites list, and/or cohort from the worksheet data type panel, the button will display “Apply to Worksheet”.
- The feedback/help section has been moved to the top of the page to provide the user a more convenient way to send us feedback.

**Bug Fixes**
 
- User can no longer add a duplicate gene to same gene favorites list. 
- To edit a gene name the user must now delete and re-type the desired gene name. 
- The functionality of a duplicate worksheet drop down menu reflects the same functionality of the original worksheet.
- The Last Updated section reflects any changes made to the variable list, cohort list, and gene list in their corresponding tables.
- The File list page now allows the user to add a maximum of five files to use in the IGV browser between all the pages in the file list table.
- When a user hovers over clinical feature panel for Sample Type and Tumor Tissue Type the top row when hovered over the name is displayed clearly.
- Order by Ascending/Descending is working properly for Existing Cohorts table page.
- The user is now able to plot gene’s with a hyphen(-) in the gene name itself.
- The user is now able to download a maximum of 85,000 files at a time, in the File List page for a selected cohort. 

*May 10, 2016* `v1.3 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.3>`_
 
**Known Issues**
  
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

**Enhancements**
  
- Data Use Certification Agreement link updated and the help link was removed. -
- The Data Type section in the Create new Cohort page name change from MIRNA Sequencing to miRNA Sequencing and SNP CN to SNP Copy-Number. 
- The number of patients is now dynamically displayed in the create new cohort page when selecting filters in the details panel.
- The number of samples is now dynamically displayed in the create new cohort page when selecting filters in the details panel.
- By default in the create new cohort page, you will have the TCGA data filter selected.
- When creating a cohort, checking feature boxes will be throttled so as to avoid miss-represented data.
- Tooltips were added to the Sample Type section in the clinical features panel.
- Minor changes were made in personal details page.

**Bug Fixes**
  
- The Clinical Features Panel in the create new cohort page will no longer display BRCA even if unselected.
- The last updated section in existing workbooks panel does update when changes are made to existing workbook.
- Set operation Union patient number is working correctly.
- Upon duplicating a cohort it will duplicate the selected filter(s) as well.
- User is able to download file list as csv for any cohort with any filter selected.
- There is no legend cut off for violin plot or any other analysis type when the color by feature is set to Prior Diagnosis or any other variable. 
- When user switches gene in plot settings the feature choices for that specification will refresh. 
- The variable clinical search feature works properly when the user searches for clinical variables and then are used for analysis.

*April 27, 2016* `v1.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.2>`_

**Known Issues** 

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

**Enhancements**

- The comments section now has a max number of characters 1000 limit.
- Link created to Extend controlled access period to 24-hours from the moment the link is clicked.

**Bug Fixes**

- A user can now click new worksheet multiple times within a few seconds and only produce one sheet.
- The user must now add a new filter in an existing cohort to edit it the cohort.
- The duplicate button for an existing cohort will only make one duplicate at a time.
- Clicking 150+ selected filters will not create an error page.
- Cancel button on Create new gene list page will send you to Gene list favorites table menu.
- Violin plot : User can not add categorial value to y-axis.
- If user edits an existing cohort, the old filter(s) will not be removed.
- If a new worksheet is generated, the worksheet functionality is working properly.
- User will get the ‘500: There was an error while handling your request. If you are trying to access a cohort please log out - and log back in. Sorry for the inconvenience.’ if the user is inactive for more in 15 minutes when trying to create/use existing cohort.
- Clinical Feature Panel is displayed properly and reacts to filters being added/removed quickly.
- The user must have text to add a comment.
- All columns in file list table will be transferred/displayed when exported as csv file.

*April 14, 2016* `v1.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.1>`_
  
**Known Issues** 

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
  
**Enhancements**
  
- Tool tips added for disease code in create new cohort page
- Disease in longname in tool tips the first letter is capitalized

**Bug Fixes**
  
- The user detail page will now display the correct date
- The plot settings for a new worksheet are now working properly
- Plot settings for duplicate worksheets are now working properly
- The plot settings will now match the analysis type for existing worksheet plot
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

*March 14, 2016* `v1.0 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.0>`_

- When working with a worksheet two plots will be generated occasionally.
- Axis labels and tick values sometimes overlap and get cutoff.
- Page elongated when Cubby Hole plot generated and there are lots of values in the y axis.

*December 23, 2015* `v0.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.1>`_

- Treemap graphs in cohort details and cohort creation pages will not apply its own filters to itself. For example, if you select a study, the study treemap graph will not update.
- Cohort file list download not working.

*December 3, 2015* `v0.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.0>`_

- First tagged release of the web-app
