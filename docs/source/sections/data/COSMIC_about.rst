***************
COSMIC Data Set
***************

About the Catalog Of Somatic Mutations In Cancer
-------------------------------------------------

The `Catalogue Of Somatic Mutations In Cancer <https://cancer.sanger.ac.uk/cosmic>`_ (COSMIC) is the world's largest and most comprehensive resource for exploring the impact of somatic mutations in human cancer. The COSMIC tables in BigQuery are produced in collaboration with the `Wellcome Trust Sanger Institute <http://www.sanger.ac.uk/>`_ to provide a new way to explore and understand the mutations driving cancer. 

About the Catalog Of Somatic Mutations In Cancer Data
------------------------------------------------------

The BigQuery data sets contain *all* of the CSV and TSV files available for download from the `COSMIC Download page <http://cancer.sanger.ac.uk/cosmic/download>`_. Please explore the tables at (after registering for access):

* `isb-cgc.COSMIC_v90_grch38 <https://console.cloud.google.com/bigquery?p=isb-cgc&d=COSMIC_v90_grch38&page=dataset>`_
* `isb-cgc.COSMIC_v90_grch37 <https://console.cloud.google.com/bigquery?p=isb-cgc&d=COSMIC_v90_grch37&page=dataset>`_

Accessing the Catalog Of Somatic Mutations In Cancer Data
------------------------------------------------------

To access the BigQuery tables, you will need to link your Google identity with a COSMIC account.

* **New COSMIC User:** `Register <https://cancer.sanger.ac.uk/cosmic/register>`_ for a new COSMIC account. During registration, fill in the 'Google ID' field with your base Google Identity.

*A COSMIC account and academic use of the data is free, though commercial use of the COSMIC data is subject to licensing fees. Please review the* `COSMIC terms <https://cancer.sanger.ac.uk/cosmic/terms>`_ *for more information.*

* **Registered COSMIC User:** After logging in, navigate to the `Account Settings <https://cancer.sanger.ac.uk/cosmic/myaccount>`_ page and fill in the 'Google ID' field with your base Google Identity.


Once you have linked your Google Identity to a COSMIC account, ISB-CGC will obtain your Google Identity. After a short delay, you will have "viewer" access to the COSMIC tables in BigQuery. You will then be able to view the data sets in the BigQuery UI under the ``isb-cgc`` Google Cloud project and query the tables with your own Google Cloud Project. If you are new to using ISB-CGC Google BigQuery data sets, see the `Quickstart Guide <HowToGetStartedonISB-CGC.html>`_ to learn how to obtain a Google identity and how to set up a Google Cloud Project. Additionally, we offer free cloud credits for cancer research, you can find out more `here <sections/HowtoRequestCloudCredits.html>`_.

If you can't successfully run a query or see the COSMIC tables under the isb-cgc project, please `verify <https://accounts.google.com/ForgotPasswd>`_
that the Google ID you have provided is a valid Google account. If you are still unable to run a query or view the data sets under the ``isb-cgc`` Google Cloud Project, please contact us at feedback@isb-cgc.org.
