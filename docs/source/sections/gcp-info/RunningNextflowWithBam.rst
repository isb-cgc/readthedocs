=========================================================
Running NEXTFLOW pipeline on public Bam file From ISB-CGC
=========================================================

The same pipeline in Snakemake can be found at

.. toctree::
   :maxdepth: 1

   RunningSnakemakeWithBam.rst


Requirements:
=============

- Docker
- Gcsfuse
- Nextflow
- A public bam file from ISB-CGC at the address: gs://gdc-ccle-open/692a845c-7957-41f2-b679-5434c69ba25b/G27328.Calu-6.1.bam

To install Docker and Nextflow, you can visit our **Cheatsheet**, and to set up the gcsfuse to get access to the bam file please visit **Running Workflow with GCSFUSE** listed below:

.. toctree::
   :maxdepth: 1

   Cheatsheet.rst
   WorkflowWithGCSFUSE.rst


Download this tutorial:
=======================
::

 $sudo add-apt-repository universe
 $sudo apt update
 $sudo apt install subversion

 #cloning this tutorial
 $svn checkout https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/trunk/Nextflow-GCgather

Running Nextflow
================
You should have a **Nextflow-GCgather** directory with 1 file called **Nextflow-GCgather.nf** inside. We are going to change the address in this file to the one you created in the **Running Workflow with GCSFUSE** tutorial

::

  #go into the folder
  $cd Nextflow-GCgather
  $nano Nextflow-GCgather.nf

At the top of the file you will see this:

::

  #!/usr/bin/env nextflow
  myBamSample = Channel.fromPath('/home/thinh_vo/sample/*.bam')


Replace "/home/thinh_vo/sample/\*.bam" with your new address from the gcsfuse tutorial for example: "/opt/testGcsfuse/\*.bam". Now the script is ready to run with Nextflow.

::

  #go to where the Nextflow executable file was installed in this example it will be outside the Nextflow-GCgather directory
  #first, we go out of Nextflow-GCgather directory
  $cd ..
  #execute nextflow with docker image:
  $./nextflow run Nextflow-GCgather/Nextflow-GCgather.nf -with-docker gcr.io/genomics-tools/samtools

.. note:: This Bam file is quite large, it may take about 15 mins ~ 20 mins to run.

Once Nextflow is finished, the result will be on the screen, or you can find it at **Nextflow-GCgather/Sam_results/final_gc_stats_out.txt**

Running Nextflow with visualization
-----------------------------------
You can use this command instead to run Nextflow, it will out put a visualization file named "flowchart.png"


::

  $./nextflow run Nextflow-GCgather/Nextflow-GCgather.nf -with-dag flowchart.png


It should look like this:

.. image:: RunningNextflowWithBam.png
   :align: left
