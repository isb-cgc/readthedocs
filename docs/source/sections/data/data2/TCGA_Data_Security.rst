***************************
Understanding Data Security
***************************

Much of the low-level TCGA and TARGET data (including DNA and RNA reads, and SNP CEL files, for example) are 
classified as "controlled access data" and are under the control of the 
`dbGaP <http://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/about.html>`_ 
Data Access Committee (DAC).

Investigator(s) requesting to receive Genomic data in accordance with the 
`NIH Genomic Data Sharing Policy <https://gds.nih.gov/>`_
are required to submit:

* a **data access request** (DAR)
* a **research use statement** (RUS)

**Note:** Requesters and institutional signing officials (SO) must have NIH eRA user IDs to begin this process. 
Visit the `electronic Research Administration <http://era.nih.gov>`_ (eRA) for more information on 
registering for a NIH eRA account. NIH staff may utilize their NIH log-in. 
(See the `dbGaP Data Access Request Portal <http://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?login=&page=login>`_ 
for additional `instructions <http://www.genome.gov/20019654>`_.)

Additionally, they must:
 
*  Submit a `Data Use Certification <http://www.genome.gov/20019653>`_ (DUC) co-signed by the designated Institutional Official(s) at their sponsoring institution (`sample DUC <http://gds.nih.gov/pdf/Model_DUC.pdf>`_);
*  Protect data confidentiality (any data which has been designated "controlled" **must** be protected accordingly, unless prior release authorization is obtained from a NCI data custodian);  and 
*  Ensure that appropriate data security measures are in place.

In the context of Google Cloud Platform (GCP) projects, it is important to realize that all members of a GCP project have (at least) read access
to all data stored within that project, as well as to all virtual machines, boot-disks, and persistent disks attached to that project.
Therefore, if a PI establishes a GCP project (project-A) for the purposes of analyzing controlled data (*eg* performing mutation analysis on TCGA sequence
data), then *all* members of project-A must be authorized to view controlled data.  The outputs of certain analyses performed on controlled data,
if they are summary in nature, may no longer be controlled data and could be copied to a second GCP project (project-B) for further downstream
analyses by researchers who are not authorized to view controlled data.  Researchers who are not authorized to view controlled data could be made
members of project-B, while users who *are* authorized could be members of both project-A *and* project-B.

**Note:**  The PI and the PI's institution are *responsible* for and will be held *accountable* for ensuring the security of controlled data, 
not the cloud service provider.  The Google Cloud Platform has been certified as 
`FedRAMP compliant <https://www.fedramp.gov/marketplace/compliant-systems/google-google-services/>`_
which means that it has been independently assessed and shown to meet all necessary 
`FedRAMP security controls <https://www.fedramp.gov/files/2015/03/FedRAMP-Security-Controls-Preface-FINAL-1.pdf>`_.  
This provides the assurance that the data-security and access control mechanisms
implemented by the Google Cloud Platform and made
available to end-users are sufficient to safeguard the data.  However, it remains the PI's responsibility
to ensure that these access control mechanisms are used appropriately and effectively within the 
context of the PI's GCP project.

You should think about securing controlled data within the context of your GCP project in the same way that you
would think about securing controlled data that you might download to a file-server or compute-cluster at your
own institution.  Your responsibilities regarding the appropriate use of the data are the same in a cloud environment.   
For more information, please refer to 
`NIH Security Best Practices for Controlled-Access Data <http://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/GetPdf.cgi?document_name=dbgap_2b_security_procedures.pdf>`_.  

*"The Investigator and their associated institution assume the responsibility for the security of the dbGaP data.  As such, NIH has tried to provide as much information as possible for PIs, institutional signing officials (SOs) and the IT staff who will be supporting these projects, to make sure they understand their responsibilities."* (Ref: `The Cloud, dbGaP and the NIH <http://datascience.nih.gov/blog/cloud>`_ blog post 03.27.2015)

