********************************
Frequently Asked Questions (FAQ)
********************************

ISB-CGC Accounts and Cloud Projects
###################################
**Do I have to request an ISB-CGC account before I can try out the web interface?**
No, you can just "sign in" to the web-app using your Google identity.  

**I want to be able to run big jobs using Google Compute Engine on the TCGA data hosted by the ISB-CGC.  What should I do?**
You will need to request a Google Cloud Platform (GCP) project.  Please see :ref:`request-gcp` for more details
about requesting a project.

**Can I use any email address as a Google identity?**  Yes, you can.  If your email address is not
already linked to a Google account, you can create_ a Google account with your current email address.
Please note, however that although these two accounts will then share the same *name*, they will
still be two separate accounts, with two separate passwords, *etc*.  (It is also possible 
that your institutional email address is *already* a Google account, if your institution uses
Google Apps.
`This <https://support.google.com/accounts/answer/40560?hl=en&ref_topic=3382296>`_ is how to find out).

.. _create: https://accounts.google.com/signupwithoutgmail

**How do I connect my GCP project to the ISB-CGC?**
Your GCP project gives you access to all of the technologies that make
up the Google Cloud Platform (GCP).  These technologies include BigQuery, Cloud Storage, Compute Engine,
Google Genomics, etc.  The ISB-CGC makes use of a variety of these technologies to provide access
to the TCGA data, *without* necessarily inserting an extra interface layer between you and the GCP.  Although one
component of the ISB-CGC is a web-app (running on Google App Engine), some users may prefer not to go through
the web-app to access other components of the ISB-CGC.  For example, the open-access TCGA data
that we have loaded into BigQuery tables can be accessed directly via the 
`BigQuery web interface <https://www.bigquery.cloud.google.com>`_ or from Python or R.  Similarly,
the ISB-CGC programmatic API is a REST service that can be used from many different
programming languages.

The connection between your GCP project (whether it is an ISB-CGC sponsored and funded project
or your own personal project) and the ISB-CGC is your Google identity 
(also referred to as your "user credentials").  
Access to all ISB-CGC hosted data is controlled using access control lists (ACLs) which define the
permissions attached to each dataset, bucket, or object.

**Why do I add the service account 907668440978-oskt05du3ao083cke14641u35deokgjj@developer.gserviceaccount.com to my Google Cloud Project?**

This service account is needed  in your Google Cloud Project for the ISB-CGC project to be able to automatically verify that all users of your Google Cloud Project have the same appropriate access rights to the protected data that has been reuested for the project.

**What service account do I use on the Register a Service Account page to be able to gain access to protected data?**

On the Register a Service account page you are asked to input a service account ID.  You need to go to the IAM and Admin page which can be found in your console for you Google Cloud Project to find the correct service account.  The service account you would like to use is named, "Compute Engine default service account".  Please input that service account in the Register a service account page. *Please DO NOT use the service account 907668440978-oskt05du3ao083cke14641u35deokgjj@developer.gserviceaccount.com (you will be prevented from using this account by our software and an error message will be sent indicating this).* 

**Why can't I re-authorized my Service Account on my Google Cloud Project?**

Your service account may have had its permissions revoked (because, for example, the 7-day limit has expired, or you have added a member to the GCP who is not authorized to use that controlled data or has not logged into the ISB-CGC UI and authenticated using their dbGaP
credentials). If permissions were revoked because an unauthorized user was added to the project, the Google Cloud Project owner will be sent
an email specifying the Service Account, GCP Project, and user which resulted in the access being revoked. If the user has not logged into the ISB-CGC interface and or has not authenticated, you will be given a red error message saying, "There was an error in processing your service account. Please try again." when attempting to refresh using the refresh wheel.  To see which new user hasn't logged in or authenticated, please go to the Register a Service Account page and see which user it is within the table for which the dataset is not selected and there are X's in the Registered and Has NIH Identity.

.. image:: authorizedtable.PNG
   :scale: 50
   :align: center

Ensure that the user has 1)Logged into the ISB-CGC user interface and 2) Has registered their NIH Identity with their user interface identity.

To reauthorize the service account 1) remedy the problem that resulted in access being denied, and 2) select the "refresh" icon beside the
service account.

