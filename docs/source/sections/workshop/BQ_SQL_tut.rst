**********************
BigQuery SQL Tutorial
**********************

Exploring the TCGA data in BigQuery
-----------------------------------

The ISB-CGC team has aggregated and curated the TCGA
open-access clinical, biospecimen, and Level-3 molecular data and uploaded it
into BigQuery tables that are open to the public.  In this tutorial, we will show you how
you can begin to work with these tables from the Google BigQuery Web UI.

Helpful BigQuery links
----------------------

For this example, we'll be working in the `Google BigQuery Web UI <https://bigquery.cloud.google.com>`_.

We've tried to simplify what you need to know to get started using the ISB-CGC BigQuery
tables in this quick `visual walkthrough <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_BigQuery.pdf>`_.

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

Let's start by working with one of the simplest tables, the Clinical_data table.
The format of a table name in BigQuery is <project_name>:<dataset_name>.<table_name>

Or more accurately "isb-cgc:tcga_201510_alpha.Clinical_data"

Let's start by just counting the number of records in the table. Paste the
following SQL into the text field, and hit *Run Query*.

.. code-block:: sql

	SELECT
	  COUNT(1)
	FROM
	  [isb-cgc:tcga_201510_alpha.Clinical_data]


The result returned from this query is just a single value: the number of unique patients (aka participants)
across all of the TCGA studies (aka tumor types).

For consistency, and to make it easy to work with multiple tables,
all of the TCGA molecular data tables contain the fields ParticipantBarcode and Study

.. code-block:: sql

	SELECT
	  Study,
	  COUNT(*) AS n
	FROM (
	  SELECT
	    ParticipantBarcode,
	    Study
	  FROM
	    [isb-cgc:tcga_201510_alpha.Clinical_data]
	  GROUP BY
	    ParticipantBarcode,
	    Study )
	GROUP BY
	  Study
	ORDER BY
	  n DESC


Number of rows returned by this query:  33

After we've run a query, there's some options. On the upper right side of the
returned results, we can download the table, or save it as a BigQuery table!

Creating Our Cohort
-------------------

Here, we want all the associated barcodes for patients in the CESC and HNSC
studies.

A nice feature, when constructing the query, is when the cursor is in the
text field, by clicking on a column name in the table schema window, the
column name is added to the query.

To construct this query, I'm going to use the Annotations table.

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


Let's suppose we want some biospecimen data on each sample. To do this we
could use our **IN** keyword as above, or easily join tables using barcodes.

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

Bonus!
------

An example on making tables.

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
