*************
 Usage Costs
*************

The main costs associated with using BigQuery are the query costs.  BigQuery is a
cloud-based massively parallel analytic engine which can scan terabytes of data in seconds.
Query costs start at $5 (USD) per TB of data scanned, but can be higher for more
computationally intensive queries (*eg* those that include complex user-defined-functions).


In BigQuery, queries are billed according to how much data is scanned during the course of the query, and the rate is $5 per TB, although the first 1 TB is free each month. More detailed information can be found  `here <https://cloud.google.com/bigquery/pricing>`_ about how much does it costs to use BigQuery. Keep an eye on your GCP expenses on your Google Cloud Platform `Console home page <https://console.cloud.google.com/home/dashboard>`_.



There are two basic types of costs: storage costs and usage costs.  For example, ISB-CGC is hosting
PanCancer Atlas tables in BigQuery and is paying for the storage costs (with support from NCI). The size of each PanCancer Atlas table is less than 1.5 GB and therefore costs less than $0.25 per year to store.


While most cost is very (perhaps suprisingly) low, it is always important to think carefully about your queries and to make them as efficient as possible.  If you want to derive summary information about all ~20,000 genes,
for example, you could do that with a single query that might cost a few pennies, or
you might write a less-clever query that returns information only about a single gene
and then programmatically loop over all genes, running that single-gene query 20,000 times.
Your overall query costs using this less-clever approach, instead of being a few pennies
would be several hundred dollars!  This latter approach would also take significantly more time.

As your queries become more complex and you begin to join in other resources such as the
ISB-CGC genomic-reference  or the amount of data processed by a single query may increase into the GB or even TB range.

If you want to be able to upload your own data to BigQuery or save the results of your queries as new BigQuery tables,
you will need to have your own GCP project.  (All new GCP users are welcome
to take advantage of the Google `free trial <https://cloud.google.com/free/>`_
which includes up to $300 in funding to be used over a period of one year.)

*****************************
Additional Google Support
*****************************

Additional information about BigQuery can be found here:  
https://cloud.google.com/bigquery/what-is-bigquery 
https://cloud.google.com/bigquery/query-reference 
https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui

Latest information about BigQuery including quickstart guides and query references can be found at: https://cloud.google.com/bigquery 


