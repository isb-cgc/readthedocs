*************
CCLE Overview
*************

The Cancer Cell Line Encyclopedia (CCLE) project is an effort to conduct a detailed genetic characterization of a large panel of human cancer cell lines. The CCLE provides public access analysis and visualization of DNA copy number, mRNA expression, mutation data and more, for 1000 cancer cell lines.

The CCLE aligned reads (BAM files) are currently available in an open-access
Cloud Storage bucket which you can browse 
`here <https://console.cloud.google.com/storage/browser/isb-cgc-open/NCI-GDC/legacy/CCLE/>`_.

These reads have also been imported into 
`Google Genomics <https://cloud.google.com/genomics/>`_
and can be queried using the
`GA4GH API <https://media.readthedocs.org/pdf/ga4gh-schemas/latest/ga4gh-schemas.pdf>`_.
Please refer to this
`page <http://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/data/data2/data_in_GG.html>`_ 
for additional information.

An older set of BigQuery tables containing CCLE data are available in the
``isb-cgc:ccle_201602_alpha`` 
`dataset <https://bigquery.cloud.google.com/dataset/isb-cgc:ccle_201602_alpha>`_.
This data will be updated and reformatted to look more like the newer TCGA and TARGET datasets after the GDC formally releases CCLE, to
optimize usage in the cancer research community.

