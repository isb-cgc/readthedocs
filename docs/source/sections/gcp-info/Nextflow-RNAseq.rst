=======================
Running NEXTFLOW RNAseq
=======================


Requirements:
=============

- Docker
- Java (required to install Nextflow)
- Nextflow


To install Docker and Nextflow, you can visit our **Cheatsheet**.
- `Cheatsheet <http://insertlink>`_

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

The file **main.nf** contains all the codes to execute the workflow, and **nextflow.config** provide the name of docker image that contains all the tool for this run.
To run:
::

 #Assume the executable file "nextflow" is installed in the same directory with the folder you download "Nextflow-RNAseq"
 $./nextflow run Nextflow-RNAseq

After finish running the folder should look like this:

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
