==================================
Walk Through of Google BigQuery
==================================
This will serve as a guide to navigate through the Google web-interface for BigQuery and do some introductory queiries using ISB-CGC hosted TCGA data.  For those who would rather use R or Python to programmatically interact with BigQuery, detailed tutorials are provided `here <http://isb-cancer-genomics-cloud.readthedocs.org/en/latest/sections/progapi/Tutorials.html>`_.

***************
Gaining Access
***************
Please refer to documentation on `how to access BigQuery from the Google Console <HowToAccessBigQueryFromTheGoogleCloudPlatform.html>`_ if you have not done this before. 

Also to add ISB-CGC data to your BigQuery platform please refer to the documentaion for `linking ISB-CGC data to BigQuery in the Google Console <LinkingBigQueryToIsb-cgcProject.html>`_.

*****************************
ISB-CGC Data Sets in BigQuery
*****************************
Below are the list of ISB-CGC hosted data sets that can be accessed once you have linked your platform to the ISB-CGC project.

* **isb-cgc:ccle_201602_alpha**
 
 This dataset has been created and curated by the ISB-CGC project to be used in conjunction with the TCGA and other datasets currently hosted by the ISB-CGC.  For more information about the ISB-CGC, please see our documentation on `readthedocs.   <http://isb-cancer-genomics-cloud.readthedocs.org/en/latest/>`_

 This specific dataset contains data from the Broad-Novartis Cancer Cell Line Encyclopedia (CCLE) project and is being redistributed with permission from the Broad Institute.
 
 Neither the CCLE project nor the Broad institute are responsible for any errors that may have been made when creating these tables.  For more information about the CCLE project and to access the original datasets, please refer to the `CCLE website.  <http://www.broadinstitute.org/ccle/home>`_

* **isb-cgc:genome_reference**

 This dataset contains reference tables that have been compiled by the ISB-CGC team from publicly available sources.  Please see each table for details about the source of the information contained in that table.

* **isb-cgc:platform_reference**

 This dataset contains platform reference tables that have been compiled by the ISB-CGC team from publicly available sources.  Specifically, these tables are used as additional annotation for data from results provided by instrumentation used in the TCGA project to collect data.

* **isb-cgc:tcga_201510_alpha**

 This set of BigQuery tables was produced by the ISB-CGC project, based on the open-access TCGA data available at the TCGA Data Portal as of October 2015.  For more information, see `here for more details <https://github.com/isb-cgc/examples-Python/blob/master/notebooks/The%20ISB-CGC%20open-access%20TCGA%20tables%20in%20BigQuery.ipynb>`_ or e-mail info@isb-cgc.org .

* **isb-cgc:tcga_cohorts**

 This dataset contains individual "cohort" tables for each of the TCGA tumor types, as well as a single table in which all of these tables have been concatenated.  To be included in this list, there must be at least some molecular data available for each sample, and there must not be any disqualifying annotations for either the patient or the sample.

 These cohort tables were created based on the isb-cgc:tcga_201510_alpha dataset and are provided as a resource to the research community by the ISB-CGC.

* **isb-cgc:tcga_seq_metadata**

 This dataset contains metadata and FastQC metrics for thousands of TCGA DNA-seq and RNA-seq data files:
 
 * CGHub_Manifest table contains metadata for all TCGA files at CGHub as of April 27th, 2016
 * GCS_listing_27apr2016 table contains metadata for all TCGA files hosted by ISB-CGC in GCS
 * RNAseq_FastQC table contains metrics derived from FastQC runs on the RNAseq data files, including urls to the FastQC html reports that you can cut and paste directly into your browser
 * WXS_FastQC table contains metrics derived from FastQC runs on the exome DNAseq data files


************************
Syntax Queries Examples
************************
Below are some sample queries that will get you started using BigQuery and these ISB-CGC datasets for your own analyses.  One easy way is to use the BigQuery web UI (see screenshot below).  See Google's `BigQuery Web UI Tutorial <https://developers.google.com/bigquery/docs/hello_bigquery_gui>`_ for more general details of how to use this tool.

