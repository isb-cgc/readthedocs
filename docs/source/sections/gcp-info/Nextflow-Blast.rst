======================
Running NEXTFLOW Blast
======================


This workflow extracts contigs of interest from a mixed library of DNA, uses Blastn and Python Script


Requirements:
=============

- Docker
- Java (required to install Nextflow)
- Python (to run the scripts)
- Nextflow
- Graphviz


To install Docker, Java, Python, Graphviz and Nextflow, you can visit our **Cheatsheet**.


- `Cheatsheet <https://isb-cancer-genomics-cloud.readthedocs.io/en/kyle-staging/sections/gcp-info/Cheatsheet.html>`_

Download this tutorial:
=======================

::

 $sudo add-apt-repository universe
 $sudo apt update
 $sudo apt install subversion

 #cloning this tutorial
 $svn checkout https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/trunk/Nextflow-Blast


Rationales
==========

The input of this workflow (**sample.fa**) is produced by genome assembly software. It contains contigs from multiple organisms (eukaryote, prokaryotes) due to the way the sample was prepared and sequenced.
In this example, we are interested in the prokaryotes' genome only, and will separate their contigs from the eukaryote ones. In order to do that, Blastn will do sequence alignment between the contigs and the prepared blast database (files in the folder **db**).
The output of Blastn will be a table, which maps the contigs' headers to the appropriate species. Then we demonstrate how to incorporate the use of python helper scripts in our pipeline to extract the prokaryotes' headers (**scripts/Extract_Headers.py**), contigs (**scripts/Extract_Contigs.py**), and nucleotide count (**scripts/Count_Nucleotides.py**) from the original Fasta file using the Blastn result.
The final output of the workflow will be 3 text files: **extracted_contigs.txt**, **Headers.txt**, **NucleoCount.txt**.



Running Nextflow
================
You should have a **Nextflow-Blast** directory :

 ::

    Nextflow-Blast
        ├── data
        │   └── sample.fa
        ├── db
        │   ├── SampleDB.nhr
        │   ├── SampleDB.nin
        │   └── SampleDB.nsq
        ├── main.nf
        ├── nextflow.config
        └── scripts
            ├── Count_Nucleotides.py
            ├── Extract_Contigs.py
            └── Extract_Headers.py



The file **main.nf** contains all the codes to execute the workflow, and **nextflow.config** provide the name of docker image that contains all the tool for this run.
To run:
::

 #Assume the executable file "nextflow" is installed in the same directory with the folder you download "Nextflow-Blast"
 $./nextflow run Nextflow-Blast

After finish running the folder should look like this:

::

  Nextflow-Blast
        ├── data
        │   └── sample.fa
        ├── db
        │   ├── SampleDB.nhr
        │   ├── SampleDB.nin
        │   └── SampleDB.nsq
        ├── main.nf
        ├── nextflow.config
        ├── [results]
        │   ├── [Blastn.out]
        │   ├── [extracted_contigs.txt]
        │   ├── [Headers.txt]
        │   └── [NucleoCount.txt]
        └── scripts
            ├── Count_Nucleotides.py
            ├── Extract_Contigs.py
            └── Extract_Headers.py


Running Nextflow with visualization
===================================

Use the following command:
::

 #Assume the executable file "nextflow" is installed in the same directory with the folder you download "Nextflow-Blast"
 $./nextflow run Nextflow-Blast -with-dag flowchart.png


An image file with the name **flowchart.png** will be available to download.
It should look like this:

.. image:: images/Nextflow-Blast.png
   :align: center
