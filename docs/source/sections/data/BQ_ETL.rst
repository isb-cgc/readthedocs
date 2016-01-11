***********************
ETL for BigQuery Tables
***********************

Data Quality and General Formatting
###################################

-  All data uploaded into ISB-CGC BigQuery tables have a consistent
   UTF-8 character set formatting. If the encoding of a character from
   the raw files could not be detected, the characters are simply
   ignored. The character encodings are detected using the Python
   library `Chardet <https://www.google.com/url?q=https://pypi.python.org/pypi/chardet&sa=D&usg=AFQjCNEqIpFiwf3f-ynJmNtP1ZqXe-TvRg>`__.
-  All missing information value strings such as: 'none', 'None',
   'NONE', 'null', 'Null', 'NULL', , 'NA', '\_\_UNKNOWN\_\_', <empty
   spaces>, and '?'; are represented as NULL values in the BigQuery
   tables.
-  The numbers are stored as integer or float value columns, whenever
   possible. The scientific number format (e.g. 10E2) and thousand
   separator comma is not used in any of the number columns.
-  The End of File (EOF) and End of Line (EOL) delimiters, including
   CTRL-M characters, are removed while loading data into BigQuery.
-  Single and double quotes around the values are removed. The quotes
   within a value are not changed.
-  The SDRF file was parsed to find the correct association between the
   aliquot barcode and the Level-3 data file(s), wherever needed and
   possible.

Major Data Types
################

.. toctree::
   :maxdepth: 1

   data2/ETL_Clinical
   data2/ETL_Biospecimen
   data2/ETL_somaticMutations
   data2/ETL_DNAcopyNumber
   data2/ETL_DNAmethylation
   data2/ETL_mRNAexpression
   data2/ETL_microRNAexpression
   data2/ETL_proteinExpression

