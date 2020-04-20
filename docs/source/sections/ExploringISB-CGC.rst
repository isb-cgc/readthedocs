***********************
About the ISB-CGC Data
***********************

ISB-CGC provides access to data from several research programs, such as The Cancer Genome Atlas (TCGA), Therapeutically Applicable Research to Generate Effective Treatments (TARGET), Cancer Cell Line Encyclopedia (CCLE) and Catalogue of Somatic Mutations in Cancer (COSMIC). The full list is available `here <Hosted-Data.html>`_.  

Most of this data originates at the NCI Genomic Data Commons (GDC). The GDC stores both raw and processed data from cancer patients on both Google and Amazon Web Services (AWS) cloud platforms. ISB-CGC points to the GDC-owned Google Cloud Storage buckets which contain files for both raw and processed data. The GDC has established workflows that they run on the raw data to generate the processed data. Thus users have access to the processed data instead of having to run compute intensive workflows themselves. Users who wish to run their own pipelines/workflows have access to the raw data as well. In general, almost all raw data is controlled-access and only those with proper authentication can access them. 

GDC processed data, however, are generally open-access and ISB-CGC has transformed the processed data, stored in a large number of files, into Google BigQuery tables consolidated by datatype (ex. clinical, sample, DNA Methylation, RNAseq,Copy Number Segmentation, Protein Expression, Mutation for ease of access and analysis. This novel approach allows our users to quickly analyze information from thousands of patients in our curated BigQuery tables.  

-------------------
Storing Cancer Data
-------------------

The data is stored on these Google Cloud Platform technologies:

Google BigQuery
~~~~~~~~~~~~~~~~
`Google BigQuery <https://cloud.google.com/bigquery/>`_ (BQ) is a columnar database ideal for storing tabular data. Its query speed is automatically scaled by multiprocessing. Data is accessed using a powerful SQL language interface.

ISB-CGC stores high-level clinical, biospecimen, and molecular data from the main NCI programs in the BigQuery project isb-cgc. It also stores a large amount of metadata about files that are stored in the GDC Google Cloud Storage, as well as genome reference sources (*e.g.* GENCODE, miRBase, *etc.*). All of these datasets and tables are completely *open access* and available to the research community.

Google Cloud Storage
~~~~~~~~~~~~~~~~~~~~
`Google Cloud Storage <https://cloud.google.com/storage/>`_ (GCS) is a cloud-based object-store that is used to store other types of (typically binary) data, typically processed by custom software pipelines. The data hosted by GDC is contained within Google Cloud Storage.

.. image:: DataStorageOnISBCGC.png
   :align: center
