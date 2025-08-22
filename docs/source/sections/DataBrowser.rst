***********************************
Cancer Data Resource Browser
***********************************

The `Cancer Data Resource Browser <https://portal.isb-cgc.org/cohorts/filelist/>`_ is an ISB-CGC web interface which allows you to 
explore a comprehensive selection of cancer related data files and BigQuery tables available in the cloud, including raw sequencing, cancer nucleotide variation, and pathology or radiology images.

Selecting  **Cancer Data Resource Browser** from the **Data Browsers** drop down menu on the ISB-CGC home screen will display the **Cancer Data Resource Browser** screen. 
Another way to get to this screen is to click on the **Launch** icon in the **Cancer Data Resource Browser** box in the **Data Browsers** section of the ISB-CGC home page.

You will be able to use the available filters to select a resource record list. Click on the CSV button to download this list which includes barcodes and resource locations in GCS, AWS, and BigQuery without needing to log into the ISB-CGC Web Application. Except for the ability to save output results to a Google BigQuery table or to a Google Cloud Storage Bucket (GCS), this screen has the same functionality as the one that you navigate to when selecting  the **Resource Browser** button from the **Saved Cohorts** screen, 
after signing into the Web App. To learn more about this screen, see the `Cohorts Resource Browser documentation <webapp/Saved-Cohorts.html#file-browser>`_.

Note that the maximum number of file records that can be downloaded is 65000. You'll need to use the filters to get the file listing results below this number.

If you decide to log into the ISB-CGC Web App (using **Sign In** in the upper right-hand corner), you can register a Google Cloud Project and BigQuery data set and export the file record list to a BigQuery table or a Google Cloud Storage Bucket.

.. image:: webapp/DataBrowser-noSignIn.png
   :scale: 50
   :align: center
