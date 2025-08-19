*****************************
Getting Started with Analysis
*****************************

ISB-CGC enables researchers to analyze cloud-based cancer data through a collection of powerful web-based tools and Google Cloud technologies. Learn more about the different analytical methods ISB-CGC users employ on their research projects. 

Google Cloud Project Setup and Data Access
##########################################################
A Google Cloud Project (GCP) is required to make use of all of the data, tools, and Google Cloud functionality.

**Obtain a Google identity**

 - Do you or your institution already have a Google identity, such as a Gmail account? If so, you can proceed to the next step.
 - If not, it only takes a minute to `create a Google identity <https://accounts.google.com/signup/v2/webcreateaccount?dsh=308321458437252901&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount&flowName=GlifWebSignIn&flowEntry=SignUp#FirstName=&LastName=>`_.  You can even link a non-Gmail account (eg. scientist@nih.gov) as a Google identity by `this <https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp&nogm=true>`_ method.

**Request Google Cloud Credits**

 - Take advantage of a one-time `$300 Google Credit <https://cloud.google.com/free/>`_.
 - If you have already used this one-time offer (or there is some other reason you cannot use it), see this information about how to request `ISB-CGC Cloud Credits <HowtoRequestCloudCredits.html>`_.

**Set up a Google Cloud Project**

 - See Google's documentation about how to `create a Google Cloud Project <https://cloud.google.com/resource-manager/docs/creating-managing-projects>`_.
 - Learn about how to `add members and roles to a project <https://cloud.google.com/iam/docs/quickstart>`_.
 - `Enable Required Google Cloud APIs <https://cloud.google.com/apis/docs/getting-started#enabling_apis>`_

**Connect to ISB-CGC's cancer data tables in Google BigQuery**
 
 - To obtain access to the ISB-CGC open access project tables in BigQuery, users can link these tables to their GCP project as described `here <progapi/bigqueryGUI/LinkingBigQueryToIsb-cgcProject.html>`_.
  
**Access open-access data**

 - All individual processed data files are accessible through GDC Google Cloud Storage buckets; ISB-CGC provides pointers to these files. Examples of how to find these URLs are in `this section <Hosted-Data.html>`_, on each Program's documentation page; these SQL queries can also be incorporated into notebooks or workflows.

**Getting Started with Analysis**

Now you're ready to perform analysis. ISB-CGC offers analysis with Google BigQuery and analysis using APIs and VMs.

Interactive web-based Cancer Data Analysis & Exploration
##########################################################
Explore and analyze ISB-CGC cancer data through a suite of graphical user interfaces (GUIs) that allow users to select and
filter data from one or more public data sets (such as TCGA, CCLE, and TARGET), combine these with your own uploaded data and analyze using a variety of built-in visualization tools.

.. list-table::
   :widths: 60, 40
   :header-rows: 0 

   * - Integrative Genomics Viewer (IGV)
        | *Explore and visualize genomic data. IGV is no longer integrated with ISB-CGC*
     - * `Integrative Genomics Viewer (IGV) website <https://igv.org/>`_
   * - Mitelman Database for Chromosome Aberrations and Gene Fusions in Cancer
        | *Explore relationships between chromosomal changes and cancer*
     - * `ISB-CGC Mitelman Database Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/Mitelman_about.html>`_
       * `ISB-CGC Mitelman Database <https://mitelmandatabase.isb-cgc.org/>`_
   * - The *TP53* Database
        | *The TP53 Database is no longer hosted by ISB-CGC. Explore TP53 variant data that have been reported in the published literature or are available in other public databases.*
     - * The *TP53* `Database <https://tp53.cancer.gov//>`_
     
Cancer data analysis using Google BigQuery
##########################################################
Processed data are consolidated by data type (ex. Clinical, DNA Methylation, RNAseq, Somatic Mutation, Protein Expression, etc.) from sources including 
the Genomics Data Commons (GDC) and Proteomics Data Commons (PDC) and transformed
into ISB-CGC Google BigQuery tables. This allows users to quickly analyze information from thousands of patients in curated BigQuery tables using Structured Query Language (SQL). SQL can be used from the Google BigQuery Console but can also be embedded within Python, R and complex workflows, providing users with flexibility. The easy, yet cost effective,  “burstability” of BigQuery allows you to, within minutes (as compared to days or weeks on a non-cloud based system), calculate statistical correlations across millions of combinations of data points. 

.. list-table::
   :widths: 60, 40
   :header-rows: 0
 
   * - **BigQuery Table Search User Interface**
        | *Learn more about ISB-CGC hosted BigQuery tables* 
     - * `ISB-CGC BigQuery Table Search Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/BigQueryTableSearchUI.html>`_
       * `ISB-CGC BigQuery Table Search <https://bq-search.isb-cgc.org/>`_
   * - **Google BigQuery Console**
        | *Use SQL to analyze and query ISB-CGC cancer data stored in Google’s cloud-based data warehouse* 
     - * `ISB-CGC BigQuery Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/BigQuery.html>`_
       * `Google BigQuery Documentation <https://cloud.google.com/bigquery/what-is-bigquery>`_
       * `Google Cloud BigQuery Console <https://console.cloud.google.com/bigquery>`_
   * - **Notebooks** 
        | *Seamlessly integrate ISB-CGC tables with R and Python to conduct robust analyses*
     - * `ISB-CGC Notebook Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/HowTos.html>`_  
       * `ISB-CGC Statistical Notebook Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/RegulomeExplorerNotebooks.html>`_
       * `ISB-CGC Machine Learning Notebook Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/MachineLearningNotebooks.html>`_
       * `ISB-CGC HTAN Notebook Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/HTANNotebooks.html>`_
       * `ISB-CGC Mitelman Database Notebook Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/MitelmanDBNotebooks.html>`_


Cancer data analysis using APIs & Google Cloud Virtual Machines
#################################################################
ISB-CGC enables the use of as many workflow technologies as possible through documentation, support, and necessary infrastructure.

.. list-table::
   :widths: 60, 40
   :header-rows: 0
 
   * - **ISB-CGC APIs**
        | *Programmatically access data and user-generated cancer patient cohort information* 
     - * `ISB-CGC API Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/progapi/progAPI-v4/Programmatic-Demo.html>`_
       * `ISB-CGC API <https://api-dot-isb-cgc.appspot.com/v4/swagger/>`_
   * - **Connecting to GA4GH:**
        | *Easily connect to APIs from ISB-CGC*
     - * `How to find a tool using GA4GH TRS Notebook <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_find_a_tool_using_GA4GH_TRS.ipynb>`_ 
       * `How to use a GA4GH tool using WES Notebook <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_use_a_GA4GH_tool_using_WES.ipynb>`_ 
   * - **Running workflows on ISB-CGC**
        | *Execute open-source and custom pipelines/algorithms on scalable virtual machines*
     - * `ISB-CGC Workflow Documentation <gcp-info/GCE-101.html>`_  
       * We recommend tools such as the `Google Cloud SDK <https://cloud.google.com/sdk/>`_, `Google Compute Engine <https://cloud.google.com/compute/>`_, `Virtual Machines <https://en.wikipedia.org/wiki/Virtual_machine>`_ and `Docker <https://www.docker.com/why-docker#/VM>`_ to assist your analyses. 

   
