###############################
Data in Google Genomics
###############################

`Google Genomics <https://cloud.google.com/genomics/>`_ is a database-backed technology that allowed users to query 
reads and variants using the `GA4GH API <https://media.readthedocs.org/pdf/ga4gh-schemas/latest/ga4gh-schemas.pdf>`_.

The **htsget protocol** allows users to download read data for subsections of the genome in which they are interested. This is a richer and more flexible approach to working with reads data. It allows you to keep your genomics data in a common BAM file format on Google Cloud Storage and work with it efficiently from your computation pipelines, using standard bioinformatics tools. Google has launched their own `open source implementation <https://github.com/googlegenomics/htsget>`_ of this protocol, which you can use to access your reads data. Many popular tools such as samtools and htslib have been updated by the community to support htsget. Documentation is provided `here <https://github.com/googlegenomics/htsget/blob/master/README.md>`_. 

After analyzing usage of the Variants API, Google found that users primarily used it to import variant data and then export it to BigQuery. To save time and effort, Google created **Variant Transforms**, an open source tool for directly importing VCF data into BigQuery. Variant Transforms and its documentation is published `here <https://github.com/googlegenomics/gcp-variant-transforms>`_. Variant Transforms is more scalable than the legacy Variants API, and it has a robust roadmap with a dedicated Google team.
