*******************
About the TCGA Data
*******************

The ISB-CGC hosts approximately 1 petabyte of TCGA_ data in Google Cloud
Storage (GCS_) and in BigQuery_.  

.. _TCGA: http://cancergenome.nih.gov/
.. _GCS: https://cloud.google.com/storage/
.. _BigQuery: https://cloud.google.com/bigquery/

The data being hosted by the ISB-CGC was obtained from the two main TCGA data
repositories:

* **TCGA DCC**: the TCGA Data Coordinating Center which provides a `Data Portal <https://tcga-data.nci.nih.gov/tcga/>`_ from which users may download open-access or controlled-access data.  This portal provides access to all TCGA data *except* for the low-level sequence data. 
* **CGHub**:  the `Cancer Genomics Hub <https://cghub.ucsc.edu>`_ is NCI's current secure data repository for all TCGA BAM and FASTQ sequence data files.

The ISB-CGC platform is one of NCI's `Cancer Genomics Cloud Pilots <https://cbiit.nci.nih.gov/ncip/nci-cancer-genomics-cloud-pilots>`_ 
and our mission is to host the TCGA data in the cloud so that researchers around the world may work with the data without needing 
to download and store the data at their own local institutions.

The vast majority (over 99%) of this **petabyte** of data consists of low-level sequence data, currently stored as files in
Google Cloud Storage.  Over the course of the TCGA project, this low-level (*"Level 1"*) data has been processed through 
a set of standardized pipelines and the the resulting high-level (*"Level 3"*) data is frequently the data that is used
in most downstream analyses.  The ISB-CGC platform aims to make these different types of data accessible to the widest
possible variety of users within the cancer research community, using the most appropriate Google Cloud Platform 
technologies.

More details about the TCGA data-generating platforms, data-types, and levels and can be found in the sections below:

.. toctree::
   :maxdepth: 1

   data2/TCGA_Data_Platforms
   data2/TCGA_Data_Types
   data2/TCGA_Data_Levels

In addition, we recommend that you review important information about data security and data access
in these sections:

.. toctree::
   :maxdepth: 1

   data2/TCGA_Data_Security
   data2/TCGA_Access

And finally, links to useful data reports can be found in this final section:

.. toctree::
   :maxdepth: 1

   data2/TCGA_Reports

