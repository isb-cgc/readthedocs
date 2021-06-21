***************
TARGET Data Set
***************

About the Therapeutically Applicable Research to Generate Effective Treatments
----------------
The `Therapeutically Applicable Research to Generate Effective Treatments <https://ocg.cancer.gov/programs/target>`_ (TARGET) program applied a comprehensive genomic approach to determine the molecular changes driving childhood cancers. Investigators formed a collaborative network to facilitate the discovery of molecular targets and translate those findings into the clinic. TARGET is managed by NCI's Office of Cancer Genomics and Cancer Therapy Evaluation Program.

About the Therapeutically Applicable Research to Generate Effective Treatments Data
---------------------

The ISB-CGC currently hosts several TARGET data sets in BigQuery. TARGET controlled-access data is available to authorized users in Genomic Data Commons and open-access data includes RNA-seq and miRNA-seq expression levels, and is available in BigQuery, along with the open-access clinical and biospecimen information.

The TARGET data is available at the GDC in the `legacy archive <https://portal.gdc.cancer.gov/legacy-archive/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22cases.project.program.name%22,%22value%22:%5B%22TARGET%22%5D%7D%7D%5D%7D>`_ which contains over 10,000 files for over 5,000 cases. Virtually all of this data is low-level (and controlled-access) sequence data (including 1702 RNA-seq files, 765 miRNA-seq, with the remainder being WXS or WGS DNA-seq BAMs).
Some of this data has been reprocessed and is available on the main `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=~%28op~%27and~content~%28~%28op~%27in~content~%28field~%27projects.program.name~value~%28~%27TARGET%29%29%29%29%29>`_. This newer dataset so far includes 33,402 files representing 6,197 cases and totaling over 200 TB. Over half of the files are controlled-access files, including BAM, VCF, and MAF file types, based on WXS, RNA-seq, and miRNA-seq data. The remaining files are open-access files, including RNA-seq and miRNA-seq quantification, as well as clinical and biospecimen supplement files.

BigQuery Therapeutically Applicable Research to Generate Effective Treatments Data
+++++++++++++++++++++++

The open-access TARGET data hosted by the ISB-CGC Platform includes:

* Clinical (de-identified) and Biospecimen data: these data were originally provided in XML files (Level-1)
* Gene (mRNA) expression data:  these data were originally provided as TSV files (Level-3)
* microRNA expression data:  these data were originally provided as TSV files (Level-3)

The information scattered over thousands of XLSX and TSV files at the GDC is provided in a *much more accessible* form in a series of 
BigQuery tables.

For more information on TARGET data, please refer to the site below:

- `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22projects.program.name%22%2C%22value%22%3A%5B%22TARGET%22%5D%7D%7D%5D%7D>`_

Accessing the Therapeutically Applicable Research to Generate Effective Treatments data on the Cloud
---------------------------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the TARGET files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'TARGET'
  AND active.file_gdc_id = GCSurl.file_gdc_id


Accessing the TARGET Data in Google BigQuery
------------------------------------------------

ISB-CGC has TARGET data, such as clinical, biospecimen, miRNA and RNA-seq, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with TARGET selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

ISB_CGC also has controlled access TARGET VCF data in Google BigQuery tables; see `here <../BigQuery/VariantDataInBigQuery.html>`_ for more information. 

The TARGET tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.TARGET`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.TARGET_versioned`` contains previously released tables, as well as the most current table.

Note that some of the tables in the isb-cgc-bq project were migrated from the isb-cgc project. If you were using data sets ``isb-cgc.TARGET_bioclin_v0`` and ``isb-cgc.TARGET_hg38_data_v0``, they still exist but are deprecated.

