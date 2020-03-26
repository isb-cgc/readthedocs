
**************************
Moving from GDC to ISB-CGC
**************************

If you've been using the National Cancer Institute's `Genomic Data Commons Portal 
<https://portal.gdc.cancer.gov/>`_ you've probably discovered that while you can identify patients and files that might be interesting, you need to download files to your own system in order to do perform unique analysis.

Fortunately, since the ISB-CGC stores data from the GDC, you can do your analysis on the cloud without having to move data. The only thing you need from GDC is a case manifest or a file manifest and in the following tutorials, we'll show you how to turn those manifests into usable analysis starting points.

Differences between GDC and ISB-CGC
====================================

Since the GDC is mostly aimed at storing data and the ISB-CGC is aimed at making use of that data there are some differences between the two that you need to understand before starting:

* While the ISB-CGC does have all the *data* from the GDC, it doesn't have all the *files* from the GDC.  This is because we've stored the analyzed data ("Level 3") in BigQuery tables rather than as files.  In fact, the only files stored at ISB-CGC are the raw, "Level 1" files.  So unless you plan on re-analyzing data from scratch, you can dive straight into BigQuery.
* GDC file manifests can be directly imported into BigQuery for use in ISB-CGC.
* GDC case manifests aren't directly importable into ISB-CGC. A bit of manipulation needs to happen to make them useful in ISB-CGC.
  
Output from  GDC
=================

For the purpose of bringing GDC information into ISB-CGC, GDC has two different outputs to consider once users have finished doing their selections, the file manifest and the case table export.  In the example shown below, various filters were set to produce a cohort of 83 cases from the three TCGA kidney cancers and that cohort has 1,790 files on hand at the GDC.  To download a File Manifest, which we'll use later to find the files in ISB-CGC, you need to click on the *View Files in Repository* button:

.. image:: GDCSetCreation4.png

  
  
Once on the file page, a file manifest can be downloaded simply by clicking on the *Download Manifest* button.  A list of Cases can be created by clicking on the *Cases* tab and then clicking on either the *JSON* or *TSV* button on the uppper right of the table (This can also be done from the previous screen).  Later in this tutorial, we'll use the JSON file to bring the cases into Big Query:

.. image:: FileManifestButton4.png
  
Links to other GDC tutorial pages:
++++++++++++++++++++++++++++++++++ 

.. toctree::
   :maxdepth: 1
   
   ImportGDCFileManifest
   ImportGDCCaseDownload
   ISB-CGC_Cohort_from_GDC_Cases
