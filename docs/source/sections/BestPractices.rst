
============
Best practices when working on the Google Cloud Console
============

***************
Overview
***************


***************
Storage
***************

A single API for all storage classes
=====================================
Cloud Storage’s consistent API, latency, and speed across storage classes simplifies development integration and reduces code complexity. Implement Object Lifecycle Management to set a Time to Live (TTL) for objects, archive older version of objects, or downgrade storage classes without compromising on latency or accessibility. Set custom policies to transition data seamlessly from one storage class to the next, depending on your cost and availability needs at the time. 

Where can I find pricing information?
-----------------------------------------

Read the `Pricing page <https://cloud.google.com/storage/pricing/>`_ for detailed information on pricing, including how Cloud Storage calculates bandwidth and storage usage.

When do I need to activate Cloud Storage and enable billing?
-------------------------------------------------------------
If you want to create buckets, store data, or control who can access your data, you must activate Cloud Storage and enable billing.

I am just trying to download or access some data that is freely available to the public. How can I do that?
--------------------------------------------------------------------------------------------------------------

You can simply use the gsutil tool to download the data, even without a Google account. You do not need to activate Cloud Storage or turn on billing for this purpose. You also do not need to create credentials or authenticate to Cloud Storage. The gsutil tool is best installed as part of the Google Cloud SDK package, but may also be downloaded and installed as a stand-alone product.

What tools and libraries are available for Cloud Storage?
----------------------------------------------------------

In addition to the `JSON API <https://cloud.google.com/storage/docs/json_api/>`_ and the `XML API <https://cloud.google.com/storage/docs/xml-api/overview/>`_, Google offers the following options for interacting with Cloud Storage:
The browser-based `Google Cloud Platform Console <https://cloud.google.com/storage/docs/xml-api/overview/>`_ performs basic operations on buckets and objects.
The `gsutil command-line tool <https://cloud.google.com/storage/docs/gsutil>`_ provides a command-line interface with Cloud Storage.
The `Cloud Storage Client Libraries <https://cloud.google.com/storage/docs/reference/libraries>`_ provide programmatic support for a number of programming languages, including Java, Python, and Ruby.
You can find additional, third-party tools and libraries, such as the `Boto library <https://cloud.google.com/storage/docs/boto-plugin>`_, by searching the Internet.

How can I get a summary of daily space usage?
----------------------------------------------

You can use the gsutil du command or Storage Logs to get the total space used by all objects for a specified bucket. For more information, see `Determining a Bucket's Size <https://cloud.google.com/storage/docs/getting-bucket-information#bucket-size>`_.



***************
Best Practices for Migrating Virtual Machines to Compute Engine
***************

Example use cases
==================

Migrating many workloads in parallel
-------------------------------------

A retail company was acquired and needed to move all of their workloads to Cloud Platform. Their Linux-based fleet of machines was spread across on-premises data centers and various cloud providers. While some machines were easy to move over, they knew they would be challenged in moving over their database and SAN devices with minimal downtime. Each minute of downtime for the retailer would mean loss of revenue.

CloudEndure was able to continuously replicate their entire fleet, in parallel, while also upgrading their Linux kernels on the destination Compute Engine VMs. They migrated the SAN storage volumes directly into Compute Engine persistent disks. When all replication had completed, the cutover window was narrowed to just a few minutes.


Migrating Windows workloads running on VMWare
----------------------------------------------

A company with multiple data centers in Asia had a heavy footprint of Windows virtual machines running on VMware. They needed to move their Windows Server 2008R2 and Windows Server 2012R2 servers to Cloud Platform, with minimal downtime to their critical services, such as Active Directory and Exchange.

Despite the many disparate apps and the mix of Windows versions, they were able to use CloudEndure’s disk-level replication to use the same migration approach for all of their systems.

Migrating a large multi-tiered application
--------------------------------------------

A company with a large, multi-tiered application workload wanted to migrate their servers from their data center to the cloud. Ninety percent of their on-premises workload was virtual, and the customer was aware of tools that allowed them to slowly ship virtual disk snapshots into the cloud and perform manual system modifications to make the machines cloud-ready. Although not ideal, because significant downtime would be required during cutover, it was possible. However, 10% of the workload was running on physical servers, which happened to host critical databases. This posed a significant migration problem because the customer couldn't use any hypervisor-based methodologies to migrate these crucial physical servers.

Using CloudEndure's infrastructure-agnostic agent, coupled with its automated machine conversion engine, the customer was able to move both the physical and virtual servers into the cloud, using the same process and tools. Furthermore, CloudEndure's disk-level replication approach kept the migration process identical across all application tiers. Block-level replication reduced the cutover downtime to minutes, instead of many hours.

Migrating a frequently updated app
------------------------------------

A company with a frequently updated application workload wanted to migrate to the cloud. Initially, the customer set up pre-configured, standby systems in the cloud, and attempted to move the source application data into the target standby systems. They planned to promote the standby applications to primary ones at a later date. However, moving the data and keeping it in sync proved to be a time consuming endeavor, during which the source application and OS continued to be frequently updated. The customer grew more concerned over time that some patches or application changes would be left behind during the cutover stage, causing an outage.

CloudEndure's block-level replication approach addressed the concern. Cloud Endure ensured that all the disk blocks would be replicated in a consistent state. Target disks would not only maintain the actual application data using its most up-to-date state, but OS patches, updates, application configuration, and more, would be kept intact, as well.

Migrating from multiple data centers
--------------------------------------

A company with multiple data centers, both on-premises and in colocation facilities, needed to consolidate all of them as part of a migration to the cloud. Aside from the typical challenges of moving applications from one infrastructure to another, the customer also ran into networking challenges. Some of the applications were using identical, private IP space in multiple segregated networks, which would have resulted in conflicts once migrated into a single, consolidated, cloud-based network. It was clear that networking changes would be required in the cloud before the migration could be executed. It was critical to be able to make such changes and test them easily, and in a non- disruptive fashion.

CloudEndure's target-machine-blueprint mechanism allowed the customer to define and redefine, as frequently as needed, how the target-server network settings were going to be provisioned in the cloud. After each blueprint configuration iteration, the customer could test spinning up the target servers in an isolated cloud network and verify their behavior without impacting the source servers. When all test criteria had been met, the cutover window was scheduled and the migration cutover was executed, with high predictability and low risk.


