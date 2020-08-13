==================
Running CWL RNA-seq
==================

This Common Workflow Language (`CWL <https://www.commonwl.org/>`_) `RNA-seq <https://www.technologynetworks.com/genomics/articles/rna-seq-basics-applications-and-protocol-299461#:~:text=RNA%2Dseq%20(RNA%2Dsequencing,patterns%20encoded%20within%20our%20RNA.>`_
 workflow maps read-pairs to a reference genome and produces a transcript. CWL enables the user to connect command line tools to create workflows; it is a specification and is therefore portable across platforms that support CWL.

Requirements:
=============

-  CWLtool
-  Docker


.. note:: Requirements is crucial in order to run this workflow, please make sure you have them installed properly prior to running this workflow.



Download this tutorial:
::

  $ sudo add-apt-repository universe
  $ sudo apt update
  $ sudo apt install subversion

  #cloning this tutorial
  $ svn checkout https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/trunk/CWL-RNAseq

To install Docker and CWL, see our `VM Workflow Tools Installation Cheatsheet <Cheatsheet.html>`_ for instructions.

Starting folder **CWL-RNAseq** should look like this:


::

  .
  └── CWL-RNAseq
      ├── create_bam.cwl
      ├── create_transcript.cwl
      ├── CWL-RNAseq.cwl
      ├── CWL-RNAseq.yml
      ├── data
      │   ├── sample_1.fq
      │   ├── sample_2.fq
      │   ├── sample.fa
      │   └── sample.gtf
      ├── hisat2_align.cwl
      └── index_build.cwl


An overview of the main CWL files:

-  **CWL-RNAseq.cwl** is the main cwl file that connects all other cwl tools and yml file together.
-  **CWL-RNAseq.yml** is the file that contains all the inputs that are necessary to run the pipeline.
-  **index_build.cwl** builds index files from a Fasta file, using Hisat2-build.
-  **hisat2_align.cwl** builds a sam file from forward and reverse reads, and the indices built from previous step, using Hisat2.
-  **create_bam.cwl** builds a bam file from the newly built sam file, using Samtools.
-  **create_transcript.cwl** creates transcript from the bam file from previous step, using Stringtie.

Let's take a look at some example of the main file **CWL-RNAseq.cwl**:
The first block describe what is required to run this workflow, more information on this CWL requirements can be found `here <https://www.commonwl.org/v1.0/CommandLineTool.html>`_
. Docker usage is also described in the **hints** section.

::

  #!/usr/bin/env cwl-runner

  cwlVersion: v1.0
  class: Workflow
  requirements:
    SubworkflowFeatureRequirement: {}
    StepInputExpressionRequirement: {}
    InlineJavascriptRequirement: {}
    ShellCommandRequirement: {}

  hints:
    DockerRequirement:
      dockerPull: kathrinklee/rna-seq-pipeline-hisat2


Below is the **inputs**, **outputs**, and **steps** blocks that come after. in **step1** the script **index_build.cwl** will be call, and its inputs (**in**)
 are taken from **inputs** section, the output (**out**) will be caught by the **outputs** (**step1/ht** and **step1/log** in this case), this declaration is important as it will decide which outputs to keep at the end of the step.

::

  inputs:
    fasta_file: File
    out_name: string

  outputs:
    index_files:
      type: Directory
      outputSource: step1/ht
    index_log:
      type: File
      outputSource: step1/log

  steps:
    step1:
      run: index_build.cwl
      in:
        fasta_file: fasta_file
        out_name: out_name
      out:
        [ht, log]




Let's run it by using:

::

  $ cwltool CWL-RNAseq.cwl CWL-RNAseq.yml

If you receive this error: "docker: Got permission denied while trying to connect to the Docker daemon socket at unix"

Try:

::

  $ sudo groupadd docker
  $ sudo usermod -aG docker ${USER}
  close and reopen VM then run the script again



Let's take a look at the folder after cwltool finishes:

::

  .
  └── CWL-RNAseq
      ├── create_bam.cwl
      ├── create_transcript.cwl
      ├── CWL-RNAseq.cwl
      ├── CWL-RNAseq.yml
      ├── data
      │   ├── sample_1.fq
      │   ├── sample_2.fq
      │   ├── sample.fa
      │   └── sample.gtf
      ├── [final_ref.gtf]
      ├── [final_transcript.gtf]
      ├── [final.tsv]
      ├── hisat2_align.cwl
      ├── [hisat2_align_out]
      │   ├── [hisat2_align_out.log]
      │   └── [sample.sam]
      ├── [hisat2_build.log]
      ├── index_build.cwl
      ├── [sample]
      │   ├── [index.1.ht2]
      │   ├── [index.2.ht2]
      │   ├── [index.3.ht2]
      │   ├── [index.4.ht2]
      │   ├── [index.5.ht2]
      │   ├── [index.6.ht2]
      │   ├── [index.7.ht2]
      │   └── [index.8.ht2]
      └── [sample.bam]


The script will call `hisat2 <http://daehwankimlab.github.io/hisat2/>`_ , `samtools <http://www.htslib.org/>`_, and `stringtie <https://ccb.jhu.edu/software/stringtie/>`_ to do the work.
**sample.sam** file will contains the sequence alignment data produced by mapping reads to the reference genome, **sample.bam**
 file will contains the compressed binary data from Sam. More description on gtf outputs, and tsv of stringtie can be found `here <http://ccb.jhu.edu/software/stringtie/index.shtml?t=manual>`_. The **final_transcript.gtf** contains details of the transcripts that StringTie assembles from RNA-Seq data, while
 **final.tsv** contains gene abundances.



 To see the result of this workflow, you can check it `here <https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/tree/master/Results/RNAseq>`_
