*********************
BigQuery SQL Cheat Sheet
*********************

If you're already familiar with programming, picking up BigQuery SQL will likely be quick. Concepts like variables and logical operators carry over nicely, making the transition straightforward. Even if you're new to programming, don't worry! BigQuery's SQL syntax is designed to be understandable, and with plenty of resources available, you can definitely learn to analyze large datasets effectively.

Here we provide a running cheat sheet of queries we use most commonly.

Conditionals
=======================
The WHERE clause in SQL can be used to subset a table by only returning rows that match a specific characteristic.

.. code-block:: sql
  SELECT
    submitter_id,
    demo__age_at_index,
    demo__vital_status
  FROM `isb-cgc-bq.TCGA_versioned.clinical_gdc_r31`
  WHERE demo__age_at_index <= 80


Basic math functions
=======================
A query to perform a simple calculation, note that it is aggregating rows with the GROUP BY functionality for selecting which values to average. There are more functions built natively into BigQuery such as MAX, STDDEV, VARIANCE etc.

.. code-block:: sql
  SELECT
    sample_type_name,
    AVG(fpkm_uq_unstranded) avg_fpkm
  FROM `isb-cgc-bq.TCGA_versioned.RNAseq_hg38_gdc_r35`
  GROUP BY sample_type_name


Joining data between tables
=======================
A query to join data from two different tables. In this example it is joining the mutational status of each gene onto the corresponding row of expression data. Note that it uses both sample barcode and gene identifier as keys.

.. code-block:: sql
  SELECT
    rna.case_barcode, rna.sample_type_name, rna.gene_name,
    rna.fpkm_uq_unstranded, mut.HGVSc
  FROM `isb-cgc-bq.TCGA_versioned.masked_somatic_mutation_hg38_gdc_r35` mut
  JOIN `isb-cgc-bq.TCGA_versioned.RNAseq_hg38_gdc_r35` rna
    ON rna.sample_barcode = mut.sample_barcode_tumor 
    AND rna.Ensembl_gene_id = mut.Gene

Chaining queries
=======================
You may encounter instances where you wish to perform multiple operations in sequence without saving to an intermediate table. You can directly "pipe" the output similar to a bash shell. As an example maybe we wish to eliminate all genetic elements that have an average expression below a specific threshold from the query example above.

.. code-block:: sql
  SELECT 
    sample_type_name,
    AVG(fpkm_uq_unstranded) avg_fpkm
  FROM
    (SELECT
      sample_type_name,
      AVG(fpkm_uq_unstranded) avg_fpkm
    FROM `isb-cgc-bq.TCGA_versioned.RNAseq_hg38_gdc_r35`
    GROUP BY sample_type_name )
  WHERE avg_fpkm < 0



Working with nested fields
=======================
You may encounter "nested" fields in some of our tables. There are several methods for interacting with these fields, such as using the UNNEST() function to create individual rows for each value.

.. code-block:: sql
  SELECT
    PatientId, 
  FROM
    `bigquery-public-data.idc_v20.quantitative_measurements`
    UNNEST() AS 
