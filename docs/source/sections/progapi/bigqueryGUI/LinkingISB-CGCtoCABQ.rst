=======================================================
Linking BigQuery to ISB-CGC Project Controlled Access Data
=======================================================

To obtain access you must first link your NIH ID via the wepp application to your Google identity to be able to use controlled data in BigQuery.  Then once linked you can obtain access to the ISB-CGC-cbq project tables in BigQuery. You must also
link these tables to your project, so that they will show up in the left panel of your BigQuery web UI.

Linking your NIH and Google identities
--------------------------------------
To link your NIH identity with your Google identity (ie the Google account you used to login to the ISB-CGC system), 
select the "persona" icon next to your login name (A in the image below) after you have signed in to the ISB-CGC Web App.  

.. image:: personaeicon-NIHLoginAssoc.png
   :scale: 50
   :align: center

You will then see the following page:

.. image:: NIHAssociationPage.png
   :scale: 50
   :align: center


You will see a pop up describing all the steps needed to link you NIH Identity to the Data Commons Framework(DCF).

.. image:: LinkNIHIDInstructions.PNG
   :scale: 50
   :align: center

Now you need to associate your Google identity with your NIH identity.  (Your NIH identity is the one associated
with your dbGaP application and authorization to work with controlled data.) 
To do this, select the "Associate with eRA Commons Account" link (highlighted in diagram above, and labeled A).  
You will then be re-directed to an NIH login page to be authenticated by NIH:

.. image:: iTrust.png
   :scale: 50
   :align: center

If you have an eRA identification, use this to sign in through panel A (see example above).  
If you have an NIH PIV card, use that to sign in through panel B on this page (see above).  
Once you have been authenticated by NIH, and your NIH identity has been verified to be on
the current dbGaP whitelist, you will have access to controlled data for 24 hours.  

.. image:: Gen3authPage.PNG
   :scale: 50
   :align: center
   

Select the Yes, I Authorize button at the bottom right of the page to authorize the Data Commons Framework to authorize your Google identity with controlled data.

.. image:: datacommons.ioLogIn.PNG
   :scale: 50
   :align: center

Select the email you used to originally log into the ISB-CGC web application to finalize the authorization.

Once logged in through eRA identification you are re-directed to the user details page and given Warning Notice referring to abiding by the rules and regulations provided by the DUCA Use Agreement.  Please refer to image below.

.. image:: warningNotice.png
   :scale: 50
   :align: center

Please note: the ISB-CGC system will enforce a one-to-one relationship between NIH identities
and Google identites.  In other words, a single NIH identity may not be used to attempt to
gain access to controlled data by multiple, different Google identities.
If you need to *unlink* your eRA account from your Google account (for example if you want to
change which Google identity you use to sign in to the ISB-CGC platform), you may do so by
selecting "Unlink <GoogleID> from the NIH username <eRA Commons ID>" (link B in the screen above).

In the unusual instance that your NIH identity has been registered with another Google identity 
(*eg* with another Google identity you own), you will see the screen below:

.. image:: eRAlinkedtoAnotherGoogle.png
   :scale: 50
   :align: center
   
If this happens, please sign in with that other account and "unlink" your eRA from that account i
(see description above).  You will then be able to register your eRA account with the desired Google identity.  
If you are not able to resolve the issue, contact us at feedback@isb-cgc.org and we will help you resolve it. 


Linking controlled access data to your Google Console
-----------------------------------------------------

To obtain access to the ISB-CGC project tables in BigQuery you must link these tables to your project so that they will show up in the left panel of your BigQuery web UI. 

When you access BigQuery from your Google Cloud Platform Console (see link `here <HowToAccessBigQueryFromTheGoogleCloudPlatform.html>`_ for more information on this), you will be presented with the following page:

.. image:: BlueArrowDropdown.PNG
   :scale: 25
   :align: center

The blue arrow will produce a drop down list; select 'Switch to Project'; then click 'display project...'

You will then be presented with the following page:

.. image:: SearchProjectSection.PNG
   :scale: 25
   :align: center

As shown in the image below you will need to type in "isb-cgc-cbq" in the project id and then click okay. 

.. image:: CABQisb-cgc-pinning.PNG
   :scale: 25
   :align: center

Once this has been completed you will see all of the BigQuery datasets made public by the ISB-CGC project on the left hand side above public data sets (see screenshot below).

.. image:: isb-cgc-cbq_tablename.PNG
   :scale: 25
   :align: center


