****************
Hosted TCGA Data 
****************

All TCGA *metadata* is considered open-access.  In other words, information *about* controlled-access data 
files is open-access.  Metadata can be obtained programmatically using the ISB-CGC programmatic API.

An overview of the TCGA data currently hosted on the ISB-CGC platform is provided in the two sections below.
The first section breaks the data down by access class (open *vs* controlled), and the second section breaks
it down by original source repository (DCC *and* CGHub).

.. toctree::
   :maxdepth: 1

   data2/byAccessClass
   data2/bySourceRepo

If you're interested instead in what type of data is stored using which Google Cloud technologies,
you may be more interested in a different way of looking at how we've organized the data:

* The higher-level, open-access data is available as a series of standardized, curated BigQuery tables.
* The original data files (as uploaded from the original source repositories) are available in Google Cloud Storage.
* In the near future, some of the sequence data will be available in Google Genomics, queryable using the GA4GH API.

Each of the following sections describes these three data resources in more detail:

.. toctree::
   :maxdepth: 1

   data2/data_in_BQ.rst
   data2/data_in_GCS.rst
   data2/data_in_GG.rst


