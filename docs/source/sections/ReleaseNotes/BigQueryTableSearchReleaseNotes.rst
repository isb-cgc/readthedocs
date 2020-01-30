#################################################
ISB-CGC BigQuery Table Search Release Notes
#################################################

For more detailed information about this discovery tool's functionality created and implemented by the ISB-CGC please visit `ISB-CGC BigQuery Table Search <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/BigQueryTableSearchUI.html>`_.

For more detailed information about the data stored in ISB-CGC BigQuery tables please visit `ISB-CGC BigQuery Tables <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/BigQuery.html>`_.

*January 30,2020*

**New Features**

- A Friendly Name column has been introduced. The Full ID can be found using the detailed table information feature.
- The ability to search by Name on left search panel. 
- Copy Full ID into the BigQuery console or virtual machine using the copy button found in the detailed table information feature.
- Paste format of Full ID will contain grave accents(`) by default.
- Files downloaded using the CSV download feature will provide Full ID in the same format as the user interface e.g., SQL Standard format and with a grave accent(`).

**Enhancements**

- For files downloaded using the CSV download feature, it will have fields column in comma-separated format.



*November 26, 2019* `v1.0 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.21>`_

**Initial Release**

- Multiple filters introduced
 - Status 
 - Categories
 - Reference Genome Build
 - Source
 - Data Type
 - Dataset ID
 - Table ID
 - Table Description
 - Labels
 - Field Name
- Search results column headers introduced
 - Dataset ID
 - Table ID 
 - Status 
 - Source
 - Data Type
 - Num Rows
 - Created Date
- Search results provide a detailed table description, including full table ID, table description, and field descriptions.
- Search results also provide the ability to preview the first eight rows in the BigQuery table of choice. 
- The ability to download a CSV format file of search results.
- The ability to show 10, 25, 50, or 100 entries at a time.
