==========================================================
Running Snakemake pipeline on public Bam file From ISB-CGC
==========================================================

The same pipeline in Nextflow, CWL, WDL can be found at:

.. toctree::
   :maxdepth: 1

   RunningNextflowWithBam.rst
   RunningCWLWithBam.rst
   RunningWDLWithBam.rst



Requirements:
=============

- Anaconda/Miniconda and how to activate the conda environment from a file
- Gcsfuse
- A public bam file from ISB-CGC at the address: gs://gdc-ccle-open/692a845c-7957-41f2-b679-5434c69ba25b/G27328.Calu-6.1.bam

To install and set up Anaconda/Miniconda, you can visit the first tutorial **Your First Workflow on Google Cloud Virtual Machine**, and to set up gcsfuse to get access to the bam file please visit **Running Workflow with GCSFUSE** listed below:

.. toctree::
   :maxdepth: 1

   FirstWorkflow.rst
   WorkflowWithGCSFUSE.rst


Download this tutorial:
=======================
::

 $sudo add-apt-repository universe
 $sudo apt update
 $sudo apt install subversion

 #cloning this tutorial
 $svn checkout https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/trunk/Snakemake-GCgather

Running Snakemake
=================
You should have a **Snakemake-GCgather** directory with 2 files **Snakefile** and **environment.yml** inside. We are going to activate the conda environment from the file (see **Your First Workflow on Google Cloud Virtual Machine** for more information)
. Then we are going to change change the address in Snakefile to the one you created in the **Running Workflow with GCSFUSE** tutorial

::

  #go into the folder
  $cd Snakemake-GCgather
  $nano Snakefile

At the top of the file you will see this:

::

  #line 1:
  IDS, = glob_wildcards("/opt/testGcsfuse/{sample}.bam")
  #line 7-8:
  input:
      "/opt/testGcsfuse/{sample}.bam"


Replace "/opt/testGcsfuse/{sample}.bam" with your new address from the gcsfuse tutorial for example: "/opt/testGcsfuse/{sample}.bam". Now the script is ready to run with Snakemake.

::

  $snakemake

.. note:: This Bam file is quite large, it may take about 15 mins ~ 20 mins to run.

Once snakemake is finished, the result will be on the screen, or you can find it at **Snakemake-GCgather/final/final_gc_stats_out.txt**

Running Snakemake with visualization
------------------------------------
You can use this command instead to run Snakemake, it will out put a visualization file named "flowchart.svg"


::

  $snakemake --dag | dot -Tsvg > flowchart.svg


It should look like this:

.. image:: RunningSnakemakeWithBam.png
   :align: left
