WITH
barcodes AS (
SELECT
  project_short_name AS label,
  sample_barcode_tumor,
  'x' AS Hugo_Symbol,
  'x' AS Variant_Classification,
  'x' AS Variant_Type
FROM
  `isb-cgc.TCGA_hg38_data_v0.Somatic_Mutation_DR10`
WHERE
  project_short_name IN ('TCGA-COAD',
    'TCGA-PAAD')
GROUP BY
  project_short_name,
  sample_barcode_tumor
),
mutations AS (
select
  project_short_name as label, 
  sample_barcode_tumor,
  Hugo_Symbol,
  CONCAT(Hugo_Symbol, ' ', Variant_Classification) as Variant_Classification,
  CONCAT(Hugo_Symbol, ' ', Variant_Type) AS Variant_Type
from
  `isb-cgc.TCGA_hg38_data_v0.Somatic_Mutation_DR10`
WHERE
  project_short_name IN ('TCGA-COAD','TCGA-PAAD')
	and Hugo_Symbol = 'TTN'  
GROUP BY
  project_short_name, 
  sample_barcode_tumor,
  Hugo_Symbol,
  Variant_Classification,
  Variant_Type
)
select
  b.label,
  b.sample_barcode_tumor,
  m.Hugo_Symbol,
  m.Variant_Classification,
  m.Variant_Type
FROM
  barcodes b
LEFT JOIN
  mutations m
ON
  b.sample_barcode_tumor = m.sample_barcode_tumor AND
  b.label = m.label
WHERE
  b.sample_barcode_tumor = 'TCGA-AD-6965-01A'
GROUP BY
  label, 
  sample_barcode_tumor,
  m.Hugo_Symbol,
  m.Variant_Classification,
  m.Variant_Type




  Row label sample_barcode_tumor  Hugo_Symbol Variant_Classification  Variant_Type   
1 TCGA-COAD TCGA-AD-6965-01A  null  null  null


But if you select a tumor with a mutation in ttn you get: 
1 TCGA-COAD TCGA-AA-3955-01A  TTN TTN In_Frame_Del  TTN DEL  
2 TCGA-COAD TCGA-AA-3955-01A  TTN TTN Nonsense_Mutation TTN SNP  
3 TCGA-COAD TCGA-AA-3955-01A  TTN TTN Intron  TTN SNP



WITH
  barcodes AS (
  SELECT
    project_short_name AS label,
    sample_barcode_tumor,
    'x' AS Hugo_Symbol,
    'x' AS Variant_Classification,
    'x' AS Variant_Type
  FROM
    `isb-cgc.TCGA_hg38_data_v0.Somatic_Mutation_DR10`
  WHERE
    project_short_name IN ('TCGA-COAD',
      'TCGA-PAAD')
  GROUP BY
    project_short_name,
    sample_barcode_tumor ),
    
    
  kras_mutations AS (
  SELECT
    project_short_name AS label,
    sample_barcode_tumor,
    Hugo_Symbol,
    CONCAT(Hugo_Symbol, ' ', Variant_Classification) AS Variant_Classification,
    CONCAT(Hugo_Symbol, ' ', Variant_Type) AS Variant_Type
  FROM
    `isb-cgc.TCGA_hg38_data_v0.Somatic_Mutation_DR10`
  WHERE
    project_short_name IN ('TCGA-COAD',
      'TCGA-PAAD')
    AND Hugo_Symbol = 'KRAS'
  GROUP BY
    project_short_name,
    sample_barcode_tumor,
    Hugo_Symbol,
    Variant_Classification,
    Variant_Type ),

    
