****************
VAREPOP Data Set
****************

About the VA Research for Precision Oncology Program
-----------------

The `Research for Precision Oncology Program (RePOP) <https://www.research.va.gov/research_in_action/Precision-Oncology-Program.cfm>`_ is a research activity that established a cohort of Veterans diagnosed with cancer and had genomic analyses performed on their tumor tissue as part of the standard of care. All data relevant to a patient's cancer and cancer care was collected under RePOP, including patient demographics, comorbidities, genomic analysis, treatments, medications, lab values, imaging studies, and outcomes. All RePOP participants signed/verbal informed consent and signed HIPAA authorization to have their data stored and shared from RePOP's Precision Oncology Program Data Repository (PODR).


About the VA Research for Precision Oncology Program Data
----------------------

The VARePOP data set consists of 7 cases with somatic mutation and targeted sequencing data. The Genomic Data Commons currently has controlled access BAM and VCF files. The Project ID in the GDC Data Portal is `VAREPOP-APOLLO <https://portal.gdc.cancer.gov/projects/VAREPOP-APOLLO>`_.

For more information on the VAREPOP data, please refer to these sites:

- `dbGaP site <https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?view_pdf&stacc=phs001374.v1.p1>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22VAREPOP%22%5D%7D%7D%5D%7D>`_

Accessing the VA Research for Precision Oncology Program on the Cloud
---------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the VAREPOP files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'VAREPOP'
  AND active.file_gdc_id = GCSurl.file_gdc_id

Accessing the VAREPOP Data in Google BigQuery
------------------------------------------------

ISB-CGC has VAREPOP data, such as clinical, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with VAREPOP selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The VAREPOP tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.VAREPOP`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.VAREPOP_versioned`` contains previously released tables, as well as the most current table.
