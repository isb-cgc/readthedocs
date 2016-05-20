************************
ISB-CGC Workshops at NCI
************************

Differential gene expression associated with HPV integration
############################################################

In this example, we will study the potential effects of HPV integration on the
expression of recurrent target genes in CESC and HNSC tumors. This example
demonstrates using R to issue BigQuery queries involving multiple tables across
multiple data sets. We will also show users how to bring in their own data to
use in conjunction with the TCGA data already available as BigQuery tables. In
this exercise, we will reproduce some figures from Tang et. al. [1] to visualize
altered expression of host genes frequently targeted by HPV.

References:
Tang et. al. The landscape of viral expression and host gene fusion and adaptation in human cancer.
Nature Communications 4, Article number:2513|doi:10.1038/ncomms3513

Loading libraries
=================

.. code-block:: R
    require(bigrquery,quietly = TRUE) || install.packages('bigrquery',verbose = FALSE)
    require(tidyr,quietly = TRUE) || install.packages('tidyr',verbose = FALSE)
    require(dplyr,quietly = TRUE) || install.packages('dplyr',verbose = FALSE)
    require(ggplot2,quietly = TRUE) || install.packages('ggplot2',verbose = FALSE)
    require(broom,quietly = TRUE) || install.packages('broom',verbose = FALSE)


Your project ID
===============

You will be using your own project ID. At certain points in the code, it will
be necessary to complete the code.

.. code-block:: R
    main_cloud_project="isb-cgc"
    my_cloud_project = "your_project_id"
    tcga_data_set = "tcga_201510_alpha"
    workshop_ds = "workspace"

First query
===========

Now let's see if things are working.

.. code-block:: R
    bigrquery::list_tables(main_cloud_project, tcga_ds)
