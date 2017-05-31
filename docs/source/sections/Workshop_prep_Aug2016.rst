************************
Pre-Workshop Information
************************

This information is currently intended only for attendees of one of our
two August 2016 workshops 
(at `ISB <https://shmulevich.systemsbiology.org/cancer-genomics-cloud-workshop/>`_, 
and at the `UEF summer school <http://summerschool.uef.fi/sumsco-biomedical-data-science>`_).
After the workshops, all materials will be made available as part of the
ISB-CGC documentation here on readthedocs.

Important Information
#####################

* All workshop attendees should bring a personal laptop.  (A few loaner-laptops may be available at the ISB workshop  --  please contact us *ASAP* if you might need one.)
* A Google identity (*eg* your gmail address) is required in order to sign in to the `ISB-CGC Web App <https://isb-cgc.appspot.com/>`_.   If you don't already have a Google identity, you can `create one <https://accounts.google.com/SignUp?dsh=308321458437252901&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount#FirstName=&LastName=>`_.

**Google Cloud Platform (GCP) project**

* All workshop attendees will be provided with temporary credentials to a GCP project, but if you already have access to a GCP project you will be able to follow along using that project. 
 
* We encourage everyone who has not already taken advantage of the `free trial <https://cloud.google.com/free/>`_ offered by Google to do so.  This offer provides you with your own personal GCP project and $300 in "cloud credits" to be used over the course of one year.  (You will need to provide a credit card, but no charges will be billed to it without your consent.)

* Please note that some of the workshop examples will require that you have "Owner" privileges to a GCP project.  The temporary credentials mentioned above will only include "Editor" privileges.

**Questions?**

* Feel free to email us (workshop@isb-cgc.org) with any questions you might have about the workshop or to give us additional information about your specific use-cases and goals for the workshop.  The workshop will be your hands-on introduction to the ISB-CGC.


Preparing for the Workshop
##########################

Here are some ways that you can prepare for the workshop:

**Strongly Recommended:**

* install `Google Chrome <https://www.google.com/chrome/browser/desktop/>`_ on your laptop
* learn your way around the `Google Cloud Console <https://console.cloud.google.com>`_ -- follow along with this `15 minute tutorial <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Console.pdf>`_
* if you have your own GCP project, enable the following APIs: BigQuery, Genomics, and Compute Engine -- this should take `less than 5 minutes <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/enabling_new_APIs.pdf>`_

**Suggested:**

* install the `Cloud SDK <https://cloud.google.com/sdk/>`_ on your laptop
* install `R <https://cran.r-project.org/>`_ and `RStudio <https://www.rstudio.com/products/rstudio/download/>`_ on your laptop, and follow `these tips <GettingStartedWithR.html>`_ to get started
* sign in to and explore the `ISB-CGC Web App <https://isb-cgc.appspot.com/>`_, peruse the `ISB-CGC Documentation <http://isb-cancer-genomics-cloud.readthedocs.org/en/latest/>`_ and our `open-source code on GitHub <https://github.com/isb-cgc/>`_

**Additional Resources:**

* ISB-CGC / Google Cloud materials

  + `A Quick Tour of the Google Cloud Console <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Console.pdf>`_
  + `How to Enable APIs for your GCP Project <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/enabling_new_APIs.pdf>`_
  + `An Introduction to BigQuery <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_BigQuery.pdf>`_
  + `An Introduction to Cloud Datalab <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Cloud_Datalab.pdf>`_
  + `An Introduction to Cloud Shell <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/intro_to_Cloud_Shell.pdf>`_

..

* Google Genomics 

  + `Overview <https://cloud.google.com/genomics/>`_
  + `Sign up <https://cloud.google.com/genomics/#contact-form>`_ to receive the Google Genomics whitepaper
  + `github repositories <https://github.com/googlegenomics>`_
  + `Google Genomics Cookbook <https://googlegenomics.readthedocs.io/en/latest/>`_ with sections on:

    - finding `published data sources <https://googlegenomics.readthedocs.io/en/latest/use_cases/discover_public_data/index.html>`_
    - `data-processing <https://googlegenomics.readthedocs.io/en/latest/sections/process_data.html>`_ on the Google Cloud
    - `data-analysis <https://googlegenomics.readthedocs.io/en/latest/sections/analyze_data.html>`_ on the Google Cloud
    - accessing data using `IGV <https://googlegenomics.readthedocs.io/en/latest/use_cases/browse_genomic_data/igv.html>`_, `BioConductor <https://googlegenomics.readthedocs.io/en/latest/use_cases/browse_genomic_data/bioconductor.html>`_, `R <https://googlegenomics.readthedocs.io/en/latest/api-client-r/index.html>`_, `Python <https://googlegenomics.readthedocs.io/en/latest/use_cases/getting-started-with-the-api/python.html>`_ and more!

..

* DREAM challenges powered by `Sage Bionetworks <http://sagebase.org/>`_

  + `Overview <http://dreamchallenges.org/>`_
  + `Design and Methodology <http://dreamchallenges.org/designmethodology/>`_
  + `FAQ <http://dreamchallenges.org/faqs/>`_
  + `Somatic Mutation Calling Challenge: RNA <https://www.synapse.org/#!Synapse:syn2813589/wiki/401435>`_ -- Registration is now open!
  + `Publications <http://dreamchallenges.org/publications/>`_ from past challenges


..

