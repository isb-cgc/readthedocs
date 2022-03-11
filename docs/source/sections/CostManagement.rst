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
     - $1 ($100) \*
   * - | Train a linear regression model using gene expression data
       | `Example: Linear Regression, Kidney Cancer Survival <https://github.com/isb-cgc/Community-Notebooks/blob/master/MachineLearning/How_to_predict_cancer_survival_with_BigQueryML.ipynb>`_
     - TCGA
     - BigQuery, BigQuery ML, Colab, Python
     - $1 ($100) \*
   * - | Train a deep neural network (DNN) regression model using gene expression data
       | `Example: Regression w/ TensorFlow, Kidney Cancer Survival <https://github.com/isb-cgc/Community-Notebooks/blob/master/MachineLearning/How_to_predict_cancer_survival_with_TensorFlow.ipynb>`_
     - TCGA
     - BigQuery, Colab, TensorFlow, Compute Engine w/ GPUs
     - $1 \*\*
   * - | Analyze RNA-seq data using the GDC workflow
       | `Example: GDC RNA-seq CWL Workflow <https://github.com/NCI-GDC/gdc-rnaseq-cwl>`_
     - TCGA
     - Compute Engine, Cloud Storage, CWL
     - $10 \*\*\*

* \*BigQuery ML costs depend on data size. In these examples, a subset of data was extracted to a temporary table, which was used as input to BigQuery ML. This reduces costs substantially. If using all gene features of a TCGA dataset, costs can grow to the order of $100.

* \*\*With small datasets, use of GPUs in Colab does not cost extra (unless using `Colab Pro <https://research.google.com/colaboratory/faq.html>`_). However, if TensorFlow code is executed in a VM with GPUs, the hourly cost can range from $1 to $10.

* \*\*\*Cost per sample depends on sample size (i.e., number of reads) and processing time.

* BigQuery ML vs. TensorFlow w/ Compute Engine or Colab GPUs: When choosing between these tools for machine learning, consider the following guidelines:

  - TensorFlow w/ Compute Engine or Colab GPUs: Appropriate for data exploration or parameter tuning requiring multiple iterations of training and evaluation. 

  - BigQuery ML: Appropriate for production deployment of machine learning models. For example, after optimizing model parameters, train and deploy the final model with BigQuery ML.





