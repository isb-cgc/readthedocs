**********************
BigQuery Usage Costs
**********************

More details about BigQuery costs can be found in the Google
`documentation <https://cloud.google.com/bigquery/pricing>`_.
There are two basic types of costs: storage costs and usage costs.  ISB-CGC is hosting
these PanCancer Atlas tables in BigQuery and is paying for the storage costs (with support from NCI).
The size of each PanCancer Atlas table is less than 1.5 GB and therefore costs less than $0.25 per year to store.

The main costs associated with using BigQuery are the query costs.  BigQuery is a
cloud-based massively parallel analytic engine which can scan terabytes of data in seconds.
Query costs start at $5 (USD) per TB of data scanned, but can be higher for more
computationally intensive queries (*eg* those that include complex user-defined-functions).

For the sample query above, we saw that clicking on the check-mark in the green circle
produced this message: Valid:  This query will process 125 MB when run.
The cost of this specific query can be estimated using this information:
($5/TB) x (125 MB / (1000000 MB/TB)) = $0.000625.  This cost is very (perhaps suprisingly) low,
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

If you want to be able to
upload your own data to BigQuery or save the results of your queries as new BigQuery tables,
you will need to have your own GCP project.  (All new GCP users are welcome
to take advantage of the Google `free trial <https://cloud.google.com/free/>`_
which includes up to $300 in funding to be used over a period of one year.)
