***************
COSMIC Data Set
***************

About the Catalog Of Somatic Mutations In Cancer
-------------------------------------------------

The `Catalogue Of Somatic Mutations In Cancer <https://cancer.sanger.ac.uk/cosmic>`_ (COSMIC) is the world's largest and most comprehensive resource for exploring the impact of somatic mutations in human cancer. The COSMIC tables in BigQuery are produced in collaboration with the `Wellcome Trust Sanger Institute <http://www.sanger.ac.uk/>`_ to provide a new way to explore and understand the mutations driving cancer. 

About the Catalog Of Somatic Mutations In Cancer Data
------------------------------------------------------

The BigQuery datasets contain *all* of the tables available for download from the `COSMIC FTP site <http://cancer.sanger.ac.uk/cosmic/download>`_. The availability of these additional tables will support many more types of queries -- please explore them at (after registering for access as described below):

* `isb-cgc.COSMIC_v91_grch38 <https://console.cloud.google.com/bigquery?p=isb-cgc&d=COSMIC_v91_grch38&page=dataset>`_
* `isb-cgc.COSMIC_v91_grch37 <https://console.cloud.google.com/bigquery?p=isb-cgc&d=COSMIC_v91_grch37&page=dataset>`_
Details about the underlying COSMIC export files are available on the `COSMIC downloads page <https://cancer.sanger.ac.uk/cosmic/download>`_.

Accessing the Catalog Of Somatic Mutations In Cancer Data
------------------------------------------------------

You will need to link your Google identity with COSMIC to access BigQuery tables.

1. `Register <https://cancer.sanger.ac.uk/cosmic/register>`_ for access to COSMIC data and agree to the Terms and Conditions

2. Navigate to the `your account <https://cancer.sanger.ac.uk/cosmic/myaccount>`_ page

3. Add a valid "Google identity" in the Google ID box

Once you have completed these steps, ISB-CGC will obtain the Google identity that you provided and you will be given "viewer" access to the COSMIC tables in BigQuery after a short delay.  You will also be added to an exploratory Google Cloud Platform (GCP) project called isb-cgc-cosmic which will allow you to run queries at no cost to you.
 
Notes
*****

* If the Email Address that you initially used when registering for COSMIC is already a valid Google identity, you may simply reenter the same email address into the Google ID box

* If you are not sure whether your institutional (or other) email address is a Google identity, you can check by entering it in the Google `password-assistance page <https://accounts.google.com/ForgotPasswd>`_; or by asking your IT staff

* a "Google ID" is the name associated with a  "Google account", this includes any Gmail address

* If you do not already have a Google account, you can `create one <https://accounts.google.com/SignUp?hl=en>`_

* If you mistype your Google ID or enter a string that is not a valid Google ID, you will not be able to access the COSMIC tables in BigQuery

* Please enter the 'base' name and avoid using an alias

  - *e.g.* the base account tb@mylab.org might have a longer-form alias like thomas.brown@mylab.org

If you can't successfully run a query or see the COSMIC tables under the isb-cgc project, please `verify <https://accounts.google.com/ForgotPasswd>`_
that the Google ID you have provided is a valid Google account.  If you are still not able to run a query or see the data sets, please contact us at feedback@isb-cgc.org.
