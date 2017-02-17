*************************************
COSMIC in BigQuery hosted by ISB-CGC
*************************************

.. image:: COSMIC.png
   :scale: 20 %
   :align: right

The COSMIC tables in BigQuery, produced in collaboration with the 
`Wellcome Trust Sanger Institute <http://www.sanger.ac.uk/>`_, provide 
a new way to explore and understand the mutations driving cancer.  
The availability of COSMIC in BigQuery enables easy integration of this 
resource with other public datasets in BigQuery, including other 
open-access datasets made available by the ISB-CGC 
(see `this <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/data2/data_in_BQ.html>`_
and `that <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/Reference-Data.html>`_ 
for more details on other BigQuery datasets).

Getting Started
###############

`Register <https://cancer.sanger.ac.uk/cosmic/register>`_ for access to
`COSMIC <https://cancer.sanger.ac.uk/cosmic/about>`_ in `BigQuery <https://cloud.google.com/bigquery/what-is-bigquery>`_:

    * if you are already a registered user of COSMIC, you will need to go to `your account <https://cancer.sanger.ac.uk/cosmic/myaccount>`_ page and add a valid "Google identity" in the Google ID box: when you are signed in to COSMIC, your name in the upper-right corner is a pull-down menu from which you can access your Account Settings;
    * if the Email Address that you initially used when registering for COSMIC is already a valid Google identity, you may simply re-enter the same email address into the Google ID box;
    * if you are not sure whether your institutional (or other) email address is a Google identity, you can check by entering it in the Google `password-assistance page <https://accounts.google.com/ForgotPasswd>`_; or by asking your IT staff;
    * if you are not currently a registered COSMIC user, you will first need to `register <https://cancer.sanger.ac.uk/cosmic/register>`_, agree to the Terms and Conditions, and supply a valid Google identity in the Google ID box;

Once you have completed these steps, ISB-CGC will obtain the Google identity that you provided and you will be given "viewer" access to the COSMIC tables in BigQuery.  You will also be added to an exploratory Google Cloud Platform (GCP) project called isb-cgc-cosmic which will allow you to run queries at no cost to you.
 
A few important notes:

    * When you register with COSMIC, you create a password for your COSMIC account -- which is associated with whatever email address you provided.  This password is your COSMIC password, please avoid reusing any other password.
    * If you are not sure what a "Google ID" is, it is the name associated wth a  "Google account"  -- this includes any gmail address.  If you do not already have a Google account, you can create one.
    * If you mistype your Google ID, or enter a string that is not a valid Google ID, you will not be able to access the COSMIC tables in BigQuery.  Google IDs are not being automatically verified at this time, so please double-check that the Google ID you provided is correct.  
    * Avoid using an alias: *eg* the base account tb@mylab.org might have a longer-form alias like thomas.brown@mylab.org -- please enter the 'base' name;

Interactive Web-based Exploration
#################################

**NB**:  After going through the registration process described above, there will be a short 
delay before your Google identity is granted the necessary access to BigQuery and the COSMIC 
data resources.  If you get an error when running the sample query in this section, please 
wait 10-15 minutes and then try again. If you are still not successful, please 
`verify <https://accounts.google.com/ForgotPasswd>`_
that the Google ID you have provided is a valid Google account.  If you are still not able
to run the sample query given below, please contact us at feedback@isb-cgc.org.

    * `login <https://accounts.google.com/Login>`_ to your Google account (`Chrome <https://www.google.com/chrome/browser/desktop/index.html>`_ is the preferred browser);
    * go to the `BigQuery web UI <https://bigquery.cloud.google.com>`_  --  if you see a welcome screen inviting you to **Create a Project** then your ISB-CGC registration process is not yet complete;
    * click on the big red **COMPOSE QUERY** button in the upper left corner;
    * click on the **Show Options**  button below the **New Query** text-box;
    * un-check the **Use Legacy SQL** check-box (the bottom-most "option");
    * click on the **Hide Options** button;
    * paste the sample query below into the New Query text-box;
    * within a second or two you should see a green circle with a check-mark below the lower-right-corner of the New Query text-box  --  if instead you see a red circle with an exclamation mark, click on it to see what your Syntax Error is;
    * once you do have the green circle, you can click on it to see a message like: "Valid: This query will process 131 MB when run."
    * to execute the query, click on **RUN QUERY** !       

