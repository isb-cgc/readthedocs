
README, COSMIC COSMIC Download Files
====================================

Version 81, 9th May 2017

---------------------------
Classification Information
---------------------------
 A comma separated table of COSMIC cancer classification information.  [http://cancer.sanger.ac.uk/cancergenome/assets/classification.csv ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Site_Primary                                       Primary tissue specified in the publication.
[2:B]                 Site_Subtype1                                      Sub tissue specified in the publication.
[3:C]                 Site_Subtype2                                      Sub tissue specified in the publication.
[4:D]                 Site_Subtype3                                      Sub tissue specified in the publication.
[5:E]                 Histology                                          Primary histology specified in the publication.
[6:F]                 Hist_Subtype1                                      Sub histology specified in the publication.
[7:G]                 Hist_Subtype2                                      Sub histology specified in the publication.
[8:H]                 Hist_Subtype3                                      Sub histology specified in the publication.
[9:I]                 Site_Primary_COSMIC                                Primary tissue specified in COSMIC.
[10:J]                Site_Subtype1_COSMIC                               Sub tissue specified in COSMIC.
[11:K]                Site_Subtype2_COSMIC                               Sub tissue specified in COSMIC.
[12:L]                Site_Subtype3_COSMIC                               Sub tissue specified in COSMIC.
[13:M]                Histology_COSMIC                                   Primary histology specified in COSMIC.
[14:N]                Hist_Subtype1_COSMIC                               Sub histology specified in COSMIC.
[15:O]                Hist_Subtype2_COSMIC                               Sub histology specified in COSMIC.
[16:P]                Hist_Subtype3_COSMIC                               Sub histology specified in COSMIC.



-------------------------------------------------
COSMIC Complete Mutation Data (Targeted Screens)
-------------------------------------------------
 A tab separated table of the complete curated COSMIC dataset (targeted screens) from the current release. It includes all coding point mutations, and the negative data set. [ /cosmic/grch37/cosmic/v81/CosmicCompleteTargetedScreensMutantExport.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Gene name                                          The gene name for which the data has been curated in COSMIC. In most cases this is the accepted HGNC symbol.
[2:B]                 Accession Number                                   The transcript identifier of the gene.
[3:C]                 Gene CDS length                                    Length of the gene (base pair) counts.
[4:D]                 HGNC id                                            Unique HGNC identifier, if the gene is in HGNC.
[5:E]                 Sample name,Sample id,Id tumour                    A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers.
[8:H]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[9:I]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[10:J]                Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[11:K]                Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[12:L]                Primary Histology                                  The histological classification of the sample.
[13:M]                Histology Subtype 1                                Further histological classification (level 1) of the sample.
[14:N]                Histology Subtype 2                                Further histological classification (level 2) of the sample.
[15:O]                Histology Subtype 3                                Further histological classification (level 3) of the sample.
[16:P]                Genome-wide screen                                 if the entire genome/exome is sequenced.
[17:Q]                Mutation Id                                        unique mutation identifier.
[18:R]                Mutation CDS                                       The change that has occurred in the nucleotide sequence. Formatting is identical to the method used for the peptide sequence.
[19:S]                Mutation AA                                        The change that has occurred in the peptide sequence. Formatting is based on the recommendations made by the Human Genome Variation Society. The description of each type can be found by following the link to Mutation Overview page.
[20:T]                Mutation Description                               Type of mutation (substitution, deletion, insertion, complex, fusion, unknown etc.)
[21:U]                Mutation zygosity                                  Information on whether the mutation was reported to be homozygous , heterozygous or unknown within the sample.
[22:V]                LOH                                                LOH Information on whether the gene was reported to have loss of heterozygosity in the sample: yes, no or unknown.
[23:W]                GRCh                                               The coordinate system used -
                        * 38 = GRCh38/Hg38
                        * 37 = GRCh37/Hg19
[24:X]                Mutation genome position                           The genomic cooridnates of the mutation.
[25:Y]                Mutation strand                                    Positive or negative.
[26:Z]                SNP                                                All the known SNPs are flagged as 'y' defined by the 1000 genomes project, dbSNP and a panel of 378 normal (non-cancer) samples from Sanger CGP sequencing.
[27:AA]               Resistance Mutation                                The mutation confers drug resistance (see CosmicResistanceMutations.tsv.gz for gene/drug details).
[28:AB]               FATHMM prediction                                  More information about FATHMM (Functional Analysis through Hidden Markov Models) is available from http://fathmm.biocompute.org.uk. FATHMM  descriptors -
                        * Pathogenic = Defined as Cancer or Damaging.
                        * Neutral = Defined as Passenger or Tolerated.
[29:AC]               FATHMM Score                                       The scores are in the form of pvalues ranging from 0 to 1. Pvalues greater than 0.5 are pathogenic while  less than 0.5 are benign. Pvalues close to 0 or 1 are the high confidence results which are more accurate. The results are annotated as 10 feature groups (separately for coding and non coding variants) details of which can be found in the original FATHMM-MKL paper.
[30:AD]               Mutation somatic status                            Information on whether the sample was reported to be Confirmed Somatic, Previously Reported or Variant of unknown origin -
                        * variant of unknown origin = when the mutation is known to be somatic but the tumour was sequenced without a matched normal.
                        * Confirmed Somatic = if the mutation has been confirmed to be somatic in the experiment by sequencing both the tumour and a matched normal from the same patient.
                        * Previously observed = when the mutation has been reported as somatic previously but not in current paper.
[31:AE]               Pubmed_PMID                                        The PUBMED ID for the paper that the sample was noted in, linking to pubmed to provide more details of the publication.
[32:AF]               Id Study                                           Lists the unique Ids of studies that have involved this sample.
[33:AG]               Sample source,Tumour origin                        Describes where the sample has originated from including the tumour type.
[35:AI]               Age                                                Age of the individual (if this information is provided with the publications).



--------------------------------------
COSMIC Mutation Data (Genome Screens)
--------------------------------------
 A tab separated table of coding point mutations from genome wide screens (including whole exome sequencing). [ /cosmic/grch37/cosmic/v81/CosmicGenomeScreensMutantExport.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Gene name                                          The gene name for which the data has been curated in COSMIC. In most cases this is the accepted HGNC identifier.
[2:B]                 Accession Number                                   The transcript identifier of the gene.
[3:C]                 Gene CDS length                                    Length of the gene (base pair) counts.
[4:D]                 HGNC id                                            Unique HGNC identifier, if the gene is in HGNC.
[5:E]                 Sample name,Sample id,Id tumour                    A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers.
[8:H]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[9:I]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[10:J]                Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[11:K]                Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[12:L]                Primary Histology                                  The histological classification of the sample.
[13:M]                Histology Subtype 1                                Further histological classification (level 1) of the sample.
[14:N]                Histology Subtype 2                                Further histological classification (level 2) of the sample.
[15:O]                Histology Subtype 3                                Further histological classification (level 3) of the sample.
[16:P]                Genome-wide screen                                 if the entire genome/exome is sequenced.
[17:Q]                Mutation Id                                        unique mutation identifier.
[18:R]                Mutation CDS                                       The change that has occurred in the nucleotide sequence. Formatting is identical to the method used for the peptide sequence.
[19:S]                Mutation AA                                        The change that has occurred in the peptide sequence. Formatting is based on the recommendations made by the Human Genome Variation Society. The description of each type can be found by following the link to Mutation Overview page.
[20:T]                Mutation Description                               Type of mutation (substitution, deletion, insertion, complex, fusion, unknown etc.)
[21:U]                Mutation zygosity                                  Information on whether the mutation was reported to be homozygous , heterozygous or unknown within the sample.
[22:V]                LOH                                                LOH Information on whether the gene was reported to have loss of heterozygosity in the sample: yes, no or unknown.
[23:W]                GRCh                                               The coordinate system used -
                        * 38 = GRCh38/Hg38
                        * 37 = GRCh37/Hg19
[24:X]                Mutation genome position                           The genomic cooridnates of the mutation.
[25:Y]                Mutation strand                                    positive or negative.
[26:Z]                SNP                                                All the known SNPs are flagged as 'y' defined by the 1000 genomes project, dbSNP and a panel of 378 normal (non-cancer) samples from Sanger CGP sequencing.
[27:AA]               FATHMM prediction                                  More information about FATHMM (Functional Analysis through Hidden Markov Models) is available from http://fathmm.biocompute.org.uk. FATHMM  descriptors -
                        * Pathogenic = Defined as Cancer or Damaging.
                        * Neutral = Defined as Passenger or Tolerated.
[28:AB]               FATHMM Score                                       The scores are in the form of pvalues ranging from 0 to 1. Pvalues greater than 0.5 are pathogenic while  less than 0.5 are benign. Pvalues close to 0 or 1 are the high confidence results which are more accurate. The results are annotated as 10 feature groups (separately for coding and non coding variants) details of which can be found in the original FATHMM-MKL paper.
[29:AC]               Mutation somatic status                            Information on whether the sample was reported to be Confirmed Somatic, Previously Reported or Variant of unknown origin -
                        * variant of unknown origin = when the mutation is known to be somatic but the tumour was sequenced without a matched normal.
                        * Confirmed Somatic = if the mutation has been confimed to be somatic in the experiment by sequencing both the tumour and a matched normal from the same patient.
                        * Previously observed = when the mutation has been reported as somatic previously but not in current paper.
[30:AD]               Pubmed_PMID                                        The PUBMED ID for the paper that the sample was noted in, linking to pubmed to provide more details of the publication.
[31:AE]               Id Study                                           Lists the unique Ids of studies that have involved this sample.
[32:AF]               Sample source,Tumour origin                        Describes where the sample has originated from including the tumour type.
[34:AH]               Age                                                Age of the individual (if this information is provided with the publications).



---------------------
COSMIC Mutation Data
---------------------
 A tab separated table of all COSMIC coding point mutations from targeted and genome wide screens from the current release. [ /cosmic/grch37/cosmic/v81/CosmicMutantExport.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Gene name                                          The gene name for which the data has been curated in COSMIC. In most cases this is the accepted HGNC identifier.
[2:B]                 Accession Number                                   The transcript identifier of the gene.
[3:C]                 Gene CDS length                                    Length of the gene (base pair) counts.
[4:D]                 HGNC id                                            if gene is in HGNC, this id helps linking it to HGNC.
[5:E]                 Sample name,Sample id,Id tumour                    A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers.
[8:H]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[9:I]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[10:J]                Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[11:K]                Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[12:L]                Primary Histology                                  The histological classification of the sample.
[13:M]                Histology Subtype 1                                Further histological classification (level 1) of the sample.
[14:N]                Histology Subtype 2                                Further histological classification (level 2) of the sample.
[15:O]                Histology Subtype 3                                Further histological classification (level 3) of the sample.
[16:P]                Genome-wide screen                                 if the entire genome/exome is sequenced.
[17:Q]                Mutation Id                                        unique mutation identifier.
[18:R]                Mutation CDS                                       The change that has occurred in the nucleotide sequence. Formatting is identical to the method used for the peptide sequence.
[19:S]                Mutation AA                                        The change that has occurred in the peptide sequence. Formatting is based on the recommendations made by the Human Genome Variation Society. The description of each type can be found by following the link to Mutation Overview page.
[20:T]                Mutation Description                               Type of mutation (substitution, deletion, insertion, complex, fusion, unknown etc.)
[21:U]                Mutation zygosity                                  Information on whether the mutation was reported to be homozygous , heterozygous or unknown within the sample.
[22:V]                LOH                                                LOH Information on whether the gene was reported to have loss of heterozygosity in the sample: yes, no or unknown.
[23:W]                GRCh                                               The coordinate system used -
                        * 38 = GRCh38/Hg38
                        * 37 = GRCh37/Hg19
[24:X]                Mutation genome position                           The genomic cooridnates of the mutation.
[25:Y]                Mutation strand                                    postive or negative.
[26:Z]                SNP                                                All the known SNPs are flagged as 'y' defined by the 1000 genomes project, dbSNP and a panel of 378 normal (non-cancer) samples from Sanger CGP sequencing.
[27:AA]               Resistance Mutation                                mutation confers drug resistance (see CosmicResistanceMutations.tsv.gz for gene/drug details).
[28:AB]               FATHMM prediction                                  More information about FATHMM (Functional Analysis through Hidden Markov Models) is available from http://fathmm.biocompute.org.uk. FATHMM  descriptors -
                        * Pathogenic = Defined as Cancer or Damaging.
                        * Neutral = Defined as Passenger or Tolerated.
[29:AC]               FATHMM Score                                       The scores are in the form of pvalues ranging from 0 to 1. Pvalues greater than 0.5 are pathogenic while  less than 0.5 are benign. Pvalues close to 0 or 1 are the high confidence results which are more accurate. The results are annotated as 10 feature groups (separately for coding and non coding variants) details of which can be found in the original FATHMM-MKL paper.
[30:AD]               Mutation somatic status                            Information on whether the sample was reported to be Confirmed Somatic, Previously Reported or Variant of unknown origin -
                        * Variant of unknown origin = when the mutation is known to be somatic but the tumour was sequenced without a matched normal.
                        * Confirmed Somatic = if the mutation has been confimed to be somatic in the experiment by sequencing both the tumour and a matched normal from the same patient.
                        * Previously observed = when the mutation has been reported as somatic previously but not in current paper.
[31:AE]               Pubmed_PMID                                        The PUBMED ID for the paper that the sample was noted in, linking to pubmed to provide more details of the publication.
[32:AF]               Id Study                                           Lists the unique Ids of studies that have involved this sample.
[33:AG]               Sample source,Tumour origin                        Describes where the sample has originated from including the tumour type.
[35:AI]               Age                                                Age of the sample (if this information is provided with the publications).



------------------------------------
Structural Genomic Reararrangements
------------------------------------
STRUCTURAL VARIANTS
 All structural variants from the current release in a tab separated table. [ /cosmic/grch37/cosmic/v81/CosmicStructExport.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Sample name                                        A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual.
[2:B]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[3:C]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[4:D]                 Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[5:E]                 Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[6:F]                 Primary Histology                                  The histological classification of the sample.
[7:G]                 Histology Subtype 1                                Further histological classification (level 1) of the sample.
[8:H]                 Histology Subtype 2                                Further histological classification (level 2) of the sample.
[9:I]                 Histology Subtype 3                                Further histological classification (level 3) of the sample.
[10:J]                Mutation Id                                        unique mutation identifier.
[11:K]                Mutation Type                                      Type of mutation : Intra/Inter (chromosomal), tandem duplication, deletion, inversion, complex substitutions, complex amplicons.
[12:L]                GRCh                                               The coordinate system used -
                        * 38 = GRCh38/Hg38
                        * 37 = GRCh37/Hg19
[13:M]                Description                                        A syntax which describes the structural variant, based on HGVS recommendations.
[14:N]                Pubmed_PMID                                        The PUBMED ID for the paper that the sample was noted in.
[15:O]                ID_STUDY                                           Lists the unique Ids of studies that have involved this structural mutation.


BREAKPOINTS
 All breakpoint data from the current release in a tab separated table. [ /cosmic/grch37/cosmic/v81/CosmicBreakpointsExport.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Sample name                                        A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers.
[2:B]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[3:C]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[4:D]                 Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[5:E]                 Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[6:F]                 Primary Histology                                  The histological classification of the sample.
[7:G]                 Histology Subtype 1                                Further histological classification (level 1) of the sample.
[8:H]                 Histology Subtype 2                                Further histological classification (level 2) of the sample.
[9:I]                 Histology Subtype 3                                Further histological classification (level 3) of the sample.
[10:J]                Mutation Type                                      Type of mutation : Intra/Inter (chromosomal), tandem duplication, deletion, inversion, complex substitutions, complex amplicons.
[11:K]                Mutation Id                                        unique mutation identifier.
[12:L]                Breakpoint Order                                   For variants involving multiple breakpoints, the predicted order along chromosome(s).Otherwise '0'.
[13:M]                GRCh                                               The coordinate system used -
                        * 38 = GRCh38/Hg38
                        * 37 = GRCh37/Hg19
[14:N]                Chrom From                                         The chromosome where the first variant/breakpoint occurs.
[15:O]                Location From min                                  The first position in breakpoint range.
[16:P]                Location From max                                  The last position in breakpoint range.
[17:Q]                Strand From                                        positive or negative.
[18:R]                Chrom To                                           The chromosome where the last variant/breakpoint occurs.
[19:S]                Location To min                                    The first position in breakpoint range.
[20:T]                Location To max                                    The last position in breakpoint range.
[21:U]                Strand To                                          positive or negative.
[22:V]                Non-templated ins seq                              Non Templated Sequence (if any) which is inserted at the breakpoint. The sequence is not encoded.
[23:W]                Pubmed_PMID                                        The PUBMED ID for the paper that the sample was noted in.
[24:X]                Id Study                                           Lists the unique Ids of studies that have involved this structural mutation.



-----------------------
Complete Fusion Export
-----------------------
 All gene fusion mutation data from the current release in a tab separated table. [ /cosmic/grch37/cosmic/v81/CosmicFusionExport.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Sample id,Sample name,                             A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers.
[3:C]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[4:D]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[5:E]                 Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[6:F]                 Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[7:G]                 Primary Histology                                  The histological classification of the sample.
[8:H]                 Histology Subtype 1                                Further histological classification (level 1) of the sample.
[9:I]                 Histology Subtype 2                                Further histological classification (level 2) of the sample.
[10:J]                Histology Subtype 3                                Further histological classification (level 3) of the sample.
[11:K]                Fusion Id                                          Unique fusion mutation identifier.
[12:L]                Translocation Name                                 Syntax describing the portions of mRNA present (in HGVS 'r.' format) from each gene (allows representation of UTR sequences).
[13:M]                Fusion type                                        Type of mutation.
[14:N]                Pubmed_PMID                                        The PUBMED ID for the paper that the sample was noted in.
[15:O]                Id Study                                           Lists the unique Ids of studies that have involved this fusion mutation.



------------------------------
All Mutations in Census Genes
------------------------------
 All coding mutations in genes listed in the Cancer Gene Census ( http://cancer.sanger.ac.uk/census ) in a tab separated table. [ /cosmic/grch37/cosmic/v81/CosmicMutantExportCensus.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Gene name                                          The gene name for which the data has been curated in COSMIC. In most cases this is the accepted HGNC identifier.
[2:B]                 Accession Number                                   The transcript identifier of the gene.
[3:C]                 Gene CDS length                                    Length of the gene (base pair) counts.
[4:D]                 HGNC id                                            if gene is in HGNC, this id helps linking it to HGNC.
[5:E]                 Sample name,Sample id,Id tumour                    A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers.
[8:H]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[9:I]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[10:J]                Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[11:K]                Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[12:L]                Primary Histology                                  The histological classification of the sample.
[13:M]                Histology Subtype 1                                Further histological classification (level 1) of the sample.
[14:N]                Histology Subtype 2                                Further histological classification (level 2) of the sample.
[15:O]                Histology Subtype 3                                Further histological classification (level 3) of the sample.
[16:P]                Genome-wide screen                                 if the entire genome/exome is sequenced.
[17:Q]                Mutation Id                                        unique mutation identifier.
[18:R]                Mutation CDS                                       The change that has occurred in the nucleotide sequence. Formatting is identical to the method used for the peptide sequence.
[19:S]                Mutation AA                                        The change that has occurred in the peptide sequence. Formatting is based on the recommendations made by the Human Genome Variation Society. The description of each type can be found by following the link to Mutation Overview page.
[20:T]                Mutation Description                               Type of mutation (substitution, deletion, insertion, complex, fusion etc.)
[21:U]                Mutation zygosity                                  Information on whether the mutation was reported to be homozygous , heterozygous or unknown within the sample.
[22:V]                LOH                                                LOH Information on whether the gene was reported to have loss of heterozygosity in the sample: yes, no or unknown.
[23:W]                GRCh                                               The coordinate system used -
                        * 38 = GRCh38/Hg38
                        * 37 = GRCh37/Hg19
[24:X]                Mutation genome position                           The genomic cooridnates of the mutation.
[25:Y]                Mutation strand                                    positive or negative.
[26:Z]                SNP                                                All the known SNPs are flagged as 'y' defined by the 1000 genomes project, dbSNP and a panel of 378 normal (non-cancer) samples from Sanger CGP sequencing.
[27:AA]               Resistance Mutation                                mutation confers drug resistance (see CosmicResistanceMutations.tsv.gz for gene/drug details).
[28:AB]               FATHMM prediction                                  More information about FATHMM (Functional Analysis through Hidden Markov Models) is available from http://fathmm.biocompute.org.uk. FATHMM  descriptors -
                        * Pathogenic = Defined as Cancer or Damaging.
                        * Neutral = Defined as Passenger or Tolerated.
[29:AC]               FATHMM score                                       The FATHMM-MKL functional score is a p-value, ranging from 0 to 1. Scores above 0.5 are deleterious, but in order to highlight the most significant data in COSMIC, only scores >= 0.7 are classified as 'Pathogenic'. Mutations are classed as 'Neutral' if the score is <= 0.5.
[30:AD]               Mutation somatic status                            Information on whether the sample was reported to be Confirmed Somatic, Previously Reported or Variant of unknown origin -
                        * Variant of unknown origin = when the mutation is known to be somatic but the tumour was sequenced without a matched normal.
                        * Confirmed Somatic = if the mutation has been confimed to be somatic in the experiment by sequencing both the tumour and a matched normal from the same patient.
                        * Previously observed = when the mutation has been reported as somatic previously but not in current paper.
[31:AE]               Pubmed_PMID                                        The PUBMED ID for the paper that the sample was noted in, linking to pubmed to provide more details of the publication.
[32:AF]               Id Study                                           Lists the unique Ids of studies that have involved this sample.
[33:AG]               Sample source,Tumour origin                        Describes where the sample has originated from including the tumour type.
[35:AI]               Age                                                Age of the sample (if this information is provided with the publications).



--------------------
Non coding variants
--------------------
 A tab separated table of all non-coding mutations from the current release. [ /cosmic/grch37/cosmic/v81/CosmicNCV.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Sample name,Sample id,Tumour id                    A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers.
[4:D]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cell_lines/classification.  In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[5:E]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[6:F]                 Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[7:G]                 Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[8:H]                 Primary Histology                                  The histological classification of the sample.
[9:I]                 Histology Subtype 1                                Further histological classification (level 1) of the sample.
[10:J]                Histology Subtype 2                                Further histological classification (level 2) of the sample.
[11:K]                Histology Subtype 3                                Further histological classification (level 3) of the sample.
[12:L]                Genome-wide screen                                 if the entire genome/exome is sequenced.
[13:M]                Id NCV                                             unique non-coding variant identifier.
[14:N]                Zygosity                                           Information on whether the mutation was reported to be homozygous , heterozygous or unknown within the sample.
[15:O]                GRCh                                               The coordinate system used -
                        * 38 = GRCh38/Hg38
                        * 37 = GRCh37/Hg19
[16:P]                Genome position                                    The genomic cooridnate of the mutation.
[17:Q]                Mutation somatic status                            Information on whether the sample was reported to be Confirmed Somatic, Previously Reported or Variant of unknown origin -
                        * variant of unknown origin = when the mutation is known to be somatic but the tumour was sequenced without a matched normal.
                        * Confirmed Somatic = if the mutation has been confimed to be somatic in the experiment by sequencing both the tumour and a matched normal from the same patient.
                        * Previously observed = when the mutation has been reported as somatic previously but not in current paper.
[18:R]                WT SEQ                                             wild type sequence.
[19:S]                MUT SEQ                                            Mutated sequence.
[20:T]                SNP                                                All the known SNPs are flagged as 'y' defined by the 1000 genomes project, dbSNP and a panel of 378 normal (non-cancer) samples from Sanger CGP sequencing.
[21:U]                FATHMM_MKL_NON_CODING_SCORE                        FATHMM-MKL non-coding score. A p-value ranging from 0 to 1 where >= 0.7 is functionally significant.
[22:V]                FATHMM_MKL_NON_CODING_GROUPS                       FATHMM-MKL group classification. More details from http://cancer.sanger.ac.uk/cosmic/analyses.
[23:W]                FATHMM_MKL_CODING_SCORE                            FATHMM-MKL coding score (p-value ranging from 0 to 1).
[24:X]                FATHMM_MKL_CODING_GROUPS                           FATHMM-MKL group classification (coding). More details from http://cancer.sanger.ac.uk/cosmic/analyses.
[25:Y]                Whole Genome Reseq                                 if the enitre genome is sequenced.
[26:Z]                Whole_Exome                                        if the enitre exome is sequenced.
[27:AA]               Id Study                                           Lists the unique Ids of studies that have involved this non coding mutation.
[28:AB]               Pubmed_PMID                                        The PUBMED ID for the paper that the sample was noted in.



---------------------
Copy Number Variants
---------------------
 All copy number abberations from the current release in a tab separated table. For more information on copy number data, please see http://cancer.sanger.ac.uk/cosmic/help/cnv/overview. [ /cosmic/grch37/cosmic/v81/CosmicCompleteCNA.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 CNV_ID                                             The unique identifier for the variant (not stable, differs between releases).
[2:B]                 Id gene,Gene name                                  The ID and symbol of the gene which overlaps the copy number segment (or '-' where there is no overlapping gene).
[4:D]                 Sample id,Id tumour                                A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers. These samples are from the ICGC and TCGA.
[6:F]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[7:G]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[8:H]                 Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[9:I]                 Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[10:J]                Primary Histology                                  The histological classification of the sample.
[11:K]                Histology Subtype 1                                Further histological classification (level 1) of the sample.
[12:L]                Histology Subtype 2                                Further histological classification (level 2) of the sample.
[13:M]                Histology Subtype 3                                Further histological classification (level 3) of the sample.
[14:N]                Sample Name                                        The name of the sample.
[15:O]                Total_CN                                           The sum of the major and minor allele counts eg if ABB, total copy number = 3.
[16:P]                Minor Allele                                       The number of copies of the least frequent allele eg if ABB, minor allele = A ( 1 copy) and major allele = B ( 2 copies).
[17:Q]                Mut Type                                           Defined as Gain or Loss. For ICGC samples; as defined in the original data. For TCGA samples reanalysed with ASCAT -
                        * GAIN = average genome ploidy <= 2.7 AND total copy number >= 5 OR average genome ploidy > 2.7  AND total copy number >= 9
                        * LOSS = average genome ploidy <= 2.7 AND total copy number = 0 OR average genome ploidy > 2.7 AND total copy number < ( average genome ploidy - 2.7 )
[18:R]                Id Study                                           Lists the unique Ids of studies that have involved this copy number variation.
[19:S]                GRCh                                               The coordinate system used -
                        * 38 = GRCh38/Hg38
                        * 37 = GRCh37/Hg19
[20:T]                Chromosome:G_Start..G_Stop                         The genomic coordinates of the variation.



----------------
Gene Expression
----------------
 All gene expression level 3 data from the TCGA portal for the current most release in a tab separated table. Please note : The platform codes currently used to produce the COSMIC gene expression values are: IlluminaGA_RNASeqV2, IlluminaHiSeq_RNASeqV2, AgilentG4502A_07_2, AgilentG4502A_07_3. For more information on the gene expression data, please see  http://cancer.sanger.ac.uk/cosmic/analyses. [ /cosmic/grch37/cosmic/v81/CosmicCompleteGeneExpression.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Sample id,Sample name                              A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers. These samples are from the ICGC and TCGA.
[3:C]                 Gene name                                          The gene name for which the data has been curated in COSMIC. In most cases this is the accepted HGNC identifier.
[4:D]                 Regulation                                         it could be over or under depending on the scores from different platforms if they are above or below the threshold.
[5:E]                 Z-score                                            z_score serves as an indicative score taken from the gene_expression from different platforms in order of preference: IlluminaHiSeq_RNASeqV2, IlluminaGA_RNASeqV2, AgilentG4502A_07_3.
[6:F]                 Id Study                                           Lists the unique Ids of studies that have involved this gene expression data.



------------
Methylation
------------
 TCGA Level 3 methylation data from the ICGC portal for the current release in a tab separated table. More information on the methylation data is available from http://cancer.sanger.ac.uk/wgs/analyses. [ /cosmic/grch37/cosmic/v81/CosmicCompleteDifferentialMethylation.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Study_ID                                           The study Id for these data.
[2:B]                 Id Sample,Sample name,Id tumour                    A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers. These samples are from the TCGA.
[5:E]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[6:F]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[7:G]                 Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[8:H]                 Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[9:I]                 Primary Histology                                  The histological classification of the sample.
[10:J]                Histology Subtype 1                                Further histological classification (level 1) of the sample.
[11:K]                Histology Subtype 2                                Further histological classification (level 2) of the sample.
[12:L]                Histology Subtype 3                                Further histological classification (level 3) of the sample.
[13:M]                Fragment Id                                        The unique probe Id for a specific CpG.
[14:N]                Genome Version                                     The coordinate system used -
                        * 38 = GRCh38/Hg38
                        * 37 = GRCh37/Hg19
[15:O]                Chromosome                                         The chromosome location of the probe (1-22, X or Y).
[16:P]                Position                                           The genome location of the CpG targeted by the probe (1-based coordinates).
[17:Q]                Strand                                             Positive or negative.
[18:R]                Gene Name                                          The gene name (if the probe falls within the coding region of a COSMIC gene) or the probe annotation as descibed by Illumina.
[19:S]                Methylation                                        The methylation level; H (High, beta-value >0.8) or L (Low, beta-value < 0.2).
[20:T]                Avg Beta Value Normal                              The average beta-value across the normal population. The beta-value of the tumour must differ from this value by >0.5 to be considered a variant.
[21:U]                Beta Value                                         The beta-value for the probe in the tumour sample. Only values >0.8 (High) or <0.2 (Low) are included.
[22:V]                Two Sided P-Value                                  The two sided p-value.



-------------------
Cancer Gene Census
-------------------
 A list of all cancer census genes from the current release in a comma separated table. The census table is exported from http://cancer.sanger.ac.uk/census and the format is the same. [ /cosmic/grch37/cosmic/v81/cancer_gene_census.csv ] 


-----------------------
COSMIC Sample Features
-----------------------
 All the features related to a sample from the current release in a tab separated file. [ /cosmic/grch37/cosmic/v81/CosmicSample.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Sample id,Sample name,Id tumour,Id Individual      A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers. These samples are from the ICGC and TCGA.
[5:E]                 Primary Site                                       The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[6:F]                 Site Subtype 1                                     Further sub classification (level 1) of the samples tissue of origin.
[7:G]                 Site Subtype 2                                     Further sub classification (level 2) of the samples tissue of origin.
[8:H]                 Site Subtype 3                                     Further sub classification (level 3) of the samples tissue of origin.
[9:I]                 Primary Histology                                  The histological classification of the sample.
[10:J]                Histology Subtype 1                                Further histological classification (level 1) of the sample.
[11:K]                Histology Subtype 2                                Further histological classification (level 2) of the sample.
[12:L]                Histology Subtype 3                                Further histological classification (level 3) of the sample.
[13:M]                Therapy Relationship                               Relates the time-point of tissue sampling to the drug therapy used to treat the tumour.
[14:N]                Sample Differentiator                              Gives additional information if more than one sample (e.g. carcinomatous and sarcomatous components) from a tumour has been screened for mutations or if samples from a tumour were taken at different time points.
[15:O]                Mutation Allele Specification                      Where a publication has information on more than one mutation for one gene in a sample and reports whether or not the mutations occurred on the same or different chromosomes.
[16:P]                Msi                                                If microsatellite instability data is given in the publication per sample then High, Low, Stable/Low, MSI or Stable is reported in COSMIC. Unknown is the default.
[17:Q]                Average Ploidy                                     The average ploidy of the sample, calculated from copy number data (where available).
[18:R]                Whole Genome Screen                                'y' if the sample was whole genome screened.
[19:S]                Whole Exome Screen                                 'y' if the sample was whole exome sequenced.
[20:T]                Sample Remark                                      Any additional sample information e.g. % mutant allele burden.
[21:U]                Drug Response                                      Clinical and in vitro responses to drugs (particularly targeted drugs). Phrasing based on RECIST guidelines.  Note that in COSMIC, SD (stable disease) and PD (progressive disease) = clinical primary non response.
[22:V]                Grade                                              Grade of tumour. The phrase 'Some Grade data are given in publication' is used when publication reports grade data or when data hasn't been given per sample. More detailed data follow commonly used grading systems in tumours.
[23:W]                Age at tumour recurrence                           Where both primary and recurrent tumour samples from an individual have been screened for mutations and the age (in years) of the patient at the time of the recurrence is different to that at diagnosis.
[24:X]                Stage                                              Stage of tumour. The phrase 'Some Stage data are given in publication' is used when publication reports stage data or when data hasn't been given per sample. More detailed data follow commonly used staging systems in tumours.
[25:Y]                Cytogenetics                                       Karyotype of the tumour.
[26:Z]                Metastatic Site                                    Tissue site of any metastases identified in an individual.
[27:AA]               Tumour Source                                      Source of tumour tissue sample e.g. primary, metastasis.
[28:AB]               Tumour Remark                                      Any additional tumour information e.g. metachronous tumour.
[29:AC]               Age                                                Age (in years) of individual at diagnosis.
[30:AD]               Ethnicity                                          Ethnicity (e.g. Caucasian) of individual.
[31:AE]               Environmental Variables                            Environmental variables to which an individual has been exposed (e.g. viral exposure, smoking status).
[32:AF]               Germline Mutation                                  Gene name/mutation if a germline mutation as well as a somatic mutation has been detected in the same gene in the same tumour sample.
[33:AG]               Therapy                                            Any significant treatment an individual has received prior to mutation screening.
[34:AH]               Family                                             Any familial cancer history for an individual or familial relationships of individuals screened for mutations in the same publication.
[35:AI]               Normal tissue tested                               If normal tissue from the same individual has been screened for mutations.
[36:AJ]               Gender                                             Sex of individual.
[37:AK]               Individual Remark                                  Any additional individual information (e.g. age group, hereditary syndromes).
[38:AL]               NCI code                                           NCI thesaurus code for tumour histological classification.



------------
COSMIC HGNC
------------
 A tab separated table showing the relationship between the Cancer Gene Census, COSMIC ID, Gene Name, HGNC ID and Entrez ID. [ /cosmic/grch37/cosmic/v81/CosmicHGNC.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 COSMIC_ID                                          COSMIC Gene ID (COSG*).
[2:B]                 COSMIC_GENE_NAME                                   Gene name used in COSMIC.
[3:C]                 Entrez_id                                          Entrez ID mapping.
[4:D]                 HGNC_ID                                            HGNC mapping.
[5:E]                 Mutated?                                           Does the gene have coding mutations y/n.
[6:F]                 Cancer_census?                                     Is the gene in the Cancer gene census y/n.
[7:G]                 Expert Curated?                                    Has the gene been manually curated by the team of expert curators y/n.



----------------------------
COSMIC Resistance Mutations
----------------------------
 A tab separated table listing the details of all mutations in COSMIC which are known to confer drug resistance. [ /cosmic/grch37/cosmic/v81/CosmicResistanceMutations.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Sample name,Sample id                              A sample is an instance of a portion of a tumour being examined for mutations. The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymisation process. A number of samples can be taken from a single tumour and a number of tumours can be obtained from one individual. A sample id is used to identify a sample within the COSMIC database. There can be multiple ids, if the same sample has been entered into the database multiple times from different papers.
[3:C]                 Gene Name                                          The gene name for which the data has been curated in COSMIC. In most cases this is the accepted HGNC identifier.
[4:D]                 Transcript                                         The transcript identifier (accession number) of the gene.
[5:E]                 Census Gene                                        Is the gene in the Cancer Gene Census (Yes, or No).
[6:F]                 Drug Name                                          The name of the drug which the mutation confers resistance to.
[7:G]                 ID Mutation                                        The unique mutation identifier (COSM).
[8:H]                 AA Mutation                                        The change that has occurred in the peptide sequence. Formatting is based on the recommendations made by the Human Genome Variation Society.
[9:I]                 CDS Mutation                                       The change that has occurred in the nucleotide sequence. Formatting is identical to the method used for the peptide sequence.
[10:J]                Primary Tissue                                     The primary tissue/cancer from which the sample originated. More details on the tissue classification are avaliable from http://cancer.sanger.ac.uk/cosmic/classification. In COSMIC we have standard classification system for tissue types and sub types because they vary a lot between different papers.
[11:K]                Tissue Subtype 1                                   Further sub classification (level 1) of the samples tissue of origin.
[12:L]                Tissue Subtype 2                                   Further sub classification (level 2) of the samples tissue of origin.
[13:M]                Histology                                          The histological classification of the sample.
[14:N]                Histology Subtype 1                                Further histological classification (level 1) of the sample.
[15:O]                Histology Subtype 2                                Further histological classification (level 2) of the sample.
[16:P]                Pubmed ID                                          The PUBMED ID for the paper that the sample was noted in, linking to pubmed to provide more details of the publication.
[17:Q]                CGP Study                                          Lists the unique Ids of studies that have involved this sample.
[18:R]                Somatic Status                                     Information on whether the sample was reported to be Confirmed Somatic, Previously Reported or Variant of unknown origin -
                        * Variant of unknown origin = when the mutation is known to be somatic but the tumour was sequenced without a matched normal.
                        * Confirmed Somatic = if the mutation has been confimed to be somatic in the experiment by sequencing both the tumour and a matched normal from the same patient.
                        * Previously observed = when the mutation has been reported as somatic previously but not in current paper.
[19:S]                Sample Source                                      Describes where the sample has originated from including the tumour type.
[20:T]                Zygosity                                           Information on whether the mutation was reported to be homozygous , heterozygous or unknown within the sample.
[21:U]                Genome Coordinates (GRCh37/38)                     The genome location of the mutation (chr:start..end), on the specified genome version.



----------------------------------
ASCAT Ploidy and Purity Estimates
----------------------------------
 A tab separated table listing the ploidy and aberrant cell fraction (purity estimate), for TCGA samples re-analysed using ASCAT. [ /cosmic/grch37/cosmic/v81/ascat_acf_ploidy.tsv ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Cancer_Type_Code                                   The disease code (decode available from https://tcga-data.nci.nih.gov/datareports/codeTablesReport.htm).
[2:B]                 Sample                                             The name of the sample.
[3:C]                 Aberrant_Cell_Fraction(Purity)                     The aberrant cell fraction (purity estimate).
[4:D]                 Ploidy                                             The ploidy of the genome.



--------------------------------------------
VCF Files (coding and non-coding mutations)
--------------------------------------------
CODING MUTATIONS
 VCF file of all coding mutations in the current release. [ /cosmic/grch37/cosmic/v81/VCF/CosmicCodingMuts.vcf.gz ] 

NON-CODING VARIANTS
 VCF file of all non coding mutations in the current release. [ /cosmic/grch37/cosmic/v81/VCF/CosmicNonCodingVariants.vcf.gz ] 


-------------------
Fasta File (genes)
-------------------
 CDS sequence for all the genes in COSMIC. [ /cosmic/grch37/cosmic/v81/All_COSMIC_Genes.fasta.gz ] 


-------------------
COSMIC Transcripts
-------------------
 A tab separated table listing the gene name and transcript accession for each gene ID. [ /cosmic/grch37/cosmic/v81/CosmicTranscripts.tsv.gz ] 

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 Gene ID                                            The unique ID of the gene.
[2:B]                 Gene_NAME                                          The name of the gene.
[3:C]                 Transcript ID                                      The accession of the transcript.



---------------------
Oracle Database Dump
---------------------
 The oracle database dump of the current release. Please see the help document OracleSchemaDocumentation.pdf for a description of the database schema. [ /cosmic/grch37/cosmic/v81/COSMIC_ORACLE_EXPORT.dmp.gz ] 


