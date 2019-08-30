***************
COSMIC Data Set
***************

About the COSMIC
----------------

The `Catalogue Of Somatic Mutations In Cancer <https://cancer.sanger.ac.uk/cosmic>`_ (COSMIC) is the world's largest and most comprehensive resource for exploring the impact of somatic mutations in human cancer. The COSMIC tables in BigQuery were produced in collaboration with the `Wellcome Trust Sanger Institute <http://www.sanger.ac.uk/>`_ to provide a new way to explore and understand the mutations driving cancer. 

About the COSMIC data
---------------------

The BigQuery datasets contain *all* of the tables available for download from the `COSMIC ftp site <http://cancer.sanger.ac.uk/cosmic/download>`_. The availability of these additional tables will support many more types of queries -- please explore them at (after registering for access as described below):

* `isb-cgc.COSMIC_v87_grch38 <https://console.cloud.google.com/bigquery?p=isb-cgc&d=COSMIC_v87_grch38&page=dataset>`_
* `isb-cgc.COSMIC_v87_grch37 <https://console.cloud.google.com/bigquery?p=isb-cgc&d=COSMIC_v87_grch37&page=dataset>`_
Details about the underlying COSMIC export files used to create these BigQuery tables can be found in the README files for `GRCh38 <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/source/sections/cosmic/README-cosmic-grch38.txt>`_ 
and `GRCh37 <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/source/sections/cosmic/README-cosmic-grch37.txt>`_.

Gaining Access to the Data
++++++++++++++++++++++++++

`Register <https://cancer.sanger.ac.uk/cosmic/register>`_ for access to `COSMIC <https://cancer.sanger.ac.uk/cosmic/about>`_ in `BigQuery <https://cloud.google.com/bigquery/what-is-bigquery>`_:

* If you are already a registered user of COSMIC, you will need to go to `your account <https://cancer.sanger.ac.uk/cosmic/myaccount>`_ page and add a valid "Google identity" in the Google ID box: when you are signed in to COSMIC, your name in the upper-right corner is a pull-down menu from which you can access your Account Settings
* If the Email Address that you initially used when registering for COSMIC is already a valid Google identity, you may simply reenter the same email address into the Google ID box
* If you are not sure whether your institutional (or other) email address is a Google identity, you can check by entering it in the Google `password-assistance page <https://accounts.google.com/ForgotPasswd>`_; or by asking your IT staff
* If you are not currently a registered COSMIC user, you will first need to `register <https://cancer.sanger.ac.uk/cosmic/register>`_, agree to the Terms and Conditions, and supply a valid Google identity in the Google ID box

Once you have completed these steps, ISB-CGC will obtain the Google identity that you provided and you will be given "viewer" access to the COSMIC tables in BigQuery.  You will also be added to an exploratory Google Cloud Platform (GCP) project called isb-cgc-cosmic which will allow you to run queries at no cost to you.
 
A few important notes:

* When you register with COSMIC, you create a password for your COSMIC account, which is associated with whatever email address you provided

  - This password is your COSMIC password, please avoid reusing any other password

* If you are not sure what a "Google ID" is, it is the name associated with a  "Google account", this includes any Gmail address

  - If you do not already have a Google account, you can `create one <https://accounts.google.com/SignUp?hl=en>`_

* If you mistype your Google ID or enter a string that is not a valid Google ID, you will not be able to access the COSMIC tables in BigQuery

  - Google IDs are not being automatically verified at this time, so please double-check that the Google ID you provided is correct

* Please enter the 'base' name and avoid using an alias

  - *e.g.* the base account tb@mylab.org might have a longer-form alias like thomas.brown@mylab.org

**Note**
After going through the registration process described above, there will be a short delay before your Google identity is granted the necessary access to BigQuery and the COSMIC data resources.  If you get an error when running a query, please wait 10-15 minutes and then try again. If you are still not successful, please `verify <https://accounts.google.com/ForgotPasswd>`_
that the Google ID you have provided is a valid Google account.  If you are still not able to run the sample query given below, please contact us at feedback@isb-cgc.org.
