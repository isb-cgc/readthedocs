***************
TARGET Data Set
***************

About the TARGET Program
------------------------
**TARGET** is the Therapeutically Applicable Research to Generate Effective Treatments program. TARGET applied a comprehensive genomic approach to determine molecular changes that drive childhood cancers. Investigators formed a collaborative network to facilitate the discovery of molecular targets and translate those findings into the clinic. TARGET is managed by NCI's Office of Cancer Genomics and Cancer Therapy Evaluation Program.

The TARGET data is available at the GDC, both in the `legacy archive <https://portal.gdc.cancer.gov/legacy-archive/search/f?filters=%7B%22op%22:%22and%22,%22content%22:%5B%7B%22op%22:%22in%22,%22content%22:%7B%22field%22:%22cases.project.program.name%22,%22value%22:%5B%22TARGET%22%5D%7D%7D%5D%7D>`_ which contains over 10,000 files for over 5,000 cases. Virtually all of this data is low-level (and controlled-access) sequence data (including 1702 RNA-seq files, 765 miRNA-seq, with the remainder being WXS or WGS DNA-seq BAMs).
Some of this data has been reprocessed and is available on the main `GDC Data Portal <https://portal.gdc.cancer.gov/projects?filters=~%28op~%27and~content~%28~%28op~%27in~content~%28field~%27projects.program.name~value~%28~%27TARGET%29%29%29%29%29>`_. This newer dataset so far includes 6183 files representing 3236 cases and totaling over 17 TB. Over half of the files (3740) are controlled-access files, including BAM, VCF, and MAF file types, based on WXS, RNA-seq, and miRNA-seq data. The remaining 2443 are open-access files, including RNA-seq and miRNA-seq quantification, as well as clinical and biospecimen supplement files.

For more information about the TARGET program, please visit the official `TARGET website <https://ocg.cancer.gov/programs/target>`_.

About the TARGET Data
---------------------

The ISB-CGC currently hosts several TARGET data sets in BigQuery. TARGET controlled-access data is available to authorized users in Genomic Data Commons and open-access data includes RNA-seq and miRNA-seq expression levels, and is available in BigQuery, along with the open-access clinical and biospecimen information.

BigQuery TARGET Data
+++++++++++++++++++++++

The open-access TARGET data hosted by the ISB-CGC Platform includes:

* Clinical (de-identified) and Biospecimen data: these data were originally provided in XML files (Level-1) by the TARGET DCC
* Gene (mRNA) expression data:  these data were originally provided as TSV files (Level-3) by the TARGET DCC
* microRNA expression data:  these data were originally provided as TSV files (Level-3) by the TARGET DCC

The information scattered over thousands of XLSX and TSV files at the GDC is provided in a *much more accessible* form in a series of 
`BigQuery tables <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/data2/data_in_BQ.html#target-clinical-biospecimen-and-molecular-data>`_.

