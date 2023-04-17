*****************
MATCH Data Set
*****************

About the Molecular Analysis for Therapy Choice (MATCH) Program
------------------------------------------------------------
The `Molecular Analysis for Therapy Choice <https://www.cancer.gov/about-cancer/treatment/clinical-trials/nci-supported/nci-match>`_ (MATCH) network is a collaboration between NCI, the Department of Defense (DoD), and the Department of Veterans Affairs (VA). Its purpose is to incorporate proteogenomics into tumor study to better pinpoint treatment therapies by examing both genetic abnormalities and protein information. It is part of NCI’s Cancer Moonshot Initiative. 

About the Molecular Analysis for Therapy Choice Data Set
---------------------------------------------------------------------

The intial studies from project MATCH are available at the `Genomics Data Commons (GDC) <https://portal.gdc.cancer.gov/>`_. 

Accessing the MATCH Data in Google BigQuery
------------------------------------------------

ISB-CGC has MATCH data, such as clinical and metadata, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with MATCH selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The MATCH tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.MATCH`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.MATCH_versioned`` contains previously released tables, as well as the most current table.
