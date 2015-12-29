***********************
Programmatic Interfaces
***********************

Programmatic access to molecular data in BigQuery, Google Cloud Storage, or Google Genomics
is based directly on the interfaces provided by the Google Cloud Platform, as 
illustrated throughout the 
`ISB-CGC code repositories on github <https://github.com/isb-cgc>`_.

In order to query the ISB-CGC metadata or to get information such as details regarding a
cohort that a user may have saved during an interactive session, a series of APIs based 
on Google Cloud Endpoints have been defined.  Details about these APIs as well as instructions
on using helper scripts for the oAuth flow can be found here.

The Google 
`APIs Explorer <https://apis-explorer.appspot.com/apis-explorer/?base=https://isb-cgc.appspot.com/_ah/api#p/>`_
can be used to see each API and try it out through your web browser.

Each API may bundle several endpoints that are functionally related.

Cohort API
##########

Cohorts are the primary organizing principle for subsetting and working with the TCGA data.  
A cohort is a list of samples (identified using the 16-character TCGA sample barcode).  Users may
create and share cohorts using the ISB-CGC web-app and then programmatically access these cohorts
using this API.

This API currently bundles several different cohort-related endpoints:

* **cohorts_list**: returns a list of all cohorts that the user has OWNER or READER access to; each cohort is identified by a unique "id" and includes other information such as "name", "comments", "last_date_saved", *etc*;

* **cohorts_patients_samples_list**: given a cohort id (required), this endpoint returns the patient_count and sample_count, as well as two lists of barcodes: one for the patients and one for the samples;  (note that the number of patients can be less than the number of samples)

* **patient_details**: given a patient barcode (of length 12, *eg* TCGA-B9-7268), this endpoint returns all available information about this patient, including a list of samples and aliquots derived from this patient;

* **sample_details**: given a sample barcode (of length 16, *eg* TCGA-B9-7268-01A), this endpoint returns all available "biospecimen" information about this sample, the associated patient barcode, a list of associated aliquots, and a list of "data_details" blocks describing each of the data files associated with this sample;

* **datafilenamekey_list**: given a sample barcode (of length 16) this endpoint returns a list of GCS objects containing data from that sample;

* **delete_cohort**: given a cohort id (required), the user may programmatically delete a cohort for which they are OWNER (this can also be done interactively via the web-app);

* **save_cohort**: 


Metadata API
############

This API currently bundles several different metadata-related endpoints:

* **metadata_list**: returns all metadata about each patient (aka participant) in the specified cohort (if a cohort id is given); a list of "selectors" can also be passed in if only some of the metadata is requested;

* **cohort_files**: given a cohort id, this endpoint returns the total number of files associated with that cohort, the counts according to platform, and details about each file;

* **sample_files**: given a sample barcode (of length 16) this endpoint returns the total number of files associated with that sample, the counts according to platform, and details about each file;

* **metadata_attr_list**: returns a list of the metadata attributes; each item contained in the list includes:
    - attribute: a string describing the attribute (*eg* "age_at_initial_pathologic_diagnosis");
    - code: indicates whether the attribute is numeric (N), binary (B), or categorical (includes strings) (C);  and
    - spec: indicates whether the attribute is a clinical feature associated with a patient (CLIN), a sample feature (SAMP).

User API
########

This API currently contains a single endpoint:

* **am_i_dbgap_authorized**:  accesses the user's Google identity and checks whether that identity is currently on the access control list (ACL) for controlled-data (which requires not only that the user have dbGaP authorization but also that the user has authenticated within the past 24 hours;  returns one of two messages:
    - *"You are not on the controlled-access google group."*  or
    - *"<user's Google identity> has dbGaP authorization and is a member of the controlled-access google group."*

Helper Scripts
##############

Two helper scripts, 
`isb_auth.py <https://github.com/isb-cgc/ISB-CGC-Webapp/blob/master/scripts/isb_auth.py>`_ 
and 
`isb_curl.py <https://github.com/isb-cgc/ISB-CGC-Webapp/blob/master/scripts/isb_curl.py>`_ 
are available for use from the command-line or from a python script.  The first one is a wrapper
for the OAuth process, and the second can be used to send a GET or POST request with the 
proper access token to the specified endpoint.