.. code-block:: sql

    WITH
      mutCounts AS (
      SELECT
        COUNT(DISTINCT(ID_tumour)) AS CaseCount,
        Mutation_AA,
        Gene_name
      FROM
        `isb-cgc.COSMIC.grch37_v80`
      GROUP BY
        Mutation_AA,
        Gene_name ),
      mutRatios AS (
      SELECT
        Mutation_AA,
        Gene_name,
        CaseCount,
        (CaseCount/SUM(CaseCount) OVER (PARTITION BY Gene_name)) AS ratio
      FROM
        mutCounts )
    SELECT
      *
    FROM
      mutRatios
    WHERE
      CaseCount>=1000
      AND ratio>=0.10
      AND NOT ( Mutation_AA LIKE "%?%" )
    ORDER BY
      Gene_name,
      ratio DESC

About the COSMIC BigQuery Tables
################################

The COSMIC BigQuery tables are based on the "CosmicMutantExport" files downloaded from the 
`Sanger ftp site <http://cancer.sanger.ac.uk/cosmic/download>`_.  
This file is a tab-separated table containing all COSMIC point mutations 
from targeted and genome-wide screens.  The ISB-CGC 
`COSMIC dataset <https://bigquery.cloud.google.com/dataset/isb-cgc:COSMIC>`_ 
in BigQuery currently 
includes the latest COSMIC release (v80) as well as the previous release (v79) for both 
GRCh37 and GRCh38.

BigQuery Usage Costs
####################

More details about BigQuery costs can be found in the Google 
`documentation <https://cloud.google.com/bigquery/pricing>`_.  
There are two basic types of costs: storage costs and usage costs.  ISB-CGC is hosting 
these COSMIC tables in BigQuery and is paying for the storage costs (with support from NCI).  
The size of each COSMIC table is less than 1.5 GB and therefore costs less than $0.25 per year to store.

The main costs associated with using BigQuery are the query costs.  BigQuery is a 
cloud-based massively parallel analytic engine which can scan terabytes of data in seconds.  
Query costs start at $5 (USD) per TB of data scanned, but can be higher for more 
computationally intensive queries (*eg* those that include complex user-defined-functions).

For the sample query above, we saw that clicking on the check-mark in the green circle 
produced this message: Valid:  This query will process 131 MB when run.
The cost of this specific query can be estimated using this information: 
($5/TB) x (131 MB / (1000000 MB/TB)) = $0.000655.  This cost is very (perhaps suprisingly) low, 
but it is always important to think carefully about your queries and to make them as 
efficient as possible.  If you want to derive summary information about all ~20,000 genes, 
for example, you could do that with a single query that might cost a few pennies, or 
you might write a less-clever query that returns information only about a single gene 
and then programmatically loop over all genes, running that single-gene query 20,000 times.  
Your overall query costs using this less-clever approach, instead of being a few pennies 
would be several hundred dollars!  This latter approach would also take significantly more time.  

As your queries become more complex and you begin to join in other resources such as the 
ISB-CGC `genomic-reference <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/Reference-Data.html>`_ 
or 
`molecular-data <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/data2/data_in_BQ.html>`_ 
tables, the amount of data processed by a 
single query may increase into the GB or even TB range.

During this introductory period (for at least the next 6 months), all registered COSMIC 
users will be added to the isb-cgc-cosmic Google Cloud Platform (GCP) project so that 
they will be able to perform exploratory queries at no cost to the user.  
(These costs will be paid by ISB-CGC, again with funding from NCI.)  Please note that 
users who perform large numbers of queries and incur significant costs will be 
removed from the isb-cgc-cosmic GCP project and will be required to create their own 
GCP projects prior to performing additional queries.  (All new GCP users are welcome 
to take advantage of the Google `free trial <https://cloud.google.com/free-trial/>`_ 
which includes up to $300 in funding to be used over a period of 60 days.)

Additional Public BigQuery Datasets
###################################

There are many public BigQuery datasets containing genomic information, and you 
can combine any of these resources into your SQL queries on the COSMIC tables -- 
all you need is the name of the table.
  
In the example query above, the table being queried is ``isb-cgc.COSMIC.grch37_v80``; 
a complete BigQuery table name has three components:

    * the first part of the name (isb-cgc) is the Google Cloud Platform (GCP) project name; 
    * the second part (COSMIC) is the dataset name; and 
    * the third part (grch37_v80) is the table name.

To add public BigQuery datasets and tables to your "view" in the BigQuery web UI you 
need to know the name of the GCP project that owns the dataset(s).  
To add the publicly accessible ISB-CGC datasets (project name: ``isb-cgc``)
follow these steps_.

