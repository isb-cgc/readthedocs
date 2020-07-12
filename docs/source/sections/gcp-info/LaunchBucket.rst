Creating a Google Cloud Storage Bucket 
####################################

Via the Google Cloud Console
=================================
`Video: Create a storage bucket <https://youtu.be/TfOO-fSzTNA>`_.

Via gcloud command-line tool
==================================================
Use the gsutil mb command:

::

    $gsutil mb gs://[BUCKET_NAME]/

Where:

- [BUCKET_NAME] is the name you want to give your bucket, subject to naming requirements. For example, my-bucket. 
Set the following optional flags to have greater control over the creation of your bucket:
- p: Specify the project with which your bucket will be associated. For example, my-project.
- c: Specify the default storage class of your bucket. For example, NEARLINE.
- l: Specify the location of your bucket. For example, US-EAST1.
- b: Enable uniform bucket-level access for your bucket.

Accessing data in your bucket by gsutil
=======================================
::

    my-cloud-bucket
    |_______myFile.txt
    |_______myOtherFile.txt

To list what in your bucket:
::

   $gsutil ls gs://my-cloud-bucket/

output:
::

   gs://my-cloud-bucket/myFile.txt
   gs://my-cloud-bucket/myOtherFile.txt


Accessing data in your bucket via GCSFuse
========================================
`How-to video <https://www.youtube.com/watch?v=mE6dLYOf8BA>`_ | `Installing Page <https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/installing.md>`_


If you have access to a bucket and want to "clone" that bucket to your VM instance, gcsfuse can mount that bucket/ or a sub-directory of that bucket to your VM directory of your choice.

Pros:


- Data can be accessed without using **gsutil** nor **gs://** address, i.e your bucket data become local in your VM instance
- Bypass the need for service account when running an application that need access to google cloud bucket


Cons:

- Since gcsfuse will actually downloading the data to your directory, make sure your VM instance has enough available storage to clone data from the bucket
- Consume available storage space
- May slowdown your performance


Quicktips
---------


Mount a bucket to your folder:

::

  $gcsfuse bucketname myfolder/to/mount

Mount a subdirectory from your bucket to your VM folder:
::

  $gcsfuse --only-dir subdirectory bucketName myFolder/to/mount
