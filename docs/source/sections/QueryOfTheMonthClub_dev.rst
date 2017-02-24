***********************
Query of the Month Club
***********************

Welcome to the 'Query of the Month Club' where we'll be creating a collection
of new and interesting queries to demonstrate the powerful combination of
BigData from the TCGA and BigQuery from Google.

Please let us know if you'd like to be featured on the "query-club"!
email: dgibbs (at) systemsbiology (dot) org


------------------


February, 2017
##############


This month, we explore user defined functions or UDFs. BigQuery allows
us to define special functions using javascript. These functions are defined as
part of the SQL and then called within the query.

`The Google UDF docs.<https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions>`_

UDFs take a set of parameters, and return a value. They are strongly typed functions,
which means that we need to define the types of inputs and outputs. For example,
we might have FLOAT64 and BOOL input types and return a STRING. See the google
docs for the complete list of available types.

In our first example, we'll define two new functions. The first classifies a sample
as having larger expression value than a given parameter. And second, a function
that glues three strings together. Then, in the SQL query we call both functions.
These initial queries will be starting points in a more complicated example below.

These queries are using Standard SQL, to if you're in the web interface,
remember to open the options and unclick the 'Use Legacy SQL' button.

.. code-block:: sql

  CREATE TEMPORARY FUNCTION
                                      -- First we tell BQ that we're defining a function.

    BiggerThan (x FLOAT64, y FLOAT64) -- then we give it a function name and input types
    RETURNS BOOL                      -- we also need to tell BQ what the return type is
    LANGUAGE js AS """

      return (x > y);                 // this is the body of the function.

    """;

  CREATE TEMPORARY FUNCTION
    Combiner (x STRING, y STRING, z STRING)  -- This function takes 3 strings
    RETURNS STRING                           -- and returns a string
    LANGUAGE js AS """

    return (x + "_" + y + "_" + z);          // The javascript '+' joins strings.

  """;
    --
    --  Now we're ready to use the UDFs in a query.
    --  Using Standard SQL, we'll define a subtable with the expression
    --  of the ESR1 gene in the BRCA cohort.
    --
  WITH
    gene1 AS (
    SELECT
      AliquotBarcode AS barcode1,
      Study AS study1,
      SampleTypeLetterCode AS code1,
      HGNC_gene_symbol AS gene_id_1,
      AVG(LOG(normalized_count+1, 2)) AS count1
    FROM
      `isb-cgc.tcga_201607_beta.mRNA_UNC_RSEM`
    WHERE
      Study = 'BRCA'
      AND SampleTypeLetterCode = 'TP'
      AND HGNC_gene_symbol = 'ESR1'
      AND normalized_count >= 0
    GROUP BY
      AliquotBarcode,
      gene_id_1,
      study1,
      code1)
    --
    --
    -- Now we can call our functions,
    -- processing the subtable.
    --
  SELECT
    Combiner(barcode1, study1, code1),
    BiggerThan(count1, 5.1)
  FROM
    gene1



Next, we're going to get complicated(!), and estimate clusters assignments
using a K-means algorithm, implemented in javascript, as a UDF!

`Here's the wikipedia link about K-means clustering.<https://en.wikipedia.org/wiki/K-means_clustering>`_

