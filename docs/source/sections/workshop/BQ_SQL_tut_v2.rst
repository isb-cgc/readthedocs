**********************
BigQuery SQL Tutorial
**********************

Exploring the TCGA data in BigQuery
-----------------------------------

The ISB-CGC team has aggregated and curated the TCGA
open-access clinical, biospecimen, and Level-3 molecular data and uploaded it
into BigQuery tables that are open to the public. Additional tables have been
added to open up new analysis options.

In this tutorial, we will show you how you can begin to work with these tables
from the Google BigQuery Web UI. 

**Note** that in order to use BigQuery,
you *must* have access to (*ie* be a member of) a GCP project.

Helpful BigQuery links
----------------------

For this example, we'll be working in the `Google BigQuery Web UI <https://bigquery.cloud.google.com>`_.

We've tried to simplify what you need to know to get started using the ISB-CGC BigQuery
tables in this quick
`visual walkthrough <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_BigQuery.pdf>`_.

It's often helpful to have a `link to the docs <https://cloud.google.com/bigquery/what-is-bigquery>`_ handy,
and especially the `query reference <https://cloud.google.com/bigquery/query-reference>`_.
(You'll probably want to open those into new tabs of your browser, for easy access.)

Let's query!
------------

In your browser, go to the `BigQuery Web UI <https://bigquery.cloud.google.com>`_

On the left side, from top to bottom we have:

1.  **Compose Query** This button opens the **New Query** text box, where we can write queries.

2.  **Query History** A list of your past queries... *very useful*.

3.  **Job History** A list of past jobs (*eg* copying or creating tables).

4.  **Your Project Datasets** Click the little blue triangle to create a new dataset or change projects.  

5.  **isb-cgc** Publicly accessible ISB-CGC curated datasets (including TCGA and reference data sources).

6.  **More data!** Other added datasets will appear here (for example, the **genomics-public-data**, *etc*).

**Note**: if you do not see the **isb-cgc** datasets, you need to add them to your "view" by clicking on the blue arrow next to your project name at the top of the left side-bar, select "Switch to Project", then "Display Project...", and enter "isb-cgc" (without quotes) in the text box labeled "Project ID".  All ISB-CGC public BigQuery datasets and tables will now be visible in the left side-bar of the BigQuery web interface.  You can repeat this process for other public datasets.

Querying: Lists, Joins, and Subqueries
--------------------------------------

BigQueries are very similar to regular SQL, but with some differences.  (Note: you can now `enable standard SQL <https://cloud.google.com/bigquery/sql-reference/enabling-standard-sql>`_ in BigQuery.)

Typically, we select some variables (aka "fields") from one or more tables, filter on some criteria,
and occasionally aggregate the results (such as taking an average).

In this first simple example, we are asking for the
barcodes for all casess in the CESC and HNSC
diseases, with an associated "primary solid tumor" sample. Note the use of the **IN** keyword.

.. code-block:: sql

	SELECT
	  project_short_name,
	  case_barcode,
	  Sample_Type_name
	FROM
	  [isb-cgc:TCGA_bioclin_v0.Biospecimen]
	WHERE
	  project_short_name IN ('TCGA-CESC', 'TCGA-HNSC')
	  AND Sample_Type_name = 'Primary solid Tumor'

Go ahead and cut and paste the above query directly into the New Query box,
and then click the red **Run Query** button.

Next, let's suppose we want to bring in some information that is available in the Clinical_data table.
To do this we need to JOIN the clinical and biospecimen tables using the SQL **... JOIN ... ON ...** construct.

.. code-block:: sql

		SELECT
		  b.case_barcode,
		  a.Sample_Barcode,
		  a.project_short_name,
		  a.Sample_Type_name,
		  a.avg_percent_tumor_cells,
		  b.hpv_status
		FROM (
		  SELECT
		    case_barcode,
		    Sample_Barcode,
		    project_short_name,
		    Sample_Type_name,
		    avg_percent_tumor_cells
		  FROM
		    [isb-cgc:TCGA_bioclin_v0.Biospecimen]
		  WHERE
		    project_short_name IN ('TCGA-CESC',
		      'TCGA-HNSC')
		    AND Sample_Type_name='Primary solid Tumor' ) AS a
		JOIN (
		  SELECT
		    case_barcode,
		    hpv_status
		  FROM
		    [isb-cgc:TCGA_bioclin_v0.Clinical] ) AS b
		ON
		  a.case_barcode = b.case_barcode
		GROUP BY
		  b.case_barcode,
		  a.Sample_Barcode,
		  a.project_short_name,
		  a.Sample_Type_name,
		  a.avg_percent_tumor_cells,
		  b.hpv_status
		  
		  
If you're really paying attention, you might notice that the first query returned
836 case barcodes from the Biospecimen_data table, but the second one returned only
835 participant and sample barcodes.  In a few cases, the Biospecimen_data table
contains information about samples that have no associated information in the Clinical_data
table, and the "JOIN" operation is by default an *INNER* JOIN which returns only the
*intersection* of the two tables being joined.

Another way to work with multiple tables is by using subqueries.
In the example below, we have an *inner* query (the middle
seven lines set off by blank space) which creates a "cohort" on the fly,
filtering by study and HPV status from the Clinical_data table.
We then use that sub-table to filter the Biospecimen_data table,
where we compute the average of the percent tumor cells, also counting
how many rows went into each average, grouped according to SampleType,
and then finally we sort by n.

.. code-block:: sql

	SELECT
	  project_short_name,
	  Sample_Type_name,
	  AVG(avg_percent_tumor_cells) AS avgPctTumor,
	  COUNT(*) AS n
	FROM
	  [isb-cgc:TCGA_bioclin_v0.Biospecimen]
	WHERE
	  case_barcode IN (

	  SELECT
	    case_barcode
	  FROM
	    [isb-cgc:TCGA_bioclin_v0.Clinical]
	  WHERE
	    hpv_status = 'Positive'
	    AND project_short_name IN ('TCGA-CESC', 'TCGA-HNSC')

          )
	GROUP BY
	  project_short_name,
	  Sample_Type_name
	ORDER BY
	  n DESC


Computing Statistics
---------------------------

A beneficial goal is to keep as much computation on the BigQuery side
as possible. That means we want to aggregate and compute functions that
return summary data.

In this query, we're going to look at some summary statistics in the
clinical table.

.. code-block:: sql

    SELECT
      case_barcode,
      project_short_name,
      sex,
      country,
      number_pack_years_smoked,
      (number_pack_years_smoked - mu) / sd AS z
    FROM
      `isb-cgc.TCGA_bioclin_v0.Clinical_View` AS a
    JOIN (
      SELECT
        vital_status,
        AVG(number_pack_years_smoked) AS mu,
        STDDEV(number_pack_years_smoked) AS sd
      FROM
        `isb-cgc.TCGA_bioclin_v0.Clinical_View`
      WHERE
        vital_status = 'Alive'
      GROUP BY
        vital_status ) AS b
    ON
      a.vital_status = b.vital_status
    ORDER BY
      z DESC


The results from this query are ordered by Z score

After running a query, there are several options in the bottom **Results** panel.
You can get an "Explanation" showing how the query was broken into multiple Stages,
the number of input and outputs from each stage, and the amount of time spent
reading, computing, *etc*.  In addition, you can Download or Save the Results in various ways,
including as a new BigQuery Table.
If your query will return a large number of results, you may need to click the
**Show Options** button to the right of the **Run Query** button and specific a
"Destination Table" and then turn on the "Allow Large Results" option.

Making Summary Tables
---------------------

Another way to create summary information is by creating tables of counts as shown below.
With summary tables, we can even compute statistics like a ChiSq.

.. code-block:: sql

	SELECT
	  table_cell,
	  COUNT(*) AS n
	FROM (
	  SELECT (
	    CASE
              WHEN gender = 'MALE' AND hpv_status = 'Positive' THEN 'Male_and_HPV_Pos'
              WHEN gender = 'MALE' AND hpv_status = 'Negative' THEN 'Male_and_HPV_Neg'
              WHEN gender = 'FEMALE' AND hpv_status = 'Positive' THEN 'Female_and_HPV_Pos'
              WHEN gender = 'FEMALE' AND hpv_status = 'Negative' THEN 'Female_and_HPV_Neg'
              ELSE 'None'
            END ) AS table_cell,
	  FROM
	    [isb-cgc:TCGA_bioclin_v0.Clinical]
	  WHERE
	    project_short_name IN ('TCGA-CESC',
	      'HNSC')
	  HAVING
	    table_cell <> 'None' )
	GROUP BY
	  table_cell
	ORDER BY
	  n DESC


LiftOver from hg19 to hg38
==========================

Suppose you want to work with the newer hg38 reference. We can use BigQuery to
perform the liftOver operation on the methylation probe coordinates using a 
simple JOIN query.  (This query takes approx 25s and produces an output table
with one row for each of the input rows in the input annotation table.)

.. code-block:: sql

    SELECT
      a.probeID AS Illumina_probeID,
      a.hg19_chr AS hg19_chr,
      a.hg19_pos AS hg19_pos,
      b.hg38_chr AS hg38_chr,
      b.hg38_pos AS hg38_pos
    FROM (
      SELECT
        IlmnID AS probeID,
        CHR AS hg19_chr,
        MAPINFO AS hg19_pos
      FROM
        [isb-cgc:platform_reference.methylation_annotation] ) a
    LEFT OUTER JOIN EACH (
      SELECT
        LTRIM(hg19_ref,"chr") AS hg19_chr,
        hg19_pos,
        LTRIM(hg38_ref,"chr") AS hg38_chr,
        hg38_pos
      FROM
        [isb-cgc:genome_reference.liftOver_hg19_to_hg38] ) b
    ON
      a.hg19_chr=b.hg19_chr
      AND a.hg19_pos=b.hg19_pos


