#############################
ISB-CGC WebApp Release Notes
#############################

Introduction text


**April 25, 2019**

**Please Note:** Work is underway to rework our cohort creation page to better display images associated with samples. 
  
The following datasets (open and controlled access) have been added to the ISB-CGC for service account registration:
  
 1. The National Cancer Institute Center for Cancer Research (NCICCR)  
 2. Foundation Medicine(FM)
 3. Clinical Trial Sequencing Project (CTSP)
 4. Veterans Research for Precision Oncology Program (VAREPOP) 
   

**Enhancements** 

- When working with Oncogrid, OncoPrint, or a SeqPeek plot on a workbook you will receive an automatic list of genes ready for analysis.
- When on a workbook additional text has been added to guide the user to select edit plot settings to select a gene/miRNA/variable filter and cohort to used in analysis selected.
- The Workbook comments section has been reformatted to better align with analysis displayed.
- On the cohort creation - filter page the filters have been updated in the left filter panel to specify the count type displayed (samples).

**Bug Fixes**

- Clicking on a legend entry to toggle display of the data points on a scatter or violin plot will now work correctly, even if the legend text has a space.
- Plotting with sample type filter on a workbook will now display counts correctly.
- When working with the color by feature on either a Scatter plot or a Violin plot, the numerical values are now displayed as a color-gradient legend.
- When using a workbook with OncoGrid analysis you are now able to plot using genomic build hg19.
- When using a workbook with a Cubby Hole plot analysis text is no longer cut off when using sample type or residual tumor as a filter.

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


**March 8, 2019**

**Please Note:** Work is underway to rework our cohort creation page to better display images associated with samples. 
  
The following datasets (open and controlled access) have been added to the ISB-CGC for service account registration:
  
 1. The National Cancer Institute Center for Cancer Research (NCICCR)  
 2. Foundation Medicine(FM)
 3. Clinical Trial Sequencing Project (CTSP)
 4. Veterans Research for Precision Oncology Program (VAREPOP) 

Is there a dataset that is a priority for you? Of this list which should we include first? If yes, please send all requests to feedback@isb-cgc.org

**Enhancements**

- When working with a workbook many overall enhancements of user functionality have been improved. 
- Cubby hole plot analysis has been reformatted to better suit the end user by now allowing resizing and scrolling through the cubby hole plot analysis.
- You are now able to work on a workbook via fullscreen for added comfort. 
- You are also now able to download plot data for Bar charts, Histogram charts, Scatter plots, Violin plot charts, and Cubby hole plots  as a CSV file.
- `OncoGrid <https://github.com/oncojs/oncogrid>`_ has been added as an analysis option when working with a workbook. 
- On the File Browser section you are now able to use full screen on all image viewers. 
-  On the register/adjust a service account page, we’ve clarified the notification message if a key or role is found associated to a service account.  

**Bug Fixes**

- When using a workbook you will no longer see text overlap when working on a violin/scatter plot with the color by feature sample type as filter option.
- When working on the Pathology images viewer you will no longer see text overlap on the top right hand side of viewer.

**Known Issues**

- Analysis Type: Seq peek Formatting is Elongated on occasion 
- If the user shares a Cohort, neither the owner nor the person who was granted access to Cohort will receive a confirmation email when sharing a Cohort. 
- CCLE data cannot be plotted when working with workbooks.  ISB-CGC will resolve this functionality after the GDC formally releases CCLE data. 
- When a user duplicates a Worksheet, then tries to implement the log scale, it will not function properly. 
- The set operation for existing Cohorts complement is behaving exceptionally slow.
- The mouse-over feature is currently disabled for program TARGET with disease code ALL.
- When uploading TARGET files using the cohort barcode creation feature from the GDC, you may get an invalid barcodes error message and unable to upload all the barcodes.
- On the File Browser page for Diagnostic images there is no GDC file UUID associated to them.
- Sharing a workbook with someone else will cause the analysis to reset.



