*****************************************
The Workflow Description Language (WDL)
*****************************************

The `Workflow Description Language <https://software.broadinstitute.org/wdl/>`_ (WDL) 
which is in use at the Broad Institute, is an alternative to CWL.
It is supported by a powerful workflow execution engine
called `Cromwell <https://github.com/broadinstitute/cromwell>`_, which 
includes multiple "backends" such as GridEngine, HTCondor, Spark,
the Google "Pipelines API" (formerly known as JES, *ie* "Job Execution Service", aka GGP),
and the new GA4GH TES (*ie* "Task Execution Service").

We will focus on the two backends that directly support running workflows 
on Google Compute Engine VMs:
    * `Google Genomics Pipelines API <https://cloud.google.com/genomics/reference/rest/v1alpha2/pipelines>`_ (formerly known as JES)
    * `GA4GH Task Execution Service <https://github.com/ga4gh/task-execution-server>`_ (aka TES)

Google Genomics Pipelines
+++++++++++++++++++++++++

The so-called "Pipelines API" is a task runner that lets you run a command-line executable in Docker on a Google Compute Engine VM.
Since it is truly a "task" runner rather than a full "pipeline" runner, we generally refer to it as GGP so that the usage
of the word "pipeline" is not confusing.  We also find the additional term "API" unnecessary.  

GGP can be "called" using command-line interface (part of the Cloud SDK ``gcloud`` tool),
or as a web service API that can be called programmatically.
When using GGP from the command-line, each task is defined in a YAML (or JSON) file.

The Google documentation for the "Genomics Pipelines" can be found
`here <https://cloud.google.com/genomics/v1alpha2/pipelines>`_
and on `readthedocs <https://googlegenomics.readthedocs.io/en/latest/use_cases/run_pipelines_in_the_cloud/index.html>`_,
and there are numerous easy-to-follow examples on github
`here <https://github.com/googlegenomics/pipelines-api-examples>`_.

You can use `wdl_runner <https://github.com/googlegenomics/pipelines-api-examples/tree/master/wdl_runner>`_
to run a WDL workflow using Cromwell+GGP on the Google Cloud.  Documentation can be found on
`github <https://github.com/googlegenomics/pipelines-api-examples/blob/master/wdl_runner/README.md>`_
and you can run a GATK workflow by following this Google Genomics
`documentation <https://cloud.google.com/genomics/v1alpha2/gatk>`_.

GA4GH Task Execution Service
++++++++++++++++++++++++++++

The GA4GH TES was inspired by GGP, with the broader goal of defining a platform agnostic interface between
workflow management systems, schedulers, and workflow language interpreters on the *frontend* of the TES
interface, and the actual workes, nodes, VMs, and filesystems on the *backend*.  Although this effort 
started only a few months ago, progress has been rapid and a reference implementation is available
on `github <https://github.com/ga4gh/task-execution-server>`_.

As described in this
`post <http://gatkforums.broadinstitute.org/wdl/discussion/9219/testing-testing-1-2-3>`_
over on the WDL Blog, TES has been recently added as a new backend to Cromwell.


