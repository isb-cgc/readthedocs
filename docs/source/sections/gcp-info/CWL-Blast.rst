==================
Running CWL Blast
==================


This workflow extracts contigs of interest from a mixed library of DNA, uses Blastn and Python scripts



Requirements:
=============


-  CWLtool
-  Docker
-  Python (to run the scripts)

To install Docker, Python, and CWL, you can visit our **Cheatsheet** listed below:

- `Cheatsheet <https://isb-cancer-genomics-cloud.readthedocs.io/en/kyle-staging/sections/gcp-info/Cheatsheet.html>`_


.. note:: Requirements is crucial in order to run this workflow, please make sure you have them installed properly prior to running this workflow.




Download this tutorial:
::

  $ sudo add-apt-repository universe
  $ sudo apt update
  $ sudo apt install subversion

  #cloning this tutorial
  $ svn checkout https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/trunk/CWL-Blast

Rationale
==========

The input of this workflow (**sample.fa**) is produced by genome assembly software. It contains contigs from multiple organisms (eukaryote, prokaryotes) because of the way the sample was prepared and sequenced.
In this example, we are interested in the prokaryote genome only, and will separate their contigs from the eukaryote ones. In order to do that, Blastn will do sequence alignment between the contigs and the prepared blast database (files in the folder **db**).
The output of Blastn will be a table, which maps the contig headers to the appropriate species. Then we demonstrate how to incorporate the use of python helper scripts in our pipeline to extract the prokaryotes' headers (**scripts/Extract_Headers.py**), contigs (**scripts/Extract_Contigs.py**), and nucleotide count (**scripts/Count_Nucleotides.py**) from the original Fasta file using the Blastn result.
The final output of the workflow will be 3 text files: **extracted_contigs.txt**, **Headers.txt**, **NucleoCount.txt**.



Running CWL
===========
You should have a **CWL-Blast** directory :

::

   CWL-Blast
   ├── blast.cwl
   ├── count_nucleotides.cwl
   ├── CWL-Blast.cwl
   ├── CWL-Blast.yml
   ├── data
   │   └── sample.fa
   ├── db
   │   ├── SampleDB.nhr
   │   ├── SampleDB.nin
   │   └── SampleDB.nsq
   ├── extract_contigs.cwl
   ├── extract_headers.cwl
   └── scripts
       ├── Count_Nucleotides.py
       ├── Extract_Contigs.py
       └── Extract_Headers.py


Let's run it by using:

::

  $ cd CWL-Blast
  $ cwltool CWL-Blast.cwl CWL-Blast.yml

Let's take a look at the folder after cwltool finishes:


::

  CWL-Blast
    ├── blast.cwl
    ├── Blastn.out
    ├── count_nucleotides.cwl
    ├── CWL-Blast.cwl
    ├── CWL-Blast.yml
    ├── data
    │   └── sample.fa
    ├── db
    │   ├── SampleDB.nhr
    │   ├── SampleDB.nin
    │   └── SampleDB.nsq
    ├── extract_contigs.cwl
    ├── extracted_contigs.txt
    ├── extract_headers.cwl
    ├── Headers.txt
    ├── NucleoCount.txt
    └── scripts
        ├── Count_Nucleotides.py
        ├── Extract_Contigs.py
        └── Extract_Headers.py



To see the result of this workflow, you can check it `here <https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/tree/master/Results/Blast>`_
