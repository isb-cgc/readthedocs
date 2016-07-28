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

Helpful BigQuery links
----------------------

For this example, we'll be working in the `Google BigQuery Web UI <https://bigquery.cloud.google.com>`_.

We've tried to simplify what you need to know to get started using the ISB-CGC BigQuery
tables in this quick
`visual walkthrough <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_BigQuery.pdf>`_.

It's often helpful to have a `link to the docs <https://cloud.google.com/bigquery/what-is-bigquery>`_ handy,
and especially the `query reference <https://cloud.google.com/bigquery/query-reference>`_.
(You'll probably want to open those into new tabs of your browser.)

Let's query!
------------

Please open the browser, and open the `BigQuery UI <https://bigquery.cloud.google.com>`_

On the left side, from top to bottom we have:

1.  **Compose Query** This button opens the text field, where we can write queries.

2.  **Query History** A list of your past queries... *very useful*.

3.  **Job History** List of past jobs, like copying tables.

4.  **Your Project Datasets** Click the little blue triangle to create a new data
    set or change projects.

5.  **isb-cgc** The TCGA data sets.

6.  **More data!** Added datasets will appear here. Such as the silver-wall-555 set.

Parts of a query
-------------------

BigQueries are very similar to regular SQL, with some differences.

We select some variables from tables, filter on some criteria, and occationally
aggregate the results (such as taking an average).

Here, we want all the associated barcodes for patients in the CESC and HNSC
studies. Note the use of the IN keyword.

.. code-block:: sql

	SELECT
	  Study,
	  ParticipantBarcode,
	  SampleType
	FROM
	  [isb-cgc:tcga_201510_alpha.Biospecimen_data]
	WHERE
	  Study IN ('CESC', 'HNSC')
	AND SampleType = 'Primary solid Tumor'


Let's suppose we want to add some biospecimen data. To do this we
join the clinical and biospecimen tables. Note the use of JOIN - ON.

.. code-block:: sql

	SELECT
	  b.ParticipantBarcode,
	  a.SampleBarcode,
	  a.Study,
	  a.SampleType,
	  a.avg_percent_tumor_cells,
	  b.hpv_status
	FROM
	  [isb-cgc:tcga_201510_alpha.Biospecimen_data] as a
	JOIN
	  [isb-cgc:tcga_201510_alpha.Clinical_data] as b
	ON
	  a.ParticipantBarcode = b.ParticipantBarcode
	  AND a.Study = b.Study
	WHERE
	    a.Study IN ('CESC','HNSC')
		AND a.SampleType = 'TP'
	GROUP BY
	  b.ParticipantBarcode,
	  a.SampleBarcode,
	  a.Study,
	  a.SampleType,
	  a.avg_percent_tumor_cells,
	  b.hpv_status


Another way to work with multiple tables is through creating sub-tables.
Here we are going to create a cohort of Patient Barcodes, filtering by
study and HPV status, and use that sub-table to filter down the
biospecimen table, finally computing an average of percent tumor cells.

.. code-block:: sql

    SELECT
      Study,
      SampleType,
      AVG(avg_percent_tumor_cells),
    FROM
      [isb-cgc:tcga_201510_alpha.Biospecimen_data]
    WHERE
      ParticipantBarcode IN (
      SELECT
        ParticipantBarcode
      FROM
        [isb-cgc:tcga_201510_alpha.Clinical_data]
      WHERE
        hpv_status = 'Positive'
        AND Study IN ('CESC',
          'HNSC') )
    GROUP BY
      Study,
      SampleType


Using aggregation functions
---------------------------

A beneficial goal is to keep as much computation on the BigQuery side
as possible. That means we want to aggregate and compute functions that
return summary data.

In this query, we're going to look at some summary statistics in the
clinical table.

.. code-block:: sql

    SELECT
      ParticipantBarcode,
      Study,
      gender,
      country,
      number_pack_years_smoked,
      number_pack_years_smoked - mu / sd AS z
    FROM
      [isb-cgc:tcga_201510_alpha.Clinical_data] AS a
    JOIN (
      SELECT
        vital_status,
        AVG(number_pack_years_smoked) AS mu,
        STDDEV(number_pack_years_smoked) AS sd
      FROM
        [isb-cgc:tcga_201510_alpha.Clinical_data]
      WHERE
        vital_status = 'Alive'
      GROUP BY
        vital_status ) AS b
    ON
      a.vital_status = b.vital_status
    ORDER BY
      z DESC


The results are ordered by Z score.

After we've run a query, there's some options. On the upper right side of the
returned results, we can download the table, or save it as a BigQuery table!

Making summary tables
---------------------

Another way to create summary information is by creating tables. With summary
tables, we can even compute statistics like a ChiSq.

.. code-block:: sql

	SELECT
	  table_cell,
	  COUNT(*)
	FROM (
	  SELECT
	    CASE WHEN gender = 'MALE' AND hpv_status = 'Positive' THEN 'Male_and_HPV_Pos'
	         WHEN gender = 'MALE' AND hpv_status = 'Negative' THEN 'Male_and_HPV_Neg'
	         WHEN gender = 'FEMALE' AND hpv_status = 'Positive' THEN 'Female_and_HPV_Pos'
	         WHEN gender = 'FEMALE' AND hpv_status = 'Negative' THEN 'Female_and_HPV_Neg'
	         ELSE 'None'
	    END AS table_cell,
	  FROM
	    [isb-cgc:tcga_201510_alpha.Clinical_data]
	  WHERE
	    Study IN ('CESC', 'HNSC')
	  HAVING
	    table_cell <> 'None' )
	GROUP BY
	  table_cell
