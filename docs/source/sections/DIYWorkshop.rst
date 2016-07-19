************
DIY Workshop
************

These materials were originally created for the workshops given at NCI on May 24th and 25th. 
They have been modified and updated to create a "Do It Yourself" workshop that you should be
able to work through on your own.  If you run into problems please send email to feedback@isb-cgc.org.

Step #1: Setting up Your Local Environment
##########################################

Your Google Identity
--------------------

You may already have a Google identity -- your institutional email may be a Google identity (if your
institution uses Google Apps), or you may have a personal GMail address.  One way to check whether 
your email address is a Google-managed identity is to go to the `password assistance page <https://www.google.com/accounts/ForgotPasswd>`_,
select *"I don't know my password"* and enter your email address.  If you get a response like *"Please contact your domain IT administrator"*
then your email address is *not* a Google identity.

If you dont' have a Google identity, it only takes a minute to
`create one <https://accounts.google.com/SignUp?dsh=308321458437252901&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount#FirstName=&LastName=>`_.

Installing the Google Cloud SDK
-------------------------------

The `Google Cloud SDK <https://cloud.google.com/sdk/>`_ is an essential toolbox 
for anyone working with the Google Cloud Platform.  The Cloud SDK is easy to install and
runs on Linux, Mac OS X, and Windows.
It includes all of the command line tools, local emulators, and libraries that you will need.
There are three key command line interfaces (CLIs) that you'll want to become comfortable using:

* `gcloud <https://cloud.google.com/sdk/gcloud/>`_ enables seamless local authentication and powerful command line access to many cloud resources
* `gsutil <https://cloud.google.com/storage/docs/gsutil>`_ lets you access Google Cloud Storage (GCS) from the command line
* `bq <https://cloud.google.com/bigquery/bq-command-line-tool>`_ provides access to BigQuery from the command line

Once you have the gcloud SDK installed, you can find out what your current/default Project ID is by 
running ``gcloud config list`` from the command line.  To initialize your default configuration, run 
``gcloud init <https://cloud.google.com/sdk/gcloud/reference/init>_`` and follow the instructions.

Updates to the SDK are published every week or two, so you will frequently see a message that says:

``Updates are available for some Cloud SDK components.  To install them, please run: $ gcloud components update``.

When you see this message, simply run ``gcloud components update`` at your convenience, and follow the
instructions.

Installing Chrome
-----------------

If you do not already use the Chrome browser, we strongly suggest that you install 
`Google Chrome <https://www.google.com/chrome/browser/desktop/>`_ on your laptop or desktop.
Although the ISB-CGC web-app should work on any modern browser, it is optimized for the Chrome browser.

Installing R and RStudio
------------------------

If you want to be able to run R scripts locally, you will want to install 
`R <https://cran.r-project.org/>`_ as well as the interactive environment 
`RStudio <https://www.rstudio.com/products/rstudio/download/>`_.
You can follow `these tips <GettingStartedWithR.html>`_ to get started.

Step #2: Setting up Your Google Cloud Platform (GCP) Project
############################################################

Creating / Obtaining your GCP Project
-------------------------------------

In order to make use of all of the data, tools, and functionality described in this workshop, 
you will also need your own GCP project.

We'd like to encourage you to take advantage of the 
`60-day free trial <https://cloud.google.com/free-trial/>`_ offered by Google.
If you have already used this one-time offer (or there is some other reason you cannot use it)
please see the information `here <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/Support.html>`_
about requesting an ISB-CGC provided (and funded) project.  (We'll also be happy to do that for
you *after* you use the $300/60-day free trial.)

Google Cloud Platform Console
-----------------------------

The Google Cloud Platform Console (which we will refer to from now on simply as the **Console**) is your
web-based interface to your GCP Project.  From the Console, you can check the overall status of your
project, create and delete Cloud Storage buckets, upload and download files, spin up and shut down VMs,
add members to your project, *etc*.  No setup or installation are required.

* sign into your Chrome (or other) browser using your Google identity (the one associated with the GCP project that you created yourself or that we set up for you)

* go to the Google Cloud Platform `Console <https://console.cloud.google.com>`_

  + you should automatically be signed in to your own GCP project;
  + in the top blue bar, towards the right, you may be able to select between two or more projects;
  + in the GCP Console, if you click on **Home** you will see your current Project ID on the Dashboard
  + this `Quick Tour of the Google Cloud Console <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Console.pdf>`_ will help you learn the basics that you are most likely to need

**NOTE**:  If you're just getting started working in the Google Cloud, you will probably only have one project.  
Over time, however, you may find that it is useful to create additional projects for any of a variety of reasons.
You may have different grants or contracts that need to be charged for specific research activities, or you may
have different groups of collaborators that you are working with, or you may be working with different sets of
controlled-access data.  All of these are good reasons to set up multiple, separate, GCP projects.  When you do
so, however, you will need to learn to pay attention to which project is your *"current"* project.  Any costs
that you may incur, will alwasy be charged to your *current* project.  The types of actions that incur costs
include uploading data to a storage bucket, spinning up a VM, running a BigQuery query, *etc*.  

* If you are using the Console, you will see the Project Name in the blue bar at the top of the page, and the browser url should look like: ``https://console.cloud.google.com/home/dashboard?project=<project-id>``.  
* At the command-line, you can use the ``gcloud`` tool to verify your current configuration (as described above).
* Finally, if you are using the BigQuery Web UI, the url should look like this: 

  + ``https://bigquery.cloud.google.com/project/<project-id>`` or 
  + ``https://bigquery.cloud.google.com/queries/<project-id>``.

Enabling ComputeEngine and Genomics APIs
----------------------------------------

You will need to enable the ComputeEngine and Genomics APIs as described in this `tutorial <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/enabling_new_APIs.pdf>`_ 

Additional Quickstart Tutorials
-------------------------------

* `An Introduction to BigQuery <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_BigQuery.pdf>`_
* `An Introduction to Cloud Datalab <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Cloud_Datalab.pdf>`_
* `An Introduction to Cloud Shell <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Cloud_Shell.pdf>`_

ISB-CGC Workshop Outline & Links
################################

* `Introduction to the ISB-CGC Platform <https://github.com/isb-cgc/readthedocs/raw/master/docs/include/workshop-intro.pdf>`_

* Integrative Analysis Tutorial

  + `Web-App Tutorial <workshop/WebApp_tut.html>`_
  + `BigQuery SQL Tutorial <workshop/BQ_SQL_tut.html>`_
  + `Analysis using R and RStudio <workshop/Workshop_R_tut.html>`_

* `Compute Pipelines Tutorial <https://docs.google.com/presentation/d/1IQkwbePfzj5qoCzqX-EV_UTbse075chzDINm5ZXGB5I/edit?usp=sharing>`_

