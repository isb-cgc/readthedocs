***************************
Understanding Data Security
***************************

Investigator(s) requesting and receiving Genomic data in accordance with the `NIH Genomic Data Sharing (GDS) Policy <https://gds.nih.gov/>`_
are expected to:

* Submit a **data access request** (DAR)
* Submit a **research use statement** (RUS)

**Note:** Requesters and institutional SOs must have an NIH eRA User ID and password to begin this process. Visit `electronic Research Administration (eRA) <http://era.nih.gov>`_ for more information on registering for a NIH eRA account. NIH staff may utilize their NIH log-in. (See additional instructions at `Data Access Request Instructions <http://www.genome.gov/20019654>`_) dbGap Data Access `Request Portal <http://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?login=&page=login>`_; 

Additionally, they must:
 
*  Submit a `Data Use Certification (DUC) <http://www.genome.gov/20019653>`_ co-signed by the designated Institutional Official(s) at their sponsoring institution. Sample `DUC form <http://gds.nih.gov/pdf/Model_DUC.pdf>`_;
*  Protect data confidentiality (any data which has been designated "controlled" **must** be protected accordingly, unless prior release authorization is obtained from NCI data custodian); 
*  Ensure that appropriate data security measures are in place

In the context of Google Cloud Platform (GCP) projects, it is important to realize that all members of a GCP project have (at least) read access
to all data stored within that project, as well as to all virtual machines, boot-disks, and persistent disks attached to that project.
Therefore, if a PI establishes a GCP project (project-A) for the purposes of analyzing controlled data (*eg* performing mutation analysis on TCGA sequence
data), then *all* members of project-A must be authorized to view controlled data.  The outputs of certain analyses performed on controlled data,
if they are summary in nature, may no longer be controlled data and could be copied to a second GCP project (project-B) for further downstream
analyses by researchers who are not authorized to view controlled data.  Researchers who are not authorized to view controlled data could be made
members of project-B, while users who *are* authorized could be members of both project-A *and* project-B.

**Note:**  YOU and YOUR institution are **responsible* for and will be held **accountable** for ensuring the security of controlled data, 
not the cloud service provider.  The Google Cloud Platform has been certified as 
`FedRAMP compliant <https://www.fedramp.gov/marketplace/compliant-systems/google-google-services/>`_
which means that it has been independently assessed and shown to meet all necessary 
`FedRAMP security controls <https://www.fedramp.gov/files/2015/03/FedRAMP-Security-Controls-Preface-FINAL-1.pdf>`_.

You should think about securing controlled data within the context of your GCP project in the same way that you
would think about securing controlled data that you might download to a file-server or compute-cluster at your
own institution.  Your responsibilities for data protection are the same in a cloud environment.   
For more information, please refer to:

*  `NIH Security Best Practices for Controlled-Access Data <http://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/GetPdf.cgi?document_name=dbgap_2b_security_procedures.pdf>`_) 
    - The Investigator and their associated institution assume the responsibility for the security of the dbGaP data.  As such, NIH has tried to provide as much information as possible for PIs, institutional signing officials (SOs) and the IT staff who will be supporting these projects, to make sure they understand their responsibilities. (Ref: The `Cloud, dbGaP and the NIH blog <http://datascience.nih.gov/blog/cloud>`_ post 03.27.2015)

Finally, they must:

*  Notify the appropriate Data Access Committee of policy violations; and 
*  Submit annual progress reports detailing significant research findings. See more at: `Policy for Sharing of Data Obtained in NIH Supported or Conducted Genome-Wide Association Studies (GWAS) <http://grants.nih.gov/grants/guide/notice-files/NOT-OD-07-088.html#sthash.Hde6DhfF.Fbj4vpAj.dpuf>`_.
