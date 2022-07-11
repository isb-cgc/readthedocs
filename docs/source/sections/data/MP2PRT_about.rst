*****************
MP2PRT Data Set
*****************

About MP2PRT
------------------------------------------------------------------------

The Molecular Profiling to Predict Response to Treatment (MP2PRT) program is part of the NCI's Cancer Moonshot Initiative. This study "Identification of Genetic Changes Associated with Relapse and/or Adaptive Resistance in Patients Registered as Favorable Histology Wilms Tumor on AREN03B2", performs genomic characterization on trio cases (normal tissue, tumor tissue at time of diagnosis, tumor tissue at time of relapse) from patients who relapsed with Favorable Histology Wilms Tumor. 

About MP2PRT Data
---------------------------------------------------------------------------------

The MP2PRT data set includes one project MP2PRT-WT with 52 cases. Data categories include sequencing reads, transcriptome profiling, simple nucleotide variation and copy number variation.

For more information on MP2PRT data, please refer to the site below:

- `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22projects.program.name%22%2C%22value%22%3A%5B%22MP2PRT%22%5D%7D%7D%5D%7D>`_


Accessing the MP2PRT Data in Google BigQuery
------------------------------------------------

ISB-CGC has MP2PRT data, such as clinical, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with MP2PRT selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The MP2PRT tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.MP2PRT`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.MP2PRT_versioned`` contains previously released tables, as well as the most current table.
