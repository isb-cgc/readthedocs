Launching a Virtual Machine (VM)
################################

You can launch a virtual machine (which we will generally refer to as a VM) from the
Console or from the command line using the Google Cloud SDK.  We will describe both
of these approaches here.

You should already be somewhat familiar with the Console, and hopefully you have tried
invoking the **gcloud** command from your command-line.
The **gcloud** command-line tool can be used to manage both your development workflow
and your GCP resources.  (For more details, please look at the official 
`gcloud Tool Guide <https://cloud.google.com/sdk/gcloud/>`_.)

Bundled into the `gcloud <https://cloud.google.com/sdk/gcloud/reference/>`_ 
CLI are several **commands** and **groups** of sub-commands.  The group of sub-commands
that allows you to read and manipulate GCE resources is 
`gcloud compute <https://cloud.google.com/sdk/gcloud/reference/compute/>`_

Launch a VM using the Console
=============================

After you have enabled the Compute Engine API for you project, you can go the Compute Engine
section of the Console.  (Select the menu icon in the far upper-left corner, and then choose
"Compute Engine" from the flyout panel.)  The first time, you may need to wait a minute or
so while "Compute Engine is getting ready."

You will now be on the "VM instances" page.  (There are may other pages that are accessible
from the left side-panel.)
The first time you visit this page, you will see two options: "Create Instance" or "Take the quickstart".
After the first time, you may see a different page with a list of existing (running or stopped) VMs
with a CPU utilization graph.  At the top of this page, you will see options to "CREATE INSTANCE",
"CREATE INSTANCE GROUP", "RESET", "START", "STOP", and "DELETE" VM instances.

After selecting the "Create Instance" option, you will be sent to the "Create an instance" page
where defaults will be selected for the Name, Zone, Machine type, etc:

    * Name: this name is relatively arbitrary, choose something that is meaningful to you;
    * Zone: choose one of the us-east or us-central zones;
    * Machine type:  you can specify a VM with anywhere between 1 and 16 cores (aka vCPUs), and with up to 100 GB of RAM (you can try the "Customize" view if you prefer a more graphical approach);  note that as you change the specifications of the VM, the estimated cost shown on this page will update;
    * Boot disk:  the default boot disk and OS will be shown, but you can change this as you wish: the "Change" button will result in a flyout panel where you can choose from a variety of Preconfigured images (Debian, CentOS, Ubuntu, RedHat, etc) or previously created images or disks; you can also choose between "standard disks" and faster (and more expensive) solid-state drives (SSDs), and specify the size of the disk (up to 64TB).

Other options below the "Management, disk, ..." line include Preemptibility (default is OFF), 
Automatic restart (default is ON), and what to do during infrastructure maintenance (default 
is to "migrate VM" so that you will not experience any downtime).

Once you have all of the options set, you can click on the blue **Create** button.  You can also 
see you could use the REST or command-line interfaces to do perform the exact same option.  
(The Console is just a friendlier interface between you and more direct REST-based access to the same
functionality.)

Creating the VM should take less than a minute, after which you will see it listed on the "VM instances"
page, with the Name, Zone, Disk, Network, and External IP address shown.  There is also an SSH button
that you can use directly from the Console.

Launch a VM using the CLI
=========================
The command to create a new GCE VM instance is ``gcloud compute instances create``.  The complete
documentaiton can be found 
`online <https://cloud.google.com/sdk/gcloud/reference/compute/instances/create>`_ 
or by typing ``gcloud compute instances create --help`` on the command line.

Some defaults can be obtained (if available) 
from your configuration settings.  For example, if you don't want
to have to specify the zone of the instances, you can set the compute/zone property, for example:
```
gcloud config set compute/zone us-central1-a
```
A list of zones can be fetched by running:
```
gcloud compute zones list
```

Here is a very simple command to create a VM:
```
gcloud compute instances create my-instance --machine-type g1-small
```

Accessing your new VM
=====================
Whether you have created your VM from the Console or using the gcloud CLI, you can find it and 
ssh to it, again using either the Console or the CLI:

  * From the Console, go to Compute Engine > VM instances, and then click on the **SSH** button on the far-right of the row describing the specific VM you would like to connect to.
  * Using the CLI, simply use the command ``gcloud cmopute ssh`` followed by the instance name.


Shutting down your VM
=====================
Remember that as long as your VM is running, whether or not *you* are actually doing anything with it,
charges will be incurred.  It is therefore a good idea to get in the habit of shutting down VMs as 
soon as you are finished with your work.  They can easily be restarted an hour, day, or week later.
Note that resources that are *attached* to a stopped VM (such as persistent disks) *will*, however
continue to incur charges.  Compared to the cost of the VM, though, the cost of a persistent disk
is typically negligible:  a 50 GB standard persistent disk only costs $2 per month, and 1 TB costs $40.

If you know that you won't never need this specific VM again, or you don't want to continue paying for
the persistent disk, or you would rather start a fresh VM with an updated OS next time, then you can go 
ahead and **delete** the VM rather than just stopping it.

From the command-line, the relevant commands are ``gcloud compute instances stop`` and 
``gcloud compute instances delete``.

