**********************************
The Common Workflow Language (CWL)
**********************************

The `Common Workflow Language <http://www.commonwl.org/>`_ (CWL) is emerging as a standard
for defining and sharing bioinformatic workflows, and the 
`NCI-GDC <https://gdc.cancer.gov/>`_ is planning to release all of its 
standardized workflows in this format.

In the sections below, we present a tutorial on running a sample GDC workflow with
step-by-step instructions to run it on a sample input file ona Google Compute Engine
(GCE) VM.  The second section describes how to use a "helper-script" called cwl_runner
which wraps many of the individual steps required to create a GCE disk, spin up
a GCE VM, mount and format the disk, *etc*.

.. toctree::
   :maxdepth: 1

   CWL_intro
   CWL_script

