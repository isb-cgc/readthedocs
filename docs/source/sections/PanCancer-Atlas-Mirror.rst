*******************************
PanCancer Atlas BigQuery Data
*******************************

`The PanCancer BigQuery Mirror <https://bigquery.cloud.google.com/queries/pancancer-atlas>`_ -- produced in
collaboration with the `TCGA research network <https://cancergenome.nih.gov/>`_,
the `GDC <https://gdc.cancer.gov/>`_, and the `NCI <https://www.cancer.gov/>`_ -- provide
a new way to explore and understand the processes driving cancer.
The availability of PanCancer Atlas data in BigQuery enables easy integration of this
resource with other public datasets in BigQuery, including other
open-access datasets made available by the ISB-CGC
(see `this <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/data2/data_in_BQ.html>`_
and `that <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/Reference-Data.html>`_
for more details on other publicly accessible BigQuery datasets).

About
######

The Google BigQuery tables (`here <https://bigquery.cloud.google.com/queries/pancancer-atlas>`_) mirror the files shared by the PanCancer Atlas initiative on the `GDC <https://gdc.cancer.gov/about-data/publications/pancanatlas>`_.

For examples of usage, see `Community Notebooks <HowTos.html>`_.

Use of the tables in the Filtered dataset is suggested.

The Staging dataset are essentially unmodified uploads of the file data.  The Staging tables are universally annotated as appropriate with ParticipantBarcode, SampleBarcode, AliquotBarcode, SampleTypeLetterCode, SampleType and TCGA Study, and put in Annotated. Then the Annotated tables are filtered using the PanCancer Atlas whitelist. Those filtered tables are found in the Filtered dataset.

An exception is the (public)  *MC3 MAF file*, which is found in the  Annotated dataset.


Getting Started
###############

`Register a cloud project <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`_ for access to `BigQuery <https://cloud.google.com/bigquery/what-is-bigquery>`_ .

Adding the PanCancer Atlas tables to your workspace
###################################################

To add public BigQuery datasets and tables to your "view" in the `BigQuery web UI <https://bigquery.cloud.google.com/queries/pancancer-atlas>`_ you
need to know the name of the GCP project that owns the dataset(s).
To add the publicly accessible ISB-CGC datasets (project name: ``pancancer-atlas`` and ``isb-cgc``)
follow these steps_.

.. _steps: http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/progapi/bigqueryGUI/LinkingBigQueryToIsb-cgcProject.html

You should now be able to see and explore all of the PanCancer and ISB-CGC public datasets.
Clicking on the blue triangle next to a dataset name will open it and
show the list of tables in the dataset. Clicking on a table name will open up
information about the table in main panel, where you can
view the Schema, Details, or a Preview of the table.

Additional projects with public BigQuery datasets which you may want to explore (repeating
the same process will add these to your BigQuery side-panel) include genomics-public-data and
google.com:biggene.

Consider the ``isb-cgc:genomic_reference.SwissProt`` table;
a complete BigQuery table name has three components:

   * the first part of the name (isb-cgc) is the Google Cloud Platform (GCP) project name;
   * the second part (genomic_reference) is the dataset name; and
   * the third part (SwissProt) is the table name.


Troubleshooting
###############

After going through the registration process described above, there will be a short
delay before your Google identity is granted the necessary access to BigQuery and the PanCancer Atlas
data resources.  If you get an error when running the sample query in this section, please
wait 10-15 minutes and then try again. If you are still not successful, please
`verify <https://accounts.google.com/ForgotPasswd>`_
that the Google ID you have provided is a valid Google account.  If you are still not able
to run the sample query given below, please contact us at feedback@isb-cgc.org.


Interactive Web-based Exploration
#################################

Ready to query? Great! First see the pancancer-atlas:README, then follow the steps below to run your first BigQuery!

*Please note that some of the screen-shots on this page may be based on earlier versions of the PanCancer Atlas tables, but the sample SQL on this page has been updated (and tested) to query the latest PanCancer Atlas tables.*

* `login <https://accounts.google.com/Login>`_ to your Google account (`Chrome <https://www.google.com/chrome/browser/desktop/index.html>`_ is the preferred browser);
* go to the `BigQuery web UI <https://bigquery.cloud.google.com>`_  --  if you see a welcome screen inviting you to **Create a Project** then please do so;

Let's query using the MC3 somatic mutation table.

* click on the big red **COMPOSE QUERY** button in the upper left corner;
* click on the **Show Options**  button below the **New Query** text-box;
* un-check the **Use Legacy SQL** check-box (the bottom-most "option");
* click on the **Hide Options** button;
* paste the sample query below into the New Query text-box;
* within a second or two you should see a green circle with a check-mark below the lower-right-corner of the New Query text-box  --  if instead you see a red circle with an exclamation mark, click on it to see what your Syntax Error is;
* once you do have the green circle, you can click on it to see a message like: "Valid: This query will process 131 MB when run."
* to execute the query, click on **RUN QUERY** !


.. code-block:: sql

    WITH
      mutCounts AS (
      SELECT
        COUNT(DISTINCT(sample_barcode_tumor)) AS CaseCount,
        Hugo_Symbol,
        HGVSc
      FROM
        `pancancer-atlas.Annotated.mc3_v0_2_8_PUBLIC_maf`
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
        mutCounts )
    SELECT
      *
    FROM
      mutRatios
    WHERE
      CaseCount>=10
      AND ratio>=0.2
      AND HGVSc is not null
    ORDER BY
      ratio DESC

