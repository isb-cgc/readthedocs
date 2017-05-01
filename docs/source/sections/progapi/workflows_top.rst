******************
Running Workflows
******************

The concept of a workflow was 
`defined <http://www.aiai.ed.ac.uk/project/wfmc/ARCHIVE/DOCS/glossary/glossary.html>`_ 
about 20 years ago by the 
`Workflow Management Coalition <http://www.wfmc.org/>`_ 
as: *"The automation of a business process, in whole or part, during which documents, 
information or tasks are passed 
from one participant to another for action, according to a set of procedural rules."*
The focus of this particular organization is on something called
BPM or *Business Process Management*.

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

Although there are numerous bioinformatics workflow systems, the two that we will
focus on at this time are: 
CWL (`Common Workflow Language <http://www.commonwl.org/>`_) 
and WDL (`Workflow Description Language <https://software.broadinstitute.org/wdl/>`_)
which are further described in the sections below.

Additionally, the ISB-CGC-pipelines framework has been developed to facilitate running
single step tasks at scale, for example: running FastQC over tens of thousands of FastQ
files.

.. toctree::
   :maxdepth: 1

   CWL_top
   WDL_top
   ISB_pipelines_top


