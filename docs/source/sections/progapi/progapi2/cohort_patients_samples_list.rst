cohort_patients_samples_list
############################
Takes a cohort id as a required parameter and returns information about the participants and samples in a particular cohort. Authentication is required. User must have either READER or OWNER permissions on the cohort.

Request

HTTP request

GET https://api-dot-isb-cgc.appspot.com/\_ah/api/cohort\_api/v1/cohort\_patients\_samples\_list\``

Parameters

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cohort_id,string,Required.
	token,string,Optional.


Response

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "cohort_id": string,
    "patient_count": string,
    "patients": [string],
    "sample_count": string,
    "samples": [string]
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	cohort_id, string, "ID of the cohort."
	patient_count, string, "Total count of unique patient barcodes in the cohort."
	patients[], list, "List of patient barcodes."
	sample_count, string, "Total count of unique sample barcodes in the cohort."
	samples[], list, "List of sample barcodes."
