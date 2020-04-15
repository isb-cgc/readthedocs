*****************************************
Intro to Exploring ISB-CGC Data and Tools
*****************************************

------------
Cancer Data
------------

ISB-CGC provides access to data from several research programs, such as TCGA, TARGET, CCLE and COSMIC. The full list 
is available here.

Storage Platforms
----------------
This data available using these Google Cloud Platform technologies:

Google BigQuery
~~~~~~~~~~~~~~~~
`Google BigQuery <https://cloud.google.com/bigquery/>`_ (BQ) is a massively-parallel analytics engine that is ideal for working with data that is essentially tabular in nature. This includes the high-level clinical, biospecimen, and molecular data from the main NCI programs. It is also where we store a large amount of metadata about files that are more appropriately stored in Google Cloud Storage, as well as genome reference sources (*e.g.* GENCODE, miRBase, *etc.*). All of these datasets and tables are completely *open access* and available to the research community.

Google Cloud Storage
~~~~~~~~~~~~~~~~~~~~
`Google Cloud Storage <https://cloud.google.com/storage/>`_ (GCS) is a cloud-based object-store that is used to store other types of (typically binary) data which is typically processed by custom software pipelines. The data hosted by GDC is contained within Google Cloud Storage.

.. image:: DataStorageOnISBCGC.png
   :align: center

-----
Tools
-----
