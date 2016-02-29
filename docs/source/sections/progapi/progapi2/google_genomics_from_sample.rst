
google_genomics_from_sample
###########################

Takes a sample barcode as a required parameter and returns the Google Genomics dataset id and readgroupset id associated with the sample, if any.

**Access control:** To call this method, you must have the following
roles:

-  None

Request

HTTP request

GET https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/google_genomics_from_sample

Parameters

+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
| **Parameter name**    | **Value**   | **Description**                                                                                                    |
+=======================+=============+====================================================================================================================+
| **Path parameters**   |             |                                                                                                                    |
+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
| sample\_barcode       | string      | Required. The sample whose dataset id and readgroupset id will be retrieved.                                       |
+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+


Response

If successful, this method returns a response body with the following
structure:

.. code-block:: javascript

	{
	  "kind": "cohort_api#cohortsItem",
	  "items": [
		{
		"count": string,
		"SampleBarcode": string,
		"GG_dataset_id": string,
		"GG_readgroupset_id": string
		}
	  ] 
	}

+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| **Property name**          | **Value**               | **Description**                                                                                             |
+============================+=========================+=============================================================================================================+
| kind                       | cohort\_api#cohortsItem | The resource type.                                                                                          |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| count                      | string                  | The number of items returned. Count will be either "0" or "1".                                              |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| items[]                    | list                    | If a dataset id and readgroupset id exist for the sample, this will be a list with one object.              |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| items[].SampleBarcode      | string                  | The sample barcode passed into the request.                                                                 |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| items[].GG_dataset_id      | string                  | The dataset id of the sample.                                                                               |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| items[].GG_readgroupset_id | string                  | The readgroupset id of the sample.                                                                          |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+

