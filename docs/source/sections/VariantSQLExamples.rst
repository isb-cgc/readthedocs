SQL Query Examples 
===================

Here are examples on how to leverage SQL queries on the Google Cloud Console to analyze the data in our tables. In addition to example queries we added a list of snippets which emulates the commands from VCFTools. 

.. note:: Best practices to keep costs down for queries is to avoid using '*' and choosing specefic columns.


Emulating VCFTools
------------------

---chr

.. code-block:: sql
      
      SELECT * FROM `isb-cgc-etl.STAGING.Clustered_test2` 
      WHERE CHROM = 'chr22'
      LIMIT 1000
      
---remove-filter-all

.. code-block:: sql
      
      
      SELECT * FROM `isb-cgc-etl.STAGING.Clustered_test2` 
      WHERE FILTER = 'PASS'
      LIMIT 1000
      
---maxDP

.. code-block:: sql    

     SELECT * FROM `isb-cgc-etl.STAGING.Clustered_test2`
     WHERE DP_Normal > ’10’
     AND DP_Tumor > ‘50’
     LIMIT 1000
     


In-Depth Queries
------------------

Notes to include examples on caveats: 
POS is a integer, so in sql query don't use the quotes 

In this query, let's find all information for patients who have ALL-P2 and a Thymine mutation at position 161550724 on Chromosome 1. 

.. code-block:: sql

      SELECT * FROM `isb-cgc-etl.STAGING.Clustered_test2` 
      WHERE project_short_name = "TARGET-ALL-P2" AND CHROM = "chr1" 
      AND POS = 161550724  AND ALT = "T"
      
In this query, let us look at chromosome 1. We want to find positions between 20thousand and 5million. Not only are we interested in chromosome and position but also from a specific project and analysis workflow type and in this case we want to look into the project TARGET-WT. These are patients that are diagnosed with wilms-tumor. For the analysis workflow type we are interested in MuTect2. 


.. code-block:: sql
   
      SELECT 
         CHROM,POS,REF,ALT,GT_TUMOR,GT_NORMAL
      FROM
         `isb-cgc-etl.STAGING.Clustered_test2`
      WHERE
         CHROM = 'chr1'
         AND POS BETWEEN 20000 and 5000000
         AND project_short_name = "TARGET-WT"
         AND analysis_workflow_type = "MuTect2"
      