The examples below show the question that is being asked, and an example BigQuery SQL syntax that can be used to find the answer.  Try it yourself by pasting the query into your own instance of the BigQuery web UI.

Getting information from one table
##################################

**Q: Find all THCA participants with UNC HiSeq gene expression data for the ARID1B gene**

.. code-block:: sql

    SELECT
      ParticipantBarcode, Study, original_gene_symbol, HGNC_gene_symbol, gene_id
    FROM
      [isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM]
    WHERE
      original_gene_symbol = 'ARID1B'
    AND
      STUDY = 'THCA' LIMIT 100
  
.. image:: BigQueryExample1Query.PNG
   :scale: 50
   :align: center
  
Getting information from more than one table (Joining)
######################################################

**Q: For bladder cancer patients that have mutations in the CDKN2A (cyclin-dependent kinase inhibitor 2A) gene, what types of mutations are they, what is their gender, vital status, and days to death - and for 3 downstream genes (MDM2 (MDM2 proto-oncogene), TP53 (tumor protein p53), CDKN1A (cyclin-dependent kinase inhibitor 1A)), what are the gene expression levels for each patient?**

This question was chosen as an interesting example because the p53/Rb pathway is commonly involved in bladder cancer (see `TCGA Network paper <https://tcga-data.nci.nih.gov/docs/publications/blca_2013/>`_ "Comprehensive Molecular Characterization of Urothelial Bladder Carcinoma", Figure 4).

This is a complex question that requires information from four tables.  We will build up this complex query in three stages.

Stage 1
*******
Finding the patients with bladder cancer that have mutations in the CDKN2A gene, and displaying the patient ID and 
the type of mutation


.. code-block:: sql

    SELECT
      mutation.ParticipantBarcode,
      mutation.Variant_Type
    FROM
      [isb-cgc:tcga_201510_alpha.Somatic_Mutation_calls] AS mutation
    WHERE
      mutation.Hugo_Symbol = 'CDKN2A'
      AND Study = 'BLCA'
    GROUP BY
      mutation.ParticipantBarcode,
      mutation.Variant_Type
    ORDER BY
      mutation.ParticipantBarcode

.. image:: BigQueryExample2Query.PNG
   :scale: 50
   :align: center  
   
We now have the list of patients that have a mutation in the CDKN2A gene and the type of mutation.

Notice that we have named the "isb-cgc:tcga_201510_alpha.Somatic_Mutation_calls" table "mutation" using the AS statement.  This is useful for easier reading and composing of complex queries.

Stage 2
*******
Bringing in the patient data from the ISB-CGC TCGA Clinical table so that we can see each patient's gender, vital status and days to death.

.. code-block:: sql

    SELECT
      patient_list.mutation.ParticipantBarcode AS ParticipantBarcode,
      patient_list.mutation.Variant_Type AS Variant_Type,
      clinical.gender,
      clinical.vital_status,
      clinical.days_to_death
    FROM
      /* this will get the unique list of patients having the TP53 gene mutation in BRCA patients*/ (
      
      SELECT
        mutation.ParticipantBarcode,
        mutation.Variant_Type
      FROM
        [isb-cgc:tcga_201510_alpha.Somatic_Mutation_calls] AS mutation
      WHERE
        mutation.Hugo_Symbol = 'CDKN2A'
        AND Study = 'BLCA'
      GROUP BY
        mutation.ParticipantBarcode,
        mutation.Variant_Type
      ORDER BY
        mutation.ParticipantBarcode,
        ) AS patient_list /* end patient_list */
    JOIN
      [isb-cgc:tcga_201510_alpha.Clinical_data] AS clinical
    ON
      patient_list.ParticipantBarcode = clinical.ParticipantBarcode
  
.. image:: BigQueryExample3Query.PNG
   :scale: 50
   :align: center
   
We now have combined information from two tables through a join.  Notice in particular the join syntax, 
and the fact that
for the join (inner join by default), the fields that are identiical between the mutation table and the clinical table is "ParticipantBarcode".  

