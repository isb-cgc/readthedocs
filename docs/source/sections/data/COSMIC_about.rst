***************
COSMIC Data Set
***************

About the Catalog Of Somatic Mutations In Cancer
-------------------------------------------------

The `Catalogue Of Somatic Mutations In Cancer <https://cancer.sanger.ac.uk/cosmic>`_ (COSMIC) is the world's largest and most comprehensive resource for exploring the impact of somatic mutations in human cancer. The COSMIC tables in BigQuery are produced in collaboration with the `Wellcome Trust Sanger Institute <http://www.sanger.ac.uk/>`_ to provide a new way to explore and understand the mutations driving cancer. 

About the Catalog Of Somatic Mutations In Cancer Data
------------------------------------------------------

The BigQuery data sets contain *all* of the CSV and TSV files available for download from the `COSMIC Download page <http://cancer.sanger.ac.uk/cosmic/download>`_. Please explore the tables at (after registering for access):

* `isb-cgc-bq.COSMIC <https://console.cloud.google.com/bigquery?p=isb-cgc-bq&d=COSMIC&page=dataset>`_
* `isb-cgc-bq.COSMIC_versioned <https://console.cloud.google.com/bigquery?p=isb-cgc-bq&d=COSMIC_versioned&page=dataset>`_

*Note: the project isb-cgc contains versions 85-91 except 88 and project isb-cgc-bq contains versions 92 and higher*


Accessing the Catalog Of Somatic Mutations In Cancer Data
------------------------------------------------------

To access the BigQuery tables, you will need to link your Google identity with a COSMIC account.

* **New COSMIC User:** `Register <https://cancer.sanger.ac.uk/cosmic/register>`_ for a new COSMIC account. During registration, fill in the 'Google ID' field with your base* Google Identity.

*A COSMIC account and academic use of the data is free, though commercial use of the COSMIC data is subject to licensing fees. Please review the* `COSMIC terms <https://cancer.sanger.ac.uk/cosmic/terms>`_ *for more information.*

* **Registered COSMIC User:** After logging in, navigate to the `Account Settings <https://cancer.sanger.ac.uk/cosmic/myaccount>`_ page and fill in the 'Google ID' field with your base* Google Identity.


Once you have linked your Google identity to a COSMIC account, ISB-CGC will obtain your Google Identity. After a short delay, you will have "viewer" access to the COSMIC tables in BigQuery. You will then be able to view the data sets in the BigQuery UI under the ``isb-cgc-bq`` Google Cloud project and query the tables with your own Google Cloud Project. 

We also have tutorials on using the COSMIC data sets with BigQuery in our `Community Notebook Repository <../HowTos.html>`_ that you can check out.

* `Intro to COSMIC in BigQuery Notebook (Python) <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/Intro_to_COSMIC_in_BigQuery.ipynb>`_
* `Exploring the COSMIC Cancer Gene Census (Python) <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/Exploring_COSMICs_Cancer_Gene_Census_table.ipynb>`_

If you are new to using ISB-CGC Google BigQuery data sets, see the `Quickstart Guide <../HowToGetStartedonISB-CGC.html>`_ to learn how to obtain a Google identity and how to set up a Google Cloud Project. Additionally, we offer free cloud credits for cancer research; you can find out more `here <../HowtoRequestCloudCredits.html>`_.

If you can't successfully run a query or see the COSMIC tables under the ``isb-cgc-bq project``, please `verify <https://accounts.google.com/ForgotPasswd>`_
that the Google ID you have provided is a valid Google account. If you are still unable to run a query or view the data sets under the ``isb-cgc-bq`` Google Cloud Project, please contact us at feedback@isb-cgc.org.


\* *e.g. the base account tb@mylab.org might have a longer-form alias like thomas.brown@mylab.org*
