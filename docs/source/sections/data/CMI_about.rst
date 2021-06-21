******************************
CMI Data Set
******************************

About the CMI
-------------------------------

Count Me In (CMI) is a non-profit organization that is stewarded by four organizations: `Emerson Collective <https://www.emersoncollective.com/>`_, `Broad Institute of MIT and Harvard <https://www.broadinstitute.org/>`_, the Biden Cancer Initiative, and the `Dana-Farber Cancer Institute <https://www.dana-farber.org/>`_. Count Me In works to engage patients via online platforms and share clinical and genomic data through public databases. Count Me In: The Metastatic Breast Cancer (MBC) Project is a patient-driven research initiative to accelerate metastatic breast cancer research. Count Me In: The Angiosarcoma (ASC) Project focuses on angiosarcoma, which is an exceedingly rare soft tissue sarcoma making it difficult to conduct large-scale research studies. Thus, this project demonstrates the feasibility of directly engaging patients to democratize research and create a large patient cohort. 

About the CMI Data
------------------------------------

The CMI consists of almost 5,000 files with 236 phenotyped subjects and over 16.09 TB of data. The data is made up of mainly BAM, VCF, TXT, and TSV files. The majority of the data is whole-exome sequencing along with RNA sequencing. The Project ID in the GDC is `CMI-MBC <https://portal.gdc.cancer.gov/projects/CMI-MBC>`_ and `CMI-ASC <https://portal.gdc.cancer.gov/projects/CMI-ASC>`_.


For more information on the CMI data, please refer to these sites:

- `CMI-MBC dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001709>`_
- `CMI-ASC dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001931>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CMI%22%5D%7D%7D%5D%7D>`_

Accessing the CMI Data on the Cloud
-------------------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc-bq.GDC_case_file_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the CMI files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc-bq.GDC_case_file_metadata.fileData_active_current` as active, `isb-cgc-bq.GDC_case_file_metadata.GDCfileID_to_GCSurl_current` as GCSurl
  WHERE program_name = 'CMI'
  AND active.file_gdc_id = GCSurl.file_gdc_id

Accessing the CMI Data in Google BigQuery
------------------------------------------------

ISB-CGC has CMI data, such as clinical and RNA-seq, stored in Google BigQuery tables. Information about these tables can be found using the `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_ with CMI selected for filter PROGRAM. To learn more about this tool, see the `ISB-CGC BigQuery Table Search documentation <../BigQueryTableSearchUI.html>`_.

The CMI tables are in project isb-cgc-bq. To learn more about how to view and query tables in the Google BigQuery console, see the `ISB-CGC BigQuery Tables documentation <../BigQuery.html>`_.

- Data set ``isb-cgc-bq.CMI`` contains the latest tables for each data type.
- Data set ``isb-cgc-bq.CMI_versioned`` contains previously released tables, as well as the most current table.
