***************************
Getting Started with CWL
***************************

The `Common Workflow Language <http://www.commonwl.org/>`_ (CWL) is emerging as a standard
for defining and sharing bioinformatic workflows, and the 
`NCI-GDC <https://gdc.cancer.gov/>`_ is planning to release all of its 
standardized workflows in this format.

In this section, 
we will guide you through the steps to run the GDC's DNA-Seq harmonization workflow
on Google Compute Engine.  This workflow is available on github 
`here <https://github.com/NCI-GDC/gdc-dnaseq-cwl>`_.
The instructions here are based on the GDC's 
`README <https://github.com/NCI-GDC/gdc-dnaseq-cwl/blob/master/README.md>`_ 
and have been customized to run on GCE.

1. Create a GCE VM with Disk
============================

From the Cloud Console > Compute Engine > VM instances 
`page <https://console.cloud.google.com/compute/instances>`_
click on **[+] CREATE INSTANCE**, and:

    - set Name (*eg* cwl-test-1)
    - set Zone (*eg* us-central1-c)
    - set Machine type (eg 4 vCPUs with 15 GB memory)
    - Change the boot disk to Ubuntu 14.04 LTS with 10 GB standard persistent disk (note that the boot disk will be named the same as the VM, *ie* cwl-test-1)
    - leave the Identity and API access box as is (with "Compute Engine default service account" and "Allow default access" selected)
    - expand the "Management, disk, networking, SSH keys section":

        + select the Disks tab
        + click on **+ Add item**
        + in the Name pull-down, select "Create disk": a "Create a disk" panel will open:

            * set Name (*eg* cwl-disk-1) -- do not use the same name as the VM!
            * set Source type to "None (blank disk)"
            * set Size (*eg* 500 GB)
            * leave default Encryption (which is "Automatic (recommended)")
            * click on the blue **Create** button -- this will create the disk only at this time

        + before clicking on the **Create** button (for the VM), click on the bottom line where it says "Equivalent REST or command line" -- you can save this command-line and re-use it later to create the same VM from the command-line rather than repeating this interactive process; it is also a nice record of exactly how the VM was created
        + now click on the **Create** button -- you will see the VM "spinning up" on the VM instances page



