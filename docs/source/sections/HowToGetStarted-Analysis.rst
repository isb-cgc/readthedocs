*****************************
Getting Started with Analysis
*****************************

ISB-CGC enables researchers to analyze cloud-based cancer data through a collection of powerful web-based tools and Google Cloud technologies. Learn more about the different analytical methods ISB-CGC users employ on their research projects. 

Interactive web-based Cancer Data Analysis & Exploration
##########################################################
Explore and analyze ISB-CGC cancer data through a suite of graphical user interfaces (GUIs) that allow users to select and
filter data from one or more public data sets (such as TCGA, CCLE, and TARGET), combine these with your own uploaded data and analyze using a variety of built-in visualization tools.

.. list-table::
   :widths: 60, 40
   :header-rows: 0 

   * - **Cohort Builder/Data Explorer**
         | *Create and explore cohorts of interest*
     - * `ISB-CGC Cohort Builder/Data Explorer Documentation <DataExplorer.html>`_ 
       * `ISB-CGC Cohort Builder/Data Explorer <https://isb-cgc.appspot.com/cohorts/new_cohort/>`_ 
   * - **Interactive Pathology and Radiology Image Viewers**  
        | *View images from cancer patients using integrated image viewers*
     - * `ISB-CGC Image Viewers Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/OsimisWebViewer.html>`_ 
   * - **Integrative Genomics Viewer (IGV)**
        | *Explore and visualize genomic data*
     - * `ISB-CGC Integrative Genomics Viewer (IGV) Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/IGV-Browser.html>`_
   * - **Cancer Data File Browser**   
        | *Browse and identify files associated with cohorts of interest*
     - * `ISB-CGC Cancer Data File Browser Documentation <DataBrowser.html>`_
       * `ISB-CGC Cancer Data File Browser <https://isb-cgc.appspot.com/cohorts/filelist/>`_ 
   * - **Mitelman Database for Chromosome Aberrations and Gene Fusions in Cancer**
        | *Explore relationships between chromosomal changes and cancer*
     - * `ISB-CGC Mitelman Database Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/Mitelman_about.html>`_
       * `ISB-CGC Mitelman Database <https://mitelmandatabase.isb-cgc.org/>`_
     
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
       * `ISB-CGC BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_
   * - **Google BigQuery Console**
        | *Use SQL to analyze and query ISB-CGC cancer data stored in Google’s cloud-based data warehouse* 
     - * `ISB-CGC BigQuery Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/BigQuery.html>`_
       * `Google BigQuery Documentation <https://cloud.google.com/bigquery/what-is-bigquery>`_
       * `Google Cloud BigQuery Console <https://console.cloud.google.com/bigquery>`_
   * - **Notebooks** 
        | *Seamlessly integrate ISB-CGC tables with R and Python to conduct robust analyses*
     - * `ISB-CGC Notebook Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/HowTos.html>`_  
       * `ISB-CGC Statistical Notebook Documentation <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/RegulomeExplorerNotebooks.html>`_

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
   * - **Connecting to GA4GH and Cloud Life Sciences APIs:**
        | *Easily connect to APIs from ISB-CGC*
     - * `How to find a tool using GA4GH TRS Notebook <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_find_a_tool_using_GA4GH_TRS.ipynb>`_ 
       * `How to use a GA4GH tool using WES Notebook <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_use_a_GA4GH_tool_using_WES.ipynb>`_ 
       * `Google API Documentation <https://cloud.google.com/life-sciences/docs/apis>`_
   * - **Running workflows on ISB-CGC**
        | *Execute open-source and custom pipelines/algorithms on scalable virtual machines*
     - * `ISB-CGC Workflow Documentation <gcp-info/GCE-101.html>`_  
       * We recommend tools such as the `Google Cloud SDK <https://cloud.google.com/sdk/>`_, `Google Compute Engine <https://cloud.google.com/compute/>`_, `Virtual Machines <https://en.wikipedia.org/wiki/Virtual_machine>`_ and `Docker <https://www.docker.com/why-docker#/VM>`_ to assist your analyses. 

   
