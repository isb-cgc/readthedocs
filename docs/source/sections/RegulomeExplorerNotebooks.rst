********************
Statistical Notebooks
********************
Integrated statistical analysis and exploration of multiple genomic and clinical data types provide researchers with a great possibility to expand our current knowledge of cancer. The ISB-CGC offers a vast source of diverse data types, including gene expression, somatic mutations, clinical data, etc. We have developed a series of notebooks that use BigQuery to compute statistical associations between different combinations of the data types available in ISB-CGC.

Bioinformatic notebooks
=======================
.. list-table:: 
   :widths: 100 10 10
   :align: center
   :header-rows: 0
  
   * - One-way ANOVA with BigQuery
     - `Python <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_perform_an_ANOVA_test_in_BigQuery.ipynb>`_
     - `R <https://github.com/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_perform_an_ANOVA_test_in_BigQuery.md>`_
   * - Score gene sets in BigQuery
     - `Python <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_score_gene_sets_with_BigQuery.ipynb>`_
     - `R <https://github.com/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_perform_an_ANOVA_test_in_BigQuery.md>`_
   * - Nearest Centroid Classification using BigQuery
     - `Python <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_perform_Nearest_Centroid_Classification_with_BigQuery.ipynb>`_
     - `R <https://github.com/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_perform_Nearest_Centroid_Classification_with_BigQuery.md>`_

Standard pairwise statistics
============================
Statistical significance assessment for an association between pairs of data types uses rank-ordered data and a statistical test appropriate to each data type pair depending on categorical or numerical categorization. The following table lists the statistical methods implemented in the notebooks, and the data types used as examples. The Regulome Explorer inspired notebook is a special notebook that allows the computation of associations between all possible data types available in the TCGA dataset; more details are below.

.. list-table:: 
   :widths: 25 25 50
   :align: center
   :header-rows: 1
  
   * - Data type 
     - Data type
     - Statistical test/notebook
   * - Gene expression
     - Clinical
     - `Kruskal-Wallis score <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/BigQuery-KruskalWallis.ipynb>`_
   * - Gene expression
     - Somatic mutation
     - `T-test score <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/BigQuery-StudentTest.ipynb>`_   
   * - Gene expression
     - Gene expression
     - `Spearman Correlation <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/BigQuery-SpearmanCorrelation.ipynb>`__
   * - Somatic mutation
     - Clinical
     - `Chi Square test <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/BigQuery-Chisquare.ipynb>`_
   * - Somatic mutation
     - Somatic Mutation
     - `Fisher’s exact test <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/BigQuery-FisherExact.ipynb>`_
   * - All types
     - All types
     - `Regulome Explorer inspired notebook <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RegulomeExplorer-notebook.ipynb>`_

Regulome Explorer Inspired Notebook
===================================
`Regulome Explorer <http://explorer.cancerregulome.org/>`_ is a well-established web tool for the exploration and visualization of associations between clinical and molecular features of TCGA data. Institute for Systems Biology and the MD Anderson Cancer Center collaborated closely to develop Regulome Explorer. It allowed users to search and visualize pre-computed statistical data filtered according to user-specified parameters for 20 of the 38 TCGA data sets. Although Regulome Explorer has broad functionality and high-quality graphics make it a valuable tool, it does not contain an analysis of recent releases of TCGA and difficult to apply to data sets other than TCGA. 

The `Regulome Explorer Inspired Notebook <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RegulomeExplorer-notebook.ipynb>`_ is a more flexible version of Regulome Explorer developed by ISB-CGC. It replicates the capabilities of Regulome Explorer, as a Python notebook using the Google Cloud resources and performs statistical analyses dynamically using the cloud rather than using static data. Furthermore, it is extendable to additional data sets available In BigQuery from the ISB-CGC, such as TCGA, TARGET, CCLE, and COSMIC.
