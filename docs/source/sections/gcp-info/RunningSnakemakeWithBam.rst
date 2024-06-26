==========================================================
Running SNAKEMAKE pipeline on public Bam file from ISB-CGC
==========================================================


This workflow gathers GC content from a bam file or a list of Bam files to a text file.


Requirements:
=============

- Anaconda/Miniconda and how to activate the conda environment from a file
- Gcsfuse
- A public bam file from ISB-CGC at the address: gs://gdc-ccle-open/692a845c-7957-41f2-b679-5434c69ba25b/G27328.Calu-6.1.bam

To install and set up Anaconda/Miniconda, you can visit the first tutorial `Your First Workflow on Google Cloud Virtual Machine <FirstWorkflow.html>`_, To set up gcsfuse in order to get access to the BAM file, please visit `Running Workflow with GCSFUSE <WorkflowWithGCSFUSE.html>`_.


.. note:: The requirements above are crucial to running this workflow. Please make sure you have them installed properly prior to running this workflow



Download this tutorial:
=======================
::

 $ sudo add-apt-repository universe
 $ sudo apt update
 $ sudo apt install subversion

 #cloning this tutorial
 $ svn checkout https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/trunk/Snakemake-GCgather

Running Snakemake
=================
You should have a **Snakemake-GCgather** directory with 2 files **Snakefile** and **environment.yml** inside. We are going to activate the conda environment from the file (see **Your First Workflow on Google Cloud Virtual Machine** for more information)
. Then we are going to change change the address in Snakefile to the one you created in the **Running Workflow with GCSFUSE** tutorial

::

  #go into the folder
  $ cd Snakemake-GCgather
  $ nano Snakefile

At the top of the file you will see this:

::

  #line 1:
  IDS, = glob_wildcards("/home/thinh_vo/testGcsfuse/{sample}.bam")
  #line 7-8:
  input:
      "/home/thinh_vo/testGcsfuse/{sample}.bam"

Replace "/home/thinh_vo/testGcsfuse/{sample}.bam" with your new address from the gcsfuse tutorial for example: "/home/thinh_vo/testGcsfuse/{sample}.bam". Now the script is ready to run with Snakemake.

::

  $ snakemake

.. note:: This Bam file is quite large, it may take about 15 mins ~ 20 mins to run.

Once snakemake is finished, the result will be on the screen, or you can find it at **Snakemake-GCgather/final/final_gc_stats_out.txt**

Running Snakemake with visualization
------------------------------------
You can use this command instead to run Snakemake, it will out put a visualization file named "flowchart.svg"


::

  $ snakemake --dag | dot -Tsvg > flowchart.svg


It should look like this:

.. image:: images/RunningSnakemakeWithBam.png
   :align: left


To see the result of this workflow, you can check it `here <https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/tree/master/Results/GC-gather>`_
