*************************************
COSMIC in BigQuery hosted by ISB-CGC
*************************************

The COSMIC tables in BigQuery, produced in collaboration with the `Wellcome Trust Sanger Institute <http://www.sanger.ac.uk/>`_, provide a new way to explore and understand the mutations driving cancer.  The availability of COSMIC in BigQuery enables easy integration of this resource with other public datasets in BigQuery, including other open-access datasets made available by the ISB-CGC.

Getting Started
###############

`Register <https://cancer.sanger.ac.uk/cosmic/register>`_ with 
`COSMIC <https://cancer.sanger.ac.uk/cosmic/about>`_:

    * if you are already a registered user of COSMIC, you will need to go to `your account <https://cancer.sanger.ac.uk/cosmic/myaccount>`_ page and add a valid "Google identity" in the Google ID box -- when you are signed in to COSMIC, your name in the upper-right corner is a pull-down menu from which you can access your Account Settings;
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
    * go to the `BigQuery web UI <bigquery.cloud.google.com>`_  --  if you see a welcome screen inviting you to **Create a Project** then your ISB-CGC registration process is not yet complete;
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
from targeted and genome-wide screens.  The ISB-CGC COSMIC dataset in BigQuery currently 
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
ISB-CGC genomic-reference or molecular-data tables, the amount of data processed by a 
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
  
In the example query above, the table being queried is isb-cgc.COSMIC.grch37_v80: the first part of the name (isb-cgc) is the Google Cloud Platform (GCP) project name; the second part (COSMIC) is the dataset name; and the third part (grch37_v80) is the table name.
To add public BigQuery datasets and tables to your "view" in the BigQuery web UI you need to know the name of the GCP project that owns the dataset(s).  To add the publicly accessible ISB-CGC datasets follow these steps:
click on the blue triangle near the top of the left side-panel of the Big Query web  UI

select "Switch to project" and then "Display project."

in the pop-up window, enter isb-cgc in the Project ID box, and click OK
You should now be able to see and explore all of the ISB-CGC public datasets, including the COSMIC dataset, if you are a registered COSMIC user.  Clicking on the blue triangle next to a dataset name will open it and show the list of tables in the dataset.  Clicking on a table name will open up information about the table in main panel, where you can view the Schema, Details, or a Preview of the table.
Additional projects with public BigQuery datasets which you may want to explore (by repeating the process described above) include genomics-public-data, google.com:biggene, and silver-wall-555 (a project made available by Tute Genomics).

Additional BigQuery Documentation
The main Google BigQuery documentation can be found here.  
Legacy SQL vs Standard SQL
BigQuery introduced support for Standard SQL last year.  The previous version of SQL supported by BigQuery is now known as Legacy SQL.  Note that when you first go to the BigQuery web UI, Legacy SQL will be activated by default and you will need to enable Standard SQL if you want to use Standard SQL.  For simple queries, the same syntax will work in both, except for one important detail which is how you specify the table name.  A simple Standard SQL query might look like:
SELECT *
  FROM `isb-cgc.COSMIC.grch37_v80`
  LIMIT 1000

whereas the same query in Legacy SQL requires square brackets around the table name and a colon between the project name and the dataset name, like this:
SELECT *
  FROM [isb-cgc:COSMIC.grch37_v80]
  LIMIT 1000
