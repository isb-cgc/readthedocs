-----------------------------------
Registering a Google Cloud Project
-----------------------------------
This section will show you how to register a Google Cloud Project (GCP), thereby gaining access to controlled data which you can use programmatically. Users need to have access to a Google Cloud Project to perform the steps in this section. If you don't, see the the  `ISB-CGC Quick-Start Guide <../HowToGetStartedonISB-CGC.html>`_.

To allow flexibility while working with different research teams and different processes, you can have many GCPs registered with ISB-CGC.

Registering your Google Cloud Project Service Account
--------------------------------------------------------------
Click on screen shots to enlarge them.

To register your Google Cloud Project and its service account with ISB-CGC, go to the Account Details page. After signing into the ISB-CGC Web App, 
either select the "persona" icon next to your login name or select **Account Details** from the drop down menu under your login name, 
which takes you to the following page:

.. image:: ../webapp/RegisteredGCPs.png
   :scale: 35
   :align: center
   
Click the **Register** button in the Google Cloud Platform section.  That takes you to the following page:

.. image:: ../webapp/RegisterAGCPForm.png
   :scale: 35
   :align: center
   
The instructions will walk you through how to add the necessary ISB-CGC and DCF service accounts to your project. Go to the `Google Cloud Platform <https://console.cloud.google.com/>`_ and follow these steps.
You can hide the instructions by selecting the blue **Instructions** button.  

Please be sure to add both service accounts listed below. If you don't add both service accounts you will run into issues viewing the controlled data in ISB-CGC.
Then return to the ISB-CGC Register a Google Cloud Project page, enter your Google Cloud Project ID and, click **Verify**.

.. image:: ../webapp/RegisterServiceAccountsList.png
   :scale: 35
   :align: center

Once you have completed these steps, a listing of the Google Cloud Project members will display:

.. image:: ../webapp/GCPMembers.png
   :scale: 50
   :align: center
   
Click the **Register** button to go to the next screen:

.. image:: ../webapp/0007projectregistered.PNG
   :scale: 35
   :align: center
   
Select **Register Service Account** from the drop down menu on the left of the GCP to which you want to add a service account.  By default, there will be the 
Compute Engine Default service account in the **Enter the service account ID** text box (see screenshot below).  Under **Which dataset(s) would you like to use?**, select the programs for which you would like to have controlled access.

.. image:: ../webapp/RegisterAServiceAccountFirstScreen.PNG
   :scale: 35
   :align: center

If you receive the error message listed below, this signifies you need to enable the Default Compute Engine API for your Google Cloud Project.  
For more information on how to enable all the API's you will need to work on a Google Cloud Project please go
`here <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/DIYWorkshop.html#enabling-required-google-apis>`_.

.. image:: ../webapp/EnableComputeEngineError.PNG
   :scale: 30
   :align: center

Once you click the **Verify Service Account Users** at the bottom of the page, you will be presented with multiple lists. You will be presented with the
Verification Results, Google Cloud Project User ISB-CGC Registration and Identity Linkages, Dataset Permissions Verification, Registered Service Account Verification
Results, Google Cloud Project Verification Results, and the Google Cloud Project Service Account Verification Results (see screenshots below). 
All columns must have a green checkmark in them for each user before your service account can be registered.

.. image:: ../webapp/ServiceAcctRegTable.png
   :scale: 30
   :align: center
   
.. image:: ../webapp/ServiceAcctRegTable2.png
   :scale: 30
   :align: center

If all the requirements for registering a service account are met, the account will be registered for controlled access.  If not, the service account can only use
open access data.  View the registered data set name by selecting the drop down menu next to the number of service accounts (see below).

.. image:: ../webapp/ServiceAcctRegSuccess.png
   :scale: 30
   :align: center

Managing your Google Cloud Projects
---------------------------------------------------
You can add or delete Google Cloud Projects by following the instructions below.

Adding additional Google Cloud Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To register additional Google Cloud Projects, select the **+ Register New Google Cloud Project** button from the "Registered Google Cloud Projects" page (see screenshot below).

.. image:: ../webapp/RegisterAnotherGCP.PNG
   :scale: 35
   :align: center

Deleting Google Cloud Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To unregister a GCP, select the **Unregister Project** button from the drop down menu beside the project on the "Registered Google Cloud Projects" page (see screenshot below).

.. image:: ../webapp/UnregisterAGCP.PNG
   :scale: 35
   :align: center





