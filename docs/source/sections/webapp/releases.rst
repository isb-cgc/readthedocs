*********************
Web-App Release Notes
*********************

* **October 13,2017**

 *Please Note: We need to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.*
 
 **Issues resolved in Sprint 20 as of 10/11/2017**
 
 New Enhancements
 
 - You can now upload sample and case identifiers from programs TCGA, CCLE and TARGET to create a cohort. 
 - We have begun to allow the addition/removal of a service account with a new button instead of the user having to re-register the service account every time.
 - For the Set Operations feature when working with cohorts has been enhanced and has become easier to work with. 
 - For the Set Operation Complement feature you will now create a cohort faster than before.
 - You will now be displayed mouse over text when working with the New Workbook, Delete, Set Operations, and Share button on the Cohorts list details page.  
 - The About Us link in the top left of the page has been re-named to Homepage. 
 
 Bug Fixes
 
 - All bam files for the TARGET program are available to be used with the IGV browser. 
 - On the Cohort creation page, you can now select a filter for your Cohort by selecting an option from the Clinical Feature graphs using Histological Type for program CCLE. 
 
 **Known Issues in Sprint 20 as of 10/12/2017**
 
 - Analysis Type: Seq peek Formatting Elongated on occasion 
 - If the user shares a Cohort neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort.
 - CCLE data cannot be plotted when working with workbooks.  ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
 - When a user duplicates a Worksheet, then tries to implement the log scale it will not function properly. 
 - The set operation for existing Cohorts complement is behaving exceptionally slow.
 - A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations. 
 - The mouse-over feature is currently disabled for program TARGET with disease code ALL. 
 - When working on Firefox browser a violin plot does not display the data plotted correctly when working on a Worksheet. 


* **September 21,2017** `v3.4 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.4>`_

 *Please Note: We need to rework our cohort creation page to better differentiate between samples which are from image data vs. those which are not.*
 
 **Issues that have been resolved in Sprint 19 as of 09/21/2017**
 
 
 New Enhancements
 
 - When plotting, certain values will now be displayed as categorical when before it was displayed as a numerical value e.g Tobacco Smoking History.
 - The Homepage has been updated to incorporate links for TARGET and CCLE programs.
 - The extended list of programs and projects on the new User Uploaded Data creation page is now displayed in alphabetical order.
 - On the user details page you are now shown a confirmation box when you attempt to unlink the NIH identity account associated to the Google Identity you originally logged in with. 
 - When working with Workbooks you are now shown a table on the top right hand side of Worksheet which shows what BigQuery tables the information being displayed is from. 
 - On the Cohort creation page you can now select a filter for your Cohort by selecting an option from the Clinical Features graphs. 
 - On the user details page, if you attempt to associate you Google Identity to an NIH Identity that is already registered in the system to another Google Account you are given a yellow error message stating which email the NIH Identity is already associated to. 
 
 Bug Fixes

 - When working with Workbooks the log scale graphing option will be saved when a user comes back to the Worksheet at another time. 
 - On the existing Cohorts table list page, the confirmation delete ‘blue x’ button will now remove a selected Cohort if you select another option e.g Set Operation.
 - The Google Cloud Project details page refresh wheel and delete icon are now working properly for service accounts.
 - The Cloud Project details page now lists the authorized datasets active with an associated service account. 
 - When deleting a User Uploaded program you are now sent to the existing programs list page if you delete the program.  If you delete the project you stay on the program details page. 
 - The ownership of a Variable list, Gene and miRNa list, and User Uploaded Programs are now verified. This means you can no longer view any existing in system if you are not the original creator.
 - A confirmation on the Register a Service Account page has been implemented for service accounts when the user attempts to register. 
 - On the Cohort creation when toggling between the tabs for the different programs, you now cannot switch tabs until the tab on display is loaded. 
 
 **Known issues in sprint 19 as of 09/21/2017**
 
 - Analysis Type : Seq peek Formatting Elongated on occasion 
 - If the user shares a Cohort neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort. 
 - CCLE data cannot be plotted when working with workbooks.  ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
 - When a user duplicates a Worksheet, then tries to implement the log scale it will not function properly.
 - The set operation for existing Cohorts complement is behaving exceptionally slow. 
 - A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations. 
 - The mouse over feature is currently disabled for program TARGET with disease code ALL.
 - A very small amount of bam files for program TARGET currently have the wrong file name and cannot be used with the IGV browser. 
 - When working on Firefox browser a violin plot does not display the data plotted correctly when working on a Worksheet. 

