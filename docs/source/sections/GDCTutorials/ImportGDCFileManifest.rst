Importing a GDC File Manifest into ISB-CGC
===========================================
  
The easiest way to make a GDC File manifest useful is to import it into BigQuery as its own table.  One way of keeping your file manifests organized is to create a data set specifically for the tables created to hold the manifests.  New data sets can be created by clicking on the **Create Dataset** button within your project in BigQuery.
  
Creating a table from a GDC file manifest is remarkably easy:
 
* Click on the **Create Table** button while you are within your new dataset.  
* In the resulting screen, for **Create table from**, select **Upload**. Select your manifest file and set the **File format** to **CSV**. (Tab delimited will work with this setting.)
* Have BigQuery automatically create the schema by checking the **Auto detect** box for Schema.
* Click on **Advanced options**. Select **Tab** for **Field delimiter**; enter **1** for **Header rows to skip**.
* Click on the **Create Table** button.
   
   
.. image:: BQ-CreateKidneyManifestTable.png


Now that you have a table containing the GDC file identifiers, the next step is to find the locations for the Level 1 files on the Google Cloud.  To help with that task, ISB-CGC maintains BiqQuery tables that contain the GDC file identifier and the Google bucket location for the file in data set GDC_metadata.  Adding the Google bucket location to our GDC information can be done via a very simple SQL query:

.. code-block:: sql

        SELECT gdc.*, isb.file_gdc_url
        FROM `kids-first-drc.GDC_Import.GDC_Kidney_File_manifest` as gdc,
             `isb-cgc.GDC_metadata.rel22_GDCfileID_to_GCSurl` as isb
        WHERE gdc.id = isb.file_gdc_id

Note that you'll need to replace "kids-first-drc.GDC_Import.GDC_Kidney_File_manifest" with your project and the data set and table that you created above.

This query will return the results shown below and, as with any BiqQuery result, you can either export it as a file or save it as a new table in BigQuery.


.. image:: BQ-Results-KidneyManifestURLTable.png

