#################################################
ISB-CGC BigQuery Table Search Release Notes
#################################################

For more detailed information about this discovery tool's functionality created and implemented by the ISB-CGC please visit `ISB-CGC BigQuery Table Search <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/BigQueryTableSearchUI.html>`_.

For more detailed information about the data stored in ISB-CGC BigQuery tables please visit `ISB-CGC BigQuery Tables <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/BigQuery.html>`_.

*January 30,2020* `v1.01 <https://github.com/isb-cgc/ISB-CGC-Webapp/releases/tag/3.22>`_

**New Features**

- A "Name" column consisting of user-friendly descriptive names for the BigQuery tables has been introduced. 
- The Name filter, a free-form text search field is now available allowing users to search for all or a portion of the user-friendly descriptive names.
- Columns can be now added or removed from the display by using the Columns selector option. 
- By default, Dataset ID and Table ID are no longer initially displayed in the full column view, but can be added to the display using the columns selector. 
- The Full ID, which is denoted [projectID.datasetID.TableID] (concatenation of the project ID, dataset ID and the Table ID, each separated by a period symbol) is listed under the detailed table information section found after clicking on the blue plus sign. 
- A Copy button, found adjacent to the Full ID has been added. The Full ID adheres to BigQuery Standard SQL format and contains the necessary grave accents (`) required for executing SQL queries in BigQuery.  When copied to the clipboard, the Full ID can be directly used to run queries in BigQuery Query Editor without any further manual modifications. 

**Enhancements**

- Individual table schemas captured by the "Fields" column in the CSV download now contain field information in comma-separated format. 



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
