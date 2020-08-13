====================================================
Running CWL pipeline on public Bam file from ISB-CGC
====================================================


This workflow gathers GC content from a bam file/ or a list of Bam file to a text file


Requirements:
=============

- Docker
- Gcsfuse
- CWLtool (CWL)
- A public bam file from ISB-CGC at the address: gs://gdc-ccle-open/692a845c-7957-41f2-b679-5434c69ba25b/G27328.Calu-6.1.bam

To install Docker and CWL, you can visit our **Cheatsheet**, and to set up the gcsfuse to get access to the bam file please visit **Running Workflow with GCSFUSE** listed below:

- `Cheatsheet <https://isb-cancer-genomics-cloud.readthedocs.io/en/kyle-staging/sections/gcp-info/Cheatsheet.html>`_
- `WorkflowWithGCSFUSE <https://isb-cancer-genomics-cloud.readthedocs.io/en/kyle-staging/sections/gcp-info/WorkflowWithGCSFUSE.html>`_




Download this tutorial:
=======================

::

 $ sudo add-apt-repository universe
 $ sudo apt update
 $ sudo apt install subversion

 #cloning this tutorial
 $ svn checkout https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/trunk/CWL-GCgather


Running CWLtool
===============

You should have a **CWL-GCgather** directory with 6 files inside: 1 main workflow file "CWL-GCgather.cwl", 4 **\*tools.cwl** and . We are going to change the address in **scatter_gather_pipeline.yml** file to the one you created in the **Running Workflow with GCSFUSE** tutorial

::

  #go into the folder
  $ cd CWL-GCgather
  $ nano scatter_gather_pipeline.yml

At the top of the file you will see this:

::

  filein:
    - {class: File, path: /opt/testGcsfuse/G27328.Calu-6.1.bam}


Replace "/home/thinh_vo/testGcsfuse/G27328.Calu-6.1.bam" with your new address from the gcsfuse tutorial for example: "/home/thinh_vo/testGcsfuse/G27328.Calu-6.1.bam". Now the script is ready to run with CWLtool.
Save the change, then run the script with this command:


::

 $ cwltool CWL-GCgather.cwl scatter_gather_pipeline.yml

If you receive this error: "docker: Got permission denied while trying to connect to the Docker daemon socket at unix"

Try:

::

  $ sudo groupadd docker
  $ sudo usermod -aG docker ${USER}
  close and reopen VM then run the script again


.. note:: This Bam file is quite large, it may take about 15 mins ~ 20 mins to run.

Once CWLtool is finished, the result will be in the same folder called "final_output.txt"

To see the result of this workflow, you can check it `here <https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/tree/master/Results/GC-gather>`_