kras_join AS (
  SELECT
    IF(b.label = 'TCGA-COAD',
      1,
      0) label,
    b.sample_barcode_tumor barcode,
    IFNULL(m.Hugo_Symbol,
      'notkras') kras,
    IFNULL(m.Variant_Classification,
      'notkras') krasvarclass,
    IFNULL(m.Variant_Type,
      'notkras') krasvartype
  FROM
    barcodes b
  LEFT JOIN
    kras_mutations m
  ON
    b.sample_barcode_tumor = m.sample_barcode_tumor
    AND b.label = m.label
  GROUP BY
    b.label,
    b.sample_barcode_tumor,
    m.Hugo_Symbol,
    m.Variant_Classification,
    m.Variant_Type ),
    
    
  ttn_mutations AS (
  SELECT
    project_short_name AS label,
    sample_barcode_tumor,
    Hugo_Symbol,
    CONCAT(Hugo_Symbol, ' ', Variant_Classification) AS Variant_Classification,
    CONCAT(Hugo_Symbol, ' ', Variant_Type) AS Variant_Type
  FROM
    `isb-cgc.TCGA_hg38_data_v0.Somatic_Mutation_DR10`
  WHERE
    project_short_name IN ('TCGA-COAD',
      'TCGA-PAAD')
    AND Hugo_Symbol = 'TTN'
  GROUP BY
    project_short_name,
    sample_barcode_tumor,
    Hugo_Symbol,
    Variant_Classification,
    Variant_Type ),
    
ttn_join AS (
  SELECT
    IF(b.label = 'TCGA-COAD',
      1,
      0) label,
    b.sample_barcode_tumor barcode,
    IFNULL(m.Hugo_Symbol,
      'nottn') ttn,
    IFNULL(m.Variant_Classification,
      'nottn') ttnvarclass,
    IFNULL(m.Variant_Type,
      'nottn') ttnvartype
  FROM
    barcodes b
  LEFT JOIN
    ttn_mutations m
  ON
    b.sample_barcode_tumor = m.sample_barcode_tumor
    AND b.label = m.label
  GROUP BY
    b.label,
    b.sample_barcode_tumor,
    m.Hugo_Symbol,
    m.Variant_Classification,
    m.Variant_Type )
    
    
SELECT
  k.label,
  k.barcode,
  ttn,
  ttnvarclass,
  ttnvartype,
  kras,
  krasvarclass,
  krasvartype
FROM
  kras_join k
JOIN 
  ttn_join t
ON
  k.label = t.label
  AND k.barcode = t.barcode



#standardSQL
CREATE MODEL `tcga_model_1.ttn_kras`
OPTIONS(
model_type='logistic_reg', l1_reg=1, l2_reg=1
) AS
SELECT
  label,
  ttn,
  ttnvarclass,
  ttnvartype,
  kras,
  krasvarclass,
  krasvartype
FROM
  `isb-cgc-02-0001.tcga_model_1.mut_table_ttn_kras`



  #standardSQL
SELECT
  *
FROM
  ML.EVALUATE(MODEL `tcga_model_1.ttn_kras`, (
SELECT
  label,
  ttn,
  ttnvarclass,
  ttnvartype,
  kras,
  krasvarclass,
  krasvartype
FROM
  `isb-cgc-02-0001.tcga_model_1.mut_table_ttn_kras`
WHERE
  RAND() < 0.5
  )
 )



SELECT
  category_weights
FROM
  ML.WEIGHTS(MODEL `tcga_model_1.ttn_kras`)




Row category_weights.category category_weights.weight  
1 nottn -0.23884652863687242   
TTN 0.49111909865193015  

2 TTN In_Frame_Ins  0.0  
TTN In_Frame_Del  0.0  
TTN Splice_Region 0.0  
TTN 3'UTR 0.0  
TTN Splice_Site 0.40338272595163427  
TTN Frame_Shift_Ins 0.37119878322531497  
nottn -0.23884652863687242   
TTN Nonsense_Mutation 0.2918686251062693   
TTN Missense_Mutation 0.44399718858536585  
TTN Frame_Shift_Del 0.533441637809594  
TTN Silent  0.42323474183893695  
TTN Intron  0.4542574199580538

3 TTN SNP 0.4621085151337503   
TTN DEL 0.5267357497107026   
nottn -0.23884652863687242   
TTN INS 0.5157001582798476   

4 notkras 0.41473245542848153  
KRAS  0.056467886952900635   

5 KRAS Missense_Mutation  0.0  
KRAS 3'UTR  0.24824365003763124  
KRAS Silent 0.37235076199926104  
notkras 0.41473245542848153  
KRAS Nonsense_Mutation  0.15718071796738442  

6 KRAS SNP  0.023795845825705292   
KRAS INS  0.30656303031324383  
notkras 0.41473245542848153  
KRAS DEL  0.10449786543331513

