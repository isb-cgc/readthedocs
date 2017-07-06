DNA Copy-Number Segments 
==========================

The Copy Number Seqments BigQuery table HG19 data comes from the legacy arcihves from the DCC, 
`Copy_Number_segments HG19 <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg19_data_v0.Copy_Number_Segment_Masked>`_
table contains one row *per* copy-number segment *per* TCGA aliquot.  The Copy Number Seqments BigQuery table HG38 data is pulled from the GDC, andcan be accessed  `Copy_Number_segments HG38 <https://bigquery.cloud.google.com/table/isb-cgc:TCGA_hg38_data_v0.Copy_Number_Segment_Masked>`_.
Each TCGA aliquot is uniquely represented by a
`TCGA barcode <https://wiki.nci.nih.gov/display/TCGA/TCGA+barcode>`_
of length 24, *eg* ``TCGA-04-1517-01A-01D-0533-01``.  (For more information on how TCGA barcodes
were created and how to *"read"* a TCGA barcode, click on the preceding link.)

Platform
--------
DNA Copy-Number data was generated for the TCGA project using the 
`Affymetrix GenomeWide Human SNP 6.0 Array <http://www.affymetrix.com/catalog/131533/AFFY/Genome-Wide+Human+SNP+Array+6.0#1_1>`_.

Pipeline
--------
DNA Copy-Number data was generated for the TCGA project at the
`Broad Genome Characterization Center <http://www.broadinstitute.org/collaboration/gcc/>`_.
A ``DESCRIPTION.txt`` file is included with each data archive at the DCC describing the algorithms,
methods, and protocols used to produce the Level-1, Level-2, and Level-3 data.

ETL Details
-----------
Each Level-3 data archive contains 4 output files per sample assayed: two based on the hg18 reference, and two based on the hg19 reference for the TCGA HG19 data table.  
The BigQuery table is populated only with the files ending with ``nocnv\_hg19.seg.txt``. 
The ``num_probes`` and ``segment_mean`` fields in the raw files are sometimes represented using
Exponential Scientific Notation (*eg* 8.7E+07) 
and were interpreted as integer or floating-point values respectively.

The mapping between TCGA aliquot barcodes and Level-3 data files was obtained from the SDRF file.

