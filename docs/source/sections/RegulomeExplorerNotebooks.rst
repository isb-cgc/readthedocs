************************************
Regulome Explorer Inspired Notebooks
************************************
Integrated statistical analysis and exploration of multiple genomic and clinical data types provides researchers with a great possibility to expand our current knowledge of cancer. ISB-CGC offers a great source of heterogeneous data types including gene expression, somatic mutations, clinical data, etc. We have developed a series of notebooks that use BigQuery to compute the statistical association between different combinations of data types available in ISB-CGC.

The statistical significance of each pairwise association is assessed using rank-ordered data and a statistical test appropriate to each data type pair, which are categorized as categorical or numerical. The following table lists the statistical methods implemented in the notebooks, and the data types used as examples. Regulome explorer is a special notebook that allows to compute associations between all possible data types available the TCGA dataset, more details below.

.. list-table:: 
   :widths: 25 25 50
   :align: center
   :header-rows: 1
  
   * - Data type 
     - Data type
     - Statistical test/notebook
   * - Gene expression
     - Clinical
     - `Kruskal-Wallis score <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RE-KruskalWallis.ipynb>`_
   * - Gene expression
     - Somatic mutation
     - `T-test score <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RE-StudentTest.ipynb>`_   
   * - Gene expression
     - Gene expression
     - `Spearman Correlation <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RE-SpearmanCorrelation.ipynb>`__
   * - Somatic mutation
     - Clinical
     - `Chi Square test <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RE-Chisquare.ipynb>`_
   * - Somatic mutation
     - Somatic Mutation
     - `Fisher’s exact test <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RE-FisherExact.ipynb>`_
   * - All types
     - All types
     - `Regulome explorer notebook <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RegulomeExplorer-notebook.ipynb>`_

Regulome explorer inspired notebook
===================================
`Regulome Explorer <http://explorer.cancerregulome.org/>`_ is a popular web tool for the exploration and visualization of associations between clinical and molecular features of TCGA data. Regulome explorer was developed in 2012 in close collaboration between the Institute for Systems Biology and the MD Anderson Cancer Center Regulome, and enables users to search and visualise precomputed statistical data filtered according to user-specified parameters. 

Although Regulome explorer's broad functionality and high-quality graphics make it a valuable tool for exploring and visualizing 20 of the 33 TCGA dataset, it does not yet contain analysis of recent releases of TCGA and cannot be easily applied to datasets other than TCGA. We developed a more flexible version of Regulome explorer as a python notebook that uses google cloud resources. Rather than working with pre-computed, fixed cohorts and fixed results, statistical analyses are dynamically performed in the cloud, with user defined patient cohorts. Moreover, the notebook can be extended so that users can analyze additional datasets available as part of the 'BigQuery ecosystem' such as TCGA, TARGET,  CCLE, COSMIC, and others. The notebook can be accessed in:

- `Regulome Explorer notebook <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RegulomeExplorer-notebook.ipynb>`_

