**********************************
The Common Workflow Language (CWL)
**********************************

The `Common Workflow Language <http://www.commonwl.org/>`_ (CWL) is emerging as a standard
for defining and sharing bioinformatic workflows, and the 
`NCI-GDC <https://gdc.cancer.gov/>`_ is planning to release all of its 
standardized workflows in this format.

In the sections below, we present a tutorial on running a sample NCI-GDC workflow with
step-by-step instructions to run it on a sample input BAM file using a Google Compute Engine
(GCE) VM.  The second section describes how to use a convenient "helper-script" 
called cwl_runner (available on github)
which wraps many of the individual steps required to create a GCE disk, spin up
a GCE VM, mount and format the disk, *etc*, allowing you to run a CWL workflow
in one easy step.

.. toctree::
   :maxdepth: 1

   CWL_intro
   CWL_script

