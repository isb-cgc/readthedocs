
Somatic DNA Mutations 
=======================

The 
Somatic Mutations tables, `Somatic_Mutation_DCC <https://console.cloud.google.com/bigquery?p=isb-cgc&d=TCGA_hg19_data_v0&t=Somatic_Mutation_DCC&page=table>`_, 
`Somatic_Mutation_MC3 <https://console.cloud.google.com/bigquery?p=isb-cgc&d=TCGA_hg19_data_v0&t=Somatic_Mutation_MC3&page=table>`_, and 
`Somatic_Mutation <https://console.cloud.google.com/bigquery?p=isb-cgc&d=TCGA_hg38_data_v0&t=Somatic_Mutation&page=table>`_
in BigQuery contain somatic mutation calls collected from the open-access 
`MAF <https://docs.gdc.cancer.gov/Encyclopedia/pages/Mutation_Annotation_Format_TCGAv2/>`_.

files from 30 tumor types.

For each MAF file, some
simple data-cleaning performed, it was then annotated using
`Oncotator <https://www.broadinstitute.org/cancer/cga/oncotator>`_
and then further processed to remove duplicates before being merged into a single table.

Data-Cleaning
-------------

- Remove any lines where the ``build`` is not ``37``
- Remove any lines where the ``chr`` is not in ``[1-22, X, Y]``
- Remove any lines where the ``Mutation_Status`` is not ``Somatic``
- Remove any lines where the ``Sequencer`` is not an Illumina platform
- Change the column labels to match what Oncotator expects (*eg* ``ncbi_build`` becomes ``build``, ``chromosome``, ``chr``, *etc*.

Oncotator Annotation
--------------------

Each file was then annotated using Oncotator version 1.5.1, with the ``Jan2015`` database,
and the options ``--input_format=MAFLITE --output_format=TCGAMAF``.

The outputs of Oncotator were lightly processed to change the column labels and to remove
certain special characters from strings.

Duplicate Removal
-----------------

Because many tumor types have several "current" MAF files and deciding which one is the
"best" is a non-trivial process, and also because some tumor samples may have had mutations
called relative to a tissue normal and also relative to a blood normal, it is possible that
the same mutation has been called multiple times.  In order to eliminate over-counting of
mutations, we sought to remove these duplicate calls from the result of concatenating all
of the annotated MAF files using the following rules:

- if a mutation in the same position is called in a particular tumor sample with respect to multiple matched normals, we prefer the "blood derived normal" over the "solid tissue normal"

- if a mutation in the same position is called in multiple aliquots for one tumor sample, we prefer the "D" analyte over the "W" analyte (*eg* ``TCGA-B0-5695-01A-11D-1534-10`` over ``TCGA-B0-5695-01A-11W-1584-10``)

- if both aliquots are "D" (or both are "W") analytes, then we choose based on the data-generating-center (the final two characters in the aliquot barcode), preferring first:

   - ``01``, ``08``, or ``14`` (all of which refer to ``broad.mit.edu``)
   - ``09``, ``21``, or ``30`` (all of which refer to ``genome.wustl.edu``)
   - ``10``  or ``12`` (both of which refer to ``hgsc.bcm.edu``)
   - ``13``  or ``31`` (both of which refer to ``bcgsc.ca``)
   - ``18``  or ``25`` (both of which refer to ``ucsc.edu``)

- finally, in the event that a mutation in the same position was called by the same center, with the same type of matched normal, and the same type of analyte, then we choose the aliquot with the larger value in the final 4-digit sequence in the barcode (positions 21:25)

In addition, any exact duplicates (*ie* all fields describing a mutation are the same) in the
merged file are removed, and the final result uploaded into BigQuery.

The result are tables containing over 5.8 million mutations called on 8435 tumor samples from 8373 patients.