* **August 23, 2017**: `v3.3 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.3>`_
 **Issues that have been resolved in sprint 18 as of 08/23/2017**
 
 New Enhancements
 
 - Users with NIH-approved access can now view and analyze TARGET (Therapeutically Applicable Research To Generate Effective Treatments) controlled data using service accounts and also on the IGV browser. 
 - You will be returned a more detailed error message when invalid characters are used  with user data uploading titles.
 - On the File list page you will be allowed to select only one genomic build at a time for clarity on which build will be used by the IGV browser.
 - When attempting  to duplicate the registration of your Google Cloud Project you are given an error message saying, “A Google Cloud Project with the id xxx-xxx-xxxx already exists.”
 - If you attempt to register a service account with the same datasets it already has activated, you will be given an error message saying, “Service account xxxxxxxxxxxx-compute@developer.gserviceaccount.com already exists with these datasets, and so does not need to be registered.”
 - The Data Use Certification and Agreement covering your access to all controlled data  has been added to the user details page in the interface.
 - The CCLE user.get API endpoint has been removed from the system due to the fact we do not currently host any controlled CCLE data.
 - The format of CSV file downloaded with Download IDs button from the cohort details page has been changed to display the case and sample barcodes as two separate columns.
 - From the User uploaded program detail page, you can now edit the project name and description by selecting the gear option.
 
 Bug Fixes
 
 - When creating a large cohort you are no longer returned a red error message.
 - The sharing feature for Workbooks, Cohorts, and User Uploaded Programs has been re-activated.  You must enter a valid email address that is present in the system to share the workbook, cohort, or user uploaded program. If they are not present in our system please feel free to invite them to the `ISB-CGC website <https://isb-cgc.appspot.com/>`_.
 - When working with a new worksheet or a duplicate worksheet with workbooks for categorical features e.g bar chart, you can no longer select the log option. The log option only applies to numerical options.
 - When working with workbooks, selecting the Delete button multiple times will no longer result in an error, and instead return you to the Workbooks list page after successful deletion of the Workbook.
 - Users can plot user uploaded data when working with workbooks when using variables and cohorts from the same files that were uploaded.
 - The cohort.list API endpoint will display the correct cases count for cohorts listed.
 - The Download File List as CSV on the File List page will download the correct information when genomic build hg38 is selected. 
 - You are no longer able to add XSS-vulnerable characters to the edit section for user uploaded data.
 - An improved error message is displayed  when attempting to register a Google Project you are not associated with.  
 - Making a new Gene and miRNA set from a Workbook will no longer result in lowercase gene and miRNA names. 
 - The TCGA Sample.get API endpoint will no longer return a response with sample ID duplicates.
 
 **Known issues in sprint 18 as of 08/23/2017**
 
 - Analysis Type : Seq peek Formatting Elongated on occasion
 - If the user shares a cohort neither the owner nor the person who was granted access to cohort will receive a confirmation email when sharing a cohort.
 - CCLE data cannot be plotted when working with workbooks.  ISB-CGC will resolve this functionality after the GDC formally releases CCLE data.
 - When a user duplicates a worksheet, then tries to implement the log scale it will not function properly.  
 - On the existing cohorts table list page, the confirmation delete ‘blue x’ button does not remove selected cohort if you select another option e.g Set Operation. The same issue can be found in reverse if you select the ‘blue x’ on the confirmation page for  set operation you can then select the delete button and see the cohort on the confirmation panel.
 - When working with working with workbooks the log option is not working properly for the plot settings. 
 - The set operation for existing cohorts complement is behaving exceptionally slow. 
 - A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations.
 - When plotting, certain values will be displayed as numerical when it should be a categorical value e.g Tobacco Smoking History.
 - The mouse over feature is currently disabled for program TARGET with disease code ALL. 

* **July 31, 2017**: `v3.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.2>`_

 **Please Note:** When creating large cohort you will be given a red error message saying, “There was an error saving your cohort; it may not have been saved correctly.”  This issue is planned to be resolved in the next sprint.

 **Issues that have been resolved in sprint 17 as of 07/31/2017**

 New Enhancements

 - You will be returned a more detailed error message when using invalid characters when working with user data uploading titles. 
 - On the File list page you will are allowed to select only one genomic build at a time for better clarification of which build you will view on the IGV browser.

 Bug Fixes

 - When working with Swap Values button on a worksheet, the log option selected for either axis is now carried over as well when the swap values button is selected. 
 -  On the IGV browser when working with TCGA data build hg38 the interface will no longer return a No feature found with name “efgr” at the bottom of the IGV browser page. 
 -  When working with the cohort.create API endpoint you have the ability to create a large cohort with the barcode filter without a timeout error. 
 - When creating a cohort with the cohort.create API endpoint you can view the list of barcodes from the cohort details page in the ISB-CGC user interface irrelevant of size.  
 - When working with the create a new variable favorites list page, you can now create a variable list using the USER DATA tab. 


 **Known issues in sprint 17 as of 07/31/2017**

 - The sharing feature for Workbooks, Cohorts, and User Uploaded Programs is currently disabled
 - Analysis Type : Seq peek Formatting Elongated on occasion 
 - The CCLE data in GUI is not parallel to the CCLE data in BigQuery.  
 - Cannot plot any data if you use a CCLE data cohort on a worksheet.  
 - On the existing cohorts table list page, the confirmation delete ‘blue x’ button does not remove selected cohort if you select another option e.g Set Operation. The same issue can be found in reverse if you select the ‘blue x’ on the confirmation page for  set operation you can then select the delete button and see the cohort on the confirmation panel.
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
 


