*****************
Case and File Metadata
*****************

The ISB-CGC hosts several metadata tables in Google BigQuery to help users find GDC files in Google Cloud Storage (GCS) or PDC files in Amazon Web Services (AWS) cloud storage. Preview and query these tables from the BigQuery web UI or scripting languages such as R and Python, or the command-line using the cloud SDK utility bq. 

For additional details about each of these tables, please use the `BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_. To find the metadata tables, select **File Metadata** under **Category**.  

Below, the '#' represents the GDC release number and should be replaced by it when using the tables, for example: `isb-cgc-bq.GDC_case_file_metadata_versioned.caseData_r28`. The metadata is split up into several tables per GDC release as follows in the `isb-cgc-bq <https://console.cloud.google.com/bigquery?p=isb-cgc-bq&d=GDC_case_file_metadata_versioned&page=dataset>`_ project. 
(Older metadata is in the `isb-cgc <https://console.cloud.google.com/bigquery?p=isb-cgc&d=GDC_metadata&page=dataset>`_ project and follows a slightly different table naming format.)

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - caseData_r#
     - List of all of the cases in GDC
   * - fileData_active_r#
     - List of the currently active cases in GDC along with information related to those cases
   * - fileData_legacy_r#
     - Same as the previous table but with legacy data instead
   * - aliquot2caseIDmap_r#
     - “helper” table to map between identifiers at different levels of aliquot data. The intrinsic hierarchy is program > project > case > sample > portion > analyte > aliquot
   * - slide2caseIDmap_r#
     - “helper” table to map between identifiers at different levels of tissue slide data. The intrinsic hierarchy is program > project > case > sample > portion > slide
   * - GDCfileID_to_GCSurl_r#
     - Gives the Google Cloud Storage location for each file
   * - per_sample_file_metadata_hg19_gdc_r# or per_sample_file_metadata_hg38_gdc_r#
     - Provides file ids and other metadata for samples. Information is stored in these tables by program and these tables are in the respective program data set.


PDC metadata file and case metadata are stored in data sets  `isb-cgc-bq.PDC_metadata_versioned <https://console.cloud.google.com/bigquery?p=isb-cgc-bq&d=PDC_metadata_versioned&page=dataset>`_ and  `isb-cgc-bq.PDC_metadata <https://console.cloud.google.com/bigquery?p=isb-cgc-bq&d=PDC_metadata&page=dataset>`_. 

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - file_associated_entity_mapping_V#
     - List of PDC entitites mapped to cases and file IDs
   * - file_metadata_V#
     - Gives the AWS location for each file, study information, as well as an embargo date if it applies



For examples of querying the metadata tables, please see the `ISB-CGC Community Notebook GitHub Repository <https://github.com/isb-cgc/Community-Notebooks>`_. 
