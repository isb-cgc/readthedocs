**************
Reference Data
**************

ISB-CGC Hosted Reference Data
#############################

To facilitate working with the TCGA and other program data tables that the ISB-CGC is hosting in BigQuery, additional
reference data tables have been created. Others are hosted by Google Cloud Life Sciences. Suggestions for more are welcome at feedback@isb-cgc.org.

For additional details about each of these tables, please use the `BigQuery Table Search <https://isb-cgc.appspot.com/bq_meta_search/>`_. To find the reference tables, select **Genomic Reference Database** under **Category**.  

Genome Reference Data
=====================

Reference data that describes or annotates the human or other genomes is described in this section.  
Reference data hosted by the ISB-CGC in BigQuery tables are available in the ``isb-cgc.genome_reference`` 
`data set <https://console.cloud.google.com/bigquery?p=isb-cgc&d=genome_reference&page=dataset>`_.  Tables based on 
gene-sets such as Ensembl and GENCODE can be used to find the genomic coordinates and identifiers
for genes of interest, to perform queries that join tables with gene-symbol based data
to tables with genomic-coordinate based data or tables that use other gene identifiers, for example.
    
.. list-table::
   :header-rows: 1 
   
   * - Program/Source
     - Description
   * - ClinVar
     - * `ClinVar <https://www.ncbi.nlm.nih.gov/clinvar/intro/>`_ contains reports of the relationships among human variations and phenotypes.
       * GRCh37
       * GRCh38
   * - Cytoband/UCSC  
     - * Cytoband to Genomic Coordinate Conversion
       * liftOver_hg19_to_hg38 - This table provides a mapping of each hg19 position to the corresponding position in hg38, and can be used to perform a liftOver_ operation in BigQuery.
   * - dbSNP
     - * `dbSNP <https://www.ncbi.nlm.nih.gov/snp/>`_ contains human single nucleotide variations, microsatellites, and small-scale insertions and deletions along with publication, population frequency, molecular consequence, and genomic and RefSeq mapping information for both common variations and clinical mutations
       * B150 GRCH37P13
       * B151 GRCH37P13
   * - Ensembl
     - * GRCh37: Release 75, the final build of the Ensembl_ gene-set mapped to GRCh37
       * GRCh38: Release 87, the most recent Ensembl_ gene-set mapped to GRCh38
   * - GENCODE
     - * GRCh37: Release 19, the final build of the GENCODE_ gene-set mapped to GRCH37
       * GRCh38: Releases 22, 23, and 24 from GENCODE_ are all available (because the TCGA data has been reprocessed by at least one center using each of these three different releases) 
   * - Gene Ontology Consortium
     - * Tables based on GO_ annotations and the GO_ ontology.
   * - Genome-Wide SNP Array
     - * The technical documentation for the Affymetrix Genome-Wide Human SNP Array 6.0 array can be found `here <http://www.affymetrix.com/catalog/131533/AFFY/Genome-Wide+Human+SNP+Array+6.0#1_3>`_.
   * - gnomAD  
     - * `gnomAD <https://gnomad.broadinstitute.org/>`_ aggregates and harmonizes both exome and genome sequencing data from a wide variety of large-scale sequencing projects.
       * GRCH37
   * - ICD
     - * `International Classification of Diseases <https://www.who.int/classifications/icd/en/>`_
       * ICD-10 Chapters
       * ICD-10 Codes
       * ICD-O-3 Morphology
       * ICD-O-3 Site
   * - Infinium   
     - * Infinium EPIC HG19 and HG38 Manifests
       * Infinium HM27 HG19 and HG38 Manifests
       * Infinium HM450 HG19 and HG38 Manifests
   * - ISB-CGC
     - * Gene Names Mapping: Data was loaded from multiple sources including NCBI, HGNC, ENSEMBL in Feb 2018 to simplify mapping between HGNC IDs, HGNC symbols, Entrez Gene IDs, Ensembl Gene IDs, Pubmed IDs,and RefSeq IDs.
   * - Kaviar
     - * The latest hg19- and hg38-based Kaviar_ databases are available.  Kaviar_ is a compilation of SNVs, indels, and complex variants observed in humans, designed to facilitate testing for the novelty and frequency of observed variants.
   * - miRBase
     - * GRCh37: The human portion of version 20 of the miRBase_ database; including genomic coordinates for human microRNAs.  
       * GRCh38: The human portion of version 21 of the miRBase_ database; including genomic coordinates for human microRNAs.
       * GRCh38: The human portion of version 22 of the miRBase_ database; including genomic coordinates for human microRNAs.
   * - miRTarBase
     - * The updated miRTarBase_ database (release 6.1)
   * - Reactome
     - * Ensembl2Reactome
       * miRBase2Reactome
   * - UniProtKB
     - * `UniProtKB <https://www.uniprot.org/help/uniprotkb>`_ is the central hub for the collection of functional information on proteins, with accurate, consistent and rich annotation.
       * UniProtKB Mapping
       

