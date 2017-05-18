**************************************
The cwl_runner "helper" script
**************************************

The cwl_runner script can be found on github in the **googlegenomics/pipelines-api-examples** repository, in the 
`cwl_runner <https://github.com/googlegenomics/pipelines-api-examples/tree/master/cwl_runner>`_ folder. 
You may want to refer to the 
`README <https://github.com/googlegenomics/pipelines-api-examples/blob/master/cwl_runner/README.md>`_ 
file in the github repo, we will also provide an overview and summary of what
this script does below, with some additional details that you may find useful.

The basic prerequisites to be able to run this example are:
   * you have the necessary privileges to launch a VM in a Google Cloud Project (GCP) project
   * you must have an existing Google Cloud Storage (GCS) bucket
   * you have the Cloud SDK installed 

There are three scripts in the github repo:
   * ``cwl_runner.sh`` is the main bash script which takes care of most of the steps described in this `tutorial <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/progapi/CWL_intro.html>`_;
   * ``cwl_startup.sh`` is the VM startup script which will automatically be run as soon as the VM spins up;
   * ``cwl_shutdown.sh`` is the VM shutdown script which takes care of final steps such as copying stdout and stderr to GCS;


The main script,
`cwl_runner.sh <https://raw.githubusercontent.com/googlegenomics/pipelines-api-examples/master/cwl_runner/cwl_runner.sh>`_,
is the only one that you will invoke directly.  It has several different options (which you can learn
more about by using the ``--help`` option), but the only required ones are:
   * ``--workflow-file PATH``:  the absolute path to the CWL workflow document;
   * ``--settings-file PATH``:  the absolute path to the JSON settings file;
   * ``--output GCS_PATH``:  the output location in GCS where all outputs and logs will be copied after the workflow completes.

The script then invokes two ``gcloud compute`` commands (``gcloud`` is part of the 
`cloud SDK <https://cloud.google.com/sdk/>`_:
   * ``gcloud compute disks create``: to create a persistent disk in the (optionally user-specified) zone, of (optionally user-specified) size;
   * ``gcloud compute instances create``:  to create a virtual machine (VM), in the same zone as the disk, with the previously created disk attached, with the (optionally user-specified) machine type.

If the user specifies, the VM can be a 
`preemptible <https://cloud.google.com/compute/docs/instances/preemptible>`_ 
VM, which can be a good way to minimize compute costs, under the right circumstances.

The other information that the VM needs is passed in as 
`metadata <https://cloud.google.com/compute/docs/storing-retrieving-metadata>`_.
Metadata is stored as key:value pairs.  There is a default set of metadata
entries that every VM has access to, and 
`custom metadata <https://cloud.google.com/compute/docs/storing-retrieving-metadata#custom>`_
can also be set when a VM is created.  This metadata will be available to the VM from 
the `metadata server <https://cloud.google.com/compute/docs/storing-retrieving-metadata#querying>`_.

The following metadata keys are specified by the cwl_runner script and will be available to the VM:
    * startup-script-url
    * shutdown-script-url
    * operation-id
    * workflow-file
    * settings-file
    * input
    * input-recursive
    * output
    * runner
    * status-file
    * keep-alive

The cwl_runner script invoked by the user will create a random ``OPERATION-ID`` and
write three script files to the specified output location in GCS:
    * ``cwl_runner-<OPERATION-ID>.sh``
    * ``cwl_startup-<OPERATION-ID>.sh``
    * ``cwl_shutdown-<OPERATION-ID>.sh``
and will run the ``gcloud compute disks create`` command, followed by the ``gcloud compute instances create`` command.

In this case, the "startup" script will take care of pretty much everything we want this
particular VM to do:
    * local bash variables are set based by retrieving the instance metadata from the metadata server
    * the disk is mounted and formatted
    * folders are created for workflow inputs and outputs
    * input files are copied from GCS to local disk
    * the workflow and settings files are copied from GCS to local disk
    * the executor (cwltool) is invoked to run the workflow
    * outputs are copied from local disk out to GCS
    * the VM is shut down (using the command ``gcloud compute instances delete``) unless the ``--keep-alive`` option was set

Following the example provided on github, you can invoke cwl_runner from the command-line (anywhere where you
have the Cloud SDK installed, with your GCS bucket and optional folder name instead of ``MY-BUCKET/my-work-folder`` below):

.. code-block:: none

   ./cwl_runner.sh \
     --workflow-file gs://genomics-public-data/cwl-examples/gdc-dnaseq-cwl/workflows/dnaseq/transform.cwl \
     --settings-file gs://genomics-public-data/cwl-examples/gdc-dnaseq-cwl/input/gdc-dnaseq-input.json \
     --input-recursive gs://genomics-public-data/cwl-examples/gdc-dnaseq-cwl \
     --output gs://MY-BUCKET/my-work-folder \
     --machine-type n1-standard-4


In this example, the JSON settings file specifies 5 items:
    * bam_path (a small ~300MB low-coverage BAM for chromosome 20 only from the 1000G project)
    * reference_fasta_path (the GRCh38 reference FASTA file from the `GDC Reference Files <https://gdc.cancer.gov/about-data/data-harmonization-and-generation/gdc-reference-files>`_)
    * db_snp_path
    * thread_count
    * uuid

For more details on machine-types, please see the Google documentation on 
`predefined machine types <https://cloud.google.com/compute/docs/machine-types#predefined_machine_types>`_
and if you find that none of those quite fit your requirements you
may be interested in using one of the available 
`custom machine types <https://cloud.google.com/compute/docs/machine-types#custom_machine_types>`_.

