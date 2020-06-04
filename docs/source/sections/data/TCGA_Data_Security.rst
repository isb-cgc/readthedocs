*********************************
Data Access and Security Overview
*********************************

Understanding Data Access Levels
--------------------------------

* **Public Data**  Sometimes the word "public" is misinterpreted as meaning "open".  All of the TCGA data is *public* data, and much of it is *open*, meaning that it is accessible and available to *all* users; while some low-level TCGA data is *controlled* and restricted to authorized users.
* **Open-Access Data**  Depending on how you categorize the data, *most* of the TCGA data is open-access data.  This includes all de-identified clinical and biospecimen data, as well as all Level-3 molecular data including gene expression data, DNA methylation data, DNA copy-number data, protein expression data, somatic mutation calls, etc. 
* **Controlled-Access Data**  All low-level sequence data (both DNA-seq and RNA-seq), the raw SNP array data (CEL files), germline mutation calls, and a small amount of other data are treated as *controlled* data and require that a user is properly authenticated and have dbGaP authorization prior to accessing these data.

Note that many public, open-access datasets may still be **restricted** in various ways.  Typically, a **License** document containing explicit terms of use will be associated with each dataset.  Some institutions have their own licenses, though many uses one of the `Creative Commons <https://creativecommons.org/>`_ licenses.  License terms apply to both data and source-code, so please be aware of the terms of a license whenever you plan to reuse data or source code produced by someone else. We  recommend that you review the `TCGA Publication Guidelines <https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga/using-tcga/citing-tcga>`_.


Understanding Data Security
---------------------------

Much of the low-level TCGA and TARGET data (including DNA and RNA reads, and SNP CEL files, for example) are 
classified as "controlled access data" and are under the control of the 
`dbGaP <http://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/about.html>`_ 
Data Access Committee (DAC).

Investigator(s) requesting to receive genomic data in accordance with the 
`NIH Genomic Data Sharing Policy <https://gdc.cancer.gov/access-data/data-access-policies>`_
are required to submit:

* a **data access request** (DAR)
* a **research use statement** (RUS)

**Note:** Requesters and institutional signing officials (SO) must have NIH eRA user IDs to begin this process. Visit the `electronic Research Administration <http://era.nih.gov>`_ (eRA) for more information on registering for an NIH eRA account. NIH staff may utilize their NIH login. (See the `dbGaP Data Access Request Portal <http://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?login=&page=login>`_ 
for additional `instructions <https://osp.od.nih.gov/wp-content/uploads/Extramural_Flowcharts_for_Data_Access.pdf>`_.)

Additionally, they must:
 
*  Submit a `Data Use Certification <https://osp.od.nih.gov/wp-content/uploads/Model_DUC.pdf>`_ (DUC) co-signed by the designated Institutional Official(s) at their sponsoring institution
*  Protect data confidentiality (any data which has been designated "controlled" **must** be protected accordingly, unless prior release authorization is obtained from an NCI data custodian)
*  Ensure that appropriate data security measures are in place

**Google Clould Platform and Access Control** 

In the context of Google Cloud Platform (GCP) projects, it is important to realize that all members of a GCP project must have at least read access to all data stored within that project, as well as to all virtual machines, boot disks, and persistent disks attached to that project. 

Therefore, if a principle investigator (PI) establishes a GCP project (project-A) for the purposes of analyzing controlled data (*eg* performing mutation analysis on TCGA sequence data), then:

- *All* members of project-A must be authorized to view controlled data.  
- The outputs of certain analyses performed on controlled data, if they are summary in nature, may no longer be controlled data and could be copied to a second GCP project (project-B) for further downstream analyses by researchers who are not authorized to view controlled data.  
- Researchers who are not authorized to view controlled data could be made members of project-B, while users who *are* authorized could be members of both project-A *and* project-B.

**Your Responsibilities** 

The PI and the PI's institution are *responsible* for and will be held *accountable* for ensuring the security of controlled data, not the cloud service provider.  The Google Cloud Platform has been certified as `FedRAMP compliant <https://marketplace.fedramp.gov/#/product/google-services-google-cloud-platform-products-and-underlying-infrastructure?sort=productName&productNameSearch=google>`_
which means that it has been independently assessed and shown to meet all necessary `FedRAMP <https://www.fedramp.gov/>`_ security controls.  This provides the assurance that the data security and access control mechanisms implemented by the Google Cloud Platform and made available to end users are sufficient to safeguard the data.  However, it remains the PI's responsibility to ensure that these access control mechanisms are used appropriately and effectively within the context of the PI's GCP project.

You should think about securing controlled data within the context of your GCP project in the same way that you
would think about securing controlled data that you might download to a file server or compute cluster at your
own institution.  Your responsibilities regarding the appropriate use of the data are the same in a cloud environment.   
For more information, please refer to the
`NIH Security Best Practices for Controlled-Access Data <http://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/GetPdf.cgi?document_name=dbgap_2b_security_procedures.pdf>`_.  


