=======================
Running Nextflow RNA-seq
=======================


This Nextflow workflow maps read-pairs to a reference genome and produces a transcript. By using software containers, `Nextflow <https://www.nextflow.io>`_ enables scalable and reproducible scientific workflows. Pipelines can be written in the most common scripting languages.


Requirements:
=============

- Docker
- Java (required to install Nextflow)
- Nextflow
- Graphviz


To install Docker, Graphviz and Nextflow, see our `VM Workflow Tools Installation Cheatsheet <Cheatsheet.html>`_ for instructions.

Download this tutorial:
=======================
::

 $sudo add-apt-repository universe
 $sudo apt update
 $sudo apt install subversion

 #cloning this tutorial
 $svn checkout https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/trunk/Nextflow-RNAseq

Running Nextflow
================
You should have a **Nextflow-RNAseq** directory :
::

   Nextflow-RNAseq
            ├── data
            │   ├── sample_1.fq
            │   ├── sample_2.fq
            │   ├── sample.fa
            │   └── sample.gtf
            ├── main.nf
            └── nextflow.config

The file **main.nf** contains all the code to execute the workflow, and **nextflow.config** provides the name of the Docker image that contains all of the tools for this run.
To run:
::

 #Assume the executable file "nextflow" is installed in the same directory with the folder you downloaded "Nextflow-RNAseq".
 $./nextflow run Nextflow-RNAseq

After the workflow finishes running, the folder should look like this:

::

  Nextflow-RNAseq
            ├── data
            │   ├── sample_1.fq
            │   ├── sample_2.fq
            │   ├── sample.fa
            │   └── sample.gtf
            ├── main.nf
            ├── nextflow.config
            ├── [reference]
            │   ├── [index.1.ht2]
            │   ├── [index.2.ht2]
            │   ├── [index.3.ht2]
            │   ├── [index.4.ht2]
            │   ├── [index.5.ht2]
            │   ├── [index.6.ht2]
            │   ├── [index.7.ht2]
            │   └── [index.8.ht2]
            └── [results]
                ├── [final_ref.gtf]
                ├── [final_transcript.gtf]
                ├── [sample.bam]
                ├── [sample.sam]
                └── [sample.tsv]



Running Nextflow with visualization
===================================

Use the following command:
::

 #Assume the executable file "nextflow" is installed in the same directory with the folder you downloaded "Nextflow-RNAseq".
 $./nextflow run Nextflow-RNAseq -with-dag flowchart.png


An image file with the name **flowchart.png** will be available to download.
It should look like this:

.. image:: images/Nextflow-RNAseq.png
   :align: center
