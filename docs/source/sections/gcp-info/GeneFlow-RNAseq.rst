========================
Running GeneFlow RNA-seq
========================

This GeneFlow `RNA-seq <https://www.technologynetworks.com/genomics/articles/rna-seq-basics-applications-and-protocol-299461#:~:text=RNA%2Dseq%20(RNA%2Dsequencing,patterns%20encoded%20within%20our%20RNA.>`_ workflow maps read-pairs to a reference genome and produces a transcript. 

`GeneFlow <https://github.com/CDCgov/geneflow2>`_ enables modular and reproducible scientific workflows by leveraging reusable, containerized steps. Custom workflow steps can be implemented using either Docker or Singularity containers. Additional documentation for GeneFlow can be found `here <https://geneflow.gitlab.io>`_. 

Requirements
============

- Docker
- Python 3
- GeneFlow

To install Docker, Python 3, and GeneFlow, see our `VM Workflow Tools Installation Cheatsheet <Cheatsheet.html>`_ for instructions.

.. note:: The requirements above are crucial to running this workflow. Please make sure you have them installed properly prior to running this workflow.

Install the Workflow
====================

::

	$ sudo add-apt-repository universe
	$ sudo apt update
	$ sudo apt install subversion

 	# clone the workflow
 	$ svn checkout https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/trunk/GeneFlow-RNAseq

 	# install the workflow's apps
 	$ gf install-workflow --make-apps GeneFlow-RNAseq

Running GeneFlow
================

You should have a **GeneFlow-RNAseq** directory with the following contents:

::

	GeneFlow-RNAseq
	├── apps
	│   ├── bam-sort
	│   ├── hisat2-align
	│   ├── hisat2-build
	│   └── stringtie
	├── data
	│   ├── gtf
	│   │   └── sample.gtf
	│   ├── reads
	│   │   ├── sample_1.fq
	│   │   └── sample_2.fq
	│   └── reference
	│       └── sample.fa
	└── workflow.yaml


The file **workflow.yaml** contains the workflow definition, and the **apps** folder contains definitions for each of the workflow steps. 

Let's take a look at the contents of the **workflow.yaml** file. The first block contains metadata, including workflow name, description, source repository, and version. The **final_output** block lists all steps whose output should be copied to the final output directory. 

::

	%YAML 1.1
	---
	gfVersion: v2.0
	class: workflow

	# metadata
	name: HISAT2 StringTie Workflow
	description: RNAseq workflow using HISAT2 and StringTie
	git: https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/GeneFlow-RNAseq
	version: '0.1'

	final_output:
	- sort
	- quantify

	# inputs
	inputs:
	  reads:
	    label: Input Directory
	    description: Input directory containing FASTQ files
	    type: Directory
	    default: ./data/reads
	    enable: true
	    visible: true
	  gtf:
	    label: Input GTF
	    description: GTF file describing transcriptome
	    type: File
	    default: ./data/gtf/sample.gtf
	    enable: true
	    visible: true
	  reference:
	    label: Reference Sequence FASTA
	    description: Reference sequence FASTA file
	    type: File
	    default: ./data/reference/sample.fa
	    enable: true
	    visible: true

	# parameters
	parameters: 
	  threads:
	    label: CPU Threads
	    description: Number of CPU threads for alignment
	    type: int
	    default: 2
	    enable: false
	    visible: true

	# apps
	apps:
	  hisat2-build:
	    git: https://gitlab.com/geneflow/apps/hisat2-build-gf2.git
	    version: '2.2.1-01'
	  hisat2-align:
	    git: https://gitlab.com/geneflow/apps/hisat2-align-gf2.git
	    version: '2.2.1-01'
	  bam-sort:
	    git: https://gitlab.com/geneflow/apps/bam-sort-gf2.git
	    version: '1.10-07'
	  stringtie:
	    git: https://gitlab.com/geneflow/apps/stringtie-gf2.git
	    version: '2.1.6-01'

	# steps
	steps:
	  build:
	    app: hisat2-build
	    depend: []
	    template:
	      reference: ${workflow->reference}
	      output: reference

	  align:
	    app: hisat2-align
	    depend: [ "build" ]
	    map:
	      uri: ${workflow->reads}
	      regex: (.*)_(R|)1(.*)\.((fastq|fq)(|\.gz))$
	    template:
	      input: ${workflow->reads}/${1}_${2}1${3}.${4}
	      pair: ${workflow->reads}/${1}_${2}2${3}.${4}
	      reference: ${build->output}/reference
	      threads: ${workflow->threads}
	      output: ${1}.sam

	  sort:
	    app: bam-sort
	    depend: [ "align" ]
	    map:
	      uri: ${align->output}
	      regex: (.*).sam
	    template:
	      input: ${align->output}/${1}.sam
	      output: ${1}.bam

	  quantify:
	    app: stringtie
	    depend: [ "sort" ]
	    map:
	      uri: ${sort->output}
	      regex: (.*).bam
	    template:
	      bam: ${sort->output}/${1}.bam
	      gtf: ${workflow->gtf}
	      output: ${1}
	...

