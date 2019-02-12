============
Best Practices
============


DON'T DOWNLOAD THE DATA
========================


The ISB-CGC platform is one of NCI’s `Cancer Genomics Cloud Resources <https://cbiit.cancer.gov/ncip/crdc-cloud-resources/>`_ and our mission is to host TCGA and TARGET data in the cloud so that researchers around the world may work with the data without needing to download and store the data at their own local institutions.  

Remember those times when you had to wait weeks to download the data - you don’t need to do that any more!  The data is already on the cloud, so you can collaborate with other researchers much more easily.
Be mindful that if you download data, you’ll incur egress charges.  
`Google egress charges information <https://cloud.google.com/compute/pricing#internet_egress>`_


COMPUTING ON THE CLOUD
=======================

Most of the same linux commands, scripts, pipelines/workflows, genomics software packages and docker containers that you run on your local machine can be executed on virtual machines on the Google cloud. 


 a. The basics and best practices on how to launch virtual machines (VMs) are described `here <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/gcp-info/gcp-info2/LaunchVM.html>`_ in our documentation.  


 b. Compute Engine instances can run the public images for Linux and Windows Server that Google provides as well as private custom images that you can `create <https://isb-cgc.appspot.com/>`_ or `import from your existing systems <https://cloud.google.com/compute/docs/images/importing-virtual-disks>`_. 
 
   Be careful as you spin up a machine, as the larger machines cost you more.  If you are not using a machine, shut it down, you can always restart it easily when you need it.
 
   Example use-case: You would like to run Windows-only genomics software package on the TCGA data. You can create a Windows based VM instance.

 
 c. 
