****************
ISB-CGC Workshop 
****************

This information is currently intended only for attendees who have
signed up for the 
`workshops at NCI on May 24th and 25th <https://cbiit.nci.nih.gov/ncip/nci-cancer-genomics-cloud-pilots/nci-cancer-genomics-cloud-workshop>`_.  
After the workshops, all materials will be made available as part of the
ISB-CGC documentation here on readthedocs.

Before we get started
#####################

As soon as you've found a seat and opened up your laptop, please do the 
following:

* sign into your Chrome browser using the Google identity you provided to us last week (if you did not provide us with a Google identity, please **alert one of our team**)

* check your email for the link to the WebEx for this workshop, and the link to these materials

* go to the Google Cloud Platform `Console <https://console.cloud.google.com>`_
    + you should not have to sign in again, but if you are asked to, use the Google identity you provided to us last week
    + in the top blue bar, towards the right, you chould be able to select between (at least) two projects: the "ISB-CGC Workshop" project and your own project -- if you do not see and/or cannot select between two or more projects, please **alert one of our team**

.. image:: console_top.png
   :scale: 75
   :align: center

..

* in a separate browser tab, open up the BigQuery `Web UI <https://bigquery.cloud.google.com>`_
    + just for fun, click on the red *COMPOSE QUERY* button in the upper left corner, and then cut and paste the following SQL into the **New Query** box and then click on the red **RUN QUERY** button

.. code-block:: sql

   SELECT COUNT(*) AS n, Study, Gender
   FROM [isb-cgc:tcga_201510_alpha.Clinical_data]
   GROUP BY Gender, Study
   ORDER BY n DESC, Study, Gender

Workshop Outline & Links
########################

.. toctree::
   :maxdepth: 1

   workshop/Intro_Goals
   workshop/Overview
   workshop/GCP_tour
   workshop/Integrative_Analysis_Tutorial
   workshop/Compute_Tutorial
   workshop/Wrap_Up

