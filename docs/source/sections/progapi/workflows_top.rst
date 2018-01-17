******************
Running Workflows
******************

In the last few years there has been significant renewed interest in using a 
workflow approach to perform data analysis on Genomic, RNASeq, Proteomic and
other types of data driven by the growth in big data and the popularity of 
cloud technologies ability for scalable storage and computing.  The concept 
of a workflow was 
`defined <http://www.aiai.ed.ac.uk/project/wfmc/ARCHIVE/DOCS/glossary/glossary.html>`_ 
about 20 years ago by the 
`Workflow Management Coalition <http://www.wfmc.org/>`_ 
as: *"The automation of a business process, in whole or part, during which documents, 
information or tasks are passed from one participant to another for action, 
according to a set of procedural rules."* The focus of this particular 
organization is on something called BPM or *Business Process Management*.

*Scientific* workflows have emerged to manage and describe the complexity that arises
in scientific experiments, as well as data analysis and data processing.  Complex 
workflows are created by linking or *chaining* several components or tasks into a *pipeline*.

A complete scientific workflow *system* requires first a clearly defined *language*
and *grammar* which can be used to describe a workflow.  Given a clearly specified 
workflow, a "workflow runner" of some sort is necessary in order to be able to actually 
*run* the workflow.  A "runner" generally implements the following "roles": 
a master or administrator, a scheduler, a task executor, and workers: in which the master
receives and parses workflow document(s) and communicates requirements to the scheduler;
the scheduler is typically trying to optimize usage of the available workers based
on the requirements of the master(s), the executor causes tasks to be run on the specified 
schedule, and the workers do the work.

Out of this demand for scientific workflows have emerged sseveral competing description 
languages such as the CWL (`Common Workflow Language <http://www.commonwl.org/>`_), 
WDL (`Workflow Description Language <https://software.broadinstitute.org/wdl/>`_),
and `NextFlow <https://www.nextflow.io>`_ to name a few.
These languages underwent rapid development and changes in the beginning and now
are becoming more stable for use in production environments.  Coupled with these languages
are runner implementations such as cwltool, rabix, toil, and cromwell and new API standards such
as GA4GH’s Task Execution Schema (TES) and the Workflow Execution Schema (WES).  With the 
advent of so many choices; all under rapid development and at various stages of completeness
its challenging to make a choice on any one technology.  ISB CGC's approach 
therefore has been not to make a choice but to instead enable as many of these
technologies as possible through documentation, support, and where necessary
infrastructure.

For more information on workflows see:

.. toctree::
   :maxdepth: 1

   CWL_top
   WDL_top

As an alternative to workflows, we also recommend users consider dsub, an command-line
tool that uses Docker to make it easy to submit and run single commands or batch scripts 
in the cloud.  The dsub program is loosely based off of more traditional HPC systems such
as Grid Engine or PBS where you "submit" your commands to a job scheduler that manages the
compute resources, file I/O, and process execution. 

More information on dsub and examples of its usage can be found at:

.. toctree::
   :maxdepth: 1
   
   `Google dsub Documentation <https://cloud.google.com/genomics/v1alpha2/dsub>`_
   'kallisto example <https://github.com/isb-cgc/ISB-CGC-Examples/tree/master/dsub/kallisto>'_

Lasly, the (now deprecated) ISB-CGC-pipelines framework was developed to facilitate running
single step tasks at scale, for example: running FastQC over tens of thousands of FastQ
files.

.. toctree::
   :maxdepth: 1

   ISB_pipelines_top

