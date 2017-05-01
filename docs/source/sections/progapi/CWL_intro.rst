**************************************
Running the NCI-GDC DNA-Seq workflow
**************************************

In this section, 
we will guide you through the steps to run the NCI-GDC's DNA-Seq harmonization workflow
on Google Compute Engine.  This workflow is available on github 
`here <https://github.com/NCI-GDC/gdc-dnaseq-cwl>`_.
The instructions here are based on the NCI-GDC's 
`README <https://github.com/NCI-GDC/gdc-dnaseq-cwl/blob/master/README.md>`_ 
and have been customized to run on GCE.

1. Create a GCE VM with Disk
============================

From the Cloud Console > Compute Engine > VM instances 
`page <https://console.cloud.google.com/compute/instances>`_
click on **[+] CREATE INSTANCE**, and:

    - set Name (*eg* cwl-test-1)
    - set Zone (*eg* us-central1-c)
    - set Machine type (*eg* 4 vCPUs with 15 GB memory)
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
commands differ slightly from those specified in the NCI-GDC README but the result will be the same:

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

3.1 Clone the NCI-GDC github repo
---------------------------------

You should now be in your home directory, in the (cwl) virtualenv.  Clone the NCI-GDC dna-seq-cwl repo:

.. code-block:: none

   (cwl)$ git clone https://github.com/NCI-GDC/gdc-dnaseq-cwl.git

Now you will have a subdirectory called ``gdc-dnaseq-cwl`` in your home directory, containing
the NCI-GDC DNA-Seq harmonization workflow.  The main workflow is in the CWL file 
``~/gdc-dnaseq-cwl/workflows/dnaseq/transform.cwl``.

3.2 Load Reference and Input Data Files
---------------------------------------

The DNA-Seq workflow requires some reference data files that can be obtained from the NCI-GDC.  
These include the dbsnp vcf (3 GB), the reference genome (835 MB), and the bwa indexed genome (3.2 GB).  
(Uploading these to your VM disk should take 5-10 minutes.) 

.. code-block:: none

   (cwl)$ mkdir /mnt/SCRATCH/hg38_reference
   (cwl)$ cd /mnt/SCRATCH/hg38_reference
   (cwl)$ wget https://gdc-api.nci.nih.gov/data/4ba1c087-ec80-47c4-a9d5-e9bb9933fef4 -O dbsnp_144.hg38.vcf.gz
   (cwl)$ wget https://gdc-api.nci.nih.gov/data/62f23fad-0f24-43fb-8844-990d531947cf
   (cwl)$ tar xvf 62f23fad-0f24-43fb-8844-990d531947cf
   (cwl)$ wget https://gdc-api.nci.nih.gov/data/964cbdac-1043-4fae-b068-c3a65d992f6b
   (cwl)$ tar xvf 964cbdac-1043-4fae-b068-c3a65d992f6b

Finally, let's copy a small example BAM file (300 MB) from the 1000G repository:

.. code-block:: none

   (cwl)$ cd /mnt/SCRATCH
   (cwl)$ wget ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/phase3/data/NA12878/alignment/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam

At this point you could also obtain a bam file either from the NCI-GDC or from one of the
ISB-CGC Cloud Storage buckets.

3.3 Run DNA-Seq CWL workflow
----------------------------

Now we're ready to run the workflow using the CWL-runner **cwltool**.  The input file that we just copied
to our VM disk is in ``/mnt/SCRATCH/alignment/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam``.
Let's create a sub-directory for the processed results:

.. code-block:: none

   (cwl)$ mkdir /mnt/SCRATCH/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211
   (cwl)$ cd /mnt/SCRATCH/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211
   (cwl)$ mkdir tmp cache
   (cwl)$ nohup cwltool --debug --tmpdir-prefix tmp/ --cachedir cache/ \
            ~/gdc-dnaseq-cwl/workflows/dnaseq/transform.cwl \
            ~/gdc-dnaseq-cwl/workflows/dnaseq/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.json &

While that is running, you can go back to the Cloud Console, to the Compute Engine > VM instances 
page, and click on the name of this VM.  This will take you to a page describing this specific VM,
and you can see a trace of CPU utilization, and other metrics.

Let's also take a closer look at the ``cwltool`` command used above.  
You can find more details at the 
`cwltool github repo <https://github.com/common-workflow-language/cwltool>`_
and at `commonwl.org <http://www.commonwl.org/v1.0/CommandLineTool.html>`_.
The basic form of the cwltool command is:

.. code-block:: none

   $ cwltool [tool-or-workflow-description] [input-job-settings]

Looking at the way cwltool was invoked above, we see that the ``tool-or-workflow-description``
is in ``~/gdc-dnaseq-cwl/workflows/dnaseq/transform.cwl`` and the ``input-job-settings``
are in ``~/gdc-dnaseq-cwl/workflows/dnaseq/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.json``.
Let's have a closer look at those, starting with the smaller input-job-settings JSON document.
It defines three objects, each of which is of class "File", with a specified "path", *eg*:

.. code-block:: none

   "bam_path": {
       "class": "File",
       "path": "/mnt/SCRATCH/NA12878.chrom20.ILLUMINA.bwa.CEU.low_coverage.20121211.bam"
   }

and it also specifies a "thread_count" value (8), and a "uuid".  You can see these inputs 
defined near the top of the CWL document 
(`transform.cwl <https://github.com/NCI-GDC/gdc-dnaseq-cwl/blob/master/workflows/dnaseq/transform.cwl>`_).

3.4 Run-time and Compute-costs
-------------------------------

This sample task takes about 2 hours to run.  The costs associated with running this task are:
2 hours of GCE VM time plus 2 hours of persistent disk time 
(`GCE pricing details <https://cloud.google.com/compute/pricing>`_), 
which comes to approximately $0.400 for the VM and $0.056 for the persistent disks,
for a total of **$0.456**.  
(The n1-standard-4 VM chosen above costs $0.200 per hour, and the disk costs, 
at $0.040 per GB per month for standard provisioned space, were computed as
510 GB x $0.040 per GB per month x 2 hours / 730 hours per month.)

