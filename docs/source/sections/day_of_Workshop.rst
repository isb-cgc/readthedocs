****************
ISB-CGC Workshop
****************

This information is currently intended for attendees of the August 2nd workshop at ISB.
After the workshops, all materials will be made available as part of the
ISB-CGC documentation here on readthedocs.

If you want to have another look at the Pre-Workshop information we sent you, `here <Workshop_prep_Aug2016.html>`_ it is.

Before we get started ...
#########################

As soon as you've found a seat and opened up your laptop, please do the following:

* check your email for the latest workshop information, including links to materials as well as a link to a WebEx session -- you do *not* need to join the WebEx, but you might find it a useful way to see the what is being projected directly on your laptop;

..

* sign into your Chrome browser using the Google identity you provided to us, or the "temporary" Google identity that was given to you this morning;

..

* go to the Google Cloud Platform `Console <https://console.cloud.google.com>`_

  + you should not have to sign in again, but if you are asked to, use the same Google identity again
  + in the top blue bar, towards the right, you should see a project name, *eg* "ISB-CGC Workshop" -- if you are a member of two or more projects, then you will be able to select a project using that pulldown;

..

* if you have any questions or are unable to access the Google Cloud Console, please *raise your hand!*

.. image:: console_top.png
   :scale: 75
   :align: center

..

* if you *do* have your own GCP project, now would be a good time to make sure that you have certain APIs enabled.  (If you don't know how, take a look at `this tutorial <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/enabling_new_APIs.pdf>`_.)  Specifically, you will need these APIs enabled (some may already be enabled by default):

      + Google Compute Engine
      + Google Genomics
      + Google Cloud Logging
      + Google Cloud Pub/Sub

..

* find out what access-privileges you have in your GCP project: go to the `IAM & Admin <https://console.cloud.google.com/iam-admin/iam>`_ section of the Cloud Console, look for your identity (*eg* gmail address) and look at which Role(s) are listed to the right;

..

* just for fun, if you have time: in a separate browser tab, open up the BigQuery `Web UI <https://bigquery.cloud.google.com>`_

  + click on the red *COMPOSE QUERY* button in the upper left corner, and then cut and paste the simple SQL query below into the **New Query** box and then click on the red **RUN QUERY** button
  + try out the *Format Query* button, and the *Explanation* button above the Results
  + try modifying the query to make it invalid and then click on the red exclamation mark (below the query box on the far right)
  + you can find additional information about accessing and working with the ISB-CGC BigQuery tables on several other pages here on readthedocs -- try typing "BigQuery" into the "Quick search" box over in the left panel!
  + at the bottom of this page are links to several quickstart tutorials -- one of them is all about BigQuery

.. code-block:: sql

  SELECT COUNT(*) AS n, project_short_name , vital_status
  FROM `isb-cgc.TCGA_bioclin_v0.Clinical`
  GROUP BY vital_status , project_short_name
  ORDER BY n DESC, project_short_name , vital_status

Workshop Outline & Links
########################

ISB Cancer Genomics Cloud (ISB-CGC)
===================================

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

* **Lunch and Open Q&A Session**

..


* **Computing in the Cloud**

  + Useful References: `Cloud SDK cheat sheet <https://docs.google.com/document/d/1ZZTsjHzQClA0gZyOhlBav-I4XQhW81Yx980qvgy_jr8/edit?usp=sharing>`_
  + Introduction to GCE (Google Compute Engine) (`slides <https://docs.google.com/presentation/d/13ORIDboGC27uCMf_C9w9WIi0cK9tGO7cqgp6vwA2miE/edit?usp=sharing>`_)
  + Google Genomics "Pipelines" Service (`slides <https://docs.google.com/presentation/d/1_rRvlhNuA0_SQuO2SOru7ttjPvzlygW3ALILcQ-JEjg/edit?usp=sharing>`_)
  + ISB-CGC Pipelines Framework (`slides <https://docs.google.com/presentation/d/1akqoZImzei2D47O8rcWrcEzsWPYxUtL-2-eUdiBzzgo/edit?usp=sharing>`_, `github <https://github.com/isb-cgc/ISB-CGC-pipelines>`_)

..

DREAM Challenge: Somatic Mutation Challenge -- RNA
==================================================

* DREAM challenges powered by `Sage Bionetworks <http://sagebase.org/>`_

  + `Presentation <https://docs.google.com/presentation/d/1p5W7ZDdahBYKBOcHu1wTeDClBbq7baDJs6EdMscupkc/edit?usp=sharing>`_
  + `Somatic Mutation Calling Challenge: RNA <https://www.synapse.org/#!Synapse:syn2813589/wiki/401435>`_ -- Registration is now open!

..

Google Genomics
===============

  + `Overview <https://cloud.google.com/genomics/>`_
  + `github repositories <https://github.com/googlegenomics>`_
  + `Google Genomics Cookbook <https://googlegenomics.readthedocs.io/en/latest/>`_ with sections on:

    - finding `published data sources <https://googlegenomics.readthedocs.io/en/latest/use_cases/discover_public_data/index.html>`_
    - `data-processing <https://googlegenomics.readthedocs.io/en/latest/sections/process_data.html>`_ on the Google Cloud
    - `data-analysis <https://googlegenomics.readthedocs.io/en/latest/sections/analyze_data.html>`_ on the Google Cloud
    - accessing data using `IGV <https://googlegenomics.readthedocs.io/en/latest/use_cases/browse_genomic_data/igv.html>`_, `BioConductor <https://googlegenomics.readthedocs.io/en/latest/use_cases/browse_genomic_data/bioconductor.html>`_, `R <https://googlegenomics.readthedocs.io/en/latest/api-client-r/index.html>`_, `Python <https://googlegenomics.readthedocs.io/en/latest/use_cases/getting-started-with-the-api/python.html>`_ and more!

..

Quickstart Tutorials and Other Useful Links
###########################################

* `An Introduction to BigQuery <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_BigQuery.pdf>`_
* `An Introduction to Cloud Datalab <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Cloud_Datalab.pdf>`_
* `An Introduction to Cloud Shell <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Cloud_Shell.pdf>`_
