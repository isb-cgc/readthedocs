Protein (RPPA)
==============

The raw protein data file contains just two columns: The "Composite Element REF", which corresponds to the third column in the antibody
annotation file, and the estimated expression value for that particular
protein. The "Composite Element REF" was parsed to generate additional
information(see details in the formatting section). The BigQuery
`table <https://bigquery.cloud.google.com/table/isb-cgc:tcga_201510_alpha.Protein_RPPA_data>`_ 
was populated with all TCGA Level-3 RPPA data matching the pattern -
"%\_RPPA\_Core.protein\_expression%.txt".

The antibody annotation files are parsed to get the relationship between
the antibody name and the associated proteins, and genes. Below is the
detailed explanation about the generation of the antibody, gene, protein
map.

Generation of Composite\_element\_ref, gene, and protein name map
-----------------------------------------------------------------

      (Manual Curation of the gene and protein names)

-  Check the antibody annotation files for missing columns.

-  If “protein\_name” is missing, generate one from
   “composite\_element\_ref”

-  Make a map of ‘composite\_element\_ref’,’ gene\_name’,
   ‘protein\_name’ values.
-  Check any other variant of the gene and protein symbols in the table.
-  HGNC Validation

-  If the gene symbol is in the HGNC approved symbols, ‘Approved’.
    Gene\_symbol = Gene\_symbol.
-  If not, check the Alias symbols. If found,  Gene\_symbol =
   Alias\_symbol.
-  If not, check the Previous symbols. If found, Gene\_symbol =
   “Approved” Gene\_symbol.
-  If not, Gene\_symbol = Gene\_symbol
-  The file generated is manually curated and fed back into the
   algorithm.

Formatting
----------

-  Duplicate the rows if there are multiple genes concatenated in the
   "gene\_name" value. For example: ‘gene\_name’ with value like ‘AKT1
   AKT2 AKT3’ is stored as three separate rows with each gene in a row.
-  'Protein\_Name' is split into 'Protein\_Basename', Phospho' and are
   stored as separate columns.
-  ‘Composite element ref’ is parsed to get 'validationStatus' and
   'antibodySource' – both are stored as separate columns in the
   BigQuery table.
-  Data from both Illumina GA and HiSeq platforms are stored in the same
   table.

