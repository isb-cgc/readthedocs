Setting up your GCP project
###########################

This setup guide assumes that you are already a member of a GCP project with either
"Owner" or "Editor" rights.  If you need a GCP project, you may request one as part of
the ISB-CGC community evaluation phase going on now.

Google Cloud Console
====================
If you are new to the Google Cloud, it is a good idea to become familiar with the 
`Cloud Console <https://console.cloud.google.com>`_ (which we will 
generally refer to simply as the Console).  You can get help from within the Console
by clicking on the Help (question mark) icon near the upper right-hand corner.
The Console provides a convenient web UI for managing resources within your cloud project, 
and can be useful for obtaining a quick, high-level snapshot of the state of your project.
The "Home" page will list, for example, the number of buckets you have created in Cloud
Storage, the number of datasets in BigQuery, and the number of VMs you have running under
App Engine or Compute Engine.  
It also shows the charges incurred by this project so far this month.

Enable the Compute Engine API
=============================
The Compute Engine API is probably enabled by default on your GCP project, but you
can verify this through the Console: click on the menu icon 
in the upper left hand corner (when you hover over it you will see "Products and services"),
and then select the API Manager.  The API Manager page has two sections: Overview and
Credentials.  Within the Overview page, you can see a list of all "Google APIs" and
a list of the "Enabled APIs".

You can check your list of "Enabled APIs", or simply select the "Compute Engine API" link
which should be at the very top of the list of "Popular APIs".  Once you are on the 
"Google Compute Engine" page, you should either see a blue button with the word "Enable"
or a white "Disable button.  
If the button says Enable, click on it.  This process will take a minute or two,
after which you will be prompted to "Go to Credentials".  You should not need to create 
new credentials at this time -- you will typically be using 
`Application Default Credentials <https://developers.google.com/identity/protocols/application-default-credentials?hl=en_US>`_.
(This `blog post <http://googlecloudplatform.blogspot.com/2015/07/Easier-Auth-for-Google-Cloud-APIs-Introducing-the-Application-Default-Credentials-feature.html>`_ 
introducing Application Default Credentials may also be helpful.)  
The proper use of credentials is frequently one of the most complicated
aspects of interacting with the Google Cloud Platform.  If you are having problems, please
let us know.

You may also find the official Compute Engine 
`Getting Started Guide <https://cloud.google.com/compute/docs/quickstart>`_ helpful.

Google Cloud SDK
================
Depending on how you choose to interact with the Google Cloud Platform, you may want
to install the `Google Cloud SDK <https://cloud.google.com/sdk/>`_ on your local workstation.  
The Google Cloud SDK is a set of command-line interface (CLI) tools 
that you can use to manage resources and applications
hosted on GCP.  
(Note that components of the the SDK are updated quite frequently.  You will be notified
when updates are available anytime you use one of the SDK tools.  The command will still run,
but you will be notified that
"Updates are available for some Cloud SDK components" and you will be given instructions on how to 
update your local copy of the SDK.)

Confirm that you have installed the SDK and have access to it by typing ``gcloud --version``
at the command line of your own linux workstation or from the Cloud Shell (for more details
about the Cloud Shell, see the next section).  You should see something like this::

    Google Cloud SDK 98.0.0
    
    bq 2.0.18
    bq-nix 2.0.18
    core 2016.02.22
    core-nix 2016.02.05
    gcloud 
    gsutil 4.16
    gsutil-nix 4.15

Google Cloud Shell
==================
`Google Cloud Shell <https://cloud.google.com/shell/docs/>`_ provides you with command-line
access to computing resources hosted on GCP is available from the Console.  Cloud Shell provides
you with a temporary VM running a Debian-based Linux OS, with 5 GB of persistent disk storage
per user, and the Google Cloud SDK and other tools pre-installed.

From the Console, you will find the icon for the Cloud Shell in the top-most blue bar, near
the right-hand corner, between your GCP project name and the "Send feedback" icon.  If you
click on that icon (the hover-card should read "Activate Google Cloud Shell"), 
it will take a minute or two for you VM
to be provisioned, after which you will see a prompt saying "Welcome to Cloud Shell" in the
new window that has appeared at the bottom of your Console page.  You can "pop" that 
window out of your browser page by clicking on the "Open in new window" icon in the upper
right-hand corner of the shell window.

.. _authenticategoogle:

Authenticate with Google
========================
Regardless of how you choose to interact with the Google Cloud, you will need to authenticate
yourself.  How this authentication takes place will depend on "where" you are.  If you
have signed into Chrome using your Google identity and you then go to the Console, you will
already have been authenticated.  If you are at the Linux prompt of the Cloud Shell, you 
have also already been authenticated because that Shell (and that VM) were launched for
you from your Console.  If you are at the Linux prompt of your local workstation, you will
need to authenticate using the **gcloud** command line utility.

There are two approaches:

  * `gcloud init <https://cloud.google.com/sdk/gcloud/reference/init>`_  launches an interactive Getting Started workflow for gcloud;  
  * `gcloud auth login <https://cloud.google.com/sdk/gcloud/reference/auth/login>`_  obtains access credentials for your user account via a web-based authorization flow.

These approaches may ask you to cut-and-paste a long URL into a browser, sign in using your Google
credentials, click "Allow" to allow Google to access certain information about you, and may also
ask that you cut-and-paste an authorization token from your browser back into the Linux shell.

Once you have authenticated, you can see information about your current configuration by
typing ``gcloud config list``.  You can set additional properties using the ``gcloud config set``
command.  The most common properties you are likely to want to verify
(`list <https://cloud.google.com/sdk/gcloud/reference/config/list>`_), or 
`set <https://cloud.google.com/sdk/gcloud/reference/config/set>`_ explicitly are:

  * account
  * project
  * compute/region
  * compute/zone
  * container/cluster