* **June 14, 2017**: `v3.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.1>`_

    **Please Note:**

    NOTE 1: A number of TCGA and CCLE case IDs shown below will have been removed from all cohorts since they are no longer available from NCI’s Genomics Data Commons, and ISB-CGC is trying to mirror that data as closely as possible.
 
    TCGA cases: TCGA-33-4579, TCGA-35-3621, TCGA-66-2746, TCGA-66-2747, TCGA-66-2750, TCGA-66-2751, TCGA-66-2752, TCGA-AN-A0FE, TCGA-AN-A0FG, TCGA-BH-A0B2, TCGA-BR-4186, TCGA-BR-4190, TCGA-BR-4194, TCGA-BR-4195, TCGA-BR-4196, TCGA-BR-4197, TCGA-BR-4199, TCGA-BR-4200, TCGA-BR-4205, TCGA-BR-4259, TCGA-BR-4260, TCGA-BR-4261, TCGA-BR-4263, TCGA-BR-4264, TCGA-BR-4265, TCGA-BR-4266, TCGA-BR-4270, TCGA-BR-4271, TCGA-BR-4272, TCGA-BR-4273, TCGA-BR-4274, TCGA-BR-4276, TCGA-BR-4277, TCGA-BR-4278, TCGA-BR-4281, TCGA-BR-4282, TCGA-BR-4283, TCGA-BR-4284, TCGA-BR-4285, TCGA-BR-4286, TCGA-BR-4288, TCGA-BR-4291, TCGA-BR-4298, TCGA-BR-4375, TCGA-BR-4376, TCGA-DM-A286, TCGA-E2-A1IP, TCGA-F4-6857, TCGA-GN-A261, TCGA-O2-A5IC, TCGA-PN-A8M9
 
    CCLE cases: LS123, LS1034
 
    NOTE 2: The number of cases and samples when viewed in the User Interface as compared to the BigQuery tables vary across all three projects (TCGA, TARGET, and CCLE).  This is because the user interface reflects the data available at the Genomic Data Commons, whereas data in BigQuery reflects either data at the original TCGA data coordinating center supplemented with Genomic Data Commons Data (for TCGA and CCLE), or for TARGET, data received from the TARGET data coordinating center, not the Genomic Data Commons.
 
    NOTE 3: We have removed Google Genomics functionality from the user interface. You will still be able to access CCLE open access data in Google Genomics from the command line. We are open to adding Google Genomics controlled data back into the user interface if you have a use case for it.  Also we are restructuring the handling of multiple Programs of data. Please feel free to provide `feedback <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_. 
 
    NOTE 4: For TARGET data the clinical and Gene Expression files themselves are available in the system. The bam files will be available soon! 
   
    **Known Issues in Sprint 16 as of 06/14/2017**
 
      - Analysis Type : Seq peek Formatting Elongated on occasion 
      - The CCLE data in the Webapp is not exactly the same as the CCLE data in BigQuery.  
      - Users cannot plot any data from a CCLE cohort on a worksheet.
      - In the Webapp, the log scale on graphs does not function properly for duplicated worksheets. 
      - On the existing cohorts table list page, the confirmation delete ‘blue x’ button does not remove selected cohort if you select another option e.g Set Operation. The same issue can be found in reverse if you select the ‘blue x’ on the confirmation page for  set operation you can then select the delete button and see the cohort on the confirmation panel.
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
      
    **Issues that have been resolved in sprint 16 as of 06/14/2017**

     New Enhancements

     - You will be returned a more detailed error message when uploading your own user data.
     - On the Data Availability section on the cohort details page now displays the HG38 somatic mutation information for program TCGA.
     
     Bug Fixes
     
     - There is now a 2000 character limit for the workbook title section. 
     - When selecting the cohort link to complete analysis section on a worksheet will send you to the existing cohort list table page. 
     - Latency issues when working with the cohort creation page have been resolved.
     - When working with TCGA data the IGV browser will not give you a 401 or a 404 error. 
     - The mouse over feature will display the long name for disease code and project short name for all programs.
     - On the cohort creation page you can now filter with the HG38 somatic mutation data  by gene for program TCGA using the Molecular tab. 
     - On the IGV Browser when working with TCGA genomic build hg38 you will no longer get  a 404 error. 
     - On the cohort creation page when working with User Data tab, the left filter panel sorts the other filter. 
     - Cohorts created with API specific filters are now accessible to access by their cohort details page. 
     - You are now able to plot miRNA data with genomic build hg38 for TARGET data. 
      

*  **May 25, 2017**: `v3.0 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.0>`_
    In collaboration with the GDC we now have TARGET pediatric cancer data available for analysis in the user interface.  You are now able to create cohorts and plot analysis with information from TARGET, TCGA, and CCLE data. 
 
    In addition, we have  replaced the previous APIs with a new version that supports  the new user interface.
 
    We have also released the analyzed data types that are based on genome build GRCh38 for TCGA and TARGET data.  GRCh37 (HG19) is also still available for TCGA, TARGET, and CCLE datasets.
 
    Workbooks, cohorts, and variables favorites list created before the data structure migration will still be available for analysis and have been labeled as legacy and version 1.  If you have difficulty using version 1 workbooks, please contact us

    **Please Note:**

    NOTE 1:A number of TCGA and CCLE case IDs shown below will have been removed from all cohorts since they are no longer available from NCI’s Genomics Data Commons, and ISB-CGC is trying to mirror that data as much as possible.
 
    TCGA cases: TCGA-33-4579, TCGA-35-3621, TCGA-66-2746, TCGA-66-2747, TCGA-66-2750, TCGA-66-2751, TCGA-66-2752, TCGA-AN-A0FE, TCGA-AN-A0FG, TCGA-BH-A0B2, TCGA-BR-4186, TCGA-BR-4190, TCGA-BR-4194, TCGA-BR-4195, TCGA-BR-4196, TCGA-BR-4197, TCGA-BR-4199, TCGA-BR-4200, TCGA-BR-4205, TCGA-BR-4259, TCGA-BR-4260, TCGA-BR-4261, TCGA-BR-4263, TCGA-BR-4264, TCGA-BR-4265, TCGA-BR-4266, TCGA-BR-4270, TCGA-BR-4271, TCGA-BR-4272, TCGA-BR-4273, TCGA-BR-4274, TCGA-BR-4276, TCGA-BR-4277, TCGA-BR-4278, TCGA-BR-4281, TCGA-BR-4282, TCGA-BR-4283, TCGA-BR-4284, TCGA-BR-4285, TCGA-BR-4286, TCGA-BR-4288, TCGA-BR-4291, TCGA-BR-4298, TCGA-BR-4375, TCGA-BR-4376, TCGA-DM-A286, TCGA-E2-A1IP, TCGA-F4-6857, TCGA-GN-A261, TCGA-O2-A5IC, TCGA-PN-A8M9
 
    CCLE cases: LS123, LS1034
 
    NOTE 2: The number of cases and samples when viewed in the User Interface as compared to the BigQuery tables vary across all three projects (TCGA, TARGET, and CCLE).  This is because the user interface reflects the data available at the Genomic Data Commons, whereas data in BigQuery reflects either (for TCGA and CCLE) data at the original TCGA data coordinating center supplemented with Genomic Data Commons Data, or for TARGET, data received from the TARGET data coordinating center, not the Genomic Data Commons.
 
    NOTE 3: We have removed Google Genomics functionality from the user interface. You will still be able to access CCLE open access data in Google Genomics from the command line. We are open to adding Google Genomics controlled data back into the user interface if you have a use case for it.  Also we are restructuring the handling of multiple Programs of data. Please feel free to provide `feedback <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_. 
 
    NOTE 4: For TARGET data the clinical and Gene Expression files themselves are available in the system. The bam files will be available soon! 

    **Known Issues in this Data Structure Migration Sprint as of 05/25/2017**

    - Analysis Type : Seq peek Formatting Elongated on occasion 
    - The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
    - If the user shares a cohort neither the owner nor the person who was granted access to cohort will receive a confirmation email. 
    - Cannot plot any data if you use a CCLE data cohort on a worksheet.
    - When a user duplicates a worksheet, then tries to implement the log scale it will not function properly. 
    - On the existing cohorts table list page, the confirmation delete ‘blue x’ button does not remove selected cohort if you select another option e.g Set Operation. The same issue can be found in reverse if you select the ‘blue x’ on the confirmation page for  set operation you can then select the delete button and see the cohort on the confirmation panel. 
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
    - On the File List page you currently unable to access the bam files  for the IGV Browser associated to build hg38 when working with TCGA data.

    **Issues that are resolved in the data structure migration sprint as of 05/25/2017**
    
    New Enhancements

    - You will be returned a more detailed error message when uploading your own user data. 
    - The user interface now displays the same nomenclature as the Genomic Data Commons (GDC).

    Bug Fixes

    - The user data upload is enabled and users can now upload their own datasets and create cohorts using existing programs and newly uploaded data by the user.
    - You can now have multiple Google Cloud Projects associated to your account and use only one bucket and dataset on one project with no interference. 


