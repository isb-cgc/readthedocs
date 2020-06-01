*******************************
PanCancer Atlas BigQuery Data
*******************************

`The PanCancer BigQuery Mirror <https://console.cloud.google.com/bigquery?project=isb-cgc&page=dataset&d=pancancer_atlas&p=isb-cgc&redirect_from_classic=true>`_ -- produced in
collaboration with the `TCGA research network <https://cancergenome.nih.gov/>`_,
the `GDC <https://gdc.cancer.gov/>`_, and the `NCI <https://www.cancer.gov/>`_ -- allows an integrated examination of the full set of tumors characterized in the robust TCGA dataset, thus providing a new way to explore and analyze the processes driving cancer.

The availability of PanCancer Atlas data in BigQuery enables easy integration of this
resource with other public datasets in BigQuery, including other
open-access datasets made available by the ISB-CGC
(see `this <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/Hosted-Data.html>`_
and `that <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/Reference-Data.html>`_
for more details on other publicly accessible BigQuery datasets).

About
#####

The Google BigQuery tables (`here <https://console.cloud.google.com/bigquery?project=isb-cgc&page=dataset&d=pancancer_atlas&p=isb-cgc&redirect_from_classic=true>`_) mirror the files shared by the PanCancer Atlas initiative on the `GDC <https://gdc.cancer.gov/about-data/publications/pancanatlas>`_.

The tables are generally unmodified uploads of the files in `GDC <https://gdc.cancer.gov/about-data/publications/pancanatlas>`_. The Filtered_* tables were annotated as appropriate with ParticipantBarcode, SampleBarcode, AliquotBarcode, SampleTypeLetterCode, SampleType and TCGA Study, subsequently the tables were filtered using the PanCancer Atlas whitelist. Two exceptions are the (public) *MC3 MAF file* and the *TCGA-CDR resource*, recommended for outcome data. 

Use of the tables starting with Filtered_* is recommended.

For examples of usage, see `Community Notebooks <https://github.com/isb-cgc/Community-Notebooks/tree/master/RegulomeExplorer>`_.

Getting Started
###############

`Register a cloud project <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`_ for access to `BigQuery <https://cloud.google.com/bigquery/what-is-bigquery>`_ .

Adding the PanCancer Atlas tables to your workspace
###################################################

To add public BigQuery datasets and tables to your "view" in the `BigQuery web UI <https://bigquery.cloud.google.com/dataset/isb-cgc:pancancer_atlas>`_ you
need to know the name of the GCP project that owns the dataset(s). 
To add the publicly accessible ISB-CGC datasets (project name: ``isb-cgc``) which included the PanCancer Atlas dataset ( dataset name: ``pancancer_atlas``) 
follow these steps_.

.. _steps: http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/progapi/bigqueryGUI/LinkingBigQueryToIsb-cgcProject.html

You should now be able to see and explore all of the PanCancer Atlas tables and also tables of other ISB-CGC datasets.
Clicking on the blue triangle next to a dataset name will open it and
show the list of tables in the dataset. Clicking on a table name will open up
information about the table in main panel, where you can
view the Schema, Details, or a Preview of the table.

Additional projects with public BigQuery datasets which you may want to explore (repeating
the same process will add these to your BigQuery side-panel) include genomics-public-data and
google.com:biggene.


Interactive Web-based Exploration
#################################

Ready to query? Great! follow the steps below to run your first BigQuery! More detailas `here <https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui>`_

* `login <https://accounts.google.com/Login>`_ to your Google account (`Chrome <https://www.google.com/chrome/browser/desktop/index.html>`_ is the preferred browser);
* go to the `BigQuery web UI <https://console.cloud.google.com/bigquery?project=isb-cgc&page=dataset&d=pancancer_atlas&p=isb-cgc&redirect_from_classic=true>`_  --  if you see a welcome screen inviting you to **Create a Project** then please do so.

Let's query using the MC3 somatic mutation table.

* click on **COMPOSE NEW QUERY** button;
* paste the sample query below into the text-box. 
* within a second or two you should see a green circle with a check-mark below the lower-right-corner of the New Query text-box  --  if instead you see a red circle with an exclamation mark, click on it to see what your Syntax Error is;
* once you do have the green circle, you can click on it to see a message like: "Valid: This query will process 76.3 MB when run."
* to execute the query, click on **RUN** !


.. code-block:: sql

 WITH
 mutCounts AS (
   SELECT
      COUNT(DISTINCT( Tumor_SampleBarcode )) AS CaseCount,
      Hugo_Symbol,
      HGVSc
   FROM
      `isb-cgc.pancancer_atlas.Filtered_MC3_MAF_V5_one_per_tumor_sample`
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


Troubleshooting
###############

After going through the registration process described above, there will be a short
delay before your Google identity is granted the necessary access to BigQuery and the PanCancer Atlas
data resources.  If you get an error when running the sample query in this section, please
wait 10-15 minutes and then try again. If you are still not successful, please
`verify <https://accounts.google.com/ForgotPasswd>`_
that the Google ID you have provided is a valid Google account.  If you are still not able
to run the sample query given below, please contact us at feedback@isb-cgc.org.
