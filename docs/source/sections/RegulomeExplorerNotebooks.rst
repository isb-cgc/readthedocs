*********************
Statistical Notebooks
*********************
Integrated statistical analysis and exploration of multiple genomic and clinical data types provides researchers with a great possibility to expand our current knowledge of cancer. ISB-CGC offers a great source of diverse data types including gene expression, somatic mutations, clinical data, etc. We have developed a series of notebooks that use BigQuery to compute the statistical associations between different combinations of the data types available in ISB-CGC.

Bioinformatics notebooks
=======================
.. list-table:: 
   :widths: 100 10 10
   :align: center
   :header-rows: 0
   
   * - Significant correlations and their p-values using BigQuery
     - `Python <https://github.com/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/AllPairs-correlation-GeneExpression-MicroRNA.ipynb>`_
     - 
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
The following table lists notebooks that compute associations between pairs of data types available in ISB-CGC. They assess the statistical significance for an association using rank-ordered data and a statistical test appropriate to each data type pair depending on categorical or numerical categorization. The Regulome Explorer inspired notebook is a special notebook that allows computation of associations between all possible data types available in the TCGA dataset; more details are below.

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
`Regulome Explorer <http://explorer.cancerregulome.org/>`_ is a well-established web tool for the exploration and visualization of associations between clinical and molecular features of TCGA data. Regulome Explorer was developed in 2012 in close collaboration between the Institute for Systems Biology and the MD Anderson Cancer Center. It enables users to search and visualize precomputed statistical data filtered according to user-specified parameters. Although Regulome Explorer's broad functionality and high-quality graphics make it a valuable tool for exploring and visualizing 20 of the 33 TCGA data sets, it does not yet contain analysis of recent releases of TCGA and cannot be easily applied to data sets other than TCGA.

We developed a more flexible version, replicating capabilities of Regulome Explorer, as a Python notebook that uses Google Cloud resources. Rather than working with precomputed, fixed cohorts and fixed results, statistical analyses are dynamically performed in the cloud, with user defined patient cohorts. Moreover, the notebook can be extended so that users can analyze additional data sets available as part of the 'ISB-CGC BigQuery ecosystem' such as TCGA, TARGET,  CCLE, COSMIC, and others. The notebook can be accessed in `Regulome Explorer inspired notebook <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RegulomeExplorer-notebook.ipynb>`_.
