=======================================================
Linking BigQuery to ISB-CGC Project Open Access Data
=======================================================

To obtain access to the ISB-CGC project tables in BigQuery you must link these tables to your project so that they will show up in the left panel of your BigQuery web UI. 

When you access BigQuery from your Google Cloud Platform Console (see link `here <HowToAccessBigQueryFromTheGoogleCloudPlatform.html>`_ for more information on this), you will be presented with the following page:

.. image:: BlueArrowDropdown.PNG
   :align: center

The blue arrow will produce a drop down list; select 'Switch to Project'; then click 'display project...'

You will then be presented with the following page:

.. image:: SearchProjectSection.PNG
   :scale: 25
   :align: center

As shown in the image above you will need to type in "isb-cgc" in the project id and then click okay. 

.. image:: isb-cgc_pinned.PNG
   :scale: 25
   :align: center

Once this has been completed you will see all of the BigQuery datasets made public by the ISB-CGC project on the left hand side above public data sets (see screenshot below).

.. image:: ISB-CGCBiqQueryDatasets.png
   :scale: 25
   :align: center

