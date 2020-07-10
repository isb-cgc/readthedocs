==========
RNAseq-CWL
==========
Requirements:

-  CWLtool
-  Docker

Download this tutorial:
::

  $sudo add-apt-repository universe
  $sudo apt update
  $sudo apt install subversion

  #cloning this tutorial
  $svn checkout https://github.com/votb92/RunningWorkflows-on-the-GoogleCloud/trunk/CWL-RNAseq

To install Docker and CWL, you can visit our **Cheatsheet** listed below:

- `Cheatsheet <http://insertlink>`_

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

Let's run it by using:

::

  $cwltool CWL-RNAseq.cwl CWL-RNAseq.yml

If you receive this error: "docker: Got permission denied while trying to connect to the Docker daemon socket at unix"

Try:

::

  $sudo groupadd docker
  $sudo usermod -aG docker ${USER}
  close and reopen VM then run the script again



After CWLtool finishes:

-  **CWL-RNAseq.cwl** is the main cwl file that connects all other cwl tools together
-  **CWL-RNAseq.yml** is the file that contains all the inputs that are necessary to run the pipeline
-  **index_build.cwl** builds index files from a Fasta file, using Hisat2-build
-  **hisat2_align.cwl** builds a sam file from forward and reverse reads, and the indices built from previous step, using Hisat2
-  **create_bam.cwl** builds a bam file from the newly built sam file, using Samtools
-  **create_transcript.cwl** creates transcript from the bam file from previous step, using Stringtie


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
