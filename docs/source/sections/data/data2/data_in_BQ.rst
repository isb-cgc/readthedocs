************************
Data in BigQuery
************************

The information scattered over tens of thousands of XML and TSV files in two separate archives at the 
`NCI-GDC <https://gdc.cancer.gov/>`_ is provided in a 
*much more accessible* form in a series of *open-access* BigQuery tables.  
For more details, including tutorials, SQL, 
and code examples in `Python <https://github.com/isb-cgc/examples-Python>`_ or 
`R <https://github.com/isb-cgc/examples-R>`_, 
please see our 
`Query of the Month <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/QueryOfTheMonthClub.html>`_ page and our
`github repositories <https://github.com/isb-cgc>`_.
Note that dbGaP authorization is **not** required to access these tables!

If you have suggestions or requests for additional data (*eg* TCGA isoform expression data,
or other reference data sources) that you would like to see made available as BigQuery tables,
please let us know (feedback@isb-cgc.org) and we will try to make that happen.

BigQuery Datasets and Tables
============================

Data made available by the ISB-CGC through BigQuery is organized into several *open-access* 
datasets, where a dataset is made up of multiple tables.  
Datasets in BigQuery are uniquely identified based on the Google Cloud Platform (GCP) project name 
(in this case **isb-cgc**), and the dataset name, separated by a colon (or a period, in standard SQL), 
*eg* ``isb-cgc:TCGA_bioclin_v0``.  Tables are uniquely identified by appending the table name,
preceded by a period, *eg* ``isb-cgc:TCGA_bioclin_v0.Clinical``.

The following sections describe each of the major datasets that are currently publicly-accessible, 
and the tables that each one contains.  For additional details regarding the ETL (extract, transform,
and load) process for each of these data types, please refer to the data-type specific details
below.

For a more visual overview of the contents of BigQuery and how they relate to one another,
you might find this 
`view <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/BQ_overview.html>`_ 
useful.


TCGA Clinical, Biospecimen and Molecular Data
=============================================

The TCGA data is organized into three separate datasets: **TCGA_bioclin_v0** contains clinical
and other metadata; **TCGA_hg19_data_v0** contains the original TCGA molecular data, which was
originally generated based on the GRCh37/hg19 reference; and **TCGA_hg38_data_v0** contains 
the newer GRCh38/hg38-based data now available at the NCI-GDC.

All of the tables include one or more of the following identifiers which can be used for 
performing cross-table JOINs: ``case_barcode``, ``sample_barcode``, and ``aliquot_barcode``.
(Note that these were previously called ``ParticipantBarcode``, ``SampleBarcode``, and
``AliquotBarcode``.)  In addition, most tables also containa a ``project_short_name`` field
(formerly called ``Study``, *eg* TCGA-LUAD, TCGA-BRCA, *etc*).

