Pipelines and APIs 
*******************


APIs
============

ISB-CGC provides programmatic access to cancer data (both open and controlled-access) and metadata stored on the Google Cloud Platform through a combination of ISB-CGC APIs and Google APIs. Access to ISB-CGC metadata and user-data such as patient cohort definitions is provided through the ISB-CGC API.  For more details on Google Cloud APIs, please read the extensive in-depth Google Cloud APIs  `documentation <https://cloud.google.com/apis>`_.

.. toctree::
   :maxdepth: 1
   :hidden:
   
   progapi/progAPI-v4/Programmatic-Demo


Workflow Gallery
================

We have compiled a collection of tutorials and sample workflows designed to introduce users to running workflows (CWL, Nextflow, Snakemake, WDL, and GeneFlow) on the Google Cloud Platform (GCP). ISB-CGC does not make the choice for users but instead enables as many workflow technologies as possible through documentation, support, and where necessary, infrastructure.



.. toctree::
   :maxdepth: 1
   :hidden:
   
   gcp-info/GCE-101.rst


St. Jude Bioinformatics Tools
=============================

The following bioinformatics tools and workflows developed by St. Jude have been containerized and made available for execution in the cloud. Each link below navigates to the tools' original documentation. More detailed documentation for deployment and execution within ISB-CGC will be added in the future.

.. list-table::
   :widths: 100
   :align: center
   :header-rows: 1

   * - | **CICERO** (Clipped-reads Extended for RNA Optimization) is an assembly-based algorithm to detect diverse classes of driver gene fusions from RNA-seq.
       | `GitHub <https://github.com/stjude/CICERO>`_
   * - | **RNAIndel** calls coding indels from tumor RNA-Seq data and classifies them as somatic, germline, and artifactual.
       | `GitHub <https://github.com/stjude/RNAIndel>`_
   * - | **Teltale** is a program that computes the fraction of telomeric reads in a BAM file.
       | `GitHub <https://github.com/stjude/teltale>`_
   * - | **NetBID** (Network-based Bayesian Inference of Drivers) is a data-driven system biology pipeline and toolkit for finding drivers from transcriptomics, proteomics and phosphoproteomics data, where the drivers can be either transcription factors (TF) or signaling factors (SIG).
       | `GitHub <https://github.com/jyyulab/NetBID>`_

    
