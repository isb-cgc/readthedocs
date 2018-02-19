###############################
Data in Google Genomics
###############################

`Google Genomics <https://cloud.google.com/genomics/>`_ was a database-backed technology that allowed users to query 
reads and variants using the 
`GA4GH API <https://media.readthedocs.org/pdf/ga4gh-schemas/latest/ga4gh-schemas.pdf>`_.

On December 7th, 2017 Google announced that the "reads API" has been replaced by the `htsget protocol <http://samtools.github.io/hts-specs/htsget.html>`_ , and the "variants API" has been replaced by htsget and the new open-source `"Variant Transforms" <https://github.com/googlegenomics/gcp-variant-transforms>`_ a tool for uploading variant data directly into BigQuery.

In 2017, the GA4GH team introduced the htsget protocol to allow users to download read data for subsections of the genome in which they are interested. This is a richer and more flexible approach to working with reads data. It allows you to keep your genomics data in a common BAM file format on Google Cloud Storage and work with it efficiently from your computation pipelines, using standard bioinformatics tools. Google has already launched their own `open source implementation <https://github.com/googlegenomics/htsget>`_ of this protocol, which you can use to access your reads data. Many popular tools such as samtools and htslib have been updated by the community to support htsget. Documentation is provided `here <https://github.com/googlegenomics/htsget/blob/master/README.md>`_. 

At this time, the ISB-CGC is hosting two open-access datasets in Google Genomics containing
the CCLE DNA-Seq and RNA-Seq data:

    - 1175112317461194900  ccle-dna
    - 2592944257098811032  ccle-rna

An example python script 
(`query_ccle_reads.py <https://github.com/isb-cgc/examples-Python/blob/master/python/query_ccle_reads.py>`_) 
which queries these datasets can be found in our github repo.

You can also explore the Genomics API interactively on the Google APIs Explorer
`here <https://developers.google.com/apis-explorer/#search/genomics/genomics/v1/>`_.
For example you can try out the genomics.datasets.get API call using one of the two dataset
identifiers listed above like 
`this <https://developers.google.com/apis-explorer/#search/genomics/genomics/v1/genomics.datasets.get?datasetId=1175112317461194900&_h=1&>`_ (which you can Execute without OAuth since the dataset is open-access).
Some of the API calls require several properties to be specified in the "request body" -- for example
you can try the 
`genomics.reads.search <https://developers.google.com/apis-explorer/#search/genomics/genomics/v1/genomics.reads.search?_h=1&resource=%257B%250A++%2522readGroupSetIds%2522%253A+%250A++%255B%2522CJKPhaq1GhDg3NH1jJbu6JcB%2522%250A++%255D%252C%250A++%2522referenceName%2522%253A+%25227%2522%252C%250A++%2522start%2522%253A+%2522140453133%2522%252C%250A++%2522end%2522%253A+%2522140453137%2522%250A%257D&>`_ 
API call with the following information in the request body:

.. code-block:: javascript

   {
      "readGroupSetIds": ["CJKPhaq1GhDg3NH1jJbu6JcB"],
      "referenceName":    "7",
      "start":            "140453133",
      "end":              "140453137",
   }

The APIs Explorer allows you to try out any of the Google APIs,
with interactive prompts to help you construct the request body with the parameters.
Once you click on either the "Authorize and Execute" or the "Execute without OAuth"
buttons, you will see the explict form of the https request, and the JSON response
as soon as it is received.

