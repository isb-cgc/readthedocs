********************************
Frequently Asked Questions (FAQ)
********************************

ISB-CGC Accounts and Cloud Projects
###################################

I want to be able to run big jobs using Google Compute Engine on the TCGA data hosted by the ISB-CGC.  What should I do?
-------------------------------------------------------------------------------------------------------------------------

You will need to request a Google Cloud Platform (GCP) project. 

Can I use any email address as a Google identity?
-----------------------------------------------------

Yes, you can.  If your email address is not already linked to a Google account, you can create_ a Google account with your current email address.
Please note, however that although these two accounts will then share the same *name*, they will still be two separate accounts, with two separate passwords, *etc*.  (It is also possible that your institutional email address is *already* a Google account, if your institution uses Google Apps. `This <https://support.google.com/accounts/answer/40560?hl=en&ref_topic=3382296>`_ is how to find out).

.. _create: https://accounts.google.com/signupwithoutgmail

How do I connect my Google Cloud Project to the ISB-CGC?
---------------------------------------------------------

Your Google Cloud Project gives you access to all of the technologies that make
up the Google Cloud Platform.  These technologies include BigQuery, Cloud Storage, Compute Engine, etc.  The ISB-CGC makes use of a variety of these technologies to provide access to the TCGA data, as well as many other data sets. Please see the `Google Cloud Project Setup and Data Access <HowToGetStarted-Analysis.html#google-cloud-project-setup-and-data-access>`_ section on the Getting Started with Analysis page.

The connection between your Google Cloud Project (whether it is an ISB-CGC sponsored and funded project
or your own personal project) and the ISB-CGC is your Google identity 
(also referred to as your "user credentials").  

Access to all ISB-CGC hosted data is controlled using the `Data Commons Framework Gen3 <https://dcf.gen3.org/>`_ which defines the
permissions attached to each data set, bucket, or object.

Data Access
###########

Does all TCGA data require dbGaP authorization prior to access?
----------------------------------------------------------------
No, generally only the low-level sequence (DNA and RNA) and SNP-array data (CEL files) require
dbGaP authorization.  All of the "high-level" molecular data, as well as the clinical data are
open-access and much of this has been made available in a convenient set of BigQuery tables. Note that as of August 2024, only open access data is available through ISB-CGC.

Where can I find the TCGA data that ISB-CGC has made publicly available in BigQuery tables?
----------------------------------------------------------------------------------------------

The BigQuery web interface can be accessed at https://console.cloud.google.com/bigquery.  If you have not already added the ISB-CGC data sets to your BigQuery "view", click on the blue arrow
next to your project name at the top of the left side-bar, select "Switch to Project", then "Display Project...",
and enter "isb-cgc-bq" (without quotes) in the text box labeled "Project ID". For older ISB-CGC data sets, repeat and enter "isb-cgc". All ISB-CGC public BigQuery
data sets and tables will now be visible in the left side-bar of the BigQuery web interface. 
*Note that in order to use BigQuery, you need to be a member of a Google Cloud Project.*

Python Users
############ 

I want to write Python scripts that access the TCGA data hosted by the ISB-CGC.  Do you have some examples that can get me started?
-------------------------------------------------------------------------------------------------------------------------------------

Yes, of course!  The best place to start is with our `Community Notebooks <HowTos.html>`_  or our repository in `GitHub <https://github.com/isb-cgc/Community-Notebooks>`_. You can run any of these examples yourself. It includes an introduction explaining what Notebooks are, how to get started as a novice user, and how to run more advanced analyses once you are comfortable. 

R Users
########

I want to use R and Bioconductor packages to work with the TCGA data.  How can I do that?
---------------------------------------------------------------------------------------------

You can run RStudio locally or deploy a dockerized version on a Google Compute Engine VM.  You can
find some great examples to get you started in our  `Community Notebooks <HowTos.html>`_  or our repository in `Community Notebooks GitHub <https://github.com/isb-cgc/Community-Notebooks>`_.

For an example on how to use Bioconductor packages with TCGA data in BigQuery, please check out our interactive tutorial found `here <https://isb-cgc.appspot.com/how_to_discover/#0>`_.

Regulome Explorer Users
###########################

Can I run Regulome Explorer Analyses using TCGA tables of heterogeneous data in BigQuery?
------------------------------------------------------------------------------------------

Yes, of course! A series of Python Notebooks have been created to replicate Regulome Explorer and includes detailed information on the statistical methods implemented. To get started, please visit our `Regulome Explorer <RegulomeExplorerNotebooks.html>`_ page in readthedocs or our Repository in `Regulome Explorer GitHub <https://github.com/isb-cgc/Community-Notebooks/tree/master/RegulomeExplorer>`_. 


