New Program Data Available in Google Cloud Storage
=======================================

We have new program data available via Google Cloud Storage. While we work on adding all the new programs to our cohort creation section of the web application we have created this document as a work around.  This tutorial will enable you to be albe to find files in Google Cloud Storage via the Data Commons' Framework tool IndexD. If you have any additional questions or comments please feel free to contact feedback@systemsbiology.org. 

New Programs
-------------

Foundation Medicine Adult Cancer Clinical Dataset (FM-AD)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Foundation Medicine adult cancer clinical dataset consists of 18,004 unique solid tumor samples that underwent genomic profiling on a single uniform platform as part of standard clinical care. The dataset is derived from the FoundationOne® genomic profiling assay version 2 that interrogates exonic regions of 287 cancer-related genes and selected introns from 19 genes known to undergo rearrangements in human cancer. For more information please `visit <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001179.v1.p1/>`_. 

The Data Use Aggreement for Foundation Medicine can be found `here <https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?view_pdf&stacc=phs001179.v1.p1>`_. 


Clinical Trial Sequencing Project (CTSP) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the Clinical Trials Sequencing Project (CTSP), National Cancer Institute (NCI) will utilize whole genome sequencing and/or whole exome sequencing in conjunction with transcriptome sequencing to try to identify recurrent genetic alterations (mutations, deletions, amplifications, rearrangements) and/or gene expression signatures that would be important to the hypothesis(es) submitted by the investigators. The samples will be processed and submitted for genomic characterization using pipelines and procedures established within The Cancer Genome Analysis (TCGA) project. For more information please `visit <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001175.v2.p2>`_. 

The Data Use Aggreement for The Clinical Trial Sequencing Project can be found `here <https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?view_pdf&stacc=phs001175.v2.p2>`_. 


VA APOLLO Project - Research for Precision Oncology (VAREPOP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Research for Precision Oncology Program (RePOP) is a research activity that establishes a cohort of Veterans diagnosed with cancer and who have had genomic analyses performed on their tumor tissue as part of standard of care. All data relevant to a patient's cancer and cancer care will be collected under RePOP, including patient demographics, co-morbidities, genomic analysis, treatments, medications, lab values, imaging studies, and outcomes. All RePOP participants will have signed/verbal informed consent and signed HIPAA authorization to have their data stored and shared from RePOP's Precision Oncology Program Data Repository (PODR). For more information please `visit <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001374.v1.p1>`_. 

The Data Use Aggreement for The VA Apollo Research for Precision Oncology Program can be found `here <https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?view_pdf&stacc=phs001374.v1.p1>`_.



Genomic Variation in Diffuse Large B Cell Lymphomas (NCICCR)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Integrative analysis of genetic lesions in 574 diffuse large B cell lymphomas (DLBCL). The study investigates genomic structural variation, genetic alteration and its effect on the development and biology of lymphomas by using high throughput sequencing, gene expression, and methylation status.

Study Type: Case Set
Number of study subjects that have individual level data available through Authorized Access: 489
489 phenotyped subjects

For more information please `visit <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001444.v1.p1>`_. 

The Data Use Aggreement for The Genomic Variation in Diffuse Large B Cell Lymphoma can be found `here <https://dbgap.ncbi.nlm.nih.gov/aa/wga.cgi?view_pdf&stacc=phs001444.v1.p1>`_.



Login via NIH ID to ISB-CGC
-----------------------------

To access the controlled data files you will first need to be authoenticated with your NIH ID and you Google ID using the DCF's fence.  For information on how to set up access to controlled data please go `here <https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/webapp/Gaining-Access-To-Contolled-Access-Data.html#linking-your-nih-and-google-identities>`_.



How to find files via IndexD
-----------------------------

This tutorial will go thorough how to find controlled access file paths for all four new programs FM, CTSP, VAREPOP, and NCICCR via the Genomic Data Commons.  


Find GDC ID in Genomic Data Portal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Foundation Medicine (FM)
"""""""""""""""""""""""""

The Gonomic Data Commons currently has VCF, TSV, and MAF data available. To see the GDC data portal with Foudation Medicine as program selected please select `here <https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22FM%22%5D%7D%7D%5D%7D&searchTableTab=cases>`_.

VCF: 36,008 files
TSV: 84 files
MAF: 42 files

Controlled Access: 36,050
Open Access: 84 files


Clinical Trial Sequencing Project (CTSP)
""""""""""""""""""""""""""""""""""""""""""

The Genomic Data Commons currently has only bam files currently available. To see the GDC data portal with Clinical Trial Sequencing Project please select `here <https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CTSP%22%5D%7D%7D%5D%7D&searchTableTab=cases>`_.

BAM: 89 files
ALL CONTROLLED

VA APOLLO Project - Research for Precision Oncology (VAREPOP)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The Genomic Data Commons currently has bam and vcf files.  To see the GDC data portal with Research for Precision Oncology Project please select `here <https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22VAREPOP%22%5D%7D%7D%5D%7D>`_. 

VCF: 14 files
BAM: 7 files
ALL CONTROLLED



Genomic Variation in Diffuse Large B Cell Lymphomas (NCICCR)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The Genomic Data Commons currently has only bam files currently available.  To see the GDC data portal with Genomic Variation in Diffuse Large B Cell Lymphomas Project please select `here <https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22NCICCR%22%5D%7D%7D%5D%7D>`_. 

BAM: 957 files
ALL CONTROLLED


URL to find file information in IndexD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Google Cloud Storage path
^^^^^^^^^^^^^^^^^^^^^^^^^^

