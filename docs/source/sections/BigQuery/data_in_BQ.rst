************************
Data in BigQuery
************************

The information scattered over tens of thousands of XML and TSV files in two separate archives at the 
`NCI-GDC <https://gdc.cancer.gov/>`_ is provided in a 
*much more accessible* form in a series of *open-access* BigQuery tables.  
For more details, including tutorials, SQL, 
and code examples in Python or R, 
please see our 
`Query of the Month <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/QueryOfTheMonthClub.html>`_ page and our
`Community Notebook Repository <https://github.com/isb-cgc/Community-Notebooks>`_.
Note that dbGaP authorization is **not** required to access these tables!

If you have suggestions or requests for additional data (*eg* TCGA isoform expression data,
or other reference data sources) that you would like to see made available as BigQuery tables,
please let us know (feedback@isb-cgc.org) and we will try to make that happen.

BigQuery Datasets and Tables
----------------------------

Data made available by the ISB-CGC through BigQuery is organized into several *open-access* 
datasets, where a dataset is made up of multiple tables.  
Datasets in BigQuery are uniquely identified based on the Google Cloud Platform (GCP) project name 
(in this case **isb-cgc**), and the dataset name, separated by a colon (or a period, in standard SQL), 
*eg* ``isb-cgc.TCGA_bioclin_v0``.  Tables are uniquely identified by appending the table name,
preceded by a period, *eg* ``isb-cgc.TCGA_bioclin_v0.Clinical``.

You can use the Google BigQuery graphical interface to query the BigQuery datasets.  To view and use these datasets, please see this `page <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/progapi/bigqueryGUI/LinkingISB-CGCtoCABQ.html>`_  for accessing controlled data in BigQuery or this `page <../../progapi/bigqueryGUI/LinkingBigQueryToIsb-cgcProject.html>`_ to view open access data in BigQuery.

Example of BigQuery Table Relationships
---------------------------------------

The diagram below illustrates some of the important relationships between our BigQuery tables. The yellow, red and blue nodes all represent tables in BigQuery.  The green nodes represent fields that are common to two or more tables and can be used in "JOIN" operations if you want to link information found in one table with relevant information found in another table.  These same fields may also be useful in "GROUP BY" operations.

The nodes are color-coded as follows:
  - **green** indicates a common field in the schemas of one or more tables
  - **red** indicates a TCGA table
  - **yellow** indicates a reference table (*eg* genomic or platform reference)
  - **blue** indicates a metadata table (*eg* file manifest, or other metadata)

All of the TCGA tables include patient, sample, and/or aliquot `barcodes <https://docs.gdc.cancer.gov/Encyclopedia/pages/TCGA_Barcode/>`_ on each row. (The actual field names are typically ``case_barcode``, ``sample_barcode``, or ``aliquot_barcode``.) Almost all of these tables also include a field called ``project_short_name`` which contains the TCGA tumor-type abbreviation (*eg* BRCA for breast cancer, GBM for glioblastoma multiforme, *etc*). Most of the molecular data tables include gene (or miRNA) symbols or identifiers, some include chromosomal coordinates, and some include both (*eg* the somatic mutation calls (SMC) table).

.. image:: figs/BQ-layout2b-20jul2016.png
   :scale: 75
   :align: center

..

If you want to map DNA methylation data onto copy-number data, you will need to perform multiple JOINs.  The figure below isolates these two specific TCGA data tables from the larger diagram above to make the relationships easier to see.

Both TCGA data tables (the red nodes) contain sample barcodes, allowing information from each table that pertains to the same sample to be merged into a single output row by a JOIN operation. However, neither the copy-number nor the methylation table schemas include a
field with a gene symbol which is another common way to JOIN one molecular data table to another. Instead, the methylation annotation table (yellow node) can be used to find the chromosomal coordinate for each methylation probe (by performing a JOIN operation on the probe id), and then the chromosomal coordinate of the probe can be used to find relevant copy-number segments in the copy-number table.

.. image:: figs/meth-to-cn-map.png
   :scale: 35
   :align: center

*Note: These diagrams of the relationships may change and grow as the data in BigQuery changes and grows through these diagrams can still be helpful to conceptualize the corresponding tables*

Additional Metadata
========================

Additional related metadata is organized into the following datasets:

- `isb-cgc.metadata <https://console.cloud.google.com/bigquery?folder&p=isb-cgc&d=metadata&page=dataset>`_:
  This dataset currently contains two tables which contain metadata about two additional
  TCGA data types: pathology and radiology images.  More information about these
  image datasets can be found on the 
  `TCGA-images <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/TCGA-images.html>`_ 
  documentation page.


- `isb-cgc.GDC_metadata <https://console.cloud.google.com/bigquery?folder&p=isb-cgc&d=GDC_metadata&page=dataset>`_:
  This dataset contains several tables which contain metadata describing the cases and
  files at the NCI-GDC, in both the legacy and the current data archives.


- `isb-cgc.tcga_seq_metadata <https://console.cloud.google.com/bigquery?folder&p=isb-cgc&d=tcga_seq_metadata&page=dataset>`_:
  This dataset contains several tables with metadata about the original hg19 sequence data
  (including both BAM and FASTQ files).
  The important common identifiers to link these tables back to other information is the ``CGHubAnalysisID``
  (which sometimes may be written ``CGHub_analysisID``).  In alphabetical order by name, these tables are:

   
- `isb-cgc.tcga_cohorts <https://console.cloud.google.com/bigquery?folder&p=isb-cgc&d=tcga_cohorts&page=dataset>`_: 
  This dataset contains a series of curated cohorts, one for each of the 33 TCGA tumor types, named 
  according to the tumor abbreviation, *eg* BRCA.  A "cohort" is defined as a paired list of case- 
  and sample-barcodes.  In order to be included, molecular data from at least one of the main platforms 
  must be available for that sample, and there must be no disqualifying annotation for that sample or 
  the case (aka patient).  For example, the 
  `BRCA cohort table <https://console.cloud.google.com/bigquery?folder&p=isb-cgc&d=tcga_cohorts&t=BRCA&page=table>`_ 
  contains 1086 unique cases and 2221 unique samples, but a query of the Clinical table for all 
  BRCA cases will return 1097 cases, and a similar query of the Biospecimen table for all 
  BRCA samples will return 2302 samples.  The Annotation table contains annotations of one type or 
  another for 122 "entities" in the TCGA-BRCA project affecting 33 BRCA cases, 2 BRCA samples, 18 BRCA analytes, 
  and 69 BRCA aliquots.


ETL (Extract, Transform, Load) Details 
=======================================

The data in the BigQuery tables is generally identical to the information that
can also be obtained from the NCI-GDC, but for users
interested in the nitty-gritty details, information is provided here about the ETL
(extract, transform and load) steps that were performed for each of the data types.

Before we go into data-type-specific details, a few general notes on
formatting and data curation:

-  All data uploaded into ISB-CGC BigQuery tables use a consistent
   UTF-8 character set. If the encoding of a character from
   the original file could not be detected, that character was ignored.
   Character encodings were detected using the Python
   library `Chardet <https://pypi.org/project/chardet/>`_.

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

Data-Type Specific ETL Details
******************************

.. toctree::
   :maxdepth: 1

   ETL/ETL_Clinical
   ETL/ETL_Biospecimen
   ETL/ETL_somaticMutations
   ETL/ETL_DNAcopyNumber
   ETL/ETL_DNAmethylation
   ETL/ETL_mRNAexpression
   ETL/ETL_microRNAexpression
   ETL/ETL_proteinExpression
   ETL/ETL_annotations

