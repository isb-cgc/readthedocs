***************
COSMIC Data Set
***************

About the Catalog Of Somatic Mutations In Cancer
-------------------------------------------------

The `Catalogue Of Somatic Mutations In Cancer <https://cancer.sanger.ac.uk/cosmic>`_ (COSMIC) is the world's largest and most comprehensive resource for exploring the impact of somatic mutations in human cancer. The COSMIC tables in BigQuery are produced in collaboration with the `Wellcome Trust Sanger Institute <http://www.sanger.ac.uk/>`_ to provide a new way to explore and understand the mutations driving cancer. 

About the Catalog Of Somatic Mutations In Cancer Data
------------------------------------------------------

The BigQuery datasets contain *all* of the CSV and TSV files available for download from the `COSMIC Download page <http://cancer.sanger.ac.uk/cosmic/download>`_. Please explore the tables at (after registering for access):

* `isb-cgc.COSMIC_v91_grch38 <https://console.cloud.google.com/bigquery?p=isb-cgc&d=COSMIC_v91_grch38&page=dataset>`_
* `isb-cgc.COSMIC_v91_grch37 <https://console.cloud.google.com/bigquery?p=isb-cgc&d=COSMIC_v91_grch37&page=dataset>`_

Accessing the Catalog Of Somatic Mutations In Cancer Data
------------------------------------------------------

You will need to link your Google identity with COSMIC to access BigQuery tables.

* **New COSMIC User:** `Register <https://cancer.sanger.ac.uk/cosmic/register>`_ for access to COSMIC data and agree to the Terms and Conditions and fill in the 'Google ID' field with your base Google Identity (*e.g.* the base account tb@mylab.org might have a longer-form alias like thomas.brown@mylab.org).

*A COSMIC account and acedemic use of the data is free though commercial use of the COSMIC data is subject to licensing fees. Please review the* `COSMIC terms <https://cancer.sanger.ac.uk/cosmic/terms>`_ *for more information.*

* **Registered COSMIC User:** Navigate to the `Account Settings <https://cancer.sanger.ac.uk/cosmic/myaccount>`_ page and fill in teh 'Google ID' field with your base Google Identity (*e.g.* the base account tb@mylab.org might have a longer-form alias like thomas.brown@mylab.org).

Once you have completed these steps, ISB-CGC will obtain the Google identity that you provided and you will be given "viewer" access to the COSMIC tables in BigQuery after a short delay. You will then be able to view the data sets in the BigQuery UI under the ``isb-cgc`` Google Cloud project. You will also be able to use the ``isb-cgc-cosmic`` Google Cloud Project (GCP) to run queries at no cost to you to explore the data sets.

If you can't successfully run a query or see the COSMIC tables under the isb-cgc project, please `verify <https://accounts.google.com/ForgotPasswd>`_
that the Google ID you have provided is a valid Google account.  If you are still not able to run a query or view the data sets under the isb-cgc Google Cloud Project, please contact us at feedback@isb-cgc.org.
