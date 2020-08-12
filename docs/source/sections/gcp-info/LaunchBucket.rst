Creating a Google Cloud Storage Bucket 
######################################

Why should you create a Google Cloud Storage buckets (hereto referred to as buckets) when your virtual machine can also store your data? Because Google Cloud Storage buckets are much less expensive to maintain compared to VM disks. Please see this link for the most up-to-date pricing on the different storage options offered by the Google Cloud Platform. 


Via the Google Cloud Console
=============================

`Instructional video on how to create a Google Cloud Storage bucket provided by  Google Cloud Platform: Create a storage bucket <https://youtu.be/TfOO-fSzTNA>`_.



Try it yourself:

1) Click on Cloud Storage browser on the left of the page


2) Click **Create a bucket**


3) Give the bucket a unique name, with all lower cap, no space.


4) Select region and Location and click **Create**


Via gsutil commandline tool
===========================

Use the gsutil mb command:

::

    $gsutil mb gs://[BUCKET_NAME]/ 
    
    
Where:

- [BUCKET_NAME] is the name you want to give your bucket, subject to naming requirements. For example, my-bucket.


You can set the following optional flags to have greater control over the creation of your bucket:

- p: Specify the project with which your bucket will be associated. For example, my-project.
- c: Specify the default storage class (https://cloud.google.com/storage/docs/storage-classes)) of your bucket. For example, NEARLINE.
- l: Specify the location  (https://cloud.google.com/storage/docs/locations of your bucket. For example, US-EAST1.
- b: Enable uniform bucket-level access (https://cloud.google.com/storage/docs/uniform-bucket-level-access) for your bucket.


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
==========================================
If you have access to a bucket and want to "clone" that bucket to your VM instance, gcsfuse can mount that bucket/or a sub-directory of that bucket to your VM directory of your choice.

Pros:


- Data can be accessed without using **gsutil** nor **gs://** address, i.e your bucket data become local to your VM instance

Cons:

- Since gcsfuse will actually download the data to your directory, make sure your VM instance has enough available storage to clone data from the bucket
- Consume available storage space
- May slow down your performance


**(1)** `How-to instructional video <https://www.youtube.com/watch?v=mE6dLYOf8BA>`_ 


**(2)** `Step-by-Step installation guide <https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/installing.md>`_


Quicktips
---------


Mount a bucket to your folder:

::

  $gcsfuse bucketname myfolder/to/mount

Mount a subdirectory from your bucket to your VM folder:
::

  $gcsfuse --only-dir subdirectory bucketName myFolder/to/mount
