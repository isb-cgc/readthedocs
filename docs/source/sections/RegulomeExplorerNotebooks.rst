************************************
Regulome Explorer Inspired Notebooks
************************************

`Regulome Explorer <http://explorer.cancerregulome.org/>`_, a popular web interface developed in close collaboration between the Institute for Systems Biology and the MD Anderson Cancer Center, enables exploration of significant pairwise associations within the TCGA dataset. 

We implemented a series of Python notebooks that replicate Regulome Explorer based on 
BigQuery TCGA tables of heterogeneous data such as clinical and molecular data for hundreds of patients. The clinical information includes features such as age, tumor-stage, and histology, while the molecular data may include 
any or all of the following types of high-throughput data: microRNA expression levels, copy-number alterations, DNA methylation, and somatic mutations. 
The Regulome Explorer is implemented in the following notebook:

- `Regulome Explorer notebook <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RegulomeExplorer-notebook.ipynb>`_

Within the heterogeneous TCGA dataset, information may be represented as categorical or numerical values. In the analysis, the statistical significance of each pairwise association is assessed using rank-ordered data and a statistical test appropriate to each data type pair. The following notebooks describe in detail the statistical methods implemented to compute the significance of association for each possible combination of molecular features:

.. list-table:: 
   :widths: 25 25 50
   :align: center
   :header-rows: 1
  
   * - Feature type 
     - Feature type
     - Statistical test
   * - Gene expression
     - Clinical
     - `Kruskal-Wallis score <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RE-KruskalWallis.ipynb>`_
   * - Gene expression
     - Somatic mutation
     - `T-test score <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RE-StudentTest.ipynb>`_   
   * - Gene expression
     - Gene expression
     - Spearman Correlation <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RE-SpearmanCorrelation.ipynb>`__
   * - Somatic mutation
     - Clinical
     - `Chi Square test <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RE-Chisquare.ipynb>`_
   * - Somatic mutation
     - Somatic Mutation
     - `Fisher’s exact test <https://nbviewer.jupyter.org/github/isb-cgc/Community-Notebooks/blob/master/RegulomeExplorer/RE-FisherExact.ipynb>`_
