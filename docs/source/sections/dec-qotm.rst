******************
BigQuery Tips & Tricks: 
******************

Last month, we transformed a typical genomics file type (the vcf file format) into a BigQuery table. This month, we’ll continue exploring how to load data into bigquery tables. Because genomics files are often very large in size, we'll also explore some tricks on how to partition tables to query to save both money and time!

**I. Loading CSV Data into BigQuery**

First, let's explore how to load csv files into big query. Here’s an example of a common use-case:

*A lab with which your group collaborates is generating large amounts of RNAseq gene expression data. They have been following the nice analyses your group has done using BigQuery and would like you to help them perform similar analyses. Thus far, they have saved all of their RNAseq expression data into CSV format. They need your help first loading their RNAseq data files into BigQuery.*

Here, we’ll learn how to load CSV files into BigQuery tables. We’ll accomplish this with some very useful bq command-line tools and arguments.

Before starting:

-- This tutorial assumes that you’ve already created a GCP project. If you don’t already have one, instructions on how to set up one up can be found: `here <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/HowToGetStartedonISB-CGC.html>`__

-- Ensure that you have Google Cloud SDK installed


**Loading CSV files into Google Cloud Storage**  

You can load local files as well as files from Google Cloud Storage (GCS). For this exercise, let’s make a GCS bucket to store our CSV files.

1. Make a bucket to store the RNAseq CSV
::

	gsutil mb gs://RNAseq_CSVs



2. Copy the CSVs into your newly created storage bucket
::

	gsutil cp *.csv gs://RNAseq_CSVs
  
**Creating a BigQuery dataset**  

Creating tables and loading data via the BigQuery web-UI is good if
you’re only loading a small amount of data. It can be a tediously manual
process though if you have more than a handful of files. We can create
tables and load data using Google SDK’s handy bq tool. bq is a
python-based, command-line tool for BigQuery. `https://cloud.google.com/bigquery/docs/bq-command-line-tool <https://cloud.google.com/bigquery/docs/bq-command-line-tool>`__  

Let’s create a dataset that will hold our RNAseq data:
::

	bq mk RNAseq_data
  
If successful, you will get the following message: 
::

	Dataset 'Your_Project_ID:RNAseq\_data' successfully created
  
You can also list all of the datasets associated with your project using
the following command:
::

	bq ls
  
**Generate schema for BigQuery table**

A schema for a table is a description of its field names and types.
BigQuery allows you to specify a table's schema when you load data into
a table. We can create a schema file in JSON format. You can find a
Python script (**createSchema.py**) to create a JSON schema for your
table in our github examples-Python repository.

`https://github.com/isb-cgc/examples-Python/tree/master/python <https://github.com/isb-cgc/examples-Python/tree/master/python>`__

Usage: python createSchema.py <input-filename> <nSkip>

where nSkip specifies the # of lines skipped between lines that are
parsed and checked for data-types; if the input file is small, you can
leave set nSkip to be small, but if the input file is very large, nSkip
should probably be 1000 or more (default value is 1000)

**Loading Data in BigQuery**

With the JSON schema file, we are now ready to load data into BigQuery.The bq load command is used to load data in BigQuery via the
command-line.

::

    bq load \\

    --source\_format=CSV \\

    --skip\_leading\_rows=1 \\

    TEMP_LOCATION=gs://path_to_a_temp_folder

    RNAseq_data.expressionFile \\

    gs://RNAseq_CSVs/ExpressionDataTable.csv \\   

    ExpressionDataTable.csv.json  

    
You can verify that the table loaded by showing the table properties
with this command:

::

    bq show RNAseq_data.expressionFile
    

**II. BigQuery Table Clusters**

The costs of using BigQuery center around how much of a table is read by
the query. So, the same query applied to a small table versus a very
large table will incur very different costs. It simply costs more to
query a large table! In the past, we broke tables into many subtables to
save costs and time. This was the case with the methylation tables where
the entire thing consisted of 3.9 Billion rows (932 GB)! It's pretty
expensive to query that table, so we broke it into many tables by
chromosome. OK, but not entirely convenient to work with.

Now, there's a fairly simple step to accomplish the same thing,
resulting in huge cost savings without changing your SQL or table
schema! They're called 'clustered tables', which groups rows of your
BigQuery table so that your query only reads the appropriate portions of
your table. This means you can specify the cluster to be over
chromosomes, and your query will only read the portion of the table
associated with that chromosome. `https://cloud.google.com/bigquery/docs/clustered-tables<https://cloud.google.com/bigquery/docs/clustered-tables>`__

