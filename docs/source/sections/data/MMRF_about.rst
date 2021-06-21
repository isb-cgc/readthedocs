****************
MMRF Data Set
****************

About the Multiple Myeloma Research Foundation
---------------

The `Multiple Myeloma Research Foundation <https://themmrf.org/>`_ (MMRF) seeks to provide resources and research for patients with multiple myeloma. MMRF began a ten-year study to track new Multiple Myeloma patients to create a rich data set which was led by researchers from the Dana Farber Cancer Institute, Celgene Corp., and the University of Arkansas for Medical Sciences. This trial was named CoMMpass.

About the Multiple Myeloma Research Foundation Data
--------------------

The `CoMMpass <https://themmrf.org/we-are-curing-multiple-myeloma/mmrf-commpass-study/>`_ trial is a longitudinal observation study of 1000 newly diagnosed myeloma patients receiving various standard approved treatments. This trial aims to collect tissue samples and genetic information along with quality of life, disease, and clinical outcomes. CoMMpass data consists of 995 cases with RNA, whole-exome, and whole-genome sequencing data. The NCI GDC houses all the molecular characterization data with over 10,918 VCF, 6,577 BAM, 2,577 TXT, and 1718 TSV files in around 206.63 TB of data. The Project ID in the GDC Data Portal is `MMRF-COMMPASS <https://portal.gdc.cancer.gov/projects/MMRF-COMMPASS>`_.

For more information on the MMRF data, please refer to these sites:

- `dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs000748.v7.p4>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22MMRF%22%5D%7D%7D%5D%7D>`_

Accessing Multiple Myeloma Research Foundation Data on the Cloud
--------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the MMRF files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FFROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'MMRF'
  AND active.file_gdc_id = GCSurl.file_gdc_id
  
Accessing the MMRF Data in Google BigQuery
------------------------------------------------

ISB-CGC has MMRF data, such as clinical, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with MMRF selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The MMRF tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.MMRF`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.MMRF_versioned`` contains previously released tables, as well as the most current table.
