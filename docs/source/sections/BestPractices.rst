
============
Best practices when working on the Google Cloud Console
============

***************
Overview
***************


***************
Storage
***************

A single API for all storage classes
=====================================
Cloud Storage’s consistent API, latency, and speed across storage classes simplifies development integration and reduces code complexity. Implement Object Lifecycle Management to set a Time to Live (TTL) for objects, archive older version of objects, or downgrade storage classes without compromising on latency or accessibility. Set custom policies to transition data seamlessly from one storage class to the next, depending on your cost and availability needs at the time. 

Where can I find pricing information?
-----------------------------------------

Read the `Pricing page <https://cloud.google.com/storage/pricing/>`_ for detailed information on pricing, including how Cloud Storage calculates bandwidth and storage usage.

When do I need to activate Cloud Storage and enable billing?
-------------------------------------------------------------
If you want to create buckets, store data, or control who can access your data, you must activate Cloud Storage and enable billing.

I am just trying to download or access some data that is freely available to the public. How can I do that?
--------------------------------------------------------------------------------------------------------------

You can simply use the gsutil tool to download the data, even without a Google account. You do not need to activate Cloud Storage or turn on billing for this purpose. You also do not need to create credentials or authenticate to Cloud Storage. The gsutil tool is best installed as part of the Google Cloud SDK package, but may also be downloaded and installed as a stand-alone product.

What tools and libraries are available for Cloud Storage?
----------------------------------------------------------

In addition to the `JSON API <https://cloud.google.com/storage/docs/json_api/>`_ and the `XML API <https://cloud.google.com/storage/docs/xml-api/overview/>`_, Google offers the following options for interacting with Cloud Storage:
The browser-based `Google Cloud Platform Console <https://cloud.google.com/storage/docs/xml-api/overview/>`_ performs basic operations on buckets and objects.
The `gsutil command-line tool <https://cloud.google.com/storage/docs/gsutil>`_ provides a command-line interface with Cloud Storage.
The `Cloud Storage Client Libraries <https://cloud.google.com/storage/docs/reference/libraries>`_ provide programmatic support for a number of programming languages, including Java, Python, and Ruby.
You can find additional, third-party tools and libraries, such as the `Boto library <https://cloud.google.com/storage/docs/boto-plugin>`_, by searching the Internet.

***************
Pricing
***************
