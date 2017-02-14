********************
Cancer Program Data 
********************

The ISB-CGC platform currently hosts data from three major cancer programs: 
`TCGA <https://cancergenome.nih.gov/>`_ (The Cancer Genome Atlas), 
`TARGET <https://ocg.cancer.gov/programs/target>`_ 
(Therapeutically Applicable Research to Generate Effective Treatments), and 
`CCLE <http://www.nature.com/nature/journal/v483/n7391/full/nature11003.html>`_ 
(Cancer Cell Line Encylopedia).
These large and heterogenous datasets are hosted using different Google Cloud technologies:

* The higher-level, open-access data is available as a series of standardized, curated BigQuery tables.
* The original data files (as uploaded from the original source repositories) are available in Google Cloud Storage.

Further more some of the data is "open-access" while other data is "controlled-access".  All "metadata" 
(*ie* data about the data) is considered open-access.

The sections below describe data available from different Google Cloud technologies:

.. toctree::
   :maxdepth: 1
 
    data2/data_in_BQ.rst
    data2/data_in_GCS.rst
    data2/data_in_GG.rst


