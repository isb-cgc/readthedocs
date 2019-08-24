******************************
ISB-CGC BigQuery Data Overview
******************************

The diagram below illustrates some of the important relationships between our BigQuery tables. The yellow, red and blue nodes all represent tables in BigQuery.  The green nodes represent fields that are common to two or more tables and can be used in "JOIN" operations if you want to link information found in one table with relevant information found in another table.  These same fields may also be useful in "GROUP BY" operations.

The nodes are color-coded as follows:
  - **green** indicates a common field in the schemas of one or more tables
  - **red** indicates a TCGA table
  - **yellow** indicates a reference table (*eg* genomic or platform reference)
  - **blue** indicates a metadata table (*eg* file manifest, or other metadata)

All of the TCGA tables include patient, sample, and/or aliquot `barcodes <https://docs.gdc.cancer.gov/Encyclopedia/pages/TCGA_Barcode/>`_ on each row. (The actual field names are typically ``case_barcode``, ``sample_barcode``, or ``aliquot_barcode``.) Almost all of these tables also include a field called ``project_short_name`` which contains the TCGA tumor-type abbreviation (*eg* BRCA for breast cancer, GBM for glioblastoma multiforme, *etc*). Most of the molecular data tables include gene (or miRNA) symbols or identifiers, some include chromosomal coordinates, and some include both (*eg* the somatic mutation calls (SMC) table).

.. image:: data/figs/BQ-layout2b-20jul2016.png
   :scale: 75
   :align: center

..

If you want to map DNA methylation data onto copy-number data, you will need to perform multiple JOINs.  The figure below isolates these two specific TCGA data tables from the larger diagram above to make the relationships easier to see.

Both TCGA data tables (the red nodes) contain sample barcodes, allowing information from each table that pertains to the same sample to be merged into a single output row by a JOIN operation. However, neither the copy-number nor the methylation table schemas include a
field with a gene symbol which is another common way to JOIN one molecular data table to another. Instead, the methylation annotation table (yellow node) can be used to find the chromosomal coordinate for each methylation probe (by performing a JOIN operation on the probe id), and then the chromosomal coordinate of the probe can be used to find relevant copy-number segments in the copy-number table.

.. image:: data/figs/meth-to-cn-map.png
   :scale: 35
   :align: center

*Note: These diagrams of the relationships may change and grow as the data in BigQuery changes and grows through these diagrams can still be helpful to conceptualize the corresponding tables*