(Note that in an attempt to be consistent with the NCI-GDC terminology, what we used to call a 
*project* is now called a *program* (*eg* TCGA, TARGET, CCLE, *etc*), while what was
formerly known as a *study* is now called a *project* (and has also been prepended with the
*program* name, so that ``LUAD`` has become ``TCGA-LUAD``, *etc*).

Each dataset and table described below is linked directly the corresponding view in the
`BigQuery web UI <https://bigquery.cloud.google.com>`_ where you can see the schema and 
other additional information for each table, preview its contents, *etc*.

- `isb-cgc:TCGA_bioclin_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_bioclin_v0>`_:

..

  + `Clinical <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_bioclin_v0.Clinical>`_:
    This table is contains one row for each TCGA case (aka patient or participant) with *any* 
    available clinical information -- over 11,000 cases are represented.
    Any given field in 
    this table may be ``null`` for many patients, depending on tumor-type or data-availability.  
    For example, the field ``tobacco_smoking_history`` is available for only about 3,000 patients.
  
..

  + `Biospecimen <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_bioclin_v0.Biospecimen>`_:
    This table is a *sample-centric* table, and contains one row of information for each of the (over 23,000) 
    TCGA samples.  Any given field in this table may be ``null`` for many samples, depending on the 
    sample-type or the tumor-type.

..

  + `Annotations <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_bioclin_v0.Annotations>`_:
    This table contains annotations and related information obtained from the 
    `TCGA Annotations Manager <https://wiki.nci.nih.gov/display/TCGA/TCGA+Annotations+Manager+User's+Guide>`_
    (formerly available at the TCGA DCC).
    

- `isb-cgc:TCGA_hg19_data_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_hg19_data_v0>`_:

..

  + `Copy_Number_Segment_Masked <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.Copy_Number_Segment_Masked>`_: 
    This table contains all available Copy Number segmentation data across all TCGA samples.  
    Each row in the table describes a single copy-number segment for a single aliquot.  
    The fields ``chromosome``, ``start_pos``, and ``end_pos`` specify the chromosomal coordinates (1-based) 
    for the segment, the ``num_probes`` field specifies the number of probes on the SNP chip that 
    went into estimating the mean copy-number for this segment, and finally the ``segment_mean`` 
    provides the ``log2(CN/2)`` mean value estimate.  Values near 0 represent "normal" copy-number, 
    while larger positive values indicate *amplifications* and negative values indicate *deletions*.

..

  + `DNA_Methylation <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.DNA_Methylation>`_: 
    This table contains **all** of the DNA methlyation data for all TCGA samples assayed on either the 
    HumanMethylation 27k or 450k platforms.  Please note that this is a very **large** table 
    (with close to 4 billion rows), so query it with caution -- a *single* query will cost *your* GCP project $2-3.  
    Each row contains the methylation "beta" for a particular aliquot at a particular probe.  
    Details about a particular probe, based on the ``Probe_Id`` field value (*eg* ``cg03879918``) 
    can be obtained from the ``methylation_annotation`` table (available in the 
    `isb-cgc:platform_reference <https://bigquery.cloud.google.com/dataset/isb-cgc:platform_reference>`_ dataset).
    For convenience, this data is also available in 24 chromosome-specific tables so that more
    targeted queries will need to scan less data (and will therefore be cheaper).


  + `miRNAseq_Expression <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.miRNAseq_Expression>`_: 
    This table contains **all** of the miRNAseq stem-loop expression data for all TCGA samples assayed on either the 
    Illumina GA or Illumina HiSeq platforms.  
    

  + `miRNAseq_Isoform_Expression <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.miRNAseq_Isoform_Expression>`_: 
    This table contains **all** of the miRNAseq isoform-level expression (aka isomiR) data for all 
    TCGA samples assayed on either the Illumina GA or Illumina HiSeq platforms.  
    

  + `Protein_Expression <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.Protein_Expression>`_: 
    This table contains protein expression quantification estimates based on the RPPA (reverse phase protein array) 
    platform.  Note that only a subset (~70%) of the TCGA tumor samples were assayed on this platform.  This 
    technology uses antibodies which bind (sometimes non-specifically) to the target protein.  In certain cases, 
    an antibody may target a specific phosphorylated protein.  Each row in this table
    includes an estimate of the ``protein_expression``, with the following fields specifying the 
    protein: ``gene_name`` (aka symbol), ``protein_name``, ``protein_base_name``, and ``phospho``.  
    Additional fields include the ``antibody_source`` and ``validation_status``.


  + `RNAseq_Gene_Expression_UNC_RSEM <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.RNAseq_Gene_Expression_UNC_RSEM>`_: 
    This table contains gene expression data from 10,289 samples assayed on the Illumina HiSeq platform
    and 818 samples assayed on the Illumina GA platform, all of which were then  
    processed through the UNC "RNASeqV2" RSEM pipeline.  Each row in this table contains the RSEM expression 
    estimate for a single gene in a single aliquot.  The gene symbol can be found in the fields 
    ``original_gene_symbol`` (as originally given in the file submitted by UNC to the TCGA DCC), and 
    ``HGNC_gene_symbol`` (the most current HGNC-approved gene symbol at the time this table was created).  
    More details about specific genes can be obtained from any of the ``GENCODE`` tables
    available in the `genome_reference <https://bigquery.cloud.google.com/dataset/isb-cgc:genome_reference>`_ dataset.


  + `Somatic_Mutation_DCC <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.Somatic_Mutation_DCC>`_: 
    This table contains all somatic mutations called across all TCGA tumor samples, based on aggregating all 
    of the MAF files available at the DCC as of June 2016.  Each mutation call was annotated using 
    `Oncotator <https://www.broadinstitute.org/cancer/cga/oncotator>`_, 
    and many (though not all) of the resulting annotation fields were included in this table.  Since multiple
    MAF files are sometimes available for a single tumor type, the MAF ETL process included steps to 
    filter out duplicate mutation calls.


  + `Somatic_Mutation_MC3 <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.Somatic_Mutation_MC3>`_: 
    This table is based on the unified "MC3" TCGA call set recently published by the TCGA Network.  
    For more details or the original source file, please refer to `Synapse <https://www.synapse.org/#!Synapse:syn7214402/wiki/405297>`_.
    The original input file contained 114 columns but many were empty or duplicates of other columns.  This table contains 75 columns.  
    Additional details can be found in the table schema.


- `isb-cgc:TCGA_hg38_data_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TCGA_hg38_data_v0>`_:
  This dataset by and large mirrors the ``TCGA_hg19_data_v0`` dataset, and is based on the GRCh38/hg38 data
  now available from the NCI-GDC.  In some cases the new data has been realigned to the new genome (in the case
  of any DNAseq or miRNA/mRNAseq based data), or the coordinates have been "lifted over" from hg19 to hg38
  (in the case of probe/array-based data such as the SNP6/copy-number and the DNA Methylation data).


A set of 
`reference data <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/Reference-Data.html>`_ 
tables have also been created in BigQuery which you may find helpful when analyzing the TCGA data.


TARGET Clinical, Biospecimen and Molecular Data
=================================================

The TARGET data is organized into two separate datasets: **TARGET_bioclin_v0** contains clinical
and other metadata; and **TARGET_hg38_data_v0** contains 
the GRCh38/hg38-based data now available at the NCI-GDC.

All of the tables include one or more of the following identifiers which can be used for 
performing cross-table JOINs: ``case_barcode``, ``sample_barcode``, and ``aliquot_barcode``.
In addition, most tables also containa a ``project_short_name`` field
(formerly called ``Study``, *eg* TARGET-AML, *etc*).

Each dataset and table described below is linked directly the corresponding view in the
`BigQuery web UI <https://bigquery.cloud.google.com>`_ where you can see the schema and 
other additional information for each table, preview its contents, *etc*.

- `isb-cgc:TARGET_bioclin_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TARGET_bioclin_v0>`_:

..

  + `Clinical <https://bigquery.cloud.google.com/dataset/isb-cgc:TARGET_bioclin_v0.Clinical>`_:
    This table is contains one row for each TARGET case (aka patient or participant) with *any* 
    available clinical information -- over 5,000 cases are represented.  Note that most 
    of these cases do not *yet* have molecular data available in BigQuery.
  
..

  + `Biospecimen <https://bigquery.cloud.google.com/dataset/isb-cgc:TARGET_bioclin_v0.Biospecimen>`_:
    This table is a *sample-centric* table, and contains one row of information for each of the (over 7,000) 
    TARGET samples.

..

- `isb-cgc:TARGET_hg38_data_v0 <https://bigquery.cloud.google.com/dataset/isb-cgc:TARGET_hg38_data_v0>`_:
  This dataset will by and large mirror the ``TARGET_hg38_data_v0`` dataset, and is based on the GRCh38/hg38 data
  now available from the NCI-GDC.  In some cases the new data has been realigned to the new genome (in the case
  of any DNAseq or miRNA/mRNAseq based data), or the coordinates have been "lifted over" from hg19 to hg38
  (in the case of probe/array-based data such as the SNP6/copy-number and the DNA Methylation data).

..

  + `miRNAseq_Expression <https://bigquery.cloud.google.com/table/isb-cgc:TARGET_hg38_data_v0.miRNAseq_Expression>`_: 
    This table contains **all** of the miRNAseq stem-loop expression data *currently available* from the NCI-GDC.
    

  + `miRNAseq_Isoform_Expression <https://bigquery.cloud.google.com/table/isb-cgc:TARGET_hg38_data_v0.miRNAseq_Isoform_Expression>`_: 
    This table contains **all** of the miRNAseq isoform-level expression (aka isomiR) data *currently available* from the NCI-GDC.
    

  + `RNAseq_Gene_Expression <https://bigquery.cloud.google.com/table/isb-cgc:TARGET_hg38_data_v0.RNAseq_Gene_Expression>`_: 
    This table contains gene expression data from 481 samples (434 cases).
    Each row in this table contains the HTSeq expression 
    estimates for a single gene in a single aliquot.  The gene symbol can be found in the field
    ``gene_name`` and the Ensembl ID can be found in the ``Ensembl_gene_id`` and ``Ensembl_gene_id_v`` fields.

..

Additional Metadata
========================

Additional related metadata is organized into the following datasets:

- `isb-cgc:metadata <https://bigquery.cloud.google.com/dataset/isb-cgc:metadata>`_:
  This dataset currently contains two tables which contain metadata about two additional
  TCGA data types: pathology and radiology images.  More information about these
  image datasets can be found on the 
  `TCGA-images <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/TCGA-images.html>`_ 
  documentation page.


- `isb-cgc:GDC_metadata <https://bigquery.cloud.google.com/dataset/isb-cgc:GDC_metadata>`_:
  This dataset contains several tables which contain metadata describing the cases and
  files at the NCI-GDC, in both the legacy and the current data archives.


- `isb-cgc:tcga_seq_metadata <https://bigquery.cloud.google.com/dataset/isb-cgc:tcga_seq_metadata>`_:
  This dataset contains several tables with metadata about the original hg19 sequence data
  (including both BAM and FASTQ files).
  The important common identifiers to link these tables back to other information is the ``CGHubAnalysisID``
  (which sometimes may be written ``CGHub_analysisID``).  In alphabetical order by name, these tables are:

   
- `isb-cgc:tcga_cohorts <https://bigquery.cloud.google.com/dataset/isb-cgc:tcga_cohorts>`_: 
  This dataset contains a series of curated cohorts, one for each of the 33 TCGA tumor types, named 
  according to the tumor abbreviation, *eg* BRCA.  A "cohort" is defined as a paired list of case- 
  and sample-barcodes.  In order to be included, molecular data from at least one of the main platforms 
  must be available for that sample, and there must be no disqualifying annotation for that sample or 
  the case (aka patient).  For example, the 
  `BRCA cohort table <https://bigquery.cloud.google.com/table/isb-cgc:tcga_cohorts.BRCA>`_ 
  contains 1086 unique cases and 2221 unique samples, but a query of the Clinical table for all 
  BRCA cases will return 1097 cases, and a similar query of the Biospecimen table for all 
  BRCA samples will return 2302 samples.  The Annotation table contains annotations of one type or 
  another for 122 "entities" in the TCGA-BRCA proejct affecting 33 BRCA cases, 2 BRCA samples, 18 BRCA analytes, 
  and 69 BRCA aliquots.


ETL (Extract, Transform, Load) Details 
=======================================

The data in the BigQuery tables is generally identical to the information that
can also be obtained from the NCI-GDC, but for users
interested in the nitty-gritty details, information is provided here about the ETL
(extract, transform and load) steps that were performed for each of the data types.

Before we go into data-type-specific details, a few general notes on
formatting and data curation:

-  All data uploaded into ISB-CGC BigQuery tables use a consistent
   UTF-8 character set. If the encoding of a character from
   the original file could not be detected, that character was ignored.
   Character encodings were detected using the Python
   library `Chardet <https://www.google.com/url?q=https://pypi.python.org/pypi/chardet&sa=D&usg=AFQjCNEqIpFiwf3f-ynJmNtP1ZqXe-TvRg>`_.

-  All missing information value strings such as: ``none``, ``None``,
   ``NONE``, ``null``, ``Null``, ``NULL``, , ``NA``, ``\_\_UNKNOWN\_\_``, ``<blank>``
   , and ``?``; are represented as NULL values in the BigQuery
   tables (or may not appear at all, depending on the table schema).

-  Numbers are stored as integer or floating point values.  The original ASCII
   files sometimes used scientific notation or included comma separators, but
   these are not preserved in the BigQuery tables.

-  End of File (EOF) and End of Line (EOL) delimiters, including
   CTRL-M characters, were all removed when the raw files were originally parsed.

-  Single and double quotes around the values were removed, but in cases where
   there were quotation marks within a string, they were not removed.

-  Whenever necessary, the SDRF file (in the mage-tab archive associated with each
   data archive) was parsed to find the correct association between the
   aliquot barcode and the Level-3 data file(s).

Data-Type Specific ETL Details
******************************

.. toctree::
   :maxdepth: 1

   ETL_Clinical
   ETL_Biospecimen
   ETL_somaticMutations
   ETL_DNAcopyNumber
   ETL_DNAmethylation
   ETL_mRNAexpression
   ETL_microRNAexpression
   ETL_proteinExpression
   ETL_annotations

