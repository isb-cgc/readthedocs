Biospecimen
===========

Parsing Biospecimen XML
-----------------------

Similarly, selected biospecimen fields from the biospecimen XML files
were extracted and loaded into a “biospecimen” table in BigQuery.
 Biospecimen BigQuery
\ `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Biospecimen_data&sa=D&usg=AFQjCNFWq7NUA2BkQ2br8PFG6VNySeFcxw>`__\  is
a sample-level.

In the first step, while iterating through the sample block the elements
(XML tags) and their values are collected. The slides’ info is averaged
across portions while iterating over the portions block. Also the
slides’ max and min values are calculated. The total number of slides
(num\_slides) and portions (num\_portions) is calculated for each
sample, along with the average, max and min values observed. All the
calculated and derived values are added as new columns in the BigQuery
tables.

Filters
-------

-  Samples with "is\_ffpe: is True are removed.
-  Patients/Samples where the "Project" is "null" are removed.

Formatting
----------

-  "pregnancies" and "total_number_of_pregnancies" are be merged into a
   single "pregnancies" field. The counts above four are represented as
   "4+" (e.g: [0,1,2,3,4+])
-  "number\_of\_lymphnodes\_examined" and "lymph\_node\_examined\_count" are
   merged into a single "number\_of\_lymphnodes\_examined" column.