Stage 3
*******
Show the gene expression levels for the 4 genes of interest, and order them by patient id (Participant Barcode) and gene name (HGNC_gene_symbol).  
  
.. code-block:: sql

    SELECT
      genex.ParticipantBarcode AS ParticipantBarcode,
      genex.SampleBarcode AS SampleBarcode,
      genex.AliquotBarcode AS AliquotBarcode,
      genex.HGNC_gene_symbol AS HGNC_gene_symbol,
      patient_list.Variant_Type AS Variant_Type,
      genex.gene_id AS gene_id,
      genex.normalized_count AS normalized_count,
      genex.Study AS Study,
      clinical_info.clinical.gender AS gender,
      clinical_info.clinical.vital_status AS vital_status,
      clinical_info.clinical.days_to_death AS days_to_death
    FROM ( /* This will get the clinical information for the patients*/
      SELECT
        patient_list.mutation.Variant_Type AS Variant_Type,
        patient_list.mutation.ParticipantBarcode AS ParticipantBarcode,
        clinical.gender,
        clinical.vital_status,
        clinical.days_to_death
      FROM
        /* this will get the unique list of patients having the CDKN2A gene mutation in bladder cancer BLCA patients*/ (
        
        SELECT
          mutation.ParticipantBarcode,
          mutation.Variant_Type
        FROM
          [isb-cgc:tcga_201510_alpha.Somatic_Mutation_calls] AS mutation
        WHERE
          mutation.Hugo_Symbol = 'CDKN2A'
          AND Study = 'BLCA'
        GROUP BY
          mutation.ParticipantBarcode,
          mutation.Variant_Type
        ORDER BY
          mutation.ParticipantBarcode,
          ) AS patient_list /* end patient_list */
      INNER JOIN
        [isb-cgc:tcga_201510_alpha.Clinical_data] AS clinical
      ON
        patient_list.ParticipantBarcode = clinical.ParticipantBarcode /* end clinical annotation */ ) AS clinical_info
    INNER JOIN
      [isb-cgc:tcga_201510_alpha.mRNA_UNC_HiSeq_RSEM] AS genex
    ON
      genex.ParticipantBarcode = patient_list.ParticipantBarcode
    WHERE
      genex.HGNC_gene_symbol IN ('MDM2',
        'TP53',
        'CDKN1A',
        'CCNE1')
    ORDER BY
      ParticipantBarcode,
      HGNC_gene_symbol

.. image:: BigQueryExample4Query.PNG
   :scale: 50
   :align: center  

We have now gotten all the data together in one table for further analysis.  

Note that the final join surrounds the previous join top and bottom.  This is common method of doing joins.

You can either download the results from a query in either CV or JSON format, or save it for further analysis in Google BigQuery by the "Save as Table" button.  As the next section describes, large queries continuing to combine multiple tables in a gene query may be limited by cost and resources, saving results as intermediate tables is a solution to these issues.

*********************************************
Saving Query Results in other BigQuery Tables
*********************************************
You can easily save Query results in intermediate tables in your project, allowing others to view and use them.  Details from Google on how to do that is `here <https://cloud.google.com/bigquery/bigquery-web-ui>`_.  If your query gets too complex it can take too long to run.  Creating intermediate result tables can be a good approach to obtain the same result more quickly and at a lower cost. 

*****************************
For Additional Google Support
*****************************
Google provides its users with a detailed explanation of BigQuery and how it works. 

 -https://cloud.google.com/bigquery/what-is-bigquery 

Google also provides a query reference guide 

 -https://cloud.google.com/bigquery/query-reference 

***************
Important Note
***************
`Here <https://cloud.google.com/bigquery/pricing>`_ is information about how much does it costs to use BigQuery.  Queries are billed according to how much data is scanned during the course of the query, and the rate is $5 per TB, although the first 1 TB is free each month.
You can keep an eye on your GCP expenses on your Google Cloud Platform `Console home page <https://console.cloud.google.com/home/dashboard>`_.
