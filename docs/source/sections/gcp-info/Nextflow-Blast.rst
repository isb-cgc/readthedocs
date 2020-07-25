======================
Running NEXTFLOW Blast
======================

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

 #Assume the executable file "nextflow" is installed in the same directory with the folder you download "Nextflow-RNAseq"
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