Data Access
###########
**Does all TCGA data require dbGaP authorization prior to access?**
No, generally only the low-level sequence (DNA and RNA) and SNP-array data (CEL files) require
dbGaP authorization.  All of the "high-level" molecular data, as well as the clinical data are
open-access and much of this has been made available in a convenient set of BigQuery tables. 

**Where can I find the TCGA data that ISB-CGC has made publicly available in BigQuery tables?**
The BigQuery web interface can be accessed at bigquery.cloud.google.com.  If you have not already added the ISB-CGC datasets to your BigQuery "view", click on the blue arrow
next to your project name at the top of the left side-bar, select "Switch to Project", then "Display Project...",
and enter "isb-cgc" (without quotes) in the text box labeled "Project ID".  All ISB-CGC public BigQuery
datasets and tables will now be visible in the left side-bar of the BigQuery web interface.
Note that in order to use BigQuery, you need to be a member of a Google Cloud Project.

**How can I apply for access to the low-level DNA and RNA sequence data?**
In order to access the TCGA controlled-access data, you will need to apply to dbGaP_.
Please also review our section on **Understanding Data Security**.

.. _dbGaP: https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?login=&page=login

**I have dbGaP authorization.  How do I provide this information to the ISB-CGC platform?**
In order for us to verify your dbGaP authorization, you first need to associate your Google identity
(used to sign-in to the web-app) with a valid NIH login (*eg* your eRA Commons id).  After you have
signed in, click on your avatar (next to your name in the upper-right corner) 
and you will be taken to your account details page where you can 
verify your dbGaP authorization.  You will be redirected to the NIH iTrust login page and after you
successfully authenticate you will be brought back to the ISB-CGC web-app.  After you successfully
authenticate, we will verify that you also have dbGaP authorization for the TCGA controlled-access data. 
We also ask that you review our section on **Understanding Data Security**.

**My professor has dbGaP authorization.  Do I have to have my own authorization too?**
Yes, your professor will need to add you as a "data downloader" to his/her dbGaP application so that you
have your own dbGaP authorization associated with your own eRA Commons id.  
(This `video <https://www.youtube.com/watch?v=Yem3OH26kX4>`_ explains how an authorized user of 
controlled-access data can assign a downloader role to someone in his/her institution.)

**I already authenticated using my eRA Commons id but now I want to use a different Google identity to
access the ISB-CGC web-app.  Can I re-authenticate using the same eRA Commons id?**
Yes, but you will first need to sign-in using your previous Google identity and "unlink" your eRA Commons
id from that one before you can link it with your new Google identity.  An eRA Commons id cannot be
associated with more than one Google identity within the ISB-CGC platform at any one time.

**Can I authenticate to NIH programmatically?**  No, the current NIH authentication flow requires
web-based authentication and must therefore be done from within the ISB-CGC web-app.  Once you have
authenticated to NIH via the web-app, and your dbGaP authorization has been verified, the Google 
identity associated with your account will have access to the controlled-data for 24 hours.

Data Content
############
**I get a different number of samples in BigQuery than I do with the same query in the Webapp.  Why?**  Older programs like TCGA have both legacy data (data from the original program) and harmonized data (data run through the Genomics Data Commons).  The Webapp primarily uses harmonized data where BigQuery contains both legacy and harmonized data.  In addition, some cases and samples have been removed from the Webapp if annotation suggest the data from those caases or samples are incorrect, misleading or from cases of uncertain origin.  Most of these cases and samples are still in BigQuery and users are encouraged to check the annotations tables.

Python Users
############
**I want to write python scripts that access the TCGA data hosted by the ISB-CGC.  Do you have some 
examples that can get me started?**  Yes, of course!  The best place to start is with our examples-Python_
repository on github.  You can run any of those examples yourself by signing in 
to your Google Cloud Project and deploying an instance of Google Cloud Datalab_.

.. _examples-Python: https://github.com/isb-cgc/examples-Python
.. _Datalab: https://datalab.cloud.google.com/

R and Bioconductor Users
########################
**I want to use R and Bioconductor packages to work with the TCGA data.  How can I do that?**
You can run RStudio locally or deploy a dockerized version on a Google Compute Engine VM.  You can
find some great examples to get you started in our examples-R_ repository on github, and also in
the documentation from the Google Genomics workshop_ at BioConductor 2015.

.. _examples-R: https://github.com/isb-cgc/examples-R
.. _workshop: http://googlegenomics.readthedocs.org/en/latest/workshops/bioc-2015.html

