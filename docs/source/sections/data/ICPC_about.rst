*****************
ICPC Data Set
*****************

About the International Cancer Proteogenome Consortium
------------------------------------------------------------
The `International Cancer Proteogenome Consortium <https://proteomics.cancer.gov/programs/international-cancer-proteogenome-consortium>`_ (ICPC) is a voluntary scientific organization that provides a forum for collaboration among some of the world’s leading cancer and proteogenomic research centers. Launched in late 2016, the ICPC includes researchers from over a dozen countries sharing data and results of proteogenomic analysis.

About the International Cancer Proteogenome Consortium Data Set
---------------------------------------------------------------------

ICPC has several studies available at the `Proteomics Data Commons (PDC) <https://pdc.cancer.gov/pdc/>`_. ISB-CGC has procured data for the following studies through the PDC API:

- Proteogenomics of Gastric Cancer
- HBV-Related Hepatocellular Carcinima
- Oral Squamous Cell Carcinoma Study
- Academia Sinica LUAD100

Accessing the ICPC Data in Google BigQuery
------------------------------------------------

ISB-CGC has ICPC clinical and protein expression data stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with ICPC selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The ICPC tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.ICPC`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.ICPC_versioned`` contains previously released tables, as well as the most current table.