*  **April 12, 2017**:
    Please Note: We are currently having issues viewing bam files using the IGV browser for TCGA and CCLE data. We are working to fix the issue and it should be resolved as soon as possible.

*  **February 26, 2017**: 
    
    NOTE 1: We have removed Google Genomics functionality from the user interface. You will still be able to access CCLE open access data in Google Genomics from the command line. We are open to adding Google Genomics controlled data back into the user interface if you have a use case for it.  Also we are restructuring the handling of multiple Programs of data. Please feel free to provide `feedback <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_. 

    NOTE 2: There will be a reduced number of releases and features over the next month (or so) while we do some rework required for enabling the distribution of additional data sets and types copied from the NCI-GDC.  The new data type is TARGET data, and different analyzed data types are based on the hg38 genome builds.  Stay tuned in likely the early part of 2017.
  
    NOTE 3: User data uploads are currently disabled. Any projects you have previously uploaded will continue to be available in your Saved Projects list, and you can continue to work with them, but new data cannot be added at this time.  We are working on bringing this function up again, please stay tuned.

    **Known issues in Sprint 15 as of 02/26/2017**
    
    - Analysis Type : Seq peek Formatting Elongated 
    - The CCLE data in GUI is not parallel to the CCLE data in BigQuery.
    - If the user shares a cohort neither the owner nor the person who was granted access to cohort will receive a confirmation email.
    - Cannot plot any data if you use a CCLE data cohort on a worksheet. 
    - When a user duplicates a worksheet, then tries to implement the log scale it will not function properly. 
    - On the existing cohorts table list page, the confirmation delete ‘blue x’ button does not remove selected cohort if you select another option e.g Set Operation. The same issue can be found in reverse if you select the ‘blue x’ on the confirmation page for  set operation you can then select the delete button and see the cohort on the confirmation panel. 
    - On the cohort view files page there are capitalization bugs on the Platform filter. 
    - Swap values is not working properly for the plot settings.  
    - The set operation for existing cohorts complement is behaving exceptionally slow. 
    - A duplication of the exact cohort happens when you select the confirmation multiple times while the page is loading working with Set Operations. 
    - When working with a new worksheet or a duplicate worksheet with workbooks for categorical features e.g bar chart you can select the log option. The log option only applies to numerical options. 
    - If multiple Google Cloud Projects are registered through the user interface, it is advised to to add Google buckets and BigQuery datasets to both projects currently. 
    - When working with workbooks, if you select the delete confirmation button multiple times while the page is loading you will be sent to an error page. 
    - When working on a scatter plot the Tobacco Smoking being used as the Legend is displayed in numerical values when it should be displayed as categorical values. 
    - The character limit for a workbook title name is currently inactive, if you exceed the possible limit you will be sent to an error page. 
    

    **Issues that are resolved in Sprint 15 as of 02/26/2017**
    
    Bug Fixes
    
    - User will no longer be sent to the Social Network Login page when trying to login. If this occurs, please feel free to send ISB-CGC feedback using this link `feedback <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_.

