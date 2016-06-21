*************************
Understanding Data Access
*************************

* **Public Data**  Sometimes the word "public" is misinterpreted as meaning "open".  All of the TCGA data is *public* data, and much of it is *open*, meaning that it is accessible and available to *all* users; while some low-level TCGA data is *controlled* and restricted to authorized users.
* **Open-Access Data**  Depending on how you categorize the data, *most* of the TCGA data is open-access data.  This includes all de-identified clinical and biospecimen data, as well as all Level-3 molecular data including gene expression data, DNA methylation data, DNA copy-number data, protein expression data, somatic mutation calls, etc. 
* **Controlled-Access Data**  All low-level sequence data (both DNA-seq and RNA-seq), the raw SNP array data (CEL files), germline mutation calls, and a small amount of other data are treated as *controlled* data and require that a user be properly authenticated and have dbGaP-authorization prior to accessing these data.

Note that many public, open-access datasets may still be **restricted** in various ways.  Typically, a **License** document
containing explicit terms of use will be associated with each dataset.  Some institutions have their own licenses, 
though many use one of the `Creative Commons <https://creativecommons.org/>`_ licenses.  License terms apply to both
data and source-code, so please be aware of the terms of a license whenever you plan to re-use data or source-code
produced by someone else.

In the earlier days of the TCGA data, although the data was made public as quickly as possible, it was generally under
**embargo** for some period of time, to allow the TCGA analysis working groups to produce the initial "marker paper"
for each tumor type.  Now that the TCGA project is nearing completion, none of the TCGA data is under embargo anymore,
but we still recommend that you review the `TCGA Publication Guidelines <http://cancergenome.nih.gov/publications/publicationguidelines>`_.