There's a number of different ways to partition your tables. For one,
you can partition it at the time of 'ingestion'. What that means is that
each time new data arrives, a new partition is created when the data is
appended to a new table.

So let's look at an example using a table built from wikipedia (from
Optimizing BigQuery: Cluster your tables, by `*Felipe
Hoffa* <https://medium.com/@hoffa?source=post_header_lockup>`__). This
uses a query to select-\*-everything from the table, and cluster it by
wiki and title. The order matters in clusters (see notes below)!
Clustered tables also have to be applied to partitioned tables. Below
the table is being partitioned by a date.

::

    CREATE TABLE \`fh-bigquery.wikipedia\_v3.pageviews\_2017\`

    PARTITION BY DATE(datehour)

    CLUSTER BY wiki, title

    OPTIONS(
    description="Wikipedia pageviews - partitioned by day,clustered by (wiki, title). Contact
   `*https://twitter.com/felipehoffa* <https://twitter.com/felipehoffa>`__", require\_partition\_filter=true)
     AS SELECT \* FROM \`fh-bigquery.wikipedia\_v2.pageviews\_2017\`
     WHERE datehour > '1990-01-01' # nag


Now, *Felipe* notes:

-  **CLUSTER BY wiki, title**: Whenever people query using the wiki
       column, BigQuery will optimize these queries. These queries will
       be optimized even further if the user also filters by title. If
       the user only filters by title, clustering won’t work, as the
       order is important (think boxes inside boxes).

-  **require\_partition\_filter=true**: This option reminds my users to
       always add a date filtering clause to their queries. That’s how I
       remind them that their queries could be cheaper if they only
       query through a fraction of the year.

To use a clustered table, just GROUP BY on the clustered columns, then
it's done automatically. Most often, you'll see a reduction in the
amount of data read, but you can also see where the runtime is reduced,
even if the amount of data read is the same.

::

	SELECT wiki, title, SUM(views) views
	FROM \`fh-bigquery.wikipedia\_v3.pageviews\_2017\`
	WHERE DATE(datehour) BETWEEN '2017-06-01' AND '2017-06-30'
	GROUP BY wiki, title
	ORDER BY views DESC
	LIMIT 10


without clustering

**64.8s elapsed, 180 GB processed**

with clustering

**22.1 elapsed, 180 GB processed**

So, in genomics data, this is an excellent technique to apply, and some
experimentation might be necessary to find the best clustering schema
for your work.

Let's try this on the 1000 genomes table from last month. That was a
table of genomic data, produced from a VCF file from the Wellcome Trust
1000 Genomes project.

Earlier I had written a query to flatten the VCF table, we'll use that
to partition, since some of the columns we'd like to use for
partitioning and clustering are nested fields, which are incompatible. I
saved that flat file to a new table 'flat1000genomes' with 2.7
\*Billion\* rows.

Partitioning tables (right now) only works with DATEs. So to get around
that, we'll create a 'fake date'

see:
(https://stackoverflow.com/questions/51802482/my-data-can-t-be-date-partitioned-how-do-i-use-clustering/51829225#51829225)

::

  CREATE TABLE
  \`isb-cgc-02-0001.Daves\_working\_area.Clustered1000genomes\`
  PARTITION BY fake\_date
  CLUSTER BY chr, name
  OPTIONS(
  description="1000 genomes partitioned by chr, cluster by call.name",
  require\_partition\_filter=true)
  AS SELECT \*, DATE('2018-12-14') fake\_date FROM
  \`isb-cgc-02-0001.Daves\_working\_area.flat1000genomes\`



So here's a query that counts up variants within samples.
::

  SELECT chr, name, alt1, COUNT( alt1 ) AS n
  FROM
  \`isb-cgc-02-0001.Daves\_working\_area.flat1000genomes\`
  GROUP BY chr,name,alt1
  ORDER BY n ASC

**Query complete (8.6s elapsed, 40.8 GB processed)**
::

  SELECT chr, name, alt2, COUNT( alt2 ) AS n
  FROM \`isb-cgc-02-0001.Daves\_working\_area.Clustered1000genomes\`
  WHERE fake\_date is not NULL
  GROUP BY chr, name, alt2
  ORDER BY n ASC
  LIMIT 10

**Query complete (3.6s elapsed, 61.2 GB processed)**

**That's more than 58% less time on ~50% more data!**