*  **November 30, 2016**: `v1.13 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.13>`_
    
    NOTE 1: We have removed Google Genomics functionality from the user interface. You will still be able to access CCLE open access data in Google Genomics from the command line. We are open to adding Google Genomics controlled data back into the user interface if you have a use case for it.  Also we are restructuring the handling of multiple Programs of data. Please feel free to provide `here <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_. 

    NOTE 2: There will be a reduced number of releases and features over the next month (or so) while we do some rework required for enabling the distribution of additional data sets and types copied from the NCI-GDC.  The new data type is TARGET data, and different analyzed data types are based on the hg38 genome builds.  Stay tuned in likely the early part of 2017.

    **Known issues in Sprint 14 as of 11/30/2016**
    
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

    **Issues that are resolved in Sprint 14 as of 11/30/2016**
    
    Bug Fixes
    
    - The user can no longer see BCGSC expression as an option when plotting genes if user does not select center filter on worksheet. 
    - Worksheets added to an existing workbook now behave the same as the original worksheet.
    - Cohort set operations no longer performing exceptionally slow.

    
    
*  **November 16, 2016**: `v1.12 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.12>`_

    Please Note: We are removing Google Genomics from the user interface. You will still be able to access CCLE open access data in Google Genomics from the command line. We are open to adding Google Genomics controlled data back into the user interface if you have a use case for it. Please feel free to provide `feedback <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_.
   
    **Known issues in Sprint 13 as of 11/16/2016**
    
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

    **Issues that are resolved in Sprint 13 as of 11/16/2016**
    
    New Enhancements
    
    - A warning will be displayed if the user is trying to plot with required data missing e.g. must select an analysis, gene or variable, and a cohort to create a plot. 
    - On the project details page user will be sent to upload new study in existing project tab when they select upload data. 
    - When the user plots a graph with NA values, you will be returned a notification stating no valid data was found. 
    - There is no longer text overlapping on the Cloud Hosted Datasets readthedocs page in the documentation. 
    
    
    Bug Fixes
    
    - The user can no longer add the same gene symbol twice if list to the same worksheet even if they have given their list different names. 
    - When the user selects multiple cohorts for color by feature for scatter plot all cohorts selected display on the graph. 
    - On the existing cohorts table for public cohorts, the new workbook and set operations buttons are now active. 
    - For all analysis types the x-axis and y-axis with certain variables text will no longer overlap and is displayed clearly. 
    - The upload data button is disabled on the review files page when no buckets or datasets are associated. 
    - Someone with multiple eRA accounts will be no longer have issues when trying to access controlled data. 

    

