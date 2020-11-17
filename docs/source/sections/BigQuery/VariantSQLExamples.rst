Variant Data SQL Query Examples 
==============================

Here are examples of how to leverage SQL queries to analyze the variant data in our tables on the Google Cloud Console. They include some SQL snippets which emulate the commands from VCFTools. `VCFTools <http://vcftools.sourceforge.net/man_0112b.html>`_ is a suite of functions for processing, validating, analyzing, and more on VCF files. Because this is controlled data, it can only be queried if you have authorized access; see `here <ControlledAccessVCF.html>`_ for more information.


.. note:: Best practice to keep costs down for queries is to avoid using '*' and instead select specific columns.

.. note:: In our VCF tables, the POS column is an integer; no quotes are necessary when querying for this column. The CHROM column is a string and requries quotes when querying,  for example, CHROM = 'chr1'. 

 
 
Emulating VCFTools
------------------

These SQL queries replicate the functionality of the listed VCFTools command.

---chr: Filter by position by including or excluding sites of interest; for example, searching for positions found at chromosome 22. 

.. code-block:: sql
      
      SELECT 
          CHROM, POS, REF, ALT 
      FROM 
          `isb-cgc-cbq.TARGET_versioned.vcf_hg38_gdc_r22` 
      WHERE 
          CHROM = 'chr22'
      LIMIT 1000
      
---remove-filter-all: Removes the sites which do not have the tag PASS in the FILTER column. 

.. code-block:: sql
      
      
      SELECT 
          CHROM, POS, REF, ALT, FILTER
      FROM 
          `isb-cgc-cbq.TARGET_versioned.vcf_hg38_gdc_r22` 
      WHERE 
          FILTER = 'PASS'
      LIMIT 1000
      
---maxDP: This function requires the “DP” tag to exist in the FORMAT column. The option will locate genotypes less than or equal to the “--maxDP” value.

.. code-block:: sql    

     SELECT 
          CHROM, POS, REF, ALT, DP_Tumor 
     FROM 
          `isb-cgc-cbq.TARGET_versioned.vcf_hg38_gdc_r22`
     WHERE
          AND DP_Tumor <= '50'
     LIMIT 1000
     


In-Depth Queries
------------------


In this query, let's find information for patients who have ALL-P2 and a Thymine mutation at position 161550724 on Chromosome 1. 

.. code-block:: sql

      SELECT 
          CHROM, POS, REF, ALT, project_short_name 
      FROM 
          `isb-cgc-cbq.TARGET_versioned.vcf_hg38_gdc_r22` 
      WHERE 
          project_short_name = "TARGET-ALL-P2" 
          AND CHROM = "chr1" 
          AND POS = 161550724  
          AND ALT = "T"
      
In this query, let's look at chromosome 1. We want to find positions between twenty thousand and five million. We are interested in chromosome and position from a specific project and with a certain analysis workflow type. In this case, we want to look at the project TARGET-WT. These are patients who are diagnosed with Wilms tumor. For the analysis workflow type, we are interested in MuTect2. 


.. code-block:: sql
   
      SELECT 
         CHROM,POS,REF,ALT,GT_TUMOR,GT_NORMAL
      FROM
         `isb-cgc-cbq.TARGET_versioned.vcf_hg38_gdc_r22`
      WHERE
         CHROM = 'chr1'
         AND POS BETWEEN 20000 and 5000000
         AND project_short_name = "TARGET-WT"
         AND analysis_workflow_type = "MuTect2"
   
The query below returns the ref and alt alleles found between base positions 20,000 and 5,000,000 on chromosome 1 along with genotype information for whole genome tumor and normal samples (using filter analysis_workflow_type like %LiftOver%) across all TARGET projects.
   
.. code-block:: sql

      SELECT 
          CHROM,POS,REF,ALT,project_short_name, GT_TUMOR,GT_NORMAL
      FROM
          `isb-cgc-cbq.TARGET_versioned.vcf_hg38_gdc_r22`
      WHERE
          CHROM = 'chr1'
          AND POS BETWEEN 20000 and 5000000
          AND analysis_workflow_type like "%LiftOver%"

We demonstrate a join in the query below between the TARGET VCF table and the TARGET RNAseq table to get information for the TARGET-ALL-P3 to identify mutations in the FOXD4 gene.

.. code-block:: sql

      SELECT 
          CHROM,POS,REF,ALT,vcf.project_short_name, HTSeq__FPKM, GT_TUMOR,GT_NORMAL
      FROM
          `isb-cgc-cbq.TARGET_versioned.vcf_hg38_gdc_r22` as vcf
          join `isb-cgc-bq.TARGET.RNAseq_hg38_gdc_current` as rna
          on rna.case_barcode = vcf.case_barcode
       WHERE
          vcf.project_short_name = "TARGET-ALL-P3"
          AND gene_name = "FOXD4"
       ORDER By CHROM
