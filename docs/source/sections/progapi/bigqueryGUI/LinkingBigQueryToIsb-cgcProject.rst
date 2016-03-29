=======================================================
Linking Big Query to ISB-CGC Project
=======================================================

To obtain access to the ISB-CGC project tables in big query you must link your account to ISB-CGC. 

Upon access Big Query from your Google Cloud Platform Console (see link `here <HowToAccessBigQueryFromTheGoogleCloudPlatform.rst>`_ for more information on this), you will be presented with the following page:

.. image:: BlueArrowDropdown.png
   :scale: 50
   :align: center

The blue arrow will produce a drop down list the ISB-CGC user will click 'Switch to Project'. Under this the user will then click 'display project...'

You will then be presented with the following page:

.. image:: AddISB-CGCProject.png
   :scale: 50
   :align: center

As shown in the image above you will type in "isb-cgc" in the project id then click okay. 

Once this has been completed the user will then see all of the buckets associated with isb-cgc on the left hand side above public data sets (see screenshot below).

.. image:: ISB-CGCBiqQueryDatasets.png
   :scale: 50
   :align: center

================================================
Other Genomics BigQuery Data Available on Google
================================================

Google has made available in BigQuery other genomics datasets that can be used in joins with the ISB-CGC datasets we provide.  The current list can be found `here <https://googlegenomics.readthedocs.org/en/latest/use_cases/discover_public_data/index.html>`_.  

It is possible that not all the datasets provided on this page have BigQuery data.  You can find that out by opening up that link for each dataset and seeing if there is a section called "Google BigQuery Dataset ID(s)".  If there is, you can make these available through your Google console by the same process as you did for the ISB-CGC datasets above.
