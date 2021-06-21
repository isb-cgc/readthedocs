*************
CTSP Data Set
*************

About the Clinical Trials Sequencing Project
--------------

The `Clinical Trials Sequencing Project <https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/clinical-trial-sequencing>`_ (CTSP) is a joint collaboration from the National Cancer Institute (NCI) and the Division of Cancer Treatment and Diagnosis (DCTD) to promote the use of genomics in NCI-sponsored clinical trials and elucidate the molecular basis of response and resistance to therapies studied. Breast cancer, renal cell carcinoma, and diffuse large B-cell lymphoma are the cancer types that are currently under study.


About the Clinical Trials Sequencing Project Data
-------------------

NCI utilized whole genome sequencing and/or whole-exome sequencing in conjunction with transcriptome sequencing to try to identify recurrent genetic alterations (mutations, deletions, amplifications, rearrangements) and/or gene expression signatures that would be important to the hypothesis(es) submitted by the investigators. The samples are processed and submitted for genomic characterization using pipelines and procedures established within The Cancer Genome Analysis (TCGA) project. There are 89 controlled access BAM files along with TSV files in the GDC. 

For more information on the CTSP data, please refer to these sites:

- `dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001175.v2.p2>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22projects.program.name%22%2C%22value%22%3A%5B%22CTSP%22%5D%7D%7D%5D%7D>`_

Accessing the Clinical Trials Sequencing Project Data on the Cloud
--------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the CTSP files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'CTSP'
  AND active.file_gdc_id = GCSurl.file_gdc_id

Accessing the CTSP Data in Google BigQuery
------------------------------------------------

ISB-CGC has CTSP data, such as clinical and RNA-seq, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with CTSP selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The CTSP tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.CTSP`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.CTSP_versioned`` contains previously released tables, as well as the most current table.
