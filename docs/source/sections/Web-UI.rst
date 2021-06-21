*******************************
ISB-CGC Web Interface (Web App)
*******************************

The `ISB-CGC Web Interface (Web App) <https://isb-cgc.appspot.com/>`_ provides robust functionality for the user to analyze the ISB-CGC cancer data through a user interface. Without needing to use any programming, you can select and filter data from one or more public data sets (such as TCGA, CCLE, TARGET and BEATAML1.0), combine with your own uploaded data and analyze using a variety of built-in plot types. There is also a built-in Integrative Genomics Viewer (IGV) and Radiology Viewer.

Over time we will be updating and enhancing this web interface based on your feedback.  We welcome your ideas and needs.  Please use this `link <https://groups.google.com/a/isb-cgc.org/forum/#!newtopic/feedback>`_ to provide them.

.. toctree::
   :hidden:
   :maxdepth: 1

   webapp/Overview
   webapp/Menu
   webapp/Dashboard
   webapp/Workbooks
   webapp/program_data_upload
   webapp/WebAppAnalyses
   webapp/Gene-and-miRNA-Favorites
   webapp/Variable-Favorites
   webapp/Saved-Cohorts
   webapp/GraphingUserData
   webapp/IGV-Browser
   webapp/OsimisWebViewer

**Data used by the Web App**


The Web App performs its data retrieval and counts on ISB-CGC Google BigQuery tables which are based on the latest GDC data release. This means that you will see current data, but that the same queries in the Web App could produce different results if they were run during different time periods, when the Web App was based on different GDC data releases.


**Sharing Cohorts between the Web App and the API**

Cohorts are one of the central concepts used when analyzing large datasets. Cohorts can be created either in the Web App or via the ISB-CGC REST API. What may not be as clear is that cohorts created by one of the systems can be viewed and used in the other. In other words, you can create a cohort using the API and use it in the Web App or you can create a cohort in the Web App and use it in the API. This can give users significant flexibility in creating and sharing their cohorts.

**Choosing a Web Browser**

The Web App was optimized for use with the Google Chrome web browser.  Most of the functionality should work with recent versions 
of other web browsers (e.g. Firefox, Safari, Internet Explorer).  If you find an issue and you are not using Chrome, please
try using Chrome to see if the issue appears to be browser specific.

**Web App Time Zone**

Also please note the system is set in Pacific time, so if you see some inconsistencies with the time in the workbooks or cohorts you generated, it could be due to this. 

