===============
Cost Management
===============

This section details a few use cases and their approximate costs in order to help users estimate cloud costs for their analyses. 

Estimating Costs for Common Bioinformatics and Data Analysis Tasks
==================================================================

The following table summarizes order-of-magnitude costs for common data analysis tasks. For example an order-of-magnitude cost of $10 indicates that the cost can be up to $10, estimated from the given example notebooks. Estimated costs between $10 and $100 are reported as the next order of magnitude, $100:

.. list-table::
   :widths: 100 25 25 25
   :align: center
   :header-rows: 1

   * - Bioinformatics / Data Analysis Task
     - Dataset(s)
     - Tools
     - Approx. Cost (Max)
   * - | Identify differentially expressed genes
       | `Example: Breast Cancer Tumor vs. Normal <https://github.com/isb-cgc/Community-Notebooks/blob/master/Notebooks/How_to_analyze_differential_expression_between_paired_tumor_and_normal_samples.ipynb>`_
     - TCGA
     - BigQuery, Colab, Python, R
     - $1
   * - | Train a prediction model using gene expression data
       | `Example: Logistic Regression, Ovarian Cancer Chemo Response <https://github.com/isb-cgc/Community-Notebooks/blob/master/MachineLearning/How_to_build_an_RNAseq_logistic_regression_classifier_with_BigQuery_ML.ipynb>`_
       | `Example: Logistic Regression, Breast Cancer Tumor vs. Normal <https://github.com/isb-cgc/Community-Notebooks/blob/master/TeachingMaterials/2021-10-NIHLibrarySession/BigQueryMachineLearning.ipynb>`_
     - TCGA
     - BigQuery, BigQuery ML, Colab, Python, R
     - $1 ($100) *
   * - | Train a linear regression model using gene expression data
       | `Example: Linear Regression, Kidney Cancer Survival <https://github.com/isb-cgc/Community-Notebooks/blob/master/MachineLearning/How_to_predict_cancer_survival_with_BigQueryML.ipynb>`_
     - TCGA
     - BigQuery, BigQuery ML, Colab, Python
     - $1 ($100) *
   * - | Analyze RNA-seq data using the GDC workflow
       | `Example: GDC RNA-seq CWL Workflow <https://github.com/NCI-GDC/gdc-rnaseq-cwl>`_
     - TCGA
     - Compute Engine, Cloud Storage, CWL
     - $10 **

* *BigQuery ML Note: The cost of BigQuery ML for model training greatly depends on the size of the input data. In the examples listed here, a subset of the input data was first extracted and stored in a temporary table. This temporary table was then used as the input to the BigQuery ML model creation command. By doing this, the cost of the BigQuery ML command is substantially reduced, but a small cost for storing the temporary table may be incurred. If using all gene features of a TCGA dataset, costs can grow to the order of $100.
* **This is the approximate cost per sample and may vary depending on the size of the sample (i.e., number of reads) and processing time per sample. 