.. _steps: http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/progapi/bigqueryGUI/LinkingBigQueryToIsb-cgcProject.html

You should now be able to see and explore all of the ISB-CGC public datasets, including 
the COSMIC dataset, if you are a registered COSMIC user.  Clicking on the blue triangle 
next to a dataset name will open it and show the list of tables in the dataset.  Clicking 
on a table name will open up information about the table in main panel, where you can 
view the Schema, Details, or a Preview of the table.

Additional projects with public BigQuery datasets which you may want to explore (repeating 
the same process will add these to your BigQuery side-panel) include genomics-public-data and
google.com:biggene.

Additional BigQuery Documentation
#################################

The main Google BigQuery documentation can be found `here <https://cloud.google.com/bigquery/docs/>`_.

Legacy SQL vs Standard SQL
--------------------------

BigQuery introduced support for 
`Standard SQL <https://cloud.google.com/bigquery/docs/reference/standard-sql/>`_ 
in 2016.  The previous version of SQL supported by 
BigQuery is now known as 
`Legacy SQL <https://cloud.google.com/bigquery/docs/reference/legacy-sql>`_.  
Note that when you first go to the BigQuery web UI, 
Legacy SQL will be activated by default and you will need to enable Standard SQL if you want to 
use Standard SQL.  For simple queries, the same syntax will work in both, except for one 
important detail which is how you specify the table name.  A simple Standard SQL query might look like:

.. code-block:: sql

    SELECT *
      FROM `isb-cgc.COSMIC.grch37_v80`
      LIMIT 1000

whereas the same query in Legacy SQL requires square brackets around the table name and a colon 
between the project name and the dataset name, like this:

.. code-block:: sql

    SELECT *
      FROM [isb-cgc:COSMIC.grch37_v80]
      LIMIT 1000

SQL functions
-------------

Standard SQL includes a large variety of built-in 
`functions and operators <https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators>`_ 
including logical and statistical aggregate functions, and mathematical functions, just to name a few.  
`User-defined functions <https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions>`_ (UDFs) 
are also supported and can be used to further extend the types of analyses possible in BigQuery.

Using the bq Command Line Tool
------------------------------
The **bq** command line tool is part of the 
`cloud SDK <https://cloud.google.com/sdk/>`_ and can be used to interact directly 
with BigQuery from the command line.  The cloud SDK is easy to install and 
is available for most operating systems.  You can use **bq** to create and upload
your own tables into BigQuery, and you can run queries at the command-line like
this:

.. code-block:: none

   bq query --allow_large_results \
            --destination_table="myproj:dataset:query_output" \
            --nouse_legacy_sql \
            --nodry_run \
            "$(cat myQuery.sql)"

(where myQuery.sql is a plain-text file containing the SQL, and the destination
table is in an existing BigQuery dataset in your project).

Using BigQuery from R
---------------------
BigQuery can be accessed from R using one of two powerful R packages: 
`bigrquery <https://cran.r-project.org/web/packages/bigrquery/>`_ and 
`dplyr <https://cran.r-project.org/web/packages/dplyr/>`_.  
Please refer to the documentation provided with these packages for more information.

Using BigQuery from Python
--------------------------
BigQuery 
`client libraries <https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-python>`_ 
are available that let you interact with BigQuery from Python or other languages.  
In addition, the experimental 
`pandas.io.gbq <http://pandas.pydata.org/pandas-docs/stable/io.html#google-bigquery-experimental>`_ 
module provides a wrapper for Google.s BigQuery analytics web service.

Getting Help
------------
Aside from the documentation, the best place to look for help using BigQuery and tips 
and tricks with SQL is 
`StackOverflow <http://stackoverflow.com/>`_.  If you tag your question with ``google-bigquery``     
your question will quickly get the attention of Google BigQuery experts.  You may also find 
that your question has already been asked and answered among the nearly 10,000 questions 
that have already been asked about BigQuery on StackOverflow. 

More SQL Examples
#################

Let's start with a few simple examples to explore some of the available fields in these COSMIC tables.  
Note that all of these examples are in "Standard SQL" so make sure that you have enabled it.

**1. How many mutations have been observed across KRAS?**

.. code-block:: sql

   SELECT
     COUNT(DISTINCT(ID_sample)) AS numSamples,
     COUNT(DISTINCT(ID_tumour)) AS numTumours
   FROM
     `isb-cgc.COSMIC.grch37_v79`
   WHERE
     Gene_name="KRAS"



Stay-tuned, more examples coming soon!