SQL functions
Standard SQL includes a large variety of built-in functions and operators including logical and statistical aggregate functions, and mathematical functions, just to name a few.  User-defined functions (UDFs) are also supported and can be used to further extend the types of analyses possible in BigQuery.
Using the bq Command Line Tool
The bq command line tool is part of the cloud SDK and can be used to interact directly with BigQuery from the command line.  The cloud SDK is easy to install and is available for most operating systems.
Using BigQuery from R
BigQuery can be accessed from R using one of two powerful R packages: bigrquery and dplyr.  Please refer to the documentation provided with these packages for more information.
Using BigQuery from Python
BigQuery client libraries are available that let you interact with BigQuery from Python or other languages.  In addition, the experimental pandas.io.gbq module provides a wrapper for Google.s BigQuery analytics web service.
Getting Help
Aside from the documentation, the best place to look for help using BigQuery and tips and tricks with SQL is StackOverflow.  If you tag your question with google-bigquery     your question will quickly get the attention of Google BigQuery experts.  You may also find that your question has already been asked and answered among the nearly 10,000 questions that have already been asked about BigQuery on StackOverflow. 
More SQL Examples
Joining COSMIC to the Tute Annotations 
As mentioned above there is a BigQuery dataset made available by Tute Genomics which contains a single 8.6 billion row table containing annotations for the hg19 reference genome, including a "Tute score" which is a measure of the severity of the variant.  (March 2015 press release)
This query counts up the number of unique cases in COSMIC associated with frequently-occurring point mutations and then joins that to the Tute table to rank these mutations.  This query also illustrates the use of a few of BigQuery's string functions.  Note that the genomic coordinates in the Tute table are 0-bases while the COSMIC coordinates are 1-based, and this is corrected for in the query.
This query processes 475 GB, takes about 30 seconds, and produces an ordered list of 137 mutations (scroll down to the bottom to see screen shots of the results).  
Estimated query cost:  ($5/TB) x (475 GB / (1000 GB/TB)) = $2.375
WITH
  --
  -- mutCounts
  -- This first intermediate table includes the number of unique tumours 
  -- in COSMIC with point-mutations at a given genomic position.  Since the 
  -- the COSMIC table has a single field called Mutation_genome_position,
  -- we will want to split this into chromosome, startPos, and endPos.
  mutCounts AS (
  SELECT
    COUNT(DISTINCT(ID_tumour)) AS COSMIC_caseCount,
    Mutation_CDS AS COSMIC_CDS,
    SUBSTR(Mutation_CDS,-3,3) AS COSMIC_nucChange,
    Mutation_AA AS COSMIC_AA,
    SPLIT(Mutation_genome_position,':')[OFFSET(0)] AS chromosome,
    CAST(SPLIT(SPLIT(Mutation_genome_position,':')[OFFSET(1)],'-')[OFFSET(0)] AS INT64) AS startPos,
    CAST(SPLIT(SPLIT(Mutation_genome_position,':')[OFFSET(1)],'-')[OFFSET(1)] AS INT64) AS endPos
  FROM
    `isb-cgc.COSMIC.grch37_v80`
  WHERE
    Mutation_genome_position IS NOT NULL
    AND GRCh=37
    AND SUBSTR(Mutation_CDS,-2,1)='>'
  GROUP BY
    Mutation_CDS,
    Mutation_AA,
    Mutation_genome_position
  HAVING
    COSMIC_caseCount>=100 ),
  --
  -- fromTute
  -- Next, we extract just a few columns from the Tute table, while adjusting the
  -- 0-based coordinates.
  fromTute AS (
  SELECT
    Chr,
    (Start+1) AS Start,
    (`End`+1) AS `End`,
    Func,
    Gene,
    NucleotideChange AS Tute_CDS,
    SUBSTR(NucleotideChange,-3,3) AS Tute_nucChange,
    AA AS Tute_AA,
    cytoBand,
    TUTE AS Tute_Score
  FROM
    `silver-wall-555.TuteTable.hg19`
  WHERE
    SUBSTR(NucleotideChange,-2,1)='>'
  GROUP BY
    Chr,
    Start,
    `End`,
    Func,
    Gene,
    NucleotideChange,
    AA,
    cytoBand,
    TUTE ),
  --
  -- join1
  -- Now we join these two tables by aligning rows where the chromosome, start,
  -- end, and nucleotide-change are identical.
  join1 AS (
  SELECT
    Gene,
    Chr,
    Start,
    `End`,
    cytoBand,
    Func,
    COSMIC_nucChange AS nucChange,
    COSMIC_AA,
    Tute_AA,
    Tute_Score,
    COSMIC_caseCount
  FROM
    mutCounts
  JOIN
    fromTute
  ON
    chromosome=Chr
    AND startPos=Start
    AND endPos=`End`
    AND COSMIC_nucChange=Tute_nucChange )
  --
  -- Final select on the join result.
SELECT
  *
FROM
  join1
ORDER BY
  Tute_Score DESC,
  COSMIC_caseCount DESC


...

Note that the COSMIC_AA and the Tute_AA columns may not always be identical (although they are for all rows shown above).  Although the genomic coordinates of the variation, and the nucleotide change are required to match (by the JOIN statement in the query), the amino-acid change depends on the specific transcript being used to infer the protein sequence and may therefore be different between the two data sources.


