*****************
APOLLO Data Set
*****************

About the Applied Proteogenomics Organizational Learning and Outcomes (APOLLO) Program
------------------------------------------------------------
The `Applied Proteogenomics Organizational Learning and Outcomes <https://proteomics.cancer.gov/programs/apollo-network>`_ (APOLLO) network is a collaboration between NCI, the Department of Defense (DoD), and the Department of Veterans Affairs (VA). Its purpose is to incorporate proteogenomics into tumor study to better pinpoint treatment therapies by examing both genetic abnormalities and protein information. It is part of NCI’s Cancer Moonshot Initiative. 

About the Applied Proteogenomics Organizational Learning and Outcomes Data Set
---------------------------------------------------------------------

The intial studies from APOLLO are available at the `Proteomics Data Commons (PDC) <https://pdc.cancer.gov/pdc/>`_. ISB-CGC has procured this data through the PDC API. This initial data is from lung cancer patients.

Accessing the APOLLO Data in Google BigQuery
------------------------------------------------

ISB-CGC has APOLLO data, such as clinical and metadata, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with APOLLO selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The APOLLO tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.APOLLO`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.APOLLO_versioned`` contains previously released tables, as well as the most current table.
