*************
CTSP Data Set
*************

About the Clinical Trials Sequencing Project
--------------

The `Clinical Trials Sequencing Project <https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/clinical-trial-sequencing>`_ (CTSP) is a joint collaboration from the National Cancer Institute (NCI) Division of Cancer Treatment and Diagnosis (DCTD) to promote the use of genomics in NCI-sponsored clinical trials and elucidate the molecular basis of response and resistance to therapies studied. Breast cancer, renal cell carcinoma, and diffuse large B-cell lymphoma are the cancer types that are currently under study.


About the Clinical Trials Sequencing Project Data
-------------------

NCI utilized whole genome sequencing and/or whole-exome sequencing in conjunction with transcriptome sequencing to try to identify recurrent genetic alterations (mutations, deletions, amplifications, rearrangements) and/or gene expression signatures that would be important to the hypothesis(es) submitted by the investigators. The samples are processed and submitted for genomic characterization using pipelines and procedures established within The Cancer Genome Analysis (TCGA) project. There are 89 controlled access BAM files along with TSV files in the GDC. 

For more information on the CTSP data, please refer to these sites:

- `dbGaP site <https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?view_pdf&stacc=phs001175.v2.p2>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22projects.program.name%22%2C%22value%22%3A%5B%22CTSP%22%5D%7D%7D%5D%7D>`_

Accessing the Clinical Trials Sequencing ProjectData on the Cloud
--------------------------------

Besides accessing the files on the GDC Data Portal, you can also access them from the GDC Google Cloud Storage Bucket, which means that you don’t need to download them to perform analysis. ISB-CGC stores the cloud file locations in tables in the ``isb-cgc.GDC_metadata`` data set in BigQuery.

- To access these metadata files, go to the Google BigQuery console.
- Perform SQL queries to find the WCDT files. Here is an example:

.. code-block:: sql

  SELECT active.*, file_gdc_url
  FROM `isb-cgc.GDC_metadata.rel22_fileData_active` as active, `isb-cgc.GDC_metadata.rel22_GDCfileID_to_GCSurl` as GCSurl
  WHERE program_name = 'CTSP'
  AND active.file_gdc_id = GCSurl.file_gdc_id