*  **November 2, 2016**: `v1.11 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.11>`_

    **Known issues in Sprint 12 as of 11/02/2016**

    - The user can add same gene twice if list to the same worksheet it they have different names. 
    - Analysis Type : Seq peek Formatting Elongated 
    - The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
    - If a user creates a cohort with sample type filter Cell Lines  and CCLE the total number of samples count off by one. 
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


    **Issues that are resolved in Sprint 12 as of 11/02/2016**

    New Enhancements

    - Introduce user data upload functionality  see documentation `here <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/program_data_upload.html>`_.
    - More fluid zoom feature when working with analysis worksheets. 
    - Case Sensitivity is now maintained in creating and displaying Workbook names throughout the entire User Interface. 
    - You can now create a new cohort from the menu bar. 
    - Variables menu bar is displayed similar to the rest of the favorites variables. 
    - On the dashboard, all create new buttons/links are identical. 
    - Owner of what is shared either a workbook or a cohort is able to remove multiple viewers. Viewers are also able to remove themselves. 
    - Removed BCGSC gene expression from the UI gene specification selection for plot analysis. 


    Bug Fixes

    - X or Y- Axis for text no longer overlaps on worksheet for any analysis type, except for violin plot.  
    - The Legend is no longer displayed elongated when you use multiple cohort for color by feature for violin plot. 
    - miRNA_expression_values_fixed table in dataset 2016_07_09_tcga_data_open reflect only hg19.mirbase20 files.  
    - You are now able to duplicate a workbook that has been shared with you by someone else. 
    - Added pseudo-counts to the mosaic plots on the create new cohort page. This allows you to be sure of always being able to see (and select) the smallest contributors in these mosaics. 
    - Removing the filter from the filter confirmation from the create new cohort page, this will remove it from the rest of filter selections. 
    - Select the “check-all” feature on the create new cohort page will no longer cause duplicates on the selected filters panel. 
    - Create cohort from plot selection now works with all analysis types. 
    - Data inconsistencies between the create new cohort histogram filter and the most recent BigQuery datasets has been addressed and resolved.



