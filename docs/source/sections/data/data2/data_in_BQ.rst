*********************
TCGA Data in BigQuery
*********************

The information scattered over tens of thousands of XML and TSV files at the DCC is provided in a *much more accessible* form in
a series of BigQuery tables.  For more details, including tutorials and code examples in 
`Python <https://github.com/isb-cgc/examples-Python>`_ or 
`R <https://github.com/isb-cgc/examples-R>`_, please see our `github repositories <https://github.com/isb-cgc>`_.

This `introductory tutorial <https://github.com/isb-cgc/examples-Python/blob/master/notebooks/The%20ISB-CGC%20open-access%20TCGA%20tables%20in%20BigQuery.ipynb>`_
gives a great overview of all of the tables and pointers on how to get started exploring them.  Be sure to check it out!


ETL for BigQuery Tables
#######################

The open-access TCGA data has been uploaded into a set of consistent tables
in the publicly-accessible BigQuery dataset called ``isb-cgc:tcga_201510_alpha``,
`tables <https://bigquery.cloud.google.com/dataset/isb-cgc:tcga_201510_alpha>`_
which can be accessed
via the BigQuery web interface (by anyone with an active GCP project).

In general, the data in the BigQuery tables is identical to the information that
you can also access via the TCGA Data Coordinating Center (DCC)
`Data Portal <https://tcga-data.nci.nih.gov/tcga/>`_, 
but for users
interested in the nitty-gritty details, information is provided here about the ETL
(extract, transform and load) steps that were performed for each of the data types.

Before we go into data-type-specific details, a few general notes on
formatting and data curation:

-  All data uploaded into ISB-CGC BigQuery tables use a consistent
   UTF-8 character set. If the encoding of a character from
   the original file could not be detected, that character was ignored.
   Character encodings were detected using the Python
   library `Chardet <https://www.google.com/url?q=https://pypi.python.org/pypi/chardet&sa=D&usg=AFQjCNEqIpFiwf3f-ynJmNtP1ZqXe-TvRg>`_.
-  All missing information value strings such as: ``none``, ``None``,
   ``NONE``, ``null``, ``Null``, ``NULL``, , ``NA``, ``\_\_UNKNOWN\_\_``, ``<blank>``
   , and ``?``; are represented as NULL values in the BigQuery
   tables (or may not appear at all, depending on the table schema).
-  Numbers are stored as integer or floating point values.  The original ASCII
   files sometimes used scientific notation or included comma separators, but
   these are not preserved in the BigQuery tables.
-  End of File (EOF) and End of Line (EOL) delimiters, including
   CTRL-M characters, were all removed when the raw files were originally parsed.
-  Single and double quotes around the values were removed, but in cases where
   there were quotation marks within a string, they were not removed.
-  Whenever necessary, the SDRF file (in the mage-tab archive associated with each
   data archive) was parsed to find the correct association between the
   aliquot barcode and the Level-3 data file(s).

Major Data Types
################

.. toctree::
   :maxdepth: 1

   ETL_Clinical
   ETL_Biospecimen
   ETL_somaticMutations
   ETL_DNAcopyNumber
   ETL_DNAmethylation
   ETL_mRNAexpression
   ETL_microRNAexpression
   ETL_proteinExpression
   ETL_annotations

