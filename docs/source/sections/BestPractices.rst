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


 a.) The basics and best practices on how to launch virtual machines (VMs) are described `here <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/gcp-info/gcp-info2/LaunchVM.html>`_ in our documentation.  


 b.) Compute Engine instances can run the public images for Linux and Windows Server that Google provides as well as private custom images that you can `create <https://isb-cgc.appspot.com/>`_ or `import from your existing systems <https://cloud.google.com/compute/docs/images/importing-virtual-disks>`_. 
 
   Be careful as you spin up a machine, as the larger machines cost you more.  If you are not using a machine, shut it down, you can always restart it easily when you need it.
 
   Example use-case: You would like to run Windows-only genomics software package on the TCGA data. You can create a Windows based VM instance.

 
 c.) More details on how to deploy docker containers on VMs are described here in Google’s documentation: 
  (https://cloud.google.com/compute/docs/containers/deploying-containers)
 
 d.) A good way to estimate costs for running a workflow/pipeline on large datasets is to test them first on a small subset of data.
 
 e.) There are different VM types depending on the sort of jobs you wish to execute. By default, when you create an VM instance, it remains active until you either stop it or delete it. The costs associated with VM instances are detailed here: https://cloud.google.com/compute/pricing
 
 f.) If you plan on running many short compute-intensive jobs (for example indexing and sorting thousands of large bam files), you can execute your jobs on preemptible virtual machines. They are 80% cheaper than regular instances. https://cloud.google.com/preemptible-vms/ 
 
 **Example use-cases:**
  - Using preemptible VMs, researchers were able to quantify transcript levels on over 11K TGCA RNAseq samples for a total cost of $1,065.49.
  Tatlow PJ, Piccolo SR. `A cloud-based workflow to quantify transcript-expression levels in public cancer compendia <https://www.nature.com/articles/srep39259>`_. Scientific Reports 6, 39259
  - Also Broad’s popular variant caller pipeline, GATK was designed to be able to run on preemptible VMs. 
  


STORAGE ON THE CLOUD
=====================

The Google Cloud Platform offers a number of different storage options for your virtual machine instances: https://cloud.google.com/compute/docs/disks/

 a.) 






