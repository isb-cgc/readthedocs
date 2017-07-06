********************************************
9/22 ISB-CGC Webinar - Using BigQuery with R
********************************************

This tutorial will be conducted live and allow you to follow along.

The goal of this tutorial is to show you how to explore our BigQuery tables and answer any questions you might have.

It is also a useful time for us to gather feedback and learn what our users want to be able to do. So please come with your research questions and we can try to tackle them together.

Meeting Details
***************

:Date: September 22, 2016
:Time: 10:00 AM Pacific Time, 1:00 PM Eastern Time
:WebEx Link: `https://srameeting.webex.com/srameeting/j.php?MTID=m5612d723f442fb44e016bd58d2ea3920 <https://srameeting.webex.com/srameeting/j.php?MTID=m5612d723f442fb44e016bd58d2ea3920>`_
:Audio Bridge: 1-800-747-5150, Access Code: 3201312   `Global Conference Dial-In Numbers <https://conf.cfer.com/?an=8007475150&ac=3201312&startview=gos&login=true>`_

Topics
******

Cloud Console
-------------

First let's start at the `cloud console <https://console.cloud.google.com>`_.

- Manage project settings : IAM link for permission settings
- Settings, project names
- Quotas, set maximum usage
- Buckets, used for bringing in large tables. (create / delete)
- CloudShell, can connect to a VM

BigQuery
--------

`BigQuery <https://bigquery.cloud.google.com>`_

`BigQuery Reference <https://cloud.google.com/bigquery/query-reference>`_

- The browser interface

  - query & job histories
  - switching projects

    - adding project to your workspace (silver-wall-555)

  - making data sets.

    - by saving queries

- New Tables

  - CCLE (cancer cell line encyclopedia)

    - https://portals.broadinstitute.org/ccle/home
    - check out mutation calls, schema, details, preview

  - GDC metadata for files https://gdc.cancer.gov/
  - genome references
  - tcga_hg19_data_v0

    - methylation by chr
    - joined RNA-seq tables (mRNA_UNC_RSEM)
    - joined miRNA tables (miRNA_Expression)
    - isoform tables

  - cohorts

- `example queries <https://github.com/isb-cgc/readthedocs/blob/master/docs/include/big_query_examples.sql>`_


Using R
-------


- `getting set up. <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/GettingStartedWithR.html>`_

  - `the bigrquery library <https://github.com/rstats-db/bigrquery>`_
  - `the bigrquery CRAN page <https://cran.r-project.org/web/packages/bigrquery/index.html>`_
  - bigrquery functions

- `The examples-R github repo <https://github.com/isb-cgc/examples-R>`_

  - installing the package
  - tour of the package

- `workshop doc v2 <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/workshop/Workshop_R_tut_v2.html>`_

- extra links

  - `advanced: using dplyr to make queries <https://cran.r-project.org/web/packages/dplyr/vignettes/databases.html>`_
  - `workshop doc #1 <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/workshop/Workshop_R_tut.html>`_



Other useful Links
******************

* `DIY Workshop <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/DIYWorkshop.html>`_ - Please look for the links under "ISB-CGC Open-Access BigQuery Tables."
* `Google BigQuery <https://cloud.google.com/bigquery/>`_
* `Google Examples <https://support.google.com/analytics/answer/4419694?hl=en>`_
* `Getting Started with R <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/GettingStartedWithR.html>`_
* `Code examples can be found at our github repo. <https://github.com/isb-cgc/examples-R>`_
* `BigQuery Workshop doc v2 <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/workshop/BQ_SQL_tut_v2.html>`_
