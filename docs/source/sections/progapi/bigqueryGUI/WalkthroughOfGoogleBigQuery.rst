==================================
Walk Through of Google Big Query
==================================
This will serve as a guide to navigate through the Google tool for Big Query and do some introductory queiries using isb-cgc TCGA data.

***************
Gaining Access
***************
Please refer to documentation on `how to access big query from google cloud </bigqueryGUI/HowToAccessBigQueryFromTheGoogleCloudPlatform.rst>`_. 

Also to add ISB-CGC data to your Big Query platform please refer to the documentaion for `linking isb-cgc data to big query < 	LinkingBigQueryToIsb-cgcProject.rst>`_.

*******
Tables
*******
Below are the list of tables that can be accessed once you have linked your platform to the ISB-CGC project.

* **isb-cgc:ccle_201602_alpha**
 
 This dataset has been created and curated by the ISB-CGC project to be used in conjunction with the TCGA and other datasets currently hosted by the ISB-CGC.  For more information about the ISB-CGC, please see our documentation on readthedocs.   http://isb-cancer-genomics-cloud.readthedocs.org/en/latest/

 This specific dataset contains data from the Broad-Novartis Cancer Cell Line Encyclopedia (CCLE) project and is being redistributed with permission from the Broad Institute.

 
 Neither the CCLE project nor the Broad institute are responsible for any errors that may have been made when creating these tables.  For more information about the CCLE project and to access the original datasets, please refer to the CCLE website: http://www.broadinstitute.org/ccle/home

* **isb-cgc:genome_reference**

 This dataset contains reference tables that have been compiled by the ISB-CGC team from publicly available sources.  Please see each table for details about the source of the information contained in that table.

* **isb-cgc:platform_reference**

 This dataset contains reference tables that have been compiled by the ISB-CGC team from publicly available sources.  Please see each table for details about the source of the information contained in that table.

* **isb-cgc:tcga_201510_alpha**

 This set of BigQuery tables was produced by the ISB-CGC project, based on the open-access TCGA data available at the TCGA Data Portal as of October 2015.  For more information, see https://github.com/isb-cgc/examples-Python/blob/master/notebooks/The%20ISB-CGC%20open-access%20TCGA%20tables%20in%20BigQuery.ipynb or e-mail info@isb-cgc.org

* **isb-cgc:tcga_cohorts**

 This dataset contains individual "cohort" tables for each of the TCGA tumor types, as well as a single table in which all of these tables have been concatenated.  To be included in this list, there must be at least some molecular data available for each sample, and there must not be any disqualifying annotations for either the patient or the sample.

 These cohort tables were created based on the isb-cgc:tcga_201510_alpha dataset and are provided as a resource to the research community by the ISB-CGC.


************************
Syntax Queries Examples
************************
Below are a list of queries that can and should be used for analysis.


**Tries to find all THCA participants with UNC genex data in the ARID1B gene**

Select
  ParticipantBarcode, Study, original_gene_symbol, HGNC_gene_symbol, gene_id
FROM
  [isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM]
WHERE
  original_gene_symbol = 'ARID1B'
AND
  STUDY = 'THCA' LIMIT 100


**Storing SQL query in a file and passing to BQ:**

cat query.sql | bq query

Join example 

SELECT
  xml.clinical.ParticipantBarcode,
  xml.biospecimen.SampleBarcode,
  xml.clinical.gender, 
  xml.clinical.vital_status, 
  xml.clinical.days_to_death, 
  mutation.Variant_Classification, 
  mutation.Hugo_Symbol,
  mutation.DbSNP_RS
FROM (
  SELECT 
  clinical.ParticipantBarcode,
  biospecimen.SampleBarcode,
  clinical.gender,
  clinical.vital_status,
  clinical.days_to_death
  FROM
  [isb-cgc:tcga_201510_alpha.Clinical_data] AS clinical
  JOIN
  [isb-cgc:tcga_201510_alpha.Biospecimen_data] AS biospecimen
  ON
  clinical.ParticipantBarcode = biospecimen.ParticipantBarcode
WHERE
  biospecimen.Study = 'BRCA' AND biospecimen.SampleTypeLetterCode = 'TP') AS xml JOIN [isb-cgc:tcga_201510_alpha.Somatic_Mutation_calls] AS mutation ON xml.biospecimen.SampleBarcode = mutation.Tumor_SampleBarcode where mutation.Hugo_Symbol = 'TP53' limit 10

More examples and discussions as to how to create a join query follow the link below.

 -http://stackoverflow.com/questions/12333401/joining-3-tables-in-google-bigquery

 -https://groups.google.com/forum/#!topic/bigquery-discuss/MW8LyeYE6fA


**Four-Table Q uery**

SELECT
  xml.clinical.ParticipantBarcode,
  xml.biospecimen.SampleBarcode,
  xml.biospecimen.SampleType,
  xml.clinical.gender,
  xml.clinical.vital_status,
  xml.clinical.days_to_death,
  mut.Variant_Classification,
  mut.Hugo_Symbol,
  mut.DbSNP_RS,
  genex.normalized_count
FROM (
  SELECT
    clinical.ParticipantBarcode,
    biospecimen.SampleBarcode,
    biospecimen.SampleType,
    clinical.gender,
    clinical.vital_status,
    clinical.days_to_death
  FROM
    [isb-cgc:tcga_201510_alpha.Clinical_data] AS clinical
  JOIN
    [isb-cgc:tcga_201510_alpha.Biospecimen_data] AS biospecimen
  ON
    clinical.ParticipantBarcode = biospecimen.ParticipantBarcode
  WHERE
    biospecimen.Study = 'BRCA') AS xml
JOIN (
  SELECT
    mutation.ParticipantBarcode,
    mutation.Hugo_Symbol,
    mutation.Variant_Classification,
    mutation.DbSNP_RS
  FROM
    [isb-cgc:tcga_201510_alpha.Somatic_Mutation_calls] AS mutation
  WHERE
    mutation.Hugo_Symbol = 'TP53') AS mut
ON
  xml.clinical.ParticipantBarcode = mut.mutation.ParticipantBarcode
JOIN (
  SELECT
    expression.ParticipantBarcode,
    expression.normalized_count
  FROM
    [isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM] AS expression
  WHERE
    HGNC_gene_symbol = 'MDM2' ) AS genex
ON
  xml.clinical.ParticipantBarcode = genex.expression.ParticipantBarcode
LIMIT
  100

More examples and discussions as to how to create a four table query follow the link below.

 -http://stackoverflow.com/questions/12333401/joining-3-tables-in-google-bigquery

 -https://groups.google.com/forum/#!topic/bigquery-discuss/MW8LyeYE6fA
 
 -http://stackoverflow.com/questions/27856361/bigquery-nested-challenge-involving-joins-and-having-or-where-clauses


For Additional Google Support
=============================
Google provides its users with a detailed explanation of Big Query and how it works. 

 -https://cloud.google.com/bigquery/what-is-bigquery 

Google also provides a query reference guide 

 -https://cloud.google.com/bigquery/query-reference 

***************
Important Note
***************
Insert here information about how much does it cost per query in using the google big query.
