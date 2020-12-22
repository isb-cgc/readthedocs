*****************
CBTTC Data Set
*****************

About the Pediatric Brain Cancer Pilot proteome study (PDC000180)
------------------------------------------------------------
The `National Cancer Institute’s Clinical Proteomic Tumor Analysis Consortium <https://proteomics.cancer.gov/programs/cptac>`_ (CPTAC) is a national effort to accelerate the understanding of the molecular basis of cancer through the application of large-scale proteome and genome analysis or proteogenomics.

About the Pediatric Brain Cancer Pilot proteome study Data Set
---------------------------------------------------------------------

CPTAC data consists of whole-genome sequencing, whole-exome sequencing, RNA sequencing, and miRNA sequencing.  The program analyzed more than 700 cases. The Genomic Data Commons (GDC) currently has controlled VCF, TSV, and BAM data available. The Project ID in the GDC Data Portal is `CPTAC-2 <https://portal.gdc.cancer.gov/projects/CPTAC-2>`_ and `CPTAC-3 <https://portal.gdc.cancer.gov/projects/CPTAC-3>`_.


For more information on the CPTAC data, please refer to these sites:

- `CPTAC-2 dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000892>`_
- `CPTAC-3 dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001287.v5.p4>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D&searchTableTab=files>`_

Accessing the CBTTC Data in Google BigQuery
------------------------------------------------

ISB-CGC has CBTTC data, such as protein expression, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with CBTTC selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The CBTTC tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.CBTTC`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.CBTTC_versioned`` contains previously released tables, as well as the most current table.
