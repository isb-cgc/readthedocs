*********************
User Defined Functions
*********************

BigQuery now supports `User Defined Functions <https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions>`_ (UDFs) in SQL and JavaScript that extend 
BigQuery on more specialized computations and that can be reused in notebooks and queries. 
To facilitate the analysis of cancer data, ISB-CGC offers a set 
of UDFs that implement commonly used statistical tests and methods in cancer research and bioinformatics. 
The UDFs are located in the ``isb-cgc-bq.functions`` data set, and the source code of the functions 
and examples of how to use them can be found in our `Community Notebook GitHub Repository <https://github.com/isb-cgc/Community-Notebooks/tree/master/BQUserFunctions>`_.
The following table lists all the functions avaiable in ISB-CGC.

.. list-table:: 
   :widths: 25 50 25
   :align: center
   :header-rows: 1

   * - **UDF name**
     - **Description**
     - **Notebooks**
   * - ``kmeans_current``
     - K-means method for clustering data
     - `Python <https://github.com/isb-cgc/Community-Notebooks/blob/Staging-Notebooks/Notebooks/How_to_cluster_data_using_a_BigQuery_function.ipynb>`_
   * - ``p_fisherexact_current``
     - p value of the Fisher exact test
     -
   * - ``mannwhitneyu_current``
     - Mann–Whitney U test
     -
   * - ``kruskal_walis_current``
     - Kruskal Walis test
     - `Python <https://github.com/isb-cgc/Community-Notebooks/blob/master/FeaturedNotebooks/ACM_BCB_2020_POSTER_Histogram_Associations_ProteinGeneExpression_vs_ClinicalFeatures.ipynb>`_
   * - ``significance_level_ttest2_current``
     - Significan level of the two sided T test
     - `Python <https://github.com/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/AllPairs-correlation-GeneExpression-MicroRNA.ipynb>`_
   * - ``complement_chisquare_cdf_current``
     - One minus the cdf of the Chi Square distribution
     -
   * - ``jstat_normal_cdf_current``
     - Cdf of the Normal distribution
     -
