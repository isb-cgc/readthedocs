

-- BQ examples - WebEx Workshop Sept 22, 2016


-- 1 -- basic query
select
  -- from the schema
  CCLE_name,
  count( CCLE_name ) as mut_cnt
from
  -- from the details
  [isb-cgc:ccle_201602_alpha.Mutation_calls]
where
  -- from schema, linked with ANDs
  Hugo_Symbol = 'MTOR'
group by
  -- the results are grouped by these variables
  CCLE_name
order by
  mut_cnt DESC


-- 2 -- string functions
select
  CCLE_name,
  count( CCLE_name ) as mut_cnt
from
  [isb-cgc:ccle_201602_alpha.Mutation_calls]
where
  -- string matching
  GO_Biological_Process CONTAINS 'GO:0002376'  -- immune system process
group by
  CCLE_name
order by
  mut_cnt DESC


-- 3 -- string functions group by example
select
  CCLE_name,
  -- now we'll add the gene symbol
  Hugo_Symbol,
  count( CCLE_name ) as mut_cnt
from
  [isb-cgc:ccle_201602_alpha.Mutation_calls]
where
  GO_Biological_Process CONTAINS 'GO:0002376'
group by
  CCLE_name,
  -- and we add it to the group by list
  Hugo_Symbol
order by
  mut_cnt DESC


-- 4 -- joining tables

select
  a.Hugo_Symbol,
  a.Genome_Change,
  avg( b.RMA_normalized_expression ) as avg_expr
from
  [isb-cgc:ccle_201602_alpha.Mutation_calls] as a
join
  [isb-cgc:ccle_201602_alpha.AffyU133_RMA_expression] as b
on
  a.CCLE_name = b.CCLE_name
where
  a.Hugo_Symbol = 'MCM3AP' AND
  b.HGNC_gene_symbol = 'MCM3AP'
group by
  a.Genome_Change,
  a.Hugo_Symbol
order by
  avg_expr

-- 5 how to compare gene expression with mutation and without.

-- first the cell lines that *do not* have a mutation in MCM3AP

SELECT
  CCLE_name
FROM
  [isb-cgc:ccle_201602_alpha.Mutation_calls]
WHERE
  CCLE_name NOT IN (
  SELECT
    CCLE_name
  FROM
    [isb-cgc:ccle_201602_alpha.Mutation_calls]
  WHERE
    Hugo_Symbol = 'MCM3AP' )
GROUP BY
  CCLE_name

-- next, the avg expression for cell lines without a MCM3AP mutation

SELECT
  HGNC_gene_symbol,
  count(CCLE_name) as cell_line_count,
  AVG(RMA_normalized_expression) AS avg_expr,
  STDDEV( RMA_normalized_expression) AS sd_expr
FROM
  [isb-cgc:ccle_201602_alpha.AffyU133_RMA_expression]
WHERE
  HGNC_gene_symbol = 'MCM3AP' AND
  CCLE_name IN (
  SELECT
    CCLE_name
  FROM
    [isb-cgc:ccle_201602_alpha.Mutation_calls]
  WHERE
    CCLE_name NOT IN (
    SELECT
      CCLE_name
    FROM
      [isb-cgc:ccle_201602_alpha.Mutation_calls]
    WHERE
      Hugo_Symbol = 'MCM3AP' )
  GROUP BY
    CCLE_name )
GROUP BY
  HGNC_gene_symbol

--  MCM3AP	666	7.058598444444444	0.5428160667085511

-- now let's make a couple changes, and get expression for CLs with a mutation
SELECT
  HGNC_gene_symbol,
  count(CCLE_name) as cell_line_count,
  AVG(RMA_normalized_expression) AS avg_expr,
  STDDEV( RMA_normalized_expression) AS sd_expr
FROM
  [isb-cgc:ccle_201602_alpha.AffyU133_RMA_expression]
WHERE
  HGNC_gene_symbol = 'MCM3AP' AND
  CCLE_name IN (
  SELECT
    CCLE_name
  FROM
    [isb-cgc:ccle_201602_alpha.Mutation_calls]
  WHERE
    CCLE_name NOT IN (
    SELECT
      CCLE_name
    FROM
      [isb-cgc:ccle_201602_alpha.Mutation_calls]
    WHERE
      Hugo_Symbol = 'MCM3AP' )
  GROUP BY
    CCLE_name )
GROUP BY
  HGNC_gene_symbol


--   MCM3AP	187 7.148790727272728	0.514342611529676


-- 6 -- using conditionals

-- Let's try another way:
-- build a subtable separating the cell lines
SELECT
  CCLE_name,
  IF (Hugo_Symbol CONTAINS 'MCM3AP', 1, 0) AS has_mut,
  IF (NOT Hugo_Symbol CONTAINS 'MCM3AP', 1, 0) AS non_mut,
from
  [isb-cgc:ccle_201602_alpha.Mutation_calls]
GROUP BY
  CCLE_name,
  has_mut,
  non_mut

-- that's fine, but we really want one row per cell line ...
SELECT
  CCLE_name,
  SUM(has_mut) AS has_mut_sum,
  SUM(non_mut) AS non_mut_sum,
FROM (
  SELECT
    CCLE_name,
    IF (Hugo_Symbol CONTAINS 'MCM3AP', 1, 0) AS has_mut,
    IF (NOT Hugo_Symbol CONTAINS 'MCM3AP', 1, 0) AS non_mut,
  FROM
    [isb-cgc:ccle_201602_alpha.Mutation_calls]
  GROUP BY
    CCLE_name,
    has_mut,
    non_mut )
GROUP BY
  CCLE_name


-- 7 -- making 2x2 tables
SELECT
  table_cell,
  COUNT(*) AS n
FROM (
  SELECT (
    CASE
      WHEN gender = 'MALE' AND hpv_status = 'Positive' THEN 'Male_and_HPV_Pos'
      WHEN gender = 'MALE' AND hpv_status = 'Negative' THEN 'Male_and_HPV_Neg'
      WHEN gender = 'FEMALE' AND hpv_status = 'Positive' THEN 'Female_and_HPV_Pos'
      WHEN gender = 'FEMALE' AND hpv_status = 'Negative' THEN 'Female_and_HPV_Neg'
      ELSE 'None'
    END ) AS table_cell,
  FROM
    [isb-cgc:tcga_201607_beta.Clinical_data]
  WHERE
    Study IN ('CESC',
      'HNSC')
  HAVING
    table_cell <> 'None' )
GROUP BY
  table_cell
ORDER BY
  n DESC


-- 8 -- calculations
SELECT
  ParticipantBarcode,
  Study,
  gender,
  country,
  number_pack_years_smoked,
  (number_pack_years_smoked - mu) / sd AS z
FROM
  [isb-cgc:tcga_201607_beta.Clinical_data] AS a
JOIN (
  SELECT
    vital_status,
    AVG(number_pack_years_smoked) AS mu,
    STDDEV(number_pack_years_smoked) AS sd
  FROM
    [isb-cgc:tcga_201607_beta.Clinical_data]
  WHERE
    vital_status = 'Alive'
  GROUP BY
    vital_status ) AS b
ON
  a.vital_status = b.vital_status
ORDER BY
  z DESC
