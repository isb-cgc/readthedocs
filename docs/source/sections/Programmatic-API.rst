***********************
Programmatic Interfaces
***********************

Programmatic access to molecular data in BigQuery, Google Cloud Storage, or Google Genomics
is based directly on the interfaces provided by the Google Cloud Platform, as 
illustrated throughout the ISB-CGC code repositories on github_.

.. _github: https://github.com/isb-cgc

In order to query the ISB-CGC metadata or to get information such as details regarding a
cohort that a user may have saved during an interactive session, a series of APIs based 
on Google Cloud Endpoints have been defined.  Details about these APIs as well as instructions
on using helper scripts for the oAuth flow can be found here.

The Google `APIs Explorer <https://apis-explorer.appspot.com/apis-explorer/?base=https://mvm-dot-isb-cgc.appspot.com/_ah/api#p/>`_
can be used to see each API and try it out through your web browser.

Metadata API
############
*Documentation currently under construction!  Please email info@isb-cgc.org if you have questions.*

Cohort API
##########
*Documentation currently under construction!  Please email info@isb-cgc.org if you have questions.*

User API
########
*Documentation currently under construction!  Please email info@isb-cgc.org if you have questions.*

Authorization Process
#####################
*Documentation currently under construction!  Please email info@isb-cgc.org if you have questions.*

Two helper scripts, 
`isb_auth.py <https://github.com/isb-cgc/ISB-CGC-Webapp/blob/master/scripts/isb_auth.py>`_ 
and 
`isb_curl.py <https://github.com/isb-cgc/ISB-CGC-Webapp/blob/master/scripts/isb_curl.py>`_ 
are available for use from the command-line or from a python script.  The first one is a wrapper
for the OAuth process, and the second can be used to send a GET or POST request with the 
proper access token to the specified endpoint.

