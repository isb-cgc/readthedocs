VM Workflow Tools Installation Cheat Sheet
##########################################

When working with a new Virtual Machine (VM), installing software, packages, and dependencies is usually required, and the process can be cumbersome. This cheat sheet was created with running workflows on Google Cloud VM in mind. It contains quick shortcuts to install common software, dependencies, and quick fixes.

********
NEXTFLOW
********

Install:
========

::

    $ export NXF_VER=20.01.0
    $ export NXF_MODE=google
    $ curl https://get.nextflow.io | bash

*********
SNAKEMAKE
*********

Step 1 install Miniconda:
=========================

`Installer  <https://docs.conda.io/en/latest/miniconda.html#linux-installers>`_
| `Instructions <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`_

.. note::  After “conda init fish” step **restarting your VM command line** is needed.
 In addition, if the conda command is not found, try: $export PATH=./miniconda3/bin/:$PATH

Step 2 install Snakemake:
=========================

`Instructions <https://snakemake.readthedocs.io/en/stable/getting_started/installation.html#conda-install>`_

Installer:

::

  $ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  
Snakemake environment:
----------------------

Create and activate Environment for Snakemake from a file (yml/yaml):

::

  $ conda env create --name <yourEnvironmentName> --file environment.yaml
  $ source activate <yourEnvironmentName>

Update current environment:

::

    $ conda env update -f environment.yml

.. note:: For more conda commands, visit: `Conda Cheat sheet <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`_.

***
WDL
***

`Installers <https://github.com/broadinstitute/cromwell/releases>`_ for Cromwell and Womtool

::

   $ wget https://github.com/broadinstitute/cromwell/releases/download/52/cromwell-52.jar
   $ wget https://github.com/broadinstitute/cromwell/releases/download/52/womtool-52.jar
   
***
CWL
***

::

  $ sudo apt-get install python-pip
  $ pip install --upgrade pip
  $ pip install cwltool


********
GENEFLOW
********

`Instructions and Source Code <https://github.com/CDCgov/geneflow2>`_

Install Python3 and Pip (see below), then install GeneFlow in a virtual environment with the following:

::

  $ python3 -m venv gf
  $ source gf/bin/activate
  $ pip3 install geneflow

Be sure to always activate the GeneFlow Python virtual environment before using the GeneFlow command line. 


*******************
Common dependencies
*******************

Java
====

::

  $ sudo apt install default-jre

Python
======

::

  $ sudo apt-get update
  $ sudo apt-get install python3.6

Pip install/Python-pip
======================

::

  $ sudo apt-get install python-pip
  $ pip install --upgrade pip

DOCKER
======

Install:
--------

For Ubuntu:

::

  $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  $ sudo apt-get update
  $ apt-cache policy docker-ce
  $ sudo apt-get install -y docker-ce

For Debian:

::

  $ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
  $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
  $ sudo apt-get update
  $ apt-cache policy docker-ce
  $ sudo apt-get install -y docker-ce


Check docker status:
--------------------
::

  $ sudo systemctl status docker

Check docker installation:
--------------------
::

  $ docker run hello-world

If docker doesn't run, try the fix right below or read more `here <https://linoxide.com/linux-how-to/use-docker-without-sudo-ubuntu/>`_.



Permission denied
-----------------
error prompt:

::

  docker: Got permission denied while trying to connect to the Docker daemon socket at unix

Try:
::

  $ sudo groupadd docker
  $ sudo usermod -aG docker ${USER}
  close VM and reopen


DOCKER Daemon not running:
--------------------------
::

  $ sudo service docker start
  $ sudo dockerd



Graphviz
========

::

  $ sudo apt-get install graphviz

Git/github
==========

::

  $ sudo apt install git


Wget
====
::

  $ sudo apt-get install wget
  

Subversion
==========

::

  $ sudo add-apt-repository universe
  $ sudo apt update
  $ sudo apt install subversion



*******
GCSFUSE
*******

Mount a bucket to your folder:

::

  $ gcsfuse bucketname myfolder/to/mount

Mount a subdirectory from your bucket to your VM folder:
::

  $ gcsfuse --only-dir subdirectory bucketName myFolder/to/mount

****************************
Set PATH for executable file
****************************

::

  $ export PATH=~/where/you/install/theProgram:$PATH
