Launching a Google Cloud Virtual Machine (VM)
############################################

You can launch a virtual machine (which we will generally refer to as a VM) from the web-based Google Cloud Console or from the command line interface (CLI) using the Google Cloud SDK. We will describe both of these approaches below. 

Prerequisites 
=============
#. Enable the following APIs in your Google Cloud Project:

    * Google Compute Engine

    * Google Cloud Storage

#. Check the IAM & Admin section of the Cloud Console to verify that you have "Editor" or "Owner" privileges in your Google Cloud Project, otherwise you won’t be    able to create any VMs.


Via the Google Cloud Console
=============================

An instructional video on how to launch a VM can be found on the Google Cloud Platform youtube page:  `How to launch a VM <https://youtu.be/1XH0gLlGDdk>`_.


Try it yourself: 
On your Google Cloud Platform project console page:  

* **Choose the Compute Engine option from the menu icon in the upper-left corner.**
  
* Choose the VM instances page.
   #. Note: the first time you visit the page, you will see two options: "Create Instance" or "Take the quickstart".) After that, you will see a page with a list    of existing (running or stopped) VMs. 

* Select the Create Instance option, and customize your instance preferences:
   #. **Name:** this name is relatively arbitrary, choose something that is meaningful to you;
   #. **Zone**: choose one of the us-east or us-central zones;
   #. **Machine type**:  you can specify a VM with anywhere between 1 and 16 cores (aka vCPUs), and with up to 100 GB of RAM (you can try the "Customize" view if you      prefer a more graphical approach);  note that as you change the specifications of the VM, the estimated cost shown on this page will update;
   #. **Boot disk**:  the default boot disk and OS will be shown, but you can change this as you wish: the "Change" button will result in a flyout panel where you can choose from a variety of Preconfigured images (Debian, CentOS, Ubuntu, RedHat, etc) or previously created images or disks; you can also choose between "standard disks" and faster (and more expensive) solid-state drives (SSDs), and specify the size of the disk (up to 64TB).

* Once you have all of the options set, you can click on the blue **Create** button. 
   #. Creating the VM should take less than a minute, after which you will see it listed on the "VM instances" page, with the Name, Zone, Disk, Network, and     External IP address shown.  There is also an SSH button that you can use directly from the Console.


Launch a VM using the Command Line Interface 
============================================
The command line argument to create a new VM instance is **gcloud compute instances create**.  The complete
documentation can be found 
`online <https://cloud.google.com/sdk/gcloud/reference/compute/instances/create>`_ 
or by typing **gcloud compute instances create --help** on the command line.

Some defaults can be obtained (if available) from your configuration settings.  For example, if you don't want
to have to specify the zone of the instances, you can set the compute/zone property, for example:

**gcloud config set compute/zone us-central1-a**

A list of zones can be fetched by running:

**gcloud compute zones list**


Here is a very simple command to create a VM:

**gcloud compute instances create my-instance --machine-type g1-small**


Accessing your new VM
=====================
Whether you have created your VM from the Console or using the gcloud CLI, you can find it and 
ssh to it, again using either the Console or the CLI:

  * From the Console, go to Compute Engine > VM instances, and then click on the **SSH** button on the far-right of the row describing the specific VM you would like to connect to.
  * Using the CLI, simply use the command **gcloud compute ssh** followed by the instance name.


Shutting down your VM
=====================
Remember that as long as your VM is running, whether or not *you* are actually doing anything with it,
charges will be incurred.  It is therefore a good idea to get in the habit of shutting down VMs as 
soon as you are finished with your work.  They can easily be restarted an hour, day, or week later.
Note that resources that are *attached* to a stopped VM (such as persistent disks) *will*, however
continue to incur charges.  Compared to the cost of the VM, though, the cost of a persistent disk
is typically negligible:  a 50 GB standard persistent disk only costs $2 per month, and 1 TB costs $40.

If you know that you won't ever need this specific VM again, or you don't want to continue paying for
the persistent disk, or you would rather start a fresh VM with an updated OS next time, then you can go 
ahead and **delete** the VM rather than just stopping it.

From the command-line, the relevant commands are **gcloud compute instances stop** and 
**gcloud compute instances delete**.

