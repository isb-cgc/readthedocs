*****************
File Metadata
*****************

The ISB-CGC hosts several metadata tables to help users determine which files are available in Google BigQuery. Preview and query these tables conveniently and interactively from the BigQuery web UI or scripting languages such as R and Python, or the command-line using the cloud SDK utility bq. 

For additional details about each of these tables, please use the `BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_. To find the metadata tables, select **File Metadata** under **Category**.  

Below, the '#' represents the GDC release number and should be replaced by it when using the tables, for example: isb-cgc.GDC_metadata.rel24_caseData. The metadata is split up into several tables per GDC release as follows:

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - rel#_caseData
     - List of all of the cases in GDC
   * - rel#_fileData_current or rel#_fileData_active
     - List of the currently active cases in GDC along with information related to those cases
   * - rel#_fileData_legacy
     - Same as the previous table but with legacy data instead
   * - rel#_aliquot2caseIDmap
     - “helper” table to help map between identifiers at different levels of aliquot data. The intrinsic hierarchy is program > project > case > sample > portion > analyte > aliquot
   * - rel#_slide2caseIDmap
     - “helper” table to help map between identifiers at different levels of tissue slide data. The intrinsic hierarchy is program > project > case > sample > portion > slide
   * - rel#_GDCfileID_to_GCSurl
     - Gives the Google Cloud Storage location for each file

For examples of querying the metadata tables, please see the `ISB-CGC Community Notebook GitHub Repository <https://github.com/isb-cgc/Community-Notebooks>`_. 
