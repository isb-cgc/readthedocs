****************************
Support & Other Useful Links
****************************

.. _contact-us:

Contact Us
##########

For general information about the ISB-CGC please contact us at info@isb-cgc.org.
We are especially keen on learning about your particular use-cases, and how we can
help you take advantage of the latest in cloud-computing technologies to answer your
research questions.

For feature-requests or bug-reports, please send e-mail to feedback@isb-cgc.org.

.. _request-gcp:

Your Own GCP project
####################

To request an ISB-CGC funded Google Cloud Platform (GCP) project, please send a request to request-gcp@isb-cgc.org.
(Note that if you *already* have a GCP project, and are not requesting funds as part of our
community evaluation phase, you do not need a separate GCP project in order to work with ISB-CGC
hosted data or tools.)

In your request, please describe your research goals in some detail, including information such as the type 
of data that you plan to use (whether it is your own data that you plan to upload or
TCGA data currently hosted by the ISB-CGC), the algorithms and/or methods you plan to apply,
and an estimate of the storage and computing costs you expect to incur.
Please let us know if you have students or collaborators who will also be accessing the
same cloud project.  Note that if you are working as a team on a single project, you should all
use the same cloud project -- if your group is large, we will take this into consideration when
determining your funding level.

If you have previous experience using the Google Cloud Platform, that would be 
useful for us to know -- including which specific components (*eg* Compute Engine, BigQuery,
Cloud Datalab, *etc*).

All reasonable requests will receive an
initial allocation of $300 towards storage and compute costs.  We expect that this
amount of funding will be more than enough for you 
to become familiar with the platform.  If you expect that you will need additional funding 
to complete your planned research, this initial amount should be used to perform prototype
analyses and to better estimate your total costs.  At that time, you may request additional funding.

Please be aware that we will be monitoring your cloud resource usage on a daily basis and will alert you as you begin
to approach your funding limit.  If you exceed your allocation limit and we are not able to contact
you by email for several days, we may need to take action to shut your project down which could cause you to lose work and data.

Other Useful Links
##################

The ISB-CGC platform is built on top of the Google Cloud Platform and has been designed to make
the TCGA data as accessible as possible to a wide
range of users.  For the programmatic users, this includes *complete* access to the tools that Google
is pioneering to allow users to scale-up their analyses on the Google infrastructure using a variety of means.

The ISB-CGC documentation and the example code on github will continue to grown to provide
starting-points and use-cases designed to suit the needs of a variety of end-users.  If you 
have a particular use-case that has not yet been addressed, please contact us 
(email info@isb-cgc.org) and we will work with you to determine the best approach to 
run the analysis you have in mind. 

**Cloud Datalab** is a powerful web-based interactive computational environment built on the 
familiar IPython (now known as Jupyter) environment, running on a Google VM in your own Google Cloud Project. 
Cloud Datalab_ allows you to combine
SQL-like queries into the TCGA BigQuery tables with all the power of Python packages like Pandas
and Matplotlib.  See our examples-Python_ repository on github.

.. _Datalab: https://datalab.cloud.google.com/
.. _examples-Python: https://github.com/isb-cgc/examples-Python

**Google Genomics** provides tools for storing, processing, exploring, and sharing DNA sequence
reads, reference-based alignments, and variant calls, using Google's infrastructure.  An extensive
Cookbook_ here on Read the Docs as well as an ever-growing set of examples on github_ showcase
some of the tools at your disposal.  Note that currently, only CCLE data is stored in Google Genomics

.. _Cookbook: https://googlegenomics.readthedocs.org/en/latest/
.. _github: https://github.com/googlegenomics


