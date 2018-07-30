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
	and Hugo_Symbol = 'APC'  
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


But if you select a tumor with a mutation in APC you get: 
1 TCGA-COAD TCGA-AA-3955-01A  APC APC In_Frame_Del  APC DEL  
2 TCGA-COAD TCGA-AA-3955-01A  APC APC Nonsense_Mutation APC SNP  
3 TCGA-COAD TCGA-AA-3955-01A  APC APC Intron  APC SNP



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
    
    
  APC_mutations AS (
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
    AND Hugo_Symbol = 'APC'
  GROUP BY
    project_short_name,
    sample_barcode_tumor,
    Hugo_Symbol,
    Variant_Classification,
    Variant_Type ),
    
APC_join AS (
  SELECT
    IF(b.label = 'TCGA-COAD',
      1,
      0) label,
    b.sample_barcode_tumor barcode,
    IFNULL(m.Hugo_Symbol,
      'noAPC') APC,
    IFNULL(m.Variant_Classification,
      'noAPC') APCvarclass,
    IFNULL(m.Variant_Type,
      'noAPC') APCvartype
  FROM
    barcodes b
  LEFT JOIN
    APC_mutations m
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
  APC,
  APCvarclass,
  APCvartype,
  kras,
  krasvarclass,
  krasvartype
FROM
  kras_join k
JOIN 
  APC_join t
ON
  k.label = t.label
  AND k.barcode = t.barcode



#standardSQL
CREATE MODEL `tcga_model_1.APC_kras`
OPTIONS(
model_type='logistic_reg', l1_reg=1, l2_reg=1
) AS
SELECT
  label,
  APC,
  APCvarclass,
  APCvartype,
  kras,
  krasvarclass,
  krasvartype
FROM
  `isb-cgc-02-0001.tcga_model_1.apc_kras`



  #standardSQL
SELECT
  *
FROM
  ML.EVALUATE(MODEL `tcga_model_1.APC_kras`, (
SELECT
  label,
  APC,
  APCvarclass,
  APCvartype,
  kras,
  krasvarclass,
  krasvartype
FROM
  `isb-cgc-02-0001.tcga_model_1.apc_kras`
WHERE
  RAND() < 0.5
  )
 )


Row precision recall  accuracy  f1_score  log_loss  roc_auc  
1 0.9157894736842105  0.9525547445255474  0.8969359331476323  0.9338103756708408  0.24094283986742546 0.915529  


SELECT
  category_weights
FROM
  ML.WEIGHTS(MODEL `tcga_model_1.APC_kras`)




Row category_weights.category category_weights.weight  
1 APC 0.9544645619866424   
noAPC -0.5478639995975051  
2 APC Splice_Site 0.0  
APC Missense_Mutation 0.0  
APC Silent  0.0  
noAPC -0.5478639995975051  
APC Frame_Shift_Ins 0.7843682351259976   
APC Nonsense_Mutation 0.8994029016067709   
APC Frame_Shift_Del 0.8513666758601293   
3 APC SNP 0.8319524760364977   
APC INS 0.805845479466635  
noAPC -0.5478639995975051  
APC DEL 0.8513666758601293   
4 notkras 0.5987086486843087   
KRAS  0.10426690050094438 