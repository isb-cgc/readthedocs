#################################################
ISB-CGC BigQuery Table Search Release Notes
#################################################

To learn about this discovery tool created by the ISB-CGC, please visit `ISB-CGC BigQuery Table Search <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/BigQueryTableSearchUI.html>`_.

For more detailed information about the data stored in ISB-CGC BigQuery tables please visit `ISB-CGC BigQuery Tables <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/BigQuery.html>`_.

*December 8, 2020* v1.04

**New Features**
 
- On the Filter panel, under Show More Filters, a filter BQ Project has been added. It has also been added to the Column selection dropdown list.

**Bug Fixes**

- On multi-select filters (Program, Source, Data Type, Experimental Strategy), the X button to delete the selected value did not completely display. It has been fixed so that the entire X button displays.

*July 23, 2020* v1.03

**New Features**
 
- The Access filter has been added, which has options of All, Open Access and Controlled Access. Controlled Access data cannot be previewed, but can be opened in the Google BigQuery Console, if the user has the required permissions.

*March 11, 2020* v1.02

**New Features**
 
- Users now have the ability to access, query and inspect in detail BigQuery tables in Google Cloud Platform's BigQuery console directly from the Table Search UI. Every table has a "Open" option which when clicked will send the user to the table in the BigQuery console on the Google Cloud. 
- An Open button, with the same functionality as described above, has been added to the Schema Description section.
- Program and Experimental Strategy filters were added. 
- Values for the Data Type and Source filters have been modified in order to align more closely with GDC naming conventions. 

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

The ISB-CGC BigQuery Table Search UI is a discovery tool that allows users to explore and search for ISB-CGC hosted BigQuery tables. It can be accessed directly from the ISB-CGC homepage.

Major features in the initial release include:

- The ability to search for BigQuery tables by multiple filters:
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
- Display of search results in a tabular format, with the following information about BigQuery tables:
 - Dataset ID
 - Table ID 
 - Status 
 - Source
 - Data Type
 - Num Rows
 - Created Date
- Detailed schema information for each table, including full table ID, table description, and field descriptions.
- The ability to preview the first eight rows in the BigQuery table of choice. 
- The ability to download a CSV format file of search results.

