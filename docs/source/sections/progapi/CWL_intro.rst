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

Example command-line equivalents to create the disk and the VM (you will need to substitute in your own 
Google Cloud Platform (GCP) project:

.. code-block:: none

   $ gcloud compute --project <YOUR-PROJECT-ID> disks create "cwl-disk-1" --size "500" --zone "us-central1-c" --type "pd-standard"

   $ gcloud compute --project <YOUR-PROJECT-ID> instances create "cwl-test-1" --zone "us-central1-c" --machine-type "n1-standard-4" --network "default" --maintenance-policy "MIGRATE" --scopes default="https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring.write","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --disk "name=cwl-disk-1,device-name=cwl-disk-1,mode=rw,boot=no" --image "/ubuntu-os-cloud/ubuntu-1404-trusty-v20161205" --boot-disk-size "10" --boot-disk-type "pd-standard" --boot-disk-device-name "cwl-test-1"

2. Configure the VM
====================

Now you can ssh to your VM from any command-line where you have the cloud SDK installed.  
If you don't have the cloud SDK installed on your local machine, you can use the 
`Cloud Shell <https://cloud.google.com/shell/docs/>`_ directly from your browser in the 
`Cloud Console <https://console.cloud.google.com>`_.  

.. code-block:: none

   $ gcloud compute --project <YOUR-PROJECT-ID> ssh --zone "us-central1-c" "cwl-test-1"

2.1 Install Packages
--------------------

Use the following commands to install the necessary packages:

.. code-block:: none

   $ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
   
   $ echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | sudo tee /etc/apt/sources.list.d/docker.list
   
   $ sudo aptitude update
   
   $ sudo aptitude install apt-transport-https ca-certificates docker-engine htop libffi-dev libssl-dev nodejs python-dev virtualenvwrapper

After this last command, you will need to respond "Yes" to install the new packages.

2.2 Format and Mount the Disk
-----------------------------

You can see the disks that are attached to your VM by using the following command:

.. code-block:: none

   $ ls /dev/disk/by-id

which should respond with something like:

.. code-block:: none

   google-cwl-disk-1  google-cwl-test-1-part1                 scsi-0Google_PersistentDisk_cwl-test-1
   google-cwl-test-1  scsi-0Google_PersistentDisk_cwl-disk-1  scsi-0Google_PersistentDisk_cwl-test-1-part1

The first disk listed above (google-cwl-disk-1) is the additional disk that was crated, while the 
second one (google-cwl-test-1) is the boot disk, with the same name as the VM.  The following
commands differ slightly from those specified in the GDC README but the result will be the same:

.. code-block:: none

   $ sudo mkfs.ext4 -F -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/disk/by-id/google-cwl-disk-1
   $ sudo mkdir -p /mnt/SCRATCH
   $ sudo mount -o discard,defaults /dev/disk/by-id/google-cwl-disk-1 /mnt/SCRATCH
   $ sudo chmod 777 /mnt/SCRATCH

You can now verify that the disk has been properly mounted using the ``df -h`` command:

.. code-block:: none

   $ df -h

   File system      Size    Used    Avail    Use%    Mounted on
   /dev/sdb         493G     70M     467G      1%    /mnt/SCRATCH

and as you can see, close to 500G of space is available mounted as /mnt/SCRATCH.

2.3 Prepare Docker and CWL
--------------------------

These next sets of commands will get you ready to run docker on this VM.  You will need to 
log out and log back in a couple of times to force certain changes to take effect.

.. code-block:: none

   $ mkdir /mnt/SCRATCH/docker
   $ sudo bash -c 'echo DOCKER_OPTS=\"-g /mnt/SCRATCH/docker/\" >> /etc/default/docker'
   $ sudo gpasswd -a ${USER} docker
   $ sudo service docker restart
   $ exit

The last command will log you out of your VM, so you will need to log back in using the same
``gcloud ssh`` command you used before.  Once you're back on the VM:

.. code-block:: none

   $ echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc
   $ exit

Sign back in again, and then create a "virtualenv" called "cwl".  This will change your
command-line prompt to indicate that you are in a new environment:

.. code-block:: none

   $ mkvirtualenv --python /usr/bin/python2 cwl
   (cwl) $

A few more install commands and you'll be ready to go:

.. code-block:: none

   (cwl)$ pip install --upgrade pip
   (cwl)$ pip install 'requests[security]' --no-cache-dir
   (cwl)$ wget https://github.com/NCI-GDC/cwltool/archive/1.0_gdc_g.tar.gz
   (cwl)$ pip install 1.0_gdc_g.tar.gz --no-cache-dir

3. Run the DNA-Seq workflow
===========================

3.1 Clone the GDC github repo
-----------------------------

3.2 Load Reference and Input Data Files
---------------------------------------

3.3 Run DNA-Seq CWL workflow
----------------------------

4. Additional Information
=========================

