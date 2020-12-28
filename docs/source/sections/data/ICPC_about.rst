*****************
ICPC Data Set
*****************

About the International Cancer Proteogenome Consortium
------------------------------------------------------------
The `International Cancer Proteogenome Consortium <https://proteomics.cancer.gov/programs/international-cancer-proteogenome-consortium>`_ (ICPC) is a voluntary scientific organization that provides a forum for collaboration among some of the world’s leading cancer and proteogenomic research centers. Launched in late 2016, the ICPC includes researchers from over a dozen countries sharing data and results of proteogenomic analysis in predicting the success of cancer treatment.

About theInternational Cancer Proteogenome Consortium Data Set
---------------------------------------------------------------------

CBTTC has data from over 3300 patients, with over 6500 samples available for access. It has whole genome and whole exome sequences, RNA-Seq and miRNA-Seq available for research.

CPTAC data consists of whole-genome sequencing, whole-exome sequencing, RNA sequencing, and miRNA sequencing.  The program analyzed more than 700 cases. The Genomic Data Commons (GDC) currently has controlled VCF, TSV, and BAM data available. The Project ID in the GDC Data Portal is `CPTAC-2 <https://portal.gdc.cancer.gov/projects/CPTAC-2>`_ and `CPTAC-3 <https://portal.gdc.cancer.gov/projects/CPTAC-3>`_.





Accessing the ICPC Data in Google BigQuery
------------------------------------------------

ISB-CGC has ICPC data, such as protein expression, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with ICPC selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The ICPC tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.ICPC`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.ICPC_versioned`` contains previously released tables, as well as the most current table.
