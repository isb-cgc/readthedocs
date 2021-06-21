*******************************
Pan-Cancer Atlas BigQuery Data
*******************************

`The Pan-Cancer Atlas BigQuery data set <https://console.cloud.google.com/bigquery?page=dataset&d=pancancer_atlas&p=isb-cgc-bq&redirect_from_classic=true>`_ was produced in
collaboration with the `TCGA research network <https://cancergenome.nih.gov/>`_,
the `GDC <https://gdc.cancer.gov/>`_, and the `NCI <https://www.cancer.gov/>`_. This rich data set allows for an integrated examination of the full set of tumors characterized in the robust TCGA dataset and provides a new way to explore and analyze the processes driving cancer.

The availability of Pan-Cancer Atlas data in BigQuery enables easy integration of this resource with other public data sets in BigQuery, including other open-access datasets made available by the ISB-CGC
(see `this <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/Hosted-Data.html>`_
and `that <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/Reference-Data.html>`_
for more details on other publicly accessible BigQuery data sets).

About Pan-Cancer Atlas Data
###########################

The Pan-Cancer Atlas BigQuery tables  (`accessed here <https://console.cloud.google.com/bigquery?page=dataset&d=pancancer_atlas&p=isb-cgc-bq&redirect_from_classic=true>`_) mirror most of the files shared by the Pan-Cancer Atlas initiative on the `GDC PanCanAtlas Publications page <https://gdc.cancer.gov/about-data/publications/pancanatlas>`_.

The tables are generally unmodified uploads of the files in the `GDC Pan-Cancer Atlas <https://gdc.cancer.gov/about-data/publications/pancanatlas>`_. The Filtered_* tables were annotated as appropriate with ParticipantBarcode, SampleBarcode, AliquotBarcode, SampleTypeLetterCode, SampleType and TCGA Study. Subsequently the tables were filtered using the Pan-Cancer Atlas whitelist (which is the list of TCGA barcodes included in the Pan-Cancer Atlas). Two exceptions are the (public) *MC3 MAF file* and the *TCGA-CDR resource*. 

Use of the tables starting with Filtered_* is recommended.

See examples of statistical Jupyter notebooks using the Pan-Cancer Atlas data `here <https://github.com/isb-cgc/Community-Notebooks/tree/master/RegulomeExplorer>`_.

Adding the Pan-Cancer Atlas tables to your workspace
####################################################

If you are new to using ISB-CGC Google BigQuery data sets, see the `Quickstart Guide <HowToGetStartedonISB-CGC.html>`_ to learn how to obtain a Google identity and how to set up a Google Cloud Project.

To add public BigQuery data sets and tables to your "view" in the `Google BigQuery Console <https://bigquery.cloud.google.com/dataset/isb-cgc-bq:pancancer_atlas>`_ you need to know the name of the GCP project that owns the dataset(s). 
To add the publicly accessible ISB-CGC datasets (project name: ``isb-cgc-bq``) which includes the Pan-Cancer Atlas data set ( dataset name: ``pancancer_atlas``) 
follow these steps_.  (Note that these tables also exist in project ``isb-cgc``, but that ISB-CGC is migrating current data to project ``isb-cgc-bq``. If you are using the pancancer_atlas tables in ``isb-cgc``, they are still available for you.)

.. _steps: http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/progapi/bigqueryGUI/LinkingBigQueryToIsb-cgcProject.html

You should now be able to see and explore all of the Pan-Cancer Atlas tables and also tables of other ISB-CGC data sets.
Clicking on the blue triangle next to a dataset name will open it and show the list of tables in the data set. Clicking on a table name will open up information about the table in main panel, where you can view the Schema, Details, or a Preview of the table.

Additional projects with public BigQuery data sets which you may want to explore (repeating
the same process will add these to your BigQuery side-panel) include genomics-public-data and
google.com:biggene.

You can also search for and learn about Pan-Cancer Atlas tables through the `ISB-CGC BigQuery Table Search UI <https://isb-cgc.appspot.com/bq_meta_search/>`_. Type 'pancancer' in the **Search** box in the upper right-hand corner to filter for them.

Pan-Cancer Atlas BigQuery Query Example
#######################################

Ready to query? Follow the steps below to run a query in the Google BigQuery Console. More details are `here <https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui>`_.

* `Login <https://accounts.google.com/Login>`_ to your Google account (`Chrome <https://www.google.com/chrome/browser/desktop/index.html>`_ is the preferred browser);
* Go to the `BigQuery Console <https://console.cloud.google.com/bigquery?page=dataset&d=pancancer_atlas&p=isb-cgc-bq&redirect_from_classic=true>`_. 

Let's query using the MC3 somatic mutation table.

* Click on **COMPOSE NEW QUERY** button.
* Paste the sample query below into the text-box. 
* Within a second or two you should see a green circle with a checkmark below the lower right corner of the New Query text-box.  --  If instead you see a red circle with an exclamation mark, click on it to see what your Syntax Error is.
* Once you do have the green circle, you can click on it to see a message like: "Valid: This query will process 76.3 MB when run."
* To execute the query, click on **RUN**!


.. code-block:: sql

 WITH
 mutCounts AS (
   SELECT
      COUNT(DISTINCT( Tumor_SampleBarcode )) AS CaseCount,
      Hugo_Symbol,
      HGVSc
   FROM
      `isb-cgc-bq.pancancer_atlas.Filtered_MC3_MAF_V5_one_per_tumor_sample`
   GROUP BY
      Hugo_Symbol,
      HGVSc
 ),
 mutRatios AS (
   SELECT
      HGVSc,
      Hugo_Symbol,
      CaseCount,
      (CaseCount/SUM(CaseCount) OVER (PARTITION BY Hugo_Symbol)) AS ratio
   FROM
      mutCounts 
 )
 SELECT  *
 FROM
    mutRatios
 WHERE
    CaseCount>=10
    AND ratio>=0.2
    AND HGVSc is not null
 ORDER BY
    ratio DESC
