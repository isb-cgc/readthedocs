***********************
Programmatic Interfaces
***********************

Programmatic access to molecular data in BigQuery, Google Cloud Storage, or Google Genomics
is based directly on the interfaces provided by the Google Cloud Platform, as 
illustrated throughout the 
`ISB-CGC code repositories on github <https://github.com/isb-cgc>`_.

In order to query the ISB-CGC metadata or to get information such as details regarding a
cohort that a user may have saved during an interactive session, a series of APIs based 
on Google Cloud Endpoints have been defined.  Details about these APIs can be found here.

The Google 
`APIs Explorer <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/>`_
can be used to see each API and try it out through your web browser.

Each API may bundle several endpoints that are functionally related.

Cohort API
##########

Cohorts are the primary organizing principle for subsetting and working with the TCGA data.  
A cohort is a list of samples (identified using the 16-character TCGA sample barcode).  Users may
create and share cohorts using the ISB-CGC web-app and then programmatically access these cohorts
using this API.

This API currently bundles several different cohort-related endpoints:

* **patient_details**: given a patient barcode (of length 12, *eg* TCGA-B9-7268), this endpoint returns all available information about this patient, including a list of samples and aliquots derived from this patient;

* **sample_details**: given a sample barcode (of length 16, *eg* TCGA-B9-7268-01A), this endpoint returns all available "biospecimen" information about this sample, the associated patient barcode, a list of associated aliquots, and a list of "data_details" blocks describing each of the data files associated with this sample;

* **datafilenamekey_list_from_sample**: given a sample barcode (of length 16) this endpoint returns a list of GCS objects containing data from that sample;

* **datafilenamekey_list_from_sample**: <description>;

* **preview_cohort**: 



