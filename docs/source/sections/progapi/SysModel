Computational System Model
**************************

There are two primary ways in which users can interact with ISB-CGC data.  The first method is 
through graphical interfaces such as the ISB-CGC web application or the BigQuery web interface, which provides users a convenient web-based interface from which it is easy to create and visualize collections of data hosted by the ISB-CGC.

The second method is through the ISB-CGC programmatic API or through other Google Cloud APIs.  
The ISB-CGC API provides access to much of the same computational functionality as the 
web application, and the other Google APIs can be used to access the hosted data sets depending
on which technology is used to host them:  

  * the BigQuery `Web UI <https://cloud.google.com/bigquery/web-ui-quickstart>`_, `Command-Line Tool <https://cloud.google.com/bigquery/bq-command-line-tool-quickstart>`_, or `REST API <https://cloud.google.com/bigquery/bigquery-api-quickstart>`_ for the data stored in BigQuery tables; 
  * the Google Cloud Storage (GCS) `JSON API <https://cloud.google.com/storage/docs/json_api/>`_ or `gsutil <https://cloud.google.com/storage/docs/gsutil>`_ for the data stored in GCS objects; or
  * the `Genomics REST API <https://cloud.google.com/genomics/reference/rest/>`_ for data stored in Google Genomics.

For users interested in performing custom analyses, accessing the data directly using these APIs 
will provide greater flexibility.

`Here <bigqueryGUI/HowToAccessBigQueryFromTheGoogleCloudPlatform.html>`_ are instructions on how to access BigQuery from the Google Cloud Platform.

`Here <bigqueryGUI/LinkingBigQueryToIsb-cgcProject.html>`_ are instructions on how to see ISB-CGC data through the BigQuery Web UI.

`Here <bigqueryGUI/WalkthroughOfGoogleBigQuery.html>`_ are examples of how to query ISB-CGC data using BigQuery, including using multiple tables with Joins.

The Cloud Paradigm
##################

In addition to hosting the TCGA data in the cloud, one of the main goals of the ISB-CGC is to 
"bring the computation to the data".  There are many ways that this can be done using legacy
tools, cloud-native tools, or a combination of the two.  Regardless of the details of the particular 
solution, the single most important difference between the ISB-CGC computational system model 
and traditional HPC models is that there is no single monolithic system that is 
doing the computational work.  Cloud-native solutions instead abstract the configuration 
management process from the allocation of physical hardware, making it very easy to 
programmatically request an arbitrary number of identical machines, which can then be easily 
"torn down" (and regenerated) whenever necessary.  The configuration state of these machines 
will always be identical on startup, and can be parametrized according to your algorithm’s 
resource needs.  

One important implication to understand about this new computational paradigm is that the burden 
of system administration is partially shifted to the users of the cloud: researchers and developers.  
While numerous tools exist to help simplify these tasks, there is no IT department managing your 
cloud-computing.  This means that researchers will need to learn a new skill-set.

