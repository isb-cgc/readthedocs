---------------------------------------
Interactive Access to Controlled Data 
---------------------------------------

This section shows you how to associate your Google identity to your NIH or eRA account through the Web App. This is a necessary step for gaining access to controlled data.

Click on screen shots to enlarge them.

Linking your NIH and Google identities
--------------------------------------
To link your NIH identity with your Google identity (the Google account you use to login to the ISB-CGC system), 
select the "persona" icon next to your login name (A in the image below) after you have signed in to the ISB-CGC Web App. 
Or, you can click on the drop down menu next to your name, and click on Account Details.

.. image:: ../webapp/personaeicon-NIHLoginAssoc.png
   :scale: 50
   :align: center

You will then see the following page:

.. image:: ../webapp/NIHAssociationPage.png
   :scale: 30
   :align: center


You will see a pop up describing all the steps needed to link you NIH Identity to the Data Commons Framework (DCF).

.. image:: ../webapp/LinkNIHIDInstructions.PNG
   :scale: 30
   :align: center

Now you need to associate your Google identity with your NIH identity.  (Your NIH identity is the one associated
with your dbGaP application and authorization to work with controlled data.) 
To do this, select the "Associate with eRA Commons Account" link (highlighted in the diagram above, and labeled A).  
You will then be redirected to an NIH login page to be authenticated by NIH:

.. image:: ../webapp/iTrust.png
   :scale: 30
   :align: center

If you have an eRA identification, use this to sign in through panel A (see example above).  
If you have an NIH PIV card, use that to sign in through panel B on this page (see above).  
Once you have been authenticated by NIH, and your NIH identity has been verified to be on
the current dbGaP whitelist, you will have access to controlled data for 24 hours.  

.. image:: ../webapp/Gen3authPage.PNG
   :scale: 30
   :align: center
   
Select the Yes, I Authorize button at the bottom right of the page to authorize the Data Commons Framework to authorize your Google identity with controlled data.

.. image:: ../webapp/datacommons.ioLogIn.PNG
   :scale: 30
   :align: center

Select the email you used to originally log into the ISB-CGC web application to finalize the authorization.

Once logged in through eRA identification you are redirected to the user details page and given a Warning Notice referring to abiding by the rules and regulations provided by the DUCA Use Agreement.  Please refer to image below.

.. image:: ../webapp/warningNotice.png
   :scale: 30
   :align: center

Please note: the ISB-CGC system will enforce a one-to-one relationship between NIH identities
and Google identities.  In other words, a single NIH identity may not be used to
gain access to controlled data by multiple, different Google identities.
If you need to *unlink* your eRA account from your Google account (for example if you want to
change which Google identity you use to sign in to the ISB-CGC platform), you may do so by
selecting "Unlink <GoogleID> from the NIH username <eRA Commons ID>" (link B in the screen above).

In the unusual instance that your NIH identity has been registered with another Google identity 
(*eg* with another Google identity you own), you will see the screen below:

.. image:: ../webapp/eRAlinkedtoAnotherGoogle.png
   :scale: 30
   :align: center
   
If this happens, please sign in with that other account and "unlink" your eRA from that account
(see description above).  You will then be able to register your eRA account with the desired Google identity.  
If you are not able to resolve the issue, contact us at feedback@isb-cgc.org and we will help you resolve it.   

To end your Web App session, just "Sign Out" by using the pull-down below your name 
(see image below, A).  After you sign out from the ISB-CGC Web App, your Google identity may 
still be signed in to your browser, so you may want to also sign out of the browser.

.. image:: ../webapp/SignOut.png
   :scale: 30
   :align: center

Extending Your Access by 24 hours 
-----------------------------------
Once you have received permission to view controlled access data, your user login page will look 
like the screenshot below. If you need to extend your access to controlled data for another 24 
hours from now (*eg* if you have a compute job which is using these Google credentials to access 
controlled data and it is still running), select the link "Extend controlled access 
period to 24 hours from now" (red box on figure below).  
Your time of access will be extended to 24 hours from the time you push the link. 

.. image:: ../webapp/24hrExtension.png
   :scale: 30
   :align: center

