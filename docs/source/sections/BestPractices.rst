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



 a. The basics and best practices on how to launch virtual machines (VMs) are described `here <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/gcp-info/gcp-info2/LaunchVM.html>`_ in our documentation. **NOTE: When launching VMs, please maintain the default firewall settings.**


 b. Compute Engine instances can run the public images for Linux and Windows Server that Google provides as well as private custom images that you can `create <https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images>`_ or `import from your existing systems <https://cloud.google.com/compute/docs/images/importing-virtual-disks>`_. 
 
   Be careful as you spin up a machine, as larger machines cost you more.  If you are not using a machine, shut it down. You can always restart it easily when you need it.
 
   Example use-case: You would like to run Windows-only genomics software package on the TCGA data. You can create a Windows based VM instance.

 
 c. More details on how to deploy docker containers on VMs are described here in Google’s documentation: `deploying containers <https://cloud.google.com/compute/docs/containers/deploying-containers>`_
 
 d. A good way to estimate costs for running a workflow/pipeline on large data sets is to test them first on a small subset of data.
 
 e. There are different VM types depending on the sort of jobs you wish to execute. By default, when you create a VM instance, it remains active until you either stop it or delete it. The costs associated with VM instances are detailed here:  `compute pricing <https://cloud.google.com/compute/pricing>`_
 
 f. If you plan on running many short compute-intensive jobs (for example indexing and sorting thousands of large bam files), you can execute your jobs on preemptible virtual machines. They are 80% cheaper than regular instances.  `preemptible vms <https://cloud.google.com/preemptible-vms/>`_
 
 **Example use-cases:**
 
  - Using preemptible VMs, researchers were able to quantify transcript levels on over 11K TGCA RNAseq samples for a total cost of $1,065.49.
  
    Tatlow PJ, Piccolo SR. `A cloud-based workflow to quantify transcript-expression levels in public cancer compendia <https://www.nature.com/articles/srep39259>`_. Scientific Reports 6, 39259
  - Also Broad’s popular variant caller pipeline, GATK, was designed to be able to run on preemptible VMs. 
  


Storage on the Cloud
==========================

The Google Cloud Platform offers a number of different storage options for your virtual machine instances: `disks <https://cloud.google.com/compute/docs/disks/>`_

 a. `Block Storage: <https://cloud.google.com/compute/docs/disks/#pdspecs>`_
 
  - By default, each virtual machine instance has a single boot persistent disk that contains the operating system. The default size is 10GB but can be adjusted up to 64TB in size. (Be careful! High costs here, spend wisely!) 
  - Persistent disks are restricted to the zone where your instance is located.
  - Use persistent disks if you are running analyses that require low latency and high-throughput. 
  
 b. `Object Storage: <https://cloud.google.com/compute/docs/disks/#gcsbuckets>`_ Google Cloud Storage (GCS) buckets are the most flexible and economical storage option.
 
  - Unlike persistent disks, Cloud Storage buckets are not restricted to the zone where your instance is located. 
  - Additionally, you can read and write data to a bucket from multiple instances simultaneously.
  - You can mount a GCS bucket to your VM instance when latency is not a priority or when you need to share data easily between multiple instances or zones. 
  
    An example use-case: You want to slice thousands of bam files and save the resulting slices to share with a collaborator who has instances in another zone to use for downstream statistical analyses.
  - You can save objects to GCS buckets including images, videos, blobs and unstructured data. 
  
    A comparison table detailing the current pricing of Google’s storage options can be found here: `storage features <https://cloud.google.com/storage/features/>`_

Cost Management
===============

This section details a few use cases and their approximate costs in order to help users estimate cloud costs for their analyses. 

Estimating Costs for Common Bioinformatics and Data Analysis Tasks
------------------------------------------------------------------

The following table summarizes order-of-magnitude costs for common data analysis tasks. For example an order-of-magnitude cost of $10 indicates that the cost can be up to $10, estimated from the given example notebooks. Estimated costs between $10 and $100 are reported as the next order of magnitude, $100:

.. list-table::
   :widths: 100 25 25 25
   :align: center
   :header-rows: 1

   * - Bioinformatics / Data Analysis Task
     - Dataset(s)
     - Tools
     - Approx. Cost (Max)
   * - | Identify differentially expressed genes
       | `Example: Breast Cancer Tumor vs. Normal <https://github.com/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_analyze_differential_expression_between_paired_tumor_and_normal_samples.ipynb>`_
     - TCGA
     - BigQuery, Colab, Python, R
     - $1
   * - | Train a prediction model using gene expression data
       | `Example: Logistic Regression, Ovarian Cancer Chemo Response <https://github.com/isb-cgc/Community-Notebooks/blob/master/MachineLearning/How_to_build_an_RNAseq_logistic_regression_classifier_with_BigQuery_ML.ipynb>`_
       | `Example: Logistic Regression, Breast Cancer Tumor vs. Normal <https://github.com/isb-cgc/Community-Notebooks/blob/master/TeachingMaterials/2021-10-NIHLibrarySession/BigQueryMachineLearning.ipynb>`_
     - TCGA
     - BigQuery, BigQuery ML, Colab, Python, R
     - $1 ($100) \*
   * - | Train a linear regression model using gene expression data
       | `Example: Linear Regression, Kidney Cancer Survival <https://github.com/isb-cgc/Community-Notebooks/blob/master/MachineLearning/How_to_predict_cancer_survival_with_BigQueryML.ipynb>`_
     - TCGA
     - BigQuery, BigQuery ML, Colab, Python
     - $1 ($100) \*
   * - | Train a deep neural network (DNN) regression model using gene expression data
       | `Example: Regression w/ TensorFlow, Kidney Cancer Survival <https://github.com/isb-cgc/Community-Notebooks/blob/master/MachineLearning/How_to_predict_cancer_survival_with_TensorFlow.ipynb>`_
     - TCGA
     - BigQuery, Colab, TensorFlow, Compute Engine w/ GPUs
     - $1 \*\*
   * - | Analyze RNA-seq data using the GDC workflow
       | `Example: GDC RNA-seq CWL Workflow <https://github.com/NCI-GDC/gdc-rnaseq-cwl>`_
     - TCGA
     - Compute Engine, Cloud Storage, CWL
     - $10 \*\*\*

* \*BigQuery ML costs depend on data size. In these examples, a subset of data was extracted to a temporary table, which was used as input to BigQuery ML. This reduces costs substantially. If using all gene features of a TCGA dataset, costs can grow to the order of $100.

* \*\*With small datasets, use of GPUs in Colab does not cost extra (unless using `Colab Pro <https://research.google.com/colaboratory/faq.html>`_). However, if TensorFlow code is executed in a VM with GPUs, the hourly cost can range from $1 to $10.

* \*\*\*Cost per sample depends on sample size (i.e., number of reads) and processing time.

* BigQuery ML vs. TensorFlow w/ Compute Engine or Colab GPUs: When choosing between these tools for machine learning, consider the following guidelines:

  - TensorFlow w/ Compute Engine or Colab GPUs: Appropriate for data exploration or parameter tuning requiring multiple iterations of training and evaluation. 

  - BigQuery ML: Appropriate for production deployment of machine learning models. For example, after optimizing model parameters, train and deploy the final model with BigQuery ML.

