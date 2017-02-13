**********************
Cloud-Hosted Data Sets
**********************

The ISB-CGC platform hosts the majority of the TCGA data set as well as other reference
and annotation datasets in different appropriate Google Cloud technologies:

    * low-level DNA- and RNA-Seq data are stored primarily in Google Cloud Storage;
    * some open-access CCLE sequence data is also available in `Google Genomics <https://cloud.google.com/genomics/>`_, where it can be queried using the `GA4GH API <https://media.readthedocs.org/pdf/ga4gh-schemas/latest/ga4gh-schemas.pdf>`_;
    * high-level clinical, biospecimen, and molecular data are available in a series of carefully curated datasets and tables backed by the massively-parallel analytics engine `Google BigQuery <>`_;
    * TCGA radiology and tissue image data are now also available in Google Cloud Storage;
    * TCGA proteomics (CPTAC PhaseII) data has also been uploaded to Google Cloud Storage;

The original mission of the ISB-CGC was to host the TCGA dataset.  We are now in midst
of adding data from the TARGET pediatric cancer.  Stay tuned for updates.

.. toctree::
   :maxdepth: 1

   data/BQ_overview
   data/TCGA-Data
   data/Data_on_ISBCGC
   data/Reference-Data
   data/Releases-Plus

