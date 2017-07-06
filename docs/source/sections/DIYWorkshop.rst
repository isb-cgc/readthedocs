************
DIY Workshop
************

These materials were originally created for in-person workshops, and have been modified and
updated to create a "Do It Yourself" workshop that you should be
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
`free trial <https://cloud.google.com/free/>`_ offered by Google.
If you have already used this one-time offer (or there is some other reason you cannot use it)
please see the information `here <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/Support.html>`_
about requesting an ISB-CGC provided (and funded) project.  (We'll also be happy to do that for
you *after* you use the $300 Google credit / free trial.)

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

Enabling Required Google APIs
-----------------------------

To make use of all of the functionality described in these tutorials (including running the example code
available on github), you will need to have certain APIs
enabled for your GCP project.  Specifically, you will need the following to be enabled (some may already be 
enabled by default):

      + Google Compute Engine
      + Google Genomics
      + Google BigQuery
      + Google Cloud Logging
      + Google Cloud Pub/Sub

This `tutorial <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/enabling_new_APIs.pdf>`_ will
walk you through the steps involved in enabling new APIs for your project.

Additional Quickstart Tutorials
-------------------------------

* `An Introduction to BigQuery <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_BigQuery.pdf>`_
* `An Introduction to Cloud Datalab <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Cloud_Datalab.pdf>`_
* `An Introduction to Cloud Shell <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Cloud_Shell.pdf>`_

..

ISB Cancer Genomics Cloud (ISB-CGC)
###################################

* **Introductions, Overview** *etc* 

  + `Introduction to the ISB-CGC Platform <https://github.com/isb-cgc/readthedocs/raw/master/docs/include/workshop-intro-Aug2016.pdf>`_
  + `A Quick Tour of the Google Cloud Console <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Console.pdf>`_
  + `Copy/Paste Cheat Sheet <https://docs.google.com/document/d/1LYSRlmm2RwpuOpnpqjmRxHhZ6kU18grz3o5IPq_OhJ8/edit?usp=sharing>`_ (you might find this useful later on in the day)

..

* **ISB-CGC Web App & API Endpoints**

  + Web-App Tutorial (`walkthrough <https://docs.google.com/document/d/1z3XWf_cA-IyqRwmaZofZb5FCWPaW3KU8trXsrafm46c/edit?usp=sharing>`_)  (`doc <workshop/WebApp_tut.html>`_)
  + API Endpoints demo (`doc <progapi/Programmatic-API.html>`_)

..

* **ISB-CGC Open-Access BigQuery Tables**

  + Overview of TCGA data (`doc <data/data2/data_in_BQ.html>`_)
  + `BigQuery SQL Tutorial <workshop/BQ_SQL_tut_v2.html>`_
  + `Analysis using R <workshop/Workshop_R_tut_v2.html>`_  (`github <https://github.com/isb-cgc/examples-R>`_)

..

* **Computing in the Cloud**

  + Useful References: `Cloud SDK cheat sheet <https://docs.google.com/document/d/1ZZTsjHzQClA0gZyOhlBav-I4XQhW81Yx980qvgy_jr8/edit?usp=sharing>`_ 
  + Introduction to GCE (Google Compute Engine) (`slides <https://docs.google.com/presentation/d/13ORIDboGC27uCMf_C9w9WIi0cK9tGO7cqgp6vwA2miE/edit?usp=sharing>`_)
  + Google Genomics "Pipelines" Service (`slides <https://docs.google.com/presentation/d/1_rRvlhNuA0_SQuO2SOru7ttjPvzlygW3ALILcQ-JEjg/edit?usp=sharing>`_)
  + ISB-CGC Pipelines Framework (`slides <https://docs.google.com/presentation/d/1akqoZImzei2D47O8rcWrcEzsWPYxUtL-2-eUdiBzzgo/edit?usp=sharing>`_, `github <https://github.com/isb-cgc/ISB-CGC-pipelines>`_) 

..

Other Topics
############

DREAM Challenge: Somatic Mutation Challenge -- RNA
--------------------------------------------------

  + DREAM challenges are powered by `Sage Bionetworks <http://sagebase.org/>`_
  + `Presentation <https://docs.google.com/presentation/d/1p5W7ZDdahBYKBOcHu1wTeDClBbq7baDJs6EdMscupkc/edit?usp=sharing>`_
  + `Somatic Mutation Calling Challenge: RNA <https://www.synapse.org/#!Synapse:syn2813589/wiki/401435>`_ -- Registration is now open!


Google Genomics
---------------

  + `Overview <https://cloud.google.com/genomics/>`_
  + `Sign up <https://cloud.google.com/genomics/#contact-form>`_ to receive the Google Genomics whitepaper
  + `github repositories <https://github.com/googlegenomics>`_
  + `Google Genomics Cookbook <https://googlegenomics.readthedocs.io/en/latest/>`_ with sections on:

    - finding `published data sources <https://googlegenomics.readthedocs.io/en/latest/use_cases/discover_public_data/index.html>`_
    - `data-processing <https://googlegenomics.readthedocs.io/en/latest/sections/process_data.html>`_ on the Google Cloud
    - `data-analysis <https://googlegenomics.readthedocs.io/en/latest/sections/analyze_data.html>`_ on the Google Cloud
    - accessing data using `IGV <https://googlegenomics.readthedocs.io/en/latest/use_cases/browse_genomic_data/igv.html>`_, `BioConductor <https://googlegenomics.readthedocs.io/en/latest/use_cases/browse_genomic_data/bioconductor.html>`_, `R <https://googlegenomics.readthedocs.io/en/latest/api-client-r/index.html>`_, `Python <https://googlegenomics.readthedocs.io/en/latest/use_cases/getting-started-with-the-api/python.html>`_ and more!


