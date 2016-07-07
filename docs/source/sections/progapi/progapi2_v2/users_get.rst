users().get()
##############
Returns the dbGaP authorization status of the user.

**Example**::

	python isb_curl.py https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/users

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https%3A%2F%2Fapi-dot-isb-cgc.appspot.com%2F_ah%2Fapi#p/isb_cgc_api/v2/isb_cgc_api.users.get?/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/isb_cgc_api/v2/users

**Parameters**

None

**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "dbGaP_authorized": boolean,
    "message": string
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	dbGaP_authorized, boolean, "True or false."
	message, string, "Message indicating the authorization status of the user."
