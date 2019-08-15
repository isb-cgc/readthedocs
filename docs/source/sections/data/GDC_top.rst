*******************
NCI's GDC Overview
*******************
The NCI hosts a variety of data from cancer genomic studies in the Genomic Data Commons (GDC) providing the cancer research community a unified data repository enabling data sharing to support precision medicine. The GDC Data Portal allows users to search for and download data directly via your web browser or using the GDC Data Transfer Tool. There are two sets of data available in the GDC: legacy data and harmonized data. The legacy data is from previous data coordinating centers, such as TCGA-DCC and CGHub, that the GDC inherited. The current data available in the GDC is harmonized data from the coordination centers that were re-aligned to GRCh38/hg38 and reprocessed by GDC along with new data sets.

The ISB-CGC hosts several metadata tables to help users determine which files are available in Google BigQuery. Preview and query these tables conveniently and interactively from the BigQuery web UI or scripting languages such as R and Python, or the command-line using the cloud SDK utility bq. The metadata is split up into several tables per release as follows:

.. list-table::
   :header-rows: 1

   * - Table
     - Description
   * - rel#_caseData
     - List of all of the cases in GDC
   * - rel#_fileData_current or rel17_fileData_active
     - List of the currently active cases in GDC along with information related to those cases
   * - rel#_fileData_legacy
     - Same as the previous table but with legacy data instead
   * - rel#_aliquot2caseIDmap
     - “helper” table to help map between identifiers at different levels of aliquot data. The intrinsic hierarchy is program > project > case > sample > portion > analyte > aliquot
   * - rel#_slide2caseIDmap
     - “helper” table to help map between identifiers at different levels of tissue slide data. The intrinsic hierarchy is program > project > case > sample > portion > slide
   * - rel#_GDCfileID_to_GCSurl
     - Gives the Google Cloud Storage location for each file

For examples of querying the metadata tables, please see the ISB-CGC Community Notebook GitHub Repository. If you have used the GDC portal to create cohorts or file lists, you can follow these tutorials to bring that information into ISB-CGC for use.
