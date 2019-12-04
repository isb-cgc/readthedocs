###################
Release Notes
###################

text test

===================
April 2016
===================

What's New
===========

**April 28, 2016**

GO_Ontology and GO_Annotations tables added to the isb-cgc:genome_reference BigQuery dataset

Integrations
=============

**April 27, 2019**

version `v1.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.2>`_
 
- The comments section now has a max number of characters 1000 limit
- Link created to Extend controlled access period to 24-hours from the moment the link is clicked
- A user can now click new worksheet multiple times within a few seconds and only produce one sheet
- The user must now add a new filter in an existing cohort to edit it the cohort
- The duplicate button for an existing cohort will only make one duplicate at a time
- Clicking 150+ selected filters will not create an error page
- Cancel button on Create new gene list page will send you to Gene list favorites table menu
- Violin plot : User can not add categorial value to y-axis
- If user edits an existing cohort, the old filter(s) will not be removed
- If a new worksheet is generated, the worksheet functionality is working properly
- User will get the ‘500: There was an error while handling your request. If you are trying to access a cohort please log out - and log back in. Sorry for the inconvenience.’ if the user is inactive for more in 15 minutes when trying to create/use existing cohort
- Clinical Feature Panel is displayed properly and reacts to filters being added/removed quickly
- The user must have text to add a comment
- All columns in file list table will be transferred/displayed when exported as csv file


**April 14, 2016**

version `v1.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.1>`_

- Tool tips added for disease code in create new cohort page
- Disease in longname in tool tips the first letter is capitalized
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
- Update plot button will now work on a duplicate worksheet(can be added with three)
- User can now delete all cohorts with the select all feature
- Fixed bugs with Data Type Create new cohort generating errors
- The user can now search for variable favorite with the miRNA feature
- The user can now search for a variable favorite through the clinical search feature

Known Issues and Workarounds
=============================

**April 27, 2019**

 version `v1.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.2>`_
 
- Can add same gene twice if list has different names
- User can add same filter to existing cohorts
- Create new Cohort left filters (#) does not re-populate as you select filters to match sample # in clinical feature panel
- Clinical Features Panel in create new cohort page will still display BRCA even if unselected
- Last updated section in existing workbooks panel does not update when changes are made to existing workbook
- Bar chart renders overlapping text
- Set operation Union patient # off by one
- Legend Name cut off when name is too long
- Upon duplicating a cohort it duplicates the selected filter as well
- Cannot delete whom you share cohort with from existing cohorts table
- Unable to down file list as csv for any other cohort only selected filter CCLE
- Legend Cut Off for violin plot when color by feature set to Prior Diagnosis
- When user switches gene in plot settings the feature choices for that specification disappears
 

**April 14, 2016**

version `v1.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.1>`_

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

===================
March 2016
===================

What's New
===========

**March 14, 2016**

With the release of our Web-App, controlled-data is now accessible (programmatically) to users who have previously obtained dbGaP approval for TCGA data and go through the NIH authentication process built-in to the Web-App

Known Issues and Workarounds
=============================

**March 14, 2016**

version `v1.0 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/2.0>`_

- When working with a worksheet two plots will be generated occasionally
- Axis labels and tick values sometimes overlap and get cutoff
- Page elongated when Cubby Hole plot generated and there are lots of values in the y axis

===================
February 2016
===================

What's New
===========

**February 26, 2016**

New CCLE dataset in BigQuery isb-cgc:ccle_201602_alpha includes sample metadata, mutation calls, copy-number segments, and expression data (metadata includes full cloud-storage-path for world-readable BAM and SNP CEL files, and Genomics dataset- and readgroupset-ids for sequence data imported into Google Genomics)

**February 22, 2016**

Kaviar database now available in the isb-cgc:genome_reference BigQuery dataset

**February 19, 2016**

CCLE RNAseq and DNAseq bam files imported into Google Genomics

===================
January 2016
===================

What's New
===========

**January 10, 2016**

GENCODE_r19 and miRBase_v20 tables added to the isb-cgc:genome_reference BigQuery dataset

===================
December 2015
===================

What's New
===========

**December 26, 2015**

Public release of new isb-cgc:genome_reference BigQuery dataset: the first table is based on the just-published miRTarBase release 6.1

**December, 12, 2015**

Curated TCGA cohort lists available in isb-cgc:tcga_cohorts BigQuery dataset

**December 3, 2015**

version `v0.1 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.0>`_

First tagged release of the web-app 

Known Issues and Workarounds
=============================


**December 23, 2015**

version `v0.2 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/1.1>`_

Treemap graphs in cohort details and cohort creation pages will not apply its own filters to itself. For example, if you select a study, the study treemap graph will not update 

Cohort file list download not working

===================
November 2015
===================

What's New
===========

**November 16, 2015**

Initial upload of data from CGHub into Google Cloud Storage (GCS) complete (not publicly released)

**November 2, 2015**

First public release of TCGA open-access data in BigQuery tables

- isb-cgc:tcga_201510_alpha dataset contains updated set of BigQuery tables, based on data available at the TCGA DCC as of October 2015
- includes Annotations table with information about redacted samples, etc
- isb-cgc:platform_reference contains annotation information for the Illumina DNA Methylation platform

===================
October 2015 
===================

What's New
===========

**October 4, 2015**

Complete data upload from TCGA DCC, including controlled-access data

===================
September 2015 
===================

What's New
===========

**September 21, 2015** 

Draft set of BigQuery tables (not publicly released)

- isb-cgc:tcga_201507_alpha dataset containing clinical, biospecimen, somatic mutation calls and Level-3 TCGA data available at the TCGA DCC as of July 2015

