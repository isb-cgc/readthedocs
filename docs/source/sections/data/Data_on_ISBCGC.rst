************************
ISB-CGC Hosted Data Sets
************************

Part of the mission of the ISB-CGC has been to explore the best ways
to use the available cloud technologies to provide access to the
hosted data.  To this end, the hosted data is made available
using these three main Google Cloud Platform technologies:

* `Google BigQuery <https://cloud.google.com/bigquery/>`_ (BQ), 
   a massively-parallel analytics engine is ideal for
   working with data that is essentially tabular in nature.  This includes,
   the high-level clinical, biospecimen, and molecular data from the main
   NCI programs.  It is also where we store a large amount of metadata about
   files that are more appropriately stored in Google Cloud Storage,
   as well as genome reference sources (*eg* GENCODE, miRBase, *etc*).
   All of these datasets and tables are completely *open access* and available 
   to the research community.

* `Google Cloud Storage <https://cloud.google.com/storage/>`_ (GCS), 
   a cloud-hosted object-store is used to store other types of (typically binary)
   data which is typically processed by custom software pipelines.
   In our case this means the low-level sequence data, in BAM or FASTQ
   format, as well as pathology and radiology images (in SVS or DICOM format).
   All controlled-access data is currently only available in GCS -- access
   to these data requires that a user walk through the required 
   `authentication and authorization steps <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/Gaining-Access-To-Contolled-Access-Data.html>`_.

* `Google Genomics <https://cloud.google.com/genomics/>`_ (GG),
   provides a new way to work with sequence-level data, via the `GA4GH API <http://ga4gh.org/#/>`_.
   Only the CCLE sequence data is currently hosted here, for users to experiment with.
   If and when the research community shifts away from BAM files towards using
   the GA4GH API, using this technology as our primary data-store may make more sense.

Please refer to the sections below for more details about the data available in these
three Google Cloud technologies:

.. toctree::
   :maxdepth: 1
 
   data2/data_in_BQ.rst
   data2/data_in_GCS.rst
   data2/data_in_GG.rst