In performing clustering, we're going to assign each of the BRCA sample to a cluster
depending on the expression of two genes ESR1 and EGFR. This is an iterative process
that starts with two random cluster centers, and we optimize in each iteration
by updating the sample labels (what cluster they're assigned to), and then
updating the cluster center points.

.. code-block:: sql

  CREATE TEMPORARY FUNCTION

    -- In this function, we're going to be working on arrays of values.
    -- we're also going to define a set of functions 'inside' the kMeans.

    -- *heavily borrowing from https://github.com/NathanEpstein/clusters* --

    kMeans(x ARRAY<FLOAT64>,  -- ESR1 gene expression
           y ARRAY<FLOAT64>,  -- EGFR gene expression
           iterations FLOAT64,  -- the number of iterations
           k FLOAT64)           -- the number of clusters

    RETURNS ARRAY<FLOAT64>  -- returns the cluster assignments

    LANGUAGE js AS """
    'use strict'


    function sumOfSquareDiffs(oneVector, anotherVector) {
      // the sum of squares error //
      var squareDiffs = oneVector.map(function(component, i) {
        return Math.pow(component - anotherVector[i], 2);
      });
      return squareDiffs.reduce(function(a, b) { return a + b }, 0);
    };

  function mindex(array) {
    // returns the index to the minimum value in the array
    var min = array.reduce(function(a, b) {
      return Math.min(a, b);
    });
    return array.indexOf(min);
  };

  function sumVectors(a, b) {
    // The map function gets used frequently in javascript
    return a.map(function(val, i) { return val + b[i] });
  };

  function averageLocation(points) {
    // Take all the points assigned to a cluster
    // and find the averge center point.
    // This gets used to update the cluster centroids.
    var zeroVector = points[0].location.map(function() { return 0 });
    var locations = points.map(function(point) { return point.location });
    var vectorSum = locations.reduce(function(a, b) { return sumVectors(a, b) }, zeroVector);
    return vectorSum.map(function(val) { return val / points.length });
  };

  function Point(location) {
    // A point object, each sample is represented as a point //
    var self = this;
    this.location = location;
    this.label = 1;
    this.updateLabel = function(centroids) {
      var distancesSquared = centroids.map(function(centroid) {
        return sumOfSquareDiffs(self.location, centroid.location);
      });
      self.label = mindex(distancesSquared);
    };
  };


  function Centroid(initialLocation, label) {
    // The cluster centroids //
    var self = this;
    this.location = initialLocation;
    this.label = label;
    this.updateLocation = function(points) {
      var pointsWithThisCentroid = points.filter(function(point) { return point.label == self.label });
      if (pointsWithThisCentroid.length > 0) {
        self.location = averageLocation(pointsWithThisCentroid);
      }
    };
  };


  var data = [];

  // Our data list is list of lists. The small list being each (x,y) point
  for (var i = 0; i < x.length; i++) {
    data.push([x[i],y[i]])
  }

  // initialize point objects with data
  var points = data.map(function(vector) { return new Point(vector) });


  // intialize centroids
  var centroids = [];
  for (var i = 0; i < k; i++) {
    centroids.push(new Centroid(points[i % points.length].location, i));
  };


  // update labels and centroid locations until convergence
  for (var iter = 0; iter < iterations; iter++) {
    points.forEach(function(point) { point.updateLabel(centroids) });
    centroids.forEach(function(centroid) { centroid.updateLocation(points) });
  };

  // return the cluster labels.
  var labels = []
  for (var i = 0; i < points.length; i++) {
    labels.push(points[i].label)
  }

  return labels;

  """;
  --
  -- *** In this query, we create two subtables, one for each gene of
  --     interest, then create a set of arrays in joining the two tables.
  --     We call the UDF using the arrays, and get a result back
  --     made of arrays.
  --
  --     Due to a technical issue we save the table of arrays to
  --     to a personal dataset, then unpack it. ***
  --
  WITH
    -- gene1, the first subtable
    --
    gene1 AS (
    SELECT
      ROW_NUMBER() OVER() row_number,
      AliquotBarcode AS barcode1,
      HGNC_gene_symbol AS gene_id_1,
      AVG(LOG(normalized_count+1, 2)) AS count1
    FROM
      `isb-cgc.tcga_201607_beta.mRNA_UNC_RSEM`
    WHERE
      Study = 'BRCA'
      AND SampleTypeLetterCode = 'TP'
      AND HGNC_gene_symbol = 'ESR1'
      AND normalized_count >= 0
    GROUP BY
      AliquotBarcode,
      gene_id_1),
    --
    -- gene2, the second subtable
    --
    gene2 AS (
    SELECT
      AliquotBarcode AS barcode2,
      HGNC_gene_symbol AS gene_id_2,
      AVG(LOG(normalized_count+1, 2)) AS count2
    FROM
      `isb-cgc.tcga_201607_beta.mRNA_UNC_RSEM`
    WHERE
      Study = 'BRCA'
      AND SampleTypeLetterCode = 'TP'
      AND HGNC_gene_symbol = 'EGFR'
      AND normalized_count >= 0
    GROUP BY
      AliquotBarcode,
      HGNC_gene_symbol),
    --
    -- Then we create a table of arrays
    -- and join the two gene tables.
    -- ** We need to make sure all the arrays are constructed using the same index. **
    --
    arrayTable AS (
    SELECT
      ARRAY_AGG(m1.row_number ORDER BY m1.barcode1) AS arrayn,
      ARRAY_AGG(m1.barcode1 ORDER BY m1.barcode1) AS barcode,
      ARRAY_AGG(count1 ORDER BY m1.barcode1) AS esr1,
      ARRAY_AGG(count2 ORDER BY m1.barcode1) AS egfr
    FROM
      gene1 AS m1
    JOIN
      gene2 AS m2
    ON
      m1.barcode1 = m2.barcode2 )
    --
    -- Now we call the k-means UDF.
    --
  SELECT
    arrayn,
    barcode,
    esr1,
    egfr,
    kMeans(esr1, egfr, 200.0, 2.0) AS cluster
  FROM
    arrayTable
    --
    -- save the resulting table to a personal dataset


We need to save the above results to an intermediate table. I would recommend
making yourself a dataset just for this purpose. The results from the above query
is *one* row of arrays. It's a little tricky to unpack the arrays into
rows, which is what we'll do next.

.. code-block:: sql

  --
  -- Unpacking the arrays is tricky because, you're not
  -- guaranteed that each array will have the same index,
  -- unless specified.
  --

  With
  resultTable AS
  (select * from `isb-cgc-02-0001.Daves_working_area.kmeans_genes`)

  SELECT
    index row_idx,
    barcode[OFFSET(index_offset)] AS AliquotBarcode,
    esr1[OFFSET(index_offset)] AS ESR1,
    egfr[OFFSET(index_offset)] AS EGFR,
    cluster[OFFSET(index_offset)] AS Cluster
  FROM
    resultTable,
    UNNEST(resultTable.arrayn) AS index
  WITH
  OFFSET
    index_offset
  ORDER BY
    index


Let's visualize the resulting clusters! Save the cluster assignments to
a csv file, and read it into R.

.. code-block:: R

  library(ggplot2)
  res0 <- read.table("results-from-the-k-means.csv", sep=",", header=T, stringsAsFactors=F)
  qplot(data=res0, x=EGFR, y=ESR1, col=as.factor(Cluster))


------------

.. figure:: query_figs/kmeans_plot.png
   :scale: 25
   :align: center


------------------

January, 2017
#############

This month we'll be comparing standard SQL and legacy SQL. It's possible to write
queries using either form, but as we'll see, using standard SQL can be easier to write
and improves readability.

In order to 'activate' standard SQL in the web browser, just under the
'New Query' text window, click the 'Show Options' button, and towards the bottom of the
options you'll find the 'Use Legacy SQL' check box -- uncheck that, and then you can
'Hide Options' to collapse the options away again.

To use R and bigrquery to execute
standard SQL, you'll need to make sure you're using the most up-to-date
version of the R package. I would recommend installing it from the github page
using devtools. Please see `bigrquery <https://github.com/rstats-db/bigrquery>`_ for more information
on installation. The important bit: there's now support for sending a parameter
called 'useLegacySql' in the REST calls.

Our task this month will be to compute correlations between copy number variants and gene expression, over
all genes, using only BRCA samples. The copy number data is expressed in a series
of segments, each with a chromosome, start-point, end-point, and value
indicating whether a duplication or deletion event (or neither) has taken place.

Note that the mean copy-number values are not discrete because these data represent
heterogeneous mixtures of cells -- only a fraction of the cells might include an
amplification or a deletion, so the 'mean copy-number' value represents the
effect of the discrete amplifications or deletions of a specific genomic segment,
averaged over the heterogenous population of cells.

One might hypothesize that a copy number *amplified* gene would have higher expression levels
than when *not* amplified. However, our gene expression data has no location information, making it
necessary to join the genomic locations from an appropriate reference.
The resulting annotated expression table can then be joined to the copy number segments.
But computing the overlap of DNA segments and genes locations can get tricky!
Below we show two different ways of accomplishing the task.

Data Tables
-----------

You can get familiar with the data sources by opening the BigQuery web interface
and taking a preview of the tables.

- isb-cgc.tcga_cohorts.BRCA ... Curated cohort table for TCGA BRCA study:  1087 unique patients and 2236 unique samples.


- isb-cgc.genome_reference.GENCODE_v19 ... This table is based on release 19 of the GENCODE reference gene set.  Note that these annotations are based on the hg19/GRCh37 reference genome.


- isb-cgc.tcga_201607_beta.mRNA_UNC_HiSeq_RSEM ... This table contains all mRNA expression data produced by the UNC-LCCC (Lineberger Comprehensive Cancer Center) using the Illumina HiSeq platform and processed through their RNASeqV2 / RSEM pipeline.


- isb-cgc.tcga_201607_beta.Copy_Number_segments ... This table contains one row for each copy-number segment identified for each TCGA aliquot. Affymetrix SNP6 data is used in making the calls.


Legacy SQL
-----------

.. code-block:: sql

    # This query makes use of a legacy UDF or 'user defined function'.
    # To define UDFs in R, we need to define it 'inline'.
    # For another example of inline definitions, see:
    # https://github.com/googlegenomics/bigquery-examples/blob/master/pgp/sql/schema-comparisons/missingness-udf.sql

    # Big legacy SQL queries grow like onions, they start in the center,
    # and grow in layers, until the outer-most select statement returns the result.
    # And like onions, they will make you cry.

    SELECT
      # Here's the final select statement, computing Pearson's correlation
      # on the avgCNsegMean, the copy number mean for a particular gene
      # and avglogExp, the average expression for the same gene.
      gene,
      chr,
      CORR(avgCNsegMean,avglogExp) AS corr,
      COUNT(*) AS n
    FROM (

      SELECT
        # This is the select statement on the joined CN and expr tables,
        # where averages are computed on copy number and expression.
        annotCN.gene AS gene,
        annotCN.chr AS chr,
        annotCN.SampleBarcode AS SampleBarcode,
        AVG(annotCN.CNsegMean) AS avgCNsegMean,
        AVG(exp.logExp) AS avgLogExp
      FROM (

        SELECT
          # This is the select statement that annotates the CN segments via binning.
          # To annotate the segments, the CN segment start and end positions are binned,
          # as well as the gene reference information.
          # The bins provide a sort of grid that can be used for aligning the segments
          # to gene locations.
          geneInfo.gene AS gene,
          geneInfo.chr AS chr,
          geneInfo.region_start AS gene_start,
          geneInfo.region_end AS gene_end,
          geneInfo.bin AS bin,
          cnInfo.SampleBarcode AS SampleBarcode,
          cnInfo.Segment_Mean AS CNsegMean,
          cnInfo.region_start AS cn_start,
          cnInfo.region_end AS cn_end
        FROM (
          SELECT
            label AS gene,
            chr,
            region_start,
            region_end,
            bin
          FROM js (  # This User-defined function bins the genome making the join possible.

              (SELECT
                gene_name AS label,
                FLOAT(start) AS value,
                LTRIM(seq_name,\"chr\") AS chr,
                start AS region_start,
                END AS region_end
              FROM
                [isb-cgc:genome_reference.GENCODE_v19]
              WHERE
                feature=\"gene\"
                AND gene_status=\"KNOWN\"
                AND source=\"HAVANA\"),

                label, value, chr, region_start, region_end,

                \"[{'name': 'label', 'type': 'string'},   // Output schema
                 {'name': 'value', 'type': 'float'},
                 {'name': 'chr',   'type': 'string'},
                 {'name': 'region_start', 'type': 'integer'},
                 {'name': 'region_end',   'type': 'integer'},
                 {'name': 'bin',   'type': 'integer'}]\",

                 \"function binIntervals(row, emit) {
                   // This is javascript ... here we use '//' for comments
                   // Legacy UDFs take a single row as input.
                   // and return a row.. can be a different number of columns.
                   var binSize = 10000;  // Make sure this matches the value in the SQL (if necessary)
                   var startBin = Math.floor(row.region_start / binSize);
                   var endBin = Math.floor(row.region_end / binSize);

                   // Since an interval can span multiple bins, emit
                   // a record for each bin it spans.
                   for(var bin = startBin; bin <= endBin; bin++) {
                     emit({label: row.label,
                           value: row.value,
                           chr: row.chr,
                           region_start: row.region_start,
                           region_end: row.region_end,
                           bin: bin,
                          });
                   }
                }\")) AS geneInfo

        JOIN EACH (
          # This is the join between the binned CNs, and the binned gene reference. #

          SELECT
            # This is the select statement that bins the gene reference information
            label AS SampleBarcode,
            value AS Segment_Mean,
            chr,
            region_start,
            region_end,
            bin
          FROM ( js (
              (SELECT
                SampleBarcode AS label,
                Segment_Mean AS value,
                Chromosome AS chr,
                start AS region_start,
                END AS region_end
              FROM
                [isb-cgc:tcga_201607_beta.Copy_Number_segments]
              WHERE
                SampleBarcode IN (
                SELECT
                  SampleBarcode
                FROM
                  [isb-cgc:tcga_cohorts.BRCA] ) ),

              label,value,chr,region_start,region_end,

              \"[{'name': 'label', 'type': 'string'},
                {'name': 'value', 'type': 'float'},
                {'name': 'chr',   'type': 'string'},
                {'name': 'region_start', 'type': 'integer'},
                {'name': 'region_end',   'type': 'integer'},
                {'name': 'bin',   'type': 'integer'}]\",

               \"function binIntervals(row, emit) {
                 // This is javascript ... here we use '//' for comments
                 // Legacy UDFs take a single row as input.
                 var binSize = 10000;  // Make sure this matches the value in the SQL (if necessary)
                 var startBin = Math.floor(row.region_start / binSize);
                 var endBin = Math.floor(row.region_end / binSize);
                 // Since an interval can span multiple bins, emit
                 // a record for each bin it spans.
                 for(var bin = startBin; bin <= endBin; bin++) {
                   emit({label: row.label,
                         value: row.value,
                         chr: row.chr,
                         region_start: row.region_start,
                         region_end: row.region_end,
                         bin: bin,
                        });
                 }
              }\"
            ) ) ) AS cnInfo
        ON
          ( geneInfo.chr = cnInfo.chr )
          AND ( geneInfo.bin = cnInfo.bin ) ) AS annotCN

      JOIN EACH (
        # Here's the join between annotated copy number table and the gene expression table.

        SELECT
          # Here we get the gene expression data, and barcodes.
          # We join on the SampleBarcodes in each table.
          SampleBarcode,
          HGNC_gene_symbol,
          LOG2(normalized_count+1) AS logExp
        FROM
          [isb-cgc:tcga_201607_beta.mRNA_UNC_HiSeq_RSEM]
        WHERE
          SampleBarcode IN (
          SELECT
            SampleBarcode
          FROM
            [isb-cgc:tcga_cohorts.BRCA] ) ) AS exp
      ON
        ( exp.HGNC_gene_symbol = annotCN.gene )
        AND ( exp.SampleBarcode = annotCN.SampleBarcode )
      GROUP BY
        gene,
        chr,
        SampleBarcode )
    GROUP BY
      gene,
      chr
    HAVING
      corr IS NOT NULL
    ORDER BY
      corr DESC



Standard SQL
------------
.. code-block:: sql

    # In standard SQL, we define a list of tables, that can build
    # off earlier definitions, so it's a little more linear and modular.

    WITH
    # This says: "we're going to define a list of tables WITH which we will perform subsequent SELECTs..."

      geneInfo AS (
        # First table: the gene reference information
        SELECT
          gene_name AS gene,
          LTRIM(seq_name,'chr') AS chr,
          `start` as region_start,
          `end`   as region_end
        FROM
          `isb-cgc.genome_reference.GENCODE_v19`
        WHERE
          feature='gene'
          AND gene_status='KNOWN'
          AND source = 'HAVANA'),

    cnInfo AS(
      # Second: the copy number data, but only for the BRCA samples (note the sub-query).
      SELECT
        SampleBarcode,
        Segment_Mean,
        Chromosome AS chr,
        `start` AS region_start,
        `end`   AS region_end
      FROM
        `isb-cgc.tcga_201607_beta.Copy_Number_segments`
      WHERE
        SampleBarcode IN (
        SELECT
          SampleBarcode
        FROM
          `isb-cgc.tcga_cohorts.BRCA` )),

    gexp AS (
      # Third: we get the gene expression data, again only for the BRCA samples
      # included is a LOG() transform as well as an AVG() aggregation function
      # which will only be relevant if there are multiple expression values for
      # a single (gene,sample) pair.
      SELECT
        SampleBarcode,
        HGNC_gene_symbol,
        AVG(LOG(normalized_count+1,2)) AS logExp
      FROM
        `isb-cgc.tcga_201607_beta.mRNA_UNC_HiSeq_RSEM`
      WHERE
        SampleBarcode IN (
        SELECT
          SampleBarcode
        FROM
          `isb-cgc.tcga_cohorts.BRCA` )
      GROUP BY
        SampleBarcode,
        HGNC_gene_symbol),

    cnAnnot AS (
      # Now, we start to re-use previously defined tables.  Here, we annotate
      # the copy-number segments by JOINing on matching chromosomes and
      # looking for overlapping regions between the copy-number segments and
      # the gene regions previously obtained from the GENCODE_v19 table.
      SELECT
        geneInfo.gene AS gene,
        geneInfo.chr AS chr,
        geneInfo.region_start AS gene_start,
        geneInfo.region_end AS gene_end,
        cnInfo.SampleBarcode AS SampleBarcode,
        AVG(cnInfo.Segment_Mean) AS Avg_CNsegMean
      FROM
      cnInfo JOIN geneInfo
      ON
        (geneInfo.chr = cnInfo.chr)
      WHERE
      (cnInfo.region_start BETWEEN geneInfo.region_start AND geneInfo.region_end) OR
      (cnInfo.region_end   BETWEEN geneInfo.region_start AND geneInfo.region_end) OR
      (cnInfo.region_start < geneInfo.region_start AND cnInfo.region_end > geneInfo.region_end)
      GROUP BY
        gene,
        chr,
        gene_start,
        gene_end,
        SampleBarcode
    ),

    bigJoin AS (
      # This is essentially the final step: in this last table definition, we make
      # a big join between the annotated copy-number table with the gene-expression
      # table and use the built-in CORR() function to compute a Pearson correlation.
      SELECT
        cnAnnot.gene AS gene,
        cnAnnot.chr AS chr,
        CORR(cnAnnot.Avg_CNsegMean,gexp.logExp) AS corr_cn_gexp,
        count(*) as n
      FROM
        cnAnnot join gexp
      ON
        ( gexp.HGNC_gene_symbol = cnAnnot.gene )
        AND ( gexp.SampleBarcode = cnAnnot.SampleBarcode )
      GROUP BY
        gene,
        chr
    )

    # Finally, let's pull down all the rows!
    select *
    from bigJoin


R script
########

.. code-block:: r

  # Here, we're going to execute the two above queries, and see how
  # the correlations compare.

  library(bigrquery)
  library(ggplot2)

  my_project_id <- "xyz"

  q_legacy <- " ... first query above"

  q_std <- " ... second query from above ..."

  legacy_res <- query_exec(q_legacy, project=my_project_id, useLegacySql=T)

  std_res <- query_exec(q_std, project=my_project_id, useLegacySql=F)

  res0 <- merge(legacy_res, std_res, by="gene")

  dim(std_res)
  #[1] 18447     4

  dim(legacy_res)
  #[1] 18424     4

  dim(res0)
  #[1] 18424     7

  qplot(data=res0, x=corr_cn_gexp, y=corr, main="CN and Expr correlation in BRCA",
        xlab="Standard SQL", ylab="Legacy SQL")


------------

.. figure:: query_figs/jan_results.png
   :scale: 25
   :align: center

This plot shows the correlations found using the Legacy SQL solution (y-axis) compared
to the correlations found using the Standard SQL solution (x-axis).  Note that an exact
match between the two methods was not expected because the implementation is not identical.
The "legacy" solution bins the copy-number segment values into uniform length genomic
segments, while the "standard" solution takes a simpler approah.

------------------

December, 2016
##############

The ISB-CGC team is starting to add the new hg38-based TCGA data available from the
`GDC Data Portal <https://gdc-portal.nci.nih.gov/>`_ and one of the first obvious questions
might be: how does the new hg38 expression data compare to the hg19 data?

Description
-----------

This is exactly the type of question that the ISB-CGC resources and the BigQuery engine
were made to answer.  In a single SQL query, we will compare two sets of gene-level
expression estimates based on RNA-Seq data.
The first set consists of the hg19-based
`RSEM <http://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-12-323>`_
normalized gene-level
expression values previously available from the TCGA DCC and now available in
an easy-to-use table in BigQuery (and also from the
`GDC Legacy Archive <https://gdc-portal.nci.nih.gov/legacy-archive>`_).
The second set was produced by the
`GDC mRNA Analysis Pipeline <https://gdc-docs.nci.nih.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/>`_
which includes a STAR alignment to hg38, and gene expression quantification using
`HTSeq <http://www-huber.embl.de/HTSeq/doc/overview.html>`_
(with annotation based on
`GENCODE v22 <http://www.gencodegenes.org/releases/22.html>`_).

Rather than look at one gene at a time, it's easy (and fast!) to compute correlations
for all genes simultaneously.  Note that this is done in a *single* query.  You do **not**
want to *loop* over all of the genes, computing one correlation at a time because the
*cost* of a BigQuery query depends primarily on the amount of data scanned during the
query, and since the data for *all* genes across *all* TCGA samples are in a *single*
table, if you were to loop over 10,000 genes running one query per gene, your costs would
go *up* by a factor of 10,000! As we show below, BigQuery computes across all the genes
at once (one of its benefits), and thus keeps the costs low.

In addition to using the two gene-expression data tables, our SQL query also
uses the GENCODE_v22 table (one of many tables in the **isb-cgc.genome_reference** dataset)
to map from the HGNC gene symbol (used in the older hg19 expression table) to the
Ensembl gene identifier (used in the new hg38 expression table).

The query below performs both
Pearson and Spearman correlations for each gene.
The result is a table with 20,021 rows -- one for each gene, with the Ensembl gene
identifier, the gene symbol, the Pearson and Spearman correlation coefficients,
and the difference between the two.  The table has also been sorted by the
Spearman coefficient, in descending order.  This query executes in less than
one minute and processes a total of 34 GB of data. This is a great example of how cloud
computing can significantly enhance analytic capabilities beyond running large analytic
bioinformatics pipelines quickly!

Back in June, Google
`announced <https://cloud.google.com/blog/big-data/2016/06/bigquery-111-now-with-standard-sql-iam-and-partitioned-tables>`_
full support for Standard SQL in BigQuery.  The query below makes use of Standard SQL,
so if you want to try running this query yourself by cutting-and-pasting it into the
`BigQuery web UI <https://bigquery.cloud.google.com>`_ you'll need to go into the
**Show Options** section and uncheck the "Use Legacy SQL" box.  If you're used to
using Legacy SQL, one small change you'll need to make right away is in how
you refer to tables: rather than ``[isb-cgc:genome_reference.GENCODE_v22]`` for
example, you will instead write ``isb-cgc.genome_reference.GENCODE_v22`` inside single-quotes.

As a concrete example of what these data look like, we created plots of
the expression data for EGFR in R
(see below for the SQL and R code).


BigQuery SQL
------------

.. code-block:: sql

    WITH
    --
    -- *GdcGene*
    -- We start by extracting gene-expression data from the new GDC/hg38-based
    -- table in the isb-cgc:hg38_data_previews dataset.  For each row, we
    -- extract simply the SamplesSubmitterID (aka the TCGA sample barcode),
    -- the Ensembl gene ID (eg ENSG00000182253), and the FPKM value.  The input
    -- table has ~671M rows and many more fields, but we just need these 3.
    GdcGene AS (
    SELECT
      SamplesSubmitterID AS sampleID,
      Ensembl_gene_ID AS geneID,
      HTSeq__FPKM AS HTSeq_FPKM
    FROM
      `isb-cgc.hg38_data_previews.TCGA_GeneExpressionQuantification` ),
    --
    -- *GeneRef*
    -- Next, we're going to get the gene-id to gene-symbol mapping from the GENCODE
    -- reference table because the GDC table reference above contains only the gene-id
    -- while the expression data we want to compare that to contains gene symbols.
    GeneRef AS (
    SELECT
      gene_id,
      gene_name
    FROM
      `isb-cgc.genome_reference.GENCODE_v22`
    WHERE
      feature='gene' ),
    --
    -- *Hg38*
    -- Now we'll join the two tables above to annotate the GDC expression data with gene-symbols,
    -- and we'll call it Hg38.  We're also going to create a ranking of the expression values
    -- so that we can compute a Spearman correlation later on.
    Hg38 AS (
    SELECT
      GdcGene.sampleID,
      GdcGene.geneID,
      GeneRef.gene_name,
      GdcGene.HTSeq_FPKM,
      DENSE_RANK() OVER (PARTITION BY GdcGene.geneID ORDER BY GdcGene.HTSeq_FPKM ASC) AS rankHTSeq
    FROM
      GdcGene
    JOIN
      GeneRef
    ON
      GdcGene.geneID = GeneRef.gene_id ),
    --
    -- *Hg19*
    -- Now, we'll get the older hg19-based TCGA gene expression data that was generated
    -- by UNC using RSEM.  This table has ~228M rows and we're just going to extract
    -- the sample-barcode, the gene-symbol, the normalized-count, and the platform (since
    -- this data ws produced on two different platforms and this might be relevant later).
    -- As above, we will also create ranking of the expression values.
    Hg19 AS (
    SELECT
      SampleBarcode,
      HGNC_gene_symbol,
      normalized_count as RSEM_FPKM,
      DENSE_RANK() OVER (PARTITION BY HGNC_gene_symbol ORDER BY normalized_count ASC) AS rankRSEM,
      Platform
    FROM
      `isb-cgc.tcga_201607_beta.mRNA_UNC_RSEM`
    WHERE
      HGNC_gene_symbol IS NOT NULL ),
    --
    -- *JoinAndCorr*
    -- Finally, we join the two tables and compute correlations
    JoinAndCorr AS (
    SELECT
      hg38.geneID AS gene_id,
      hg38.gene_name AS gene_name,
      CORR(LOG10(hg38.HTSeq_FPKM+1),
        LOG10(hg19.RSEM_FPKM+1)) AS gexpPearsonCorr,
      CORR(hg38.rankHTSeq,
        hg19.rankRSEM) AS gexpSpearmanCorr
    FROM
      Hg19
    JOIN
      Hg38
    ON
      hg38.sampleID=hg19.SampleBarcode
      AND hg38.gene_name=hg19.HGNC_gene_symbol
    GROUP BY
      hg38.geneID,
      hg38.gene_name )
    --
    -- Lastly, we make one last select
    -- to get a difference between Pearson and Spearman correlations.
    SELECT
      gene_id,
      gene_name,
      gexpPearsonCorr,
      gexpSpearmanCorr,
      (gexpSpearmanCorr-gexpPearsonCorr) AS deltaCorr
    FROM
      JoinAndCorr
    WHERE
      IS_NAN(gexpSpearmanCorr) = FALSE
    ORDER BY
      gexpSpearmanCorr DESC

The results of any BigQuery query executed in the BigQuery web UI can easily be saved
to a table in case you want to perform follow-up queries on the result.  For example
we might want to ask what the distribution of the correlation coefficients produced
by the preceding query look like.  We can ask BigQuery to compute the deciles
on the saved results like this:

.. code-block:: sql

    SELECT
      APPROX_QUANTILES ( gexpPearsonCorr, 10 ) AS PearsonQ,
      APPROX_QUANTILES ( gexpSpearmanCorr, 10 ) AS SpearmanQ,
      APPROX_QUANTILES ( deltaCorr, 10 ) AS deltaQ
    FROM
      `<<insert your results table name here>>`

The result of the above query shows that 80% of genes have a Pearson correlation >= 0.84 and a
Spearman correlation >= 0.88, and that 80% of the time the difference between
these two correlations is between -0.012 and +0.098.  The median Pearson
correlation is nearly 0.93 and the median Spearman correlation is nearly 0.96.


Visualizations
--------------


.. figure:: query_figs/correlation_btw_hg19_hg38_v3.jpg
   :scale: 100
   :align: center

This plot shows the cumulative distribution of the Pearson correlation between
the hg19 RSEM expression and the hg38 HTSeq expression data.  Each point
represents one gene.

------------

.. figure:: query_figs/egfr_hg19_vs_hg38_v2.jpg
   :scale: 100
   :align: center

This plot shows the EGFR log10 expression, with the hg19 RSEM values on the x-axis and
the hg38 HTSeq values on the y-axis.  Note that overall, the difference between the RSEM
and HTSeq methods may have a more significant impact on the expression values than
the change in the genome build.

------------

.. figure:: query_figs/egfr_hg19_vs_hg38_ranked_v2.jpg
   :scale: 100
   :align: center

This plot shows the ranked EGFR expression, with the hg19 RSEM values on the x-axis
and the hg38 HTSeq values on the y-axis.




R Script
--------

Note that the latest version of the bigrquery package supports standard SQL, so make sure you're up to date.


.. code-block:: r

  library(devtools)
  devtools::install_github("rstats-db/bigrquery")

  library(bigrquery)
  library(ggplot2)
  library(stringr)

  # saving the above query as a string variable named 'q'

  res1 <- query_exec(q, project='isb-cgc-02-abcd', useLegacySql = FALSE)

  n <-  dim(res1)[1]
  ys <- c(0.5, 0.9, 0.95, 0.99)
  ls <- sapply(1:4, function(i) sum(res1$gexpPearsonCorr < ys[i]))

  qplot(x=1:n, y=sort(res1$gexpPearsonCorr)) + geom_line() +
  geom_hline(yintercept = ys, col='grey', lty=2) +
  geom_vline(xintercept = ls, col='grey', lty=2) +
  annotate(geom="text", label=ls[1], x=ls[1], y=0) +
  annotate(geom="text", label=ls[2], x=ls[2], y=0) +
  annotate(geom="text", label=ls[3], x=ls[3], y=0) +
  annotate(geom="text", label=ls[4], x=ls[4], y=0) +
  annotate(geom="text", label="50", y=ys[1], x=0) +
  annotate(geom="text", label="90", y=ys[2], x=0) +
  annotate(geom="text", label="95", y=ys[3], x=0) +
  annotate(geom="text", label="99", y=ys[4], x=0) +
  xlab("> 20K genes sorted by correlation value") +
  ylab("Pearson correlation between \nhg38.a.expFPKM and hg19.normalized_count") +
  ggtitle("Pearson correlation between \nhg38.a.expFPKM and hg19.normalized_count") +
  theme_bw() +
  theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
        panel.background = element_blank(), axis.line = element_line(colour = "black"))


  # As an exercise, you could make the above plot with Spearman's correlations.


  # Then let's take a look at one of our favorite genes, EGFR.

  q <- "
    WITH
    --
    Hg38 AS (
    SELECT
      SamplesSubmitterID AS sampleID,
      Ensembl_gene_ID AS geneID,
      DENSE_RANK() OVER (PARTITION BY Ensembl_gene_ID ORDER BY HTSeq__FPKM ASC) AS rankHTSeq,
      HTSeq__FPKM AS HTseq_FPKM
    FROM
      `isb-cgc.hg38_data_previews.TCGA_GeneExpressionQuantification`
    WHERE
      Ensembl_gene_ID = 'ENSG00000146648'),
    --
    Hg19 AS (
    SELECT
      SampleBarcode,
      HGNC_gene_symbol,
      normalized_count as RSEM_FPKM,
      DENSE_RANK() OVER (PARTITION BY HGNC_gene_symbol ORDER BY normalized_count ASC) AS rankRSEM,
      Platform
    FROM
      `isb-cgc.tcga_201607_beta.mRNA_UNC_RSEM`
    WHERE
      HGNC_gene_symbol = 'EGFR' )
    --
    -- *Join and Get Expr*
    SELECT
      hg38.geneID AS gene_id,
      hg19.HGNC_gene_symbol AS gene_name,
      LOG10(hg38.HTseq_FPKM+1) as Log10_hg38_HTSeq,
      LOG10(hg19.RSEM_FPKM+1) AS Log10_hg19_RSEM,
      rankRSEM,
      rankHTSeq
    FROM
      Hg19
    JOIN
      Hg38
    ON
      hg38.sampleID=hg19.SampleBarcode
    GROUP BY
      gene_id,
      gene_name,
      Log10_hg38_HTSeq,
      Log10_hg19_RSEM,
      rankRSEM,
      rankHTSeq"

  result <- query_exec(q, project="isb-cgc-02-abcd", useLegacySql=F)

  qplot(data=result, x=Log10_hg19_RSEM, y=Log10_hg38_HTSeq, main="EGFR, hg19 vs hg38, Pearson's = 0.93", xlab="Log10 RSEM hg19", ylab="Log10 HTSeq hg38")

  qplot(data=result, x=rankRSEM, y=rankHTSeq, main="EGFR, hg19 vs hg38, Spearman's = 0.96", xlab="Rank RSEM hg19", ylab="Rank HTSeq hg38")

  # As an exercise, try plotting some other genes. Maybe genes
  # with both high and low correlations. What do you notice?

------------

Let us know if you're having trouble! We're here to help.

**Additional Resources:**

- ISB-CGC `examples-R <https://github.com/isb-cgc/examples-R>`_ github repo
- ISB-CGC :ref:`R-workshop` workshop material
- BigQuery web UI `quickstart <https://cloud.google.com/bigquery/quickstart-web-ui>`_
- BigQuery 101 `video <https://www.youtube.com/watch?v=kKBnFsNWwYM>`_
- Fun with a Petabyte: Pushing the limits of Google BigQuery `video <https://www.youtube.com/watch?v=6Nv18xmJirs>`_
