***********************
Programmatic Interfaces
***********************

Programmatic access to molecular data in BigQuery, Google Cloud Storage, or Google Genomics
is based directly on the interfaces provided by the Google Cloud Platform, as 
illustrated throughout the 
`ISB-CGC code repositories on github <https://github.com/isb-cgc>`_.

In order to query the ISB-CGC metadata or to get information such as details regarding a
cohort that a user may have saved during an interactive session, a series of APIs based 
on Google Cloud Endpoints have been defined.  Details about these APIs can be found here,
and examples illustrating how to use these endpoints from Python can be found in 
our `examples-Python <https://github.com/isb-cgc/examples-Python/python>` repository.

The Google 
`APIs Explorer <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/>`_
can be used to see each API and try it out through your web browser. Each API may bundle several endpoints that are functionally related.

Cohorts are the primary organizing principle for subsetting and working with the TCGA data.  
A cohort is a list of samples and a list of patients.  (TCGA samples are identified using a
16-character "barcode", while patients are identified using the 12-character prefix of the sample barcode.
Other datasets such as CCLE may use other less standardized naming conventions).  Users may
create and share cohorts using the ISB-CGC web-app and then programmatically access these cohorts
using this API.

The Cohort API currently bundles several different cohort-related endpoints:

.. toctree::
   :maxdepth: 1

   progapi2/cohort_patients_samples_list.rst
   progapi2/cohorts_list.rst
   progapi2/datafilenamekey_list_from_cohort.rst
   progapi2/datafilenamekey_list_from_sample.rst
   progapi2/delete_cohort.rst
   progapi2/google_genomics_from_cohort.rst
   progapi2/google_genomics_from_sample.rst
   progapi2/patient_details.rst
   progapi2/patient_details.rst
   progapi2/preview_cohort.rst
   progapi2/sample_details.rst
   progapi2/save_cohort.rst



