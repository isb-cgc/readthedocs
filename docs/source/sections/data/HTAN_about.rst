*****************
HTAN Data Set
*****************

About HTAN
------------------------------------------------------------------------

The Ukrainian National Research Center for Radiation Medicine Trio Study contains epidemiologic data of trios of parents (exposed to the radiation from the Chernobyl accident) and their unexposed offspring. The purpose of the study is to investigate the transgenerational effects following nuclear accidents to understand the consequences of parental exposure to ionizing radiation.


About the HTAN Data
---------------------------------------------------------------------------------

The TRIO data set includes whole genome sequencing (WGS) sequencing reads for 339 cases in the project TRIO-CRU.

For more information on TRIO data, please refer to the site below:

- `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22projects.program.name%22%2C%22value%22%3A%5B%22TRIO%22%5D%7D%7D%5D%7D>`_

  
Accessing the HTAN Data in Google BigQuery
------------------------------------------------

ISB-CGC has HTAN data, such as single cell RNA-Seq, clinical, biospecimen, and metadata, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with HTAN selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The HTAN tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.HTAN`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.HTAN_versioned`` contains previously released tables, as well as the most current table.
