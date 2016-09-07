*****************************
Integrative Analysis Tutorial
*****************************

This tutorial is intended to guide you through several different components of the ISB-CGC platform
and some of the different ways that you can approach working with the data that is available in
Google Cloud Storage, BigQuery, and Google Genomics.

In this example, we will study the potential effects of HPV integration on the
expression of recurrent target genes in CESC and HNSC tumors. This example
demonstrates the use of BigQuery and R to query multiple tables across
multiple data sets. We will also show users how to bring in their own data to
use in conjunction with the TCGA data already available as BigQuery tables. In
this exercise, we will (loosely) reproduce a figure from Tang et. al.,
visualizing altered expression of host genes frequently targeted by HPV.

References:
Tang et. al. The landscape of viral expression and host gene fusion and adaptation in human cancer.
Nature Communications 4, Article number:2513|doi:10.1038/ncomms3513

.. toctree::
   :maxdepth: 1

   WebApp_tut
   BQ_SQL_tut
   Workshop_R_tut