.. _liftOver: https://genome.ucsc.edu/cgi-bin/hgLiftOver
.. _GO: http://www.geneontology.org/
.. _Ensembl: http://uswest.ensembl.org/index.html
.. _GENCODE: https://www.gencodegenes.org/
.. _Kaviar: http://db.systemsbiology.net/kaviar/
.. _miRBase: http://www.mirbase.org/
.. _miRTarBase: http://nar.oxfordjournals.org/content/early/2015/11/19/nar.gkv1258.long


Platform Reference Data
=======================

Some reference data is necessary to work with data generated by specific platforms such as the
Illumina DNA Methylation array. The `platform_reference data set <https://console.cloud.google.com/bigquery?p=isb-cgc&d=GTEx_v7&page=dataset>`_  contains information on the Illumina DNA Methylation Platform.
    
.. list-table::
   :header-rows: 1 
   
   * - Program/Source
     - Description
   * - GDC
     - * HG38 DNA Methylation - Most of the DNA Methylation data produced by the TCGA project was obtained using the Illumina Infinium HumanMethylation450 (aka 450k) BeadChip array.  Some of the earlier tumor types were assayed on the older, 27k array.
   * - Infinium
     - * `Illumina <https://www.illumina.com/>`_ DNA Methylation Annotation - Platform annotation information has been uploaded into BigQuery; each CpG locus is uniquely identified as described in this `technical note <http://www.illumina.com/content/dam/illumina-marketing/documents/products/technotes/technote_cpg_loci_identification.pdf>`_ and this unique identifier can be used to look up and cross-reference data between the TCGA DNA methylation data table and the platform annotation table. 
   * - Cytoband/UCSC
     - * DNA Methylation Annotation Liftover to HG38 Coordinates - The original Illumina-provided CpG coordinates have been *"lifted over"* from hg19 to hg38.
     
     
Genotype Tissue Expression (GTEx) Project Data
=======================

The `GTEx_v7 data set <https://console.cloud.google.com/bigquery?p=isb-cgc&d=GTEx_v7&page=dataset>`_ contains tables with molecular and clinical data (gene read, gene expression, sample attributes, subject phenotype) loaded from the Genotype-Tissue Expression (GTEx) Project Data Portal on November 2017. See the  `GTEx Portal <https://gtexportal.org/>`_ for more information.

University of California Santa Cruz (UCSC) TOIL RNA-seq recompute project Data
=======================

The `Toil_recompute data set <https://console.cloud.google.com/bigquery?p=isb-cgc&d=Toil_recompute&page=dataset>`_ contains data made available by the UCSC TOIL RNA-seq recompute project. The goal of the project was to process ~20,000 RNA-seq samples to create a consistent meta-analysis of four datasets free of computational batch effects. This is best used to compare TCGA cohorts to TARGET or GTEx cohorts. For more details, see the `Zena Browser Data Pages <https://xenabrowser.net/datapages/>`_.
    

Other Reference Data Sources
############################

Google Cloud Life Sciences maintains a list of 
`publicly available data sets <https://cloud.google.com/genomics/docs/public-datasets/>`_, 
including **Reference Genomes**, 
the **Illumina Platinum Genomes**, information about the **Tute Genomics Annotation** table, *etc*.
