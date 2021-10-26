==============
Best Practices
==============


Don't Download the Data
===========================


The ISB-CGC platform is one of NCI’s `Cancer Cloud Resources <https://datascience.cancer.gov/data-commons/cloud-resources>`_ and our mission is to host cancer data (such as TCGA and TARGET data) in the cloud so that researchers around the world may work with data without needing to download and store the data at their own local institutions.  

Remember those times when you had to wait weeks to download the data - you don’t need to do that any more!  The data is already on the cloud, so you can collaborate with other researchers much more easily.
Be mindful that if you download data, you’ll incur egress charges.  
`Google egress charges information <https://cloud.google.com/compute/pricing#internet_egress>`_


Computing on the Cloud
===========================


Most of the same linux commands, scripts, pipelines/workflows, genomics software packages and docker containers that you run on your local machine can be executed on virtual machines on Google Cloud. 



 a.) The basics and best practices on how to launch virtual machines (VMs) are described `here <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/gcp-info/gcp-info2/LaunchVM.html>`_ in our documentation. **NOTE: When launching VMs, please maintain the default firewall settings.**


 b.) Compute Engine instances can run the public images for Linux and Windows Server that Google provides as well as private custom images that you can `create <https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images>`_ or `import from your existing systems <https://cloud.google.com/compute/docs/images/importing-virtual-disks>`_. 
 
   Be careful as you spin up a machine, as larger machines cost you more.  If you are not using a machine, shut it down. You can always restart it easily when you need it.
 
   Example use-case: You would like to run Windows-only genomics software package on the TCGA data. You can create a Windows based VM instance.

 
 c.) More details on how to deploy docker containers on VMs are described here in Google’s documentation: `deploying containers <https://cloud.google.com/compute/docs/containers/deploying-containers>`_
 
 d.) A good way to estimate costs for running a workflow/pipeline on large data sets is to test them first on a small subset of data.
 
 e.) There are different VM types depending on the sort of jobs you wish to execute. By default, when you create a VM instance, it remains active until you either stop it or delete it. The costs associated with VM instances are detailed here:  `compute pricing <https://cloud.google.com/compute/pricing>`_
 
 f.) If you plan on running many short compute-intensive jobs (for example indexing and sorting thousands of large bam files), you can execute your jobs on preemptible virtual machines. They are 80% cheaper than regular instances.  `preemptible vms <https://cloud.google.com/preemptible-vms/>`_
 
 **Example use-cases:**
  - Using preemptible VMs, researchers were able to quantify transcript levels on over 11K TGCA RNAseq samples for a total cost of $1,065.49.
  
    Tatlow PJ, Piccolo SR. `A cloud-based workflow to quantify transcript-expression levels in public cancer compendia <https://www.nature.com/articles/srep39259>`_. Scientific Reports 6, 39259
  - Also Broad’s popular variant caller pipeline, GATK, was designed to be able to run on preemptible VMs. 
  


Storage on the Cloud
==========================

The Google Cloud Platform offers a number of different storage options for your virtual machine instances: `disks <https://cloud.google.com/compute/docs/disks/>`_

 a.) `Block Storage: <https://cloud.google.com/compute/docs/disks/#pdspecs>`_
  - By default, each virtual machine instance has a single boot persistent disk that contains the operating system. The default size is 10GB but can be adjusted up to 64TB in size. (Be careful! High costs here, spend wisely!) 
  - Persistent disks are restricted to the zone where your instance is located.
  - Use persistent disks if you are running analyses that require low latency and high-throughput. 
  
 b.) `Object Storage: <https://cloud.google.com/compute/docs/disks/#gcsbuckets>`_ Google Cloud Storage (GCS) buckets are the most flexible and economical storage option.
 
  - Unlike persistent disks, Cloud Storage buckets are not restricted to the zone where your instance is located. 
  - Additionally, you can read and write data to a bucket from multiple instances simultaneously.
  - You can mount a GCS bucket to your VM instance when latency is not a priority or when you need to share data easily between multiple instances or zones. 
  
    An example use-case: You want to slice thousands of bam files and save the resulting slices to share with a collaborator who has instances in another zone to use for downstream statistical analyses.
  - You can save objects to GCS buckets including images, videos, blobs and unstructured data. 
  
    A comparison table detailing the current pricing of Google’s storage options can be found here: `storage features <https://cloud.google.com/storage/features/>`_
 
