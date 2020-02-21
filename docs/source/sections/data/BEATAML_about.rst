******************************
BEATAML1.0 Data Set
******************************

About the BEATAML1.0
-------------------------------

The `BEATAML1.0 <https://www.lls.org/beat-aml>`_ data is from several studies focused on acute myeloid leukemia (AML) and the effect of different therapies such as the drug Crenolanib. The implementation of targeted therapies for AML was challenging due to two reasons. First, due to the intricate mutational patterns within and across patients. Second, a shortage of pharmacologic agents for most mutational events.

The Crenolanib drug was studied because it is a potent type I pan-FLT3 (GeneID:2322) inhibitor, and FLT3 mutations are associated with poor prognosis and commonly detected in AML patients.

About the BEATAML1.0 Data
------------------------------------

The BEATAML1.0 consists of over 220 files with 56 phenotyped subjects, 672 tumor specimens collected from 562 patients, and over 36 TB of data. The data is made up of mainly BAM, VCF, TXT, and TSV files. The majority of the data is whole-exome sequencing along with RNA sequencing. The project identification in the GDC is `BEATAML1.0-CRENOLANIB <https://portal.gdc.cancer.gov/projects/BEATAML1.0-CRENOLANIB>`_ and `BEATAML1.0-COHORT <https://portal.gdc.cancer.gov/projects/BEATAML1.0-COHORT>`_.


For more information on the BEATAML1.0 data, please refer to these sites:

- `BEATAML1.0-CRENOLANIB dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001628.v1.p1>`_
- `BEATAML1.0-COHORT dbGaP site <https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001657.v1.p1>`_
- `GDC Data Portal <https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22BEATAML1.0%22%5D%7D%7D%5D%7D&searchTableTab=files>`_

Data sets and tables available in BigQuery from ISB-CGC are explorable through the `BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_. You can find the files within the ``isb-cgc.GDC_metadata`` tables in BigQuery.
