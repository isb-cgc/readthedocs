***************************
Benefits of Using The Cloud
***************************

Working in the cloud is exceptionally scalable and versatile; you only use as much as you need, whether that's in terms of storage space or processing cores. Cloud-based data is easily read by massively parallel processes, expediting results. When you're done, resources disappear! You don't have idle resources sitting around collecting dust. 

Don’t be intimidated by the cloud! Scale your analyses using the data on ISB-CGC. If you’ve conducted bioinformatics before using the command line or SQL, this will be just as easy (if not easier) and we are also here to help. Email feedback@isb-cgc.org or visit our `Community Notebooks page <HowTos.html>`_ for guides and tutorials.


Most bioinformaticians today are likely accustomed to using the high performance compute (HPC) resources provided by their institution to conduct high-throughput bioinformatics analyses. Here’s a breakdown on how the Google Cloud Platform compares to your institution’s HPC resources. 

+-----------+-------------------------------------+-----------------------------------------+
|           | Your University's HPC Resource      | Google Cloud Platform                   |
+===========+=====================================+=========================================+
| Operating | Linux, Windows                      | Virtual machines can run Linux and      |
| Systems   |                                     | Windows                                 |
|           |                                     |                                         |
+-----------+-------------------------------------+-----------------------------------------+
| Compute   | Virtual machines not determined by  | You can sign up with you own virtual    |
|           | you                                 | machines*                               |
|           |                                     |                                         |
|           |                                     |                                         |
+-----------+-------------------------------------+-----------------------------------------+
| Storage   | Block Storage                       | Block Storage & Object Storage          |
|           |                                     |                                         |
|           | - Small storage is available in     | - Each virtual machine instance has a   |
|           |   your home directory (usually      |   single boot persistent disk with a    |
|           |   around 1TB)                       |   default size of 10GB that can be      |
|           | - Some Scratch storage that is often|   adjusted up to 64TB*                  |
|           |   deleted after a certain amount of | - For storage that needs IO, consider   |
|           |   time                              |   persistent disks                      |
|           | - Storage is usually a shared       | - Google Cloud Storage (GCS) buckets are|
|           |   resource                          |   the most flexible and economical      |
|           |                                     |   storage option                        |
|           |                                     | - You can save objects to  GCS  buckets |
|           |                                     |   including images, videos, blobs, and  |
|           |                                     |   unstructured data                     |
+-----------+-------------------------------------+-----------------------------------------+
| Pricing   | Depends on the institution:         | Pay as you go                           |
|           |                                     |                                         |
|           | - Institution provides basic HPC    | - You pay for the compute resources and |
|           |   resources for researchers free of |   storage that you use*                 |
|           |   charge                            |                                         |
|           | - PIs requiring larger-scale        |                                         |
|           |   resources must purchase clusters  |                                         |
|           |   and storage space                 |                                         |
|           |                                     |                                         |
+-----------+-------------------------------------+-----------------------------------------+
| Do you    | Yes                                 | No                                      |
| have to   |                                     |                                         |
| wait?     | - Resources are shared among users  | - Once you've set up a Google Cloud     |
|           | - Scheduler systems used to schedule|   Platform account, you can spin up a   |
|           |   jobs based on resource            |   virtual machine and begin computing   |
|           |   availability                      |   quickly                               |
+-----------+-------------------------------------+-----------------------------------------+
| Is        | Yes and no, depends on what you're  | Compute resources and storage are       |
| machine   | trying to do; often it's a no       | unlimited, but you have to pay for it*  |
| powerful  |                                     |                                         |
| enough?   |                                     |                                         |
|           |                                     |                                         |
+-----------+-------------------------------------+-----------------------------------------+
| Accessing | Typically not stored on the HPC; you| Data is stored on the cloud             |
| Cancer    | have to download to your local      |                                         |
| Genomics  | machine                             |                                         |
| Data      |                                     |                                         |
+-----------+-------------------------------------+-----------------------------------------+
| How to    | Log in using Secure Shell           | Log in using Secure Shell               |
| connect   | protocol (SSH)                      | protocol (SSH)                          |
|           |                                     |                                         |
+-----------+-------------------------------------+-----------------------------------------+
***Be careful of costs** 




