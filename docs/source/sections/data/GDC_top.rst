*****************
NCI GDC Overview
*****************
The NCI hosts a variety of data from cancer genomic studies in the `Genomic Data Commons <https://gdc.cancer.gov/>`_ (GDC) providing the cancer research community a unified data repository enabling data sharing to support precision medicine. The `GDC Data Portal <https://portal.gdc.cancer.gov/>`_ allows users to search for and download data directly via your web browser or using the GDC Data Transfer Tool. There are two sets of data available in the GDC: legacy data and harmonized data. The legacy data is from previous data coordinating centers, such as TCGA-DCC and CGHub, that the GDC inherited. The current data available in the GDC is harmonized data from the coordination centers that were realigned to GRCh38/hg38 and reprocessed by GDC along with new data sets.

The ISB-CGC hosts several metadata tables to help users determine which files are available in Google BigQuery. Preview and query these tables conveniently and interactively from the BigQuery web UI or scripting languages such as R and Python, or the command-line using the cloud SDK utility bq. The metadata is split up into several tables per release as follows:

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

For examples of querying the metadata tables, please see the `ISB-CGC Community Notebook GitHub Repository <https://github.com/isb-cgc/Community-Notebooks>`_. If you have used the GDC portal to create cohorts or file lists, you can follow `these <https://isb-cancer-genomics-cloud.readthedocs.io/en/lauren-staging-theme/sections/GDCTutorials/FromGDCtoISBCGC.html>`_ tutorials to bring that information into ISB-CGC for use.
