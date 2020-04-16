*****************************************
Intro to Exploring ISB-CGC Data and Tools
*****************************************

-------------------
Storing Cancer Data
-------------------

ISB-CGC provides access to data from several research programs, such as TCGA, TARGET, CCLE and COSMIC. The full list 
is available `here <Hosted-Data.html>`_.

This data is stored on these Google Cloud Platform technologies:

Google BigQuery
~~~~~~~~~~~~~~~~
`Google BigQuery <https://cloud.google.com/bigquery/>`_ (BQ) is a columnar database ideal for storing tabular data. Its query speed is automatically scaled by multiprocessing. Data is accessed using a powerful SQL language interface.

ISB-CGC stores high-level clinical, biospecimen, and molecular data from the main NCI programs in the BigQuery project isb-cgc. It also stores a large amount of metadata about files that are stored in the GDC Google Cloud Storage, as well as genome reference sources (*e.g.* GENCODE, miRBase, *etc.*). All of these datasets and tables are completely *open access* and available to the research community.

Google Cloud Storage
~~~~~~~~~~~~~~~~~~~~
`Google Cloud Storage <https://cloud.google.com/storage/>`_ (GCS) is a cloud-based object-store that is used to store other types of (typically binary) data, typically processed by custom software pipelines. The data hosted by GDC is contained within Google Cloud Storage.

.. image:: DataStorageOnISBCGC.png
   :align: center

-------------------------
Exploring the Cancer Data
-------------------------

There are several entry points for exploring cancer data on ISB-CGC.
  * The ISB-CGC Web Application allows users to interactively create cohorts of interest.
  * The ISB-CGC API gives users the ability to programmatically deal with data such as cases, samples, cohorts, files and cloud projects.
  * The ISB-CGC BigQuery Table Search is a discovery tool that allows the user to explore and search for ISB-CGC BiqQuery tables.
  * On the Google Cloud Platform, ISB-CGC tables can be viewed and queried directly.
  * Python and R can interface with the ISB-CGC tables, retrieving and analyzing data.
  * Using Google Compute Engines and VMs, workflows can be run to perform data analysis. 
  
  Please see the USER GUIDE section to learn more about each of these tools and the MORE INFORMATION section to see examples, tutorials, Jupyter and R Notebooks, Frequently Asked Questions and more.

.. image:: ToolsForISBCGC.png
   :align: center