*  **September 21, 2016**: `v1.10 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.10>`_

    **Known issues in Sprint 11 as of 9/21/2016**
    
    - The user can add same gene twice if list to the same worksheet it they have different names. 
    - The Bar chart on the worksheet panel renders overlapping text. 
    - Analysis Type : Seq peek Formatting Elongated 
    - The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
    - If a user creates a cohort with sample type filter Cell Lines  and CCLE the total number of samples count off by one. 
    - User will occasionally be sent to the Social Network Login page when trying to login. If this occurs, please go the the home page of the Web Application and try again. 
    - If the user shares a cohort they do not receive a confirmation email.
    - The Legend is displayed elongated when you use multiple cohort for color by feature for violin plot.
    - When the user selects multiple cohorts for color by feature for scatter plot they do not display in chart. 
    - Cannot plot any data if you use CCLE data cohort on a worksheet. 
    - When the user plots a graph with NA values the UI returns a blank graph. 
    - When a user duplicates a worksheet, then tries to implement the log scale it will not function properly. 
    - There are duplicate rows in the molecular data table in BigQuery. 

    **Issues that are resolved in Sprint 11 as of 9/21/2016**

    New Enhancements
    
    - Text in confirmation box of a duplication of a workbook has been enhanced. 
    - On the registered Google Cloud Projects page, icon has been added for the user to go directly to the Google Cloud Console page if desired. 
    - When the a Service Account is removed from the Access Control List, the project owner is sent an email with an explanation as to why the account was removed. 
    - IGV File List page displays of which page user is browsing. 

    Bug Fixes

    - For a Cubby hole plot the x - axis name can be seen clearly. 
    - On a duplicate worksheet when working with gene specifications, user is able to select between all options multiple times. 
    - Page becomes elongated when the user builds a Cubby Hole plot. 
    - The selected variables for the plot setting on a worksheet are saved after the user leaves the workbook. 
    - When registering a Google Cloud Project the user is displayed the list of emails associated to the GCP only once. 


*  **September 7, 2016**: `v1.9 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.9>`_
    
    **Known issues in Sprint 10 as of 9/07/2016**

    - The user can add same gene twice if list to the same worksheet it they have different names.
    - The Bar chart on the worksheet panel renders overlapping text.
    - Analysis Type : Seq peek Formatting Elongated 
    - The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
    - If a user creates a cohort with sample type filter Cell Lines  and CCLE the total number of samples count off by one.
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

    **Issues that are resolved in Sprint 10 as of 9/07/2016**

    New Enhancements
    
    - Dictionary mapping feature types to units for use in plot displays added to worksheets. 
    - The user now has the option to make the axis logarithmic if the plot can display continuous numerical data for eg. mRNA expression levels. 
    - The NIH username entry is now case insensitive for dbGaP authorization.
    - The mouse over feature works when the user has created a long workbook name on the existing workbooks table page.
    - The mouse over functionality was added to the worksheet name within a workbook. 

    Bug Fixes
    
    - The order by ascending or descending feature is now working properly for the existing workbooks table page.
    - Tobacco Smoking History filter in the create cohort page displays the filters in descriptive values.
    - The user can now select all existing cohorts when on the add cohort(s) to worksheet page.
    - The gene specification selection on the worksheet page is now working properly.
    - When a user shares a workbook with someone the person who received viewer access to the workbook is sent a confirmation email. If the person who shared the workbook then deletes the workbook before it's opened, then the person clicks the invitation link the person is sent to  the unknown invitation page. The button to go back to the Dashboard page appears like this, "Your Dashboard"
    - The user is sent an email when the Service Account is removed the Access controlled list for having a user associated to the project who is not dbGaP authorized.


*  **August 24, 2016**: `v1.8 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.8>`_
    
    **Known issues in Sprint 9 as of 8/24/2016**
    
    - The user can add same gene twice if list to the same worksheet it they have different names. 
    - The Bar chart on the worksheet panel renders overlapping text. 
    - Analysis Type : Seq peek Formatting Elongated.
    - The CCLE data in GUI is not parallel to the CCLE data in BigQuery. 
    - If a user creates a cohort with sample type filter Cell Lines  and CCLE the total number of samples count off by one. 
    - User will occasionally be sent to the Social Network Login page when trying to login. If this occurs, please go the the home page of the Web Application and try again. 
    - Page becomes elongated when the user builds a Cubby Hole plot. 
    - X-axis name cut off for cubby hole plot  when x-axis has only 3 criteria. 
    - When the user shares a cohort they do not receive a confirmation email. 
    - User will be spammed with email every one minute when their service account is removed from the ACL control list.  To stop this, please either delete your service account from the ISB-CGC interface, or remove the GCP project member(s) who is (are) not authorized to access the controlled data set. (see documentation `here <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/Gaining-Access-To-Contolled-Access-Data.html>`_).  We are planning to reduce the frequency of the notification emails to once per day. 
    - The Legend is displayed elongated when you use multiple cohort for color by feature for violin plot. 
    - When the user selects multiple cohorts for color by feature for scatter plot they do not display in chart. 
    - When the user creates a duplicate worksheet,the bar chart with a gene with specification protein can freeze when selecting an option for the Select Feature. 
    - When a user shares a workbook with someone the person who received viewer access to the workbook is sent a confirmation email. If the person who shared the workbook then deletes the workbook before it's opened, then the person clicks the invitation link the person is sent to  the unknown invitation page. The button to go back to the Dashboard page appears like this, "Your Dashboard{" 
    - Cannot plot any data if you use CCLE data cohort on a worksheet. 

    
    **Issues that are resolved in Sprint 9 as of 8/24/2016**

    New Enhancements

    - When the researcher is on the Register Service Account page, after they have submitted the Service Account associated to their Google Cloud Project a table that shows who is authorized will be prompted.
    - There is now a column that says “Has NIH Identity”, before it said, “Has eRA Commons”. 
    - When the researcher creates a new cohort with more than 20 filters chosen the URL exceeds the limit of 2K characters and this affects the count for the Details panel. Therefore the user is now prompted with an alert box that will say, “You have selected too many filters. The current counts shown will not be accurate until one or more filter options are removed.” if this is ever the case. 
    - In the user details page, if the researcher has not registered a Google Cloud Project it will say, “Register a Google Cloud Project” on the link. 


    Bug Fixes

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


