Creating and Managing Persistent Disks
######################################

As described in the previous section, you can specify the boot disk when launching a VM from
the Console and from the command-line.  There are times when you may want to create and attach
additional disks to an instance.  There are three main steps in this process:  you must first
**create** the disk, then you must **attach** it to the instance, and finally you must **format** it.
When you are finished, you may want to **detach** the disk and when you are done with it, you
will want to **delete** it.  We will describe each of these steps in a bit more detail below.
You may also want to see the Google documentation on
`Adding Persistent Disks <https://cloud.google.com/compute/docs/disks/persistent-disks>`_.

Create a Persistent Disk
========================
The **gcloud** command for creating a persistent disk is ``gcloud compute disks create``.
The most common options you'll probably use are ``--size``, ``--type``, and ``--zone``
(see `this <https://cloud.google.com/sdk/gcloud/reference/compute/disks/create>`_ page for
more details).  For example::

    gcloud compute disks create disk-1 --size 500GB 

will create a 500 GB disk named "disk-1", using default settings (*eg* the type will be pd-standard).

Attach a Persistent Disk
========================
The **gcloud** command to attach a newly created disk to a previously created instance looks like this:

    gcloud compute instances attach-disk  --disk disk-1  --device-name  my-instance

Note that this command is part of the **gcloud compute instances** group rather than the 
**gcloud compute disks** group.  Details about additional options can be found in the
`documentation <https://cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk>`_.
For example the default mode is **rw** (read-write), but you can also specify that a 
disk be attached **ro** (read-only).

Format a Persistent Disk
========================
In order to format a disk that you've attached to an instance, you need to first log on to that instance::

    gcloud compute ssh  my-instance

For complete details, please refer to the Google documentation on
`formatting <https://cloud.google.com/compute/docs/disks/persistent-disks#formatting>`_
and mounting non-root persistent disks;
but there are two main steps:  first you must format the disk using the **mkfs** tool
(note that this will delete any *existing* data on the disk), and second you must use 
the **mount** tool to mount the disk at a specified mount-point::

    sudo mkfs.ext4 -F /dev/disk/by-id/disk-1
    sudo mkdir /mnt/pd1
    sudo mount -o discard,defaults /dev/disk/by-id/disk-1 /mnt/pd1

Detach a Persistent Disk
========================
Detaching a disk is a two step process: first you unmount the disk (using the **umount** command,
*from* the instance to which it is attached), and then (after logging out from that instance)
you use the **gcloud** tool::

    $sudo umount /dev/disk/by-id/disk-1
    $exit

    gcloud compute instances detach-disk my-instance --disk disk-1

Delete a Persistent Disk
========================
Note that a boot disk will be deleted if you delete the instance that it is attached to (as long
as the auto-delete property for the disk was set to "yes" (the default) when it was created).  In all
other cases, you will need to 
`delete <https://cloud.google.com/sdk/gcloud/reference/compute/disks/delete>`_ 
the disk manually using the ``gcloud compute disks delete``
command.  Note that disks can be deleted only if they are *not* being used by any VM instances.

You can also see and manage persistent disks from the Console on the Compute Engine > Disks page.

