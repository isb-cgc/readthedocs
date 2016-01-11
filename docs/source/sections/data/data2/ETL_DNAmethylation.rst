DNA Methylation
===============

The BigQuery
 \ `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.DNA_Methylation_betas&sa=D&usg=AFQjCNFuAXrnRbAzG0U4-f1uPmY8xC6gSQ>`__ \ is
populated only with the files matching the pattern -
%.HumanMethylation%.txt. The data from both 27k and 450k platform are
merged together into a single table. If there are samples that were run
on both platforms, then the 450k data takes precedence and the duplicate
27k data is removed from the table. The table has a platform column
indicating the name of the platform for each sample.

Filters
-------

-  Filter out rows with "Beta\_value" is NA or NULL.

Formatting
----------

-  Round "Beta\_value" to two digit float (e.g: 0.88). The original
   beta\_value is 14 digit precision floating number.

Output
------

-  Only "Probe\_Id", "Beta\_Value" from the data file are stored in the
   BigQuery table.
-  The aliquot barcode information was obtained from the SDRF file
   associated with the Level-3 data file.

