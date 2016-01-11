DNA Copy-Number Segments
========================

Each individual CNV Level-3 data archive has 4 output files - two based on the hg18 reference, and two based on the hg19 reference. 
The BigQuery `table <https://www.google.com/url?q=https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Copy_Number_segments&sa=D&usg=AFQjCNHs3vCBx_G7ls1NlgFYHwoBj1-xfw>`__ is populated only with the files ending with "nocnv\_hg19.seg.txt". 
The "num_probes: and "segment_mean" in the raw files is sometimes represented in Exponential Scientific Notation (8.7E+07) and are converted to INT or FLOAT values.

Formatting
----------

-  "num_probes" column values are stored as integer values in BigQuery
   tables. Exponential Scientific notation is not used to represent the
   integers.
-  "segment_mean" column values are formatted to 4 point float values.
   Values represented in Exponential Scientific notation in the raw
   files are converted to float values.
-  The aliquot barcode information was obtained from the SDRF file
   associated with the Level-3 data file.

