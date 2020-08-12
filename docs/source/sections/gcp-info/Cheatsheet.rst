VM Workflow Tools Installation Cheat Sheet
##########################################

When working with a new Virtual Machine (VM), more often than not installing software, packages and dependencies is required, and the process can be cumbersome. This cheat sheet was created with running workflows on Google Cloud VM in mind. It contains quick shortcuts to install common software, dependencies, and quick fixes.

********
NEXTFLOW
********

Install:
========
::

    $ export NXF_VER=20.01.0
    $ export NXF_MODE=google
    $ curl https://get.nextflow.io | bash



*******************
SNAKEMAKE
*******************
Step 1 install Miniconda:
=========================
`Installer  <https://docs.conda.io/en/latest/miniconda.html#linux-installers>`_
| `Instruction <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`_

.. note::  After “conda init fish” step **restarting your VM command line** is needed.
 In addition, if the conda command is not found, try: $export PATH=./miniconda3/bin/:$PATH



Step 2 install Snakemake:
=========================

`Instruction <https://snakemake.readthedocs.io/en/stable/getting_started/installation.html#conda-install>`_


Snakemake environment:
----------------------
Create and activate Environment for Snakemake from a file (yml/yaml):
::

  $ conda env create --name <yourEnvironmentName> --file environment.yaml
  $ source activate <yourEnvironmentName>

Updating current environment

::

    $ conda env update -f environment.yml

.. note:: for more conda commands, visit: `Conda Cheat sheet <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`_



***
WDL
***

`Installers <https://github.com/broadinstitute/cromwell/releases>`_ for Cromwell and Womtool

***
CWL
***
::

  $ sudo apt-get install python-pip
  $ pip install --upgrade pip
  $ pip install cwltool



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
::

  $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
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

if docker doesn't run try the fix right below or read more `here <https://linoxide.com/linux-how-to/use-docker-without-sudo-ubuntu/>`_
.



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