*  **August 10, 2016**: `v1.7 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.7>`_
    
    **New Functionality Released in this Sprint**
    
    - The researcher can now create a cohort of participants and samples based on the presence of a gene mutation in a specified gene. Look for the new “Molecular” tab when you are creating a cohort.
    - The bioinformatics programmer now has the ability to associate their Google Cloud Project’s Service Account. This allows the researcher to run computational pipelines from Google Virtual Machines using TCGA Controlled data (e.g. BAM files) for seven days before they have to reauthorize. For more information please select `here <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/Gaining-Access-To-Contolled-Access-Data.html>`_.
    
    
    **Known issues in Sprint 8**
    
    - The user can add same gene twice if list to the same worksheet it they have different names.
    - The Bar chart on the worksheet panel renders overlapping text. 
    - Cannot delete whom you share cohort with from existing cohorts table.  
    - Analysis Type : Seq peek Formatting Elongated
    - The CCLE data in GUI is not exactly coordinated the CCLE data in BigQuery. 
    - If a user creates a cohort with sample type filter Cell Lines  and CCLE the total number of samples count is off by one. 
    - After 24-hours of use, a dbGaP authorized user has to logout and then log back in to be prompted with NIH login link to re-access controlled data. 
    - User will occasionally be sent to the Social Network Login page when trying to login. If this occurs, please go the the home page of the Web Application and try again.
    - Page becomes elongated when the user builds a Cubby Hole plot. 
    - X-axis name cut off for Cubby Hole plot  when x-axis has only 3 criteria. 
    - When the user shares a cohort they do not receive a confirmation email. 
    - When a name is too long for variable favorites list table, the Last Updated” column will appear cut off. 
    - Filter name will appear off the verification panel when the filter is name too long for the create in cohort filter selection. 
    - Grouped Data Type filter counts (Methylation, RNA Seq, miRNA Seq) don't behave like other count groups. The counts behave as though the values were for distinct categories. 
    - User will be spammed with email every one minute when their service account is removed from the ACL control list.  To stop this, please either delete your service account from the ISB-CGC interface, or remove the GCP project member(s) who is (are) not authorized to access the controlled data set. (see documentation here).  We are planning to reduce the frequency of the notification emails to once per day.
    - The user can select a categorical variable for selection for Histogram plot, and will return a graph with no data. 
    - The Legend is displayed elongated when you use multiple cohort for color by feature for violin plot.
    - When the user selects multiple cohorts for color by feature for scatter plot they do not display in chart.
    - When the user creates a duplicate worksheet,the bar chart with a gene with specification protein can freeze when selecting an option for the Select Feature. 
    
    
    **Issues resolved in Sprint 8**
    
    
    New Enhancements
    
    - The user now has the option to select all or deselect all possible filters for any tab that has more than 10 possible options in the create new cohort page. 
    - The user can now set all existing tables by either ascending or descending order. 
    - The cohort_id has been added to the detail cohort page. This allows the user to reference a desired cohort with ease in the API endpoints. 
    - When creating a new cohort, the user is given the full description for sample type in the selected filters panel.
    
    
    Bug Fixes
    
    - Histological Type entries in create new cohort page on the user interface now match the Google BigQuery entries in terms of capitalization. 
    - Filters for data type counts in left panel currently is now working properly. 
    - When a user sets a cohort as Color by feature for violin plot legend will be set to cohort. Then when the user sets another color by feature it will update the legend.
    - The user can no longer make a gene list without selecting a gene first. 
    - The user can now list the Last Modified section for the existing cohort table by either ascending or descending order.
    - In the create new cohort page for the data type tab, the user can now select either True or False for DNA Sequencing, Protein, and SNP Copy Number filters. 
    - When the user edits a new cohort and sets the edited cohort to return zero samples, the user will be prompted to select different set of filters.


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

    **Issues resolved in Sprint 7**

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

