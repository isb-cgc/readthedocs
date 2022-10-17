******************************
Human Tumor Atlas Network Data
******************************

About HTAN
------------------------------------------------------------------------

The Human Tumor Atlas Network (`HTAN <https://humantumoratlas.org/>`_) is focused on transitions in cancer. Funded by the National Cancer Institute (NCI) Cancer Moonshot initiative, its mission is to construct three-dimensional atlases of the dynamic cellular, morphological, and molecular features of human cancers as they evolve from precancerous lesions to advanced disease (`Cell April 2020 <https://www.sciencedirect.com/science/article/pii/S0092867420303469>`_). Many HTAN studies focus on single cell and multiplex imaging modalities.


About the HTAN Data
---------------------------------------------------------------------------------

HTAN data encompasses at least 11 atlases and 17 primary tumor sites.
Data (Release 2) was extracted from the HTAN Data Portal via Synapse (https://humantumoratlas.org/data-download).

To explore HTAN data, please see the `HTAN Data Portal <https://humantumoratlas.org/explore/>`_.

Visit our `HTAN Notebooks <../HTANNotebooks.html>`_ page to see examples using the ISB-CGC hosted HTAN data.
  
Accessing the HTAN Data in Google BigQuery
------------------------------------------------

ISB-CGC has HTAN data, such as single cell RNA-Seq, clinical, biospecimen, and metadata, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with HTAN selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The HTAN tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.HTAN`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.HTAN_versioned`` contains previously released tables, as well as the most current table.