The **inputs** and **parameters** blocks define the inputs and paramaters that need to be passed to the workflow upon execution. Some of these inputs and parameters are optional or have default values. 

The **apps** block lists all apps used by the workflow and links to other, reusable source repositories for each app. Learn more about how each app works by following the Git repository links below:

* `HISAT2 Build <https://gitlab.com/geneflow/apps/hisat2-build-gf2.git>`_
* `HISAT2 Align <https://gitlab.com/geneflow/apps/hisat2-align-gf2.git>`_
* `BAM Sort <https://gitlab.com/geneflow/apps/bam-sort-gf2.git>`_
* `StringTie <https://gitlab.com/geneflow/apps/stringtie-gf2.git>`_

The **steps** block defines the order of app execution as well as step dependencies for each app. It also defines how apps are chained together via their inputs and outputs. 

To run the workflow:

::

	# assuming the GeneFlow Python virtual environment has been activated, view the command line help
 	$ gf help GeneFlow-RNAseq

	# run the workflow
	$ cd GeneFlow-RNAseq
	$ gf run . -o output 

After the workflow completes, the output folder should look similar to this:

::

	output
	└── geneflow-job-095ba2fe
	    ├── quantify
	    │   ├── _log
	    │   │   ├── gf-0-quantify-sample.err
	    │   │   ├── gf-0-quantify-sample.out
	    │   │   ├── sample-stringtie.stderr
	    │   │   └── sample-stringtie.stdout
	    │   └── sample
	    │       ├── e2t.ctab
	    │       ├── e_data.ctab
	    │       ├── i2t.ctab
	    │       ├── i_data.ctab
	    │       ├── sample.tsv
	    │       ├── sample_final_reference.gtf
	    │       ├── sample_final_transcript.gtf
	    │       └── t_data.ctab
	    └── sort
		├── _log
		│   ├── gf-0-sort-sample-bam.err
		│   ├── gf-0-sort-sample-bam.out
		│   └── sample.bam-samtools-sort.stderr
		└── sample.bam

The script will run Docker containers for `hisat2 <http://daehwankimlab.github.io/hisat2/>`_, `samtools <http://www.htslib.org/>`_, and `stringtie <https://ccb.jhu.edu/software/stringtie/>`_ to do the work. **sample.bam** contains the sequence alignment data produced by mapping reads to the reference genome **sample.bam**. Additional information about gtf and tsv outputs of stringtie can be found `here <http://ccb.jhu.edu/software/stringtie/index.shtml?t=manual>`_. The **sample_final_transcript.gtf** contains details of the transcripts that StringTie assembles from RNA-Seq data, while **sample.tsv** contains gene abundances.

View the results of this workflow `here <https://github.com/isb-cgc/RunningWorkflows-on-the-GoogleCloud/tree/master/Results/RNAseq>`_.
