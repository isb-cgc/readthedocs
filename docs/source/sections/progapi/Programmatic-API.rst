***********************
Programmatic Interfaces
***********************

Programmatic access to molecular data in BigQuery, Google Cloud Storage, or Google Genomics
is based directly on the interfaces provided by the Google Cloud Platform, as 
illustrated throughout the 
`ISB-CGC code repositories on github <https://github.com/isb-cgc>`_.

In order to query the ISB-CGC metadata or to get information such as details regarding a
cohort that a user may have saved during an interactive session, a series of APIs based 
on Google Cloud Endpoints have been defined.  Details about these APIs can be found here.

The Google 
`APIs Explorer <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/>`_
can be used to see each API and try it out through your web browser. Each API may bundle several endpoints that are functionally related.

Cohorts are the primary organizing principle for subsetting and working with the TCGA data.  
A cohort is a list of samples (identified using the 16-character TCGA sample barcode).  Users may
create and share cohorts using the ISB-CGC web-app and then programmatically access these cohorts
using this API.

The Cohort API currently bundles several different cohort-related endpoints:

patient_details 
###############

Returns information about a specific participant, including a list of samples and aliquots derived from this patient. Takes a participant barcode (of length 12, *eg* TCGA-B9-7268) as a required parameter. User does not need to be authenticated.

**Access control:** To call this method, you must have the following
roles:

-  None

Request

HTTP request

GET https://api-dot-isb-cgc.appspot.com/\_ah/api/cohort\_api/v1/patient\_details

Parameters

+-----------------------+-------------+--------------------------------------------------------------+
| **Parameter name**    | **Value**   | **Description**                                              |
+=======================+=============+==============================================================+
| **Path parameters**   |             |                                                              |
+-----------------------+-------------+--------------------------------------------------------------+
| patient\_barcode      | string      | Barcode of the patient to get information about. Required.   |
+-----------------------+-------------+--------------------------------------------------------------+

Response

If successful, this method returns a response body with the following
structure: ::

{

"kind": "cohort\_api#cohortsItem",

"aliquots": [*string*],

"clinical\_data": {

    "ParticipantBarcode": *string*,

    "Project": *string*,

    "Study": *string*,

    "age\_at\_initial\_pathologic\_diagnosis": *string*,

    "anatomic\_neoplasm\_subdivision": *string*,

    "batch\_number": *string*,

    "bcr": *string*,

    "clinical\_M": *string*,

    "clinical\_N": *string*,

    "clinical\_T": *string*,

    "clinical\_stage": *string*,

    "colorectal\_cancer": *string*,

    "country": *string*,

    "days\_to\_birth": *string*,

    "days\_to\_initial\_pathologic\_diagnosis": *string*,

    "days\_to\_last\_followup": *string*,

    "ethnicity": *string*,

    "frozen\_specimen\_anatomic\_site": *string*,

    "gender": *string*,

    "histological\_type": *string*,

    "history\_of\_colon\_polyps": *string*,

    "history\_of\_neoadjuvant\_treatment": *string*,

    "history\_of\_prior\_malignancy": *string*,

    "hpv\_calls": *string*,

    "hpv\_status": *string*,

    "icd\_10": *string*,

    "icd\_o\_3\_histology": *string*,

    "icd\_o\_3\_site": *string*,

    "lymphatic\_invasion": *string*,

    "lymphnodes\_examined": *string*,

    "lymphovascular\_invasion\_present": *string*,

    "menopause\_status": *string*,

    "mononucleotide\_and\_dinucleotide\_marker\_panel\_analysis\_status":
    *string*,

    "mononucleotide\_marker\_panel\_analysis\_status": *string*,

    "neoplasm\_histologic\_grade": *string*,,

    "new\_tumor\_event\_after\_initial\_treatment": *string*,

    "number\_of\_lymphnodes\_examined": *string*,

    "number\_of\_lymphnodes\_positive\_by\_he": *string*,

    "pathologic\_M": *string*,

    "pathologic\_N": *string*,

    "pathologic\_T": *string*,

    "pathologic\_stage": *string*,

    "person\_neoplasm\_cancer\_status": *string*,

    "pregnancies": *string*,

    "primary\_neoplasm\_melanoma\_dx": *string*,

    "primary\_therapy\_outcome\_success": *string*,

    "prior\_dx": *string*,

    "race": *string*,

    "residual\_tumor": *string*,

    "tobacco\_smoking\_history": *string*,

    "tumor\_tissue\_site": *string*,

    "tumor\_type": *string*,

    "vital\_status": *string*,

    "weiss\_venous\_invasion": *string*,

    "year\_of\_initial\_pathologic\_diagnosis": *string*

},

"samples": [],

}

+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Property name**                                                                   | **Value**                 | **Description**                                                                                                                                                    |
+=====================================================================================+===========================+====================================================================================================================================================================+
| kind                                                                                | cohort\_api#cohortsItem   | The resource type.                                                                                                                                                 |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| aliquots[]                                                                          | list                      | List of barcodes of aliquots taken from this participant.                                                                                                          |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data                                                                      | nested object             | The clinical data about the participant.                                                                                                                           |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.ParticipantBarcode                                                   | string                    | Participant barcode.                                                                                                                                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.Project                                                              | string                    | Project name, .eg. “TCGA”.                                                                                                                                         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.Study                                                                | string                    | Tumor type abbreviation, e.g. “BRCA”.                                                                                                                              |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.age\_at\_initial\_pathologic\_diagnosis                              | string                    | Age at which a condition or disease was first diagnosed in years.                                                                                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.anatomic\_neoplasm\_subdivision                                      | string                    | Text term to describe the spatial location, subdivisions and/or anatomic site name of a tumor.                                                                     |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.batch\_number                                                        | string                    | Groups samples by the batch they were processed in.                                                                                                                |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.bcr                                                                  | string                    | Biospecimen core resource, e.g. "Nationwide Children's Hospital”, “Washington University".                                                                         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.clinical\_M                                                          | string                    | Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.                      |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.clinical\_N                                                          | string                    | Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.clinical\_T                                                          | string                    | Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.                                         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.clinical\_stage                                                      | string                    | Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis for cancer.   |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.colorectal\_cancer                                                   | string                    | Text term to signify whether a patient has been diagnosed with colorectal cancer.                                                                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.country                                                              | string                    | Text to identify the name of the state, province, or country in which the sample was procured.                                                                     |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.days\_to\_birth                                                      | string                    | Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days.                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.days\_to\_initial\_pathologic\_diagnosis                             | string                    | Numeric value to represent the day of an individual's initial pathologic diagnosis of cancer.                                                                      |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.days\_to\_last\_followup                                             | string                    | Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days.                              |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.ethnicity                                                            | string                    | The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories.                                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.frozen\_specimen\_anatomic\_site                                     | string                    | Text description of the origin and the anatomic site regarding the frozen biospecimen tumor tissue sample.                                                         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.gender                                                               | string                    | Text designations that identify gender.                                                                                                                            |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.histological\_type                                                   | string                    | Text term for the structural pattern of cancer cells used to define a microscopic diagnosis.                                                                       |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.history\_of\_colon\_polyps                                           | string                    | Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report(s).              |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.history\_of\_neoadjuvant\_treatment                                  | string                    | Text term to describe the patient's history of neoadjuvant treatment and the kind of treament given prior to resection of the tumor.                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.history\_of\_prior\_malignancy                                       | string                    | Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence.                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.hpv\_calls                                                           | string                    | Results of HPV tests.                                                                                                                                              |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.hpv\_status                                                          | string                    | Current HPV status.                                                                                                                                                |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.icd\_10                                                              | string                    | The tenth version of the International Classification of Disease (ICD).                                                                                            |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.icd\_o\_3\_histology                                                 | string                    | The third edition of the International Classification of Diseases for Oncology.                                                                                    |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.icd\_o\_3\_site                                                      | string                    | The third edition of the International Classification of Diseases for Oncology.                                                                                    |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.lymphatic\_invasion                                                  | string                    | A yes/no indicator to ask if malignant cells are present in small or thin-walled vessels suggesting lymphatic involvement.                                         |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.lymphnodes\_examined                                                 | string                    | The yes/no/unknown indicator whether a lymph node assessment was performed at the primary presentation of disease.                                                 |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.lymphovascular\_invasion\_present                                    | string                    | The yes/no indicator to ask if large vessel (vascular) invasion or small, thin-walled (lymphatic) invasion was detected in a tumor specimen.                       |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.menopause\_status                                                    | string                    | Text term to signify the status of a woman's menopause, the permanent cessation of menses, usually defined by 6 to 12 months of amenorrhea.                        |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.mononucleotide\_and\_dinucleotide\_marker\_panel\_analysis\_status   | string                    | Text result of microsatellite instability (MSI) testing at using a mononucleotide and dinucleotide microsatellite panel.                                           |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.mononucleotide\_marker\_panel\_analysis\_status                      | string                    | Text result of microsatellite instability (MSI) testing using a mononucleotide microsatellite panel.                                                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.neoplasm\_histologic\_grade                                          | string                    | Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness.                                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.new\_tumor\_event\_after\_initial\_treatment                         | string                    | Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment.                                                          |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.number\_of\_lymphnodes\_examined                                     | string                    | The total number of lymph nodes removed and pathologically assessed for disease.                                                                                   |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.number\_of\_lymphnodes\_positive\_by\_he                             | string                    | Numeric value to signify the count of positive lymph nodes identified through hematoxylin and eosin (H&E) staining light microscopy.                               |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.pathologic\_M                                                        | string                    | Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the reg...           |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.pathologic\_N                                                        | string                    | The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cance...          |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.pathologic\_stage                                                    | string                    | The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria.                |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.pathologic\_T                                                        | string                    | Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American ...           |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.person\_neoplasm\_cancer\_status                                     | string                    | The state or condition of an individual's neoplasm at a particular point in time.                                                                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.pregnancies                                                          | string                    | Value to describe the number of full-term pregnancies that a woman has experienced.                                                                                |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.primary\_neoplasm\_melanoma\_dx                                      | string                    | Text indicator to signify whether a person had a primary diagnosis of melanoma.                                                                                    |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.primary\_therapy\_outcome\_success                                   | string                    | Measure of Success                                                                                                                                                 |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.prior\_dx                                                            | string                    | Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence.                                  |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.race                                                                 | string                    | The text for reporting information about race based on the Office of Management and Budget (OMB) categories.                                                       |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.residual\_tumor                                                      | string                    | Text terms to describe the status of a tissue margin following surgical resection.                                                                                 |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.tobacco\_smoking\_history                                            | string                    | Category describing current smoking status and smoking history as self-reported by a patient.                                                                      |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.tumor\_tissue\_site                                                  | string                    | Text term that describes the anatomic site of the tumor or disease.                                                                                                |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.tumor\_type                                                          | string                    | Text term to identify the morphologic subtype of papillary renal cell carcinoma.                                                                                   |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.vital\_status                                                        | string                    | The survival state of the person registered on the protocol.                                                                                                       |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.weiss\_venous\_invasion                                              | string                    | The result of an assessment using the Weiss histopathologic criteria.                                                                                              |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_data.year\_of\_initial\_pathologic\_diagnosis                             | string                    | Numeric value to represent the year of an individual’s initial pathologic diagnosis of cancer.                                                                     |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| samples[]                                                                           | list                      | List of barcodes of samples taken from this participant.                                                                                                           |
+-------------------------------------------------------------------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+



sample_details
##############

given a sample barcode (of length 16, *eg* TCGA-B9-7268-01A), this endpoint returns all available "biospecimen" information about this sample, the associated patient barcode, a list of associated aliquots, and a list of "data_details" blocks describing each of the data files associated with this sample

Returns information about a specific sample. Takes a sample barcode as a
required parameter. User does not need to be authenticated.

**Access control:** To call this method, you must have the following
roles:

-  None

Request

HTTP request

GET https://api-dot-isb-cgc.appspot.com/\_ah/api/cohort\_api/v1/sample\_details

Parameters

+-----------------------+-------------+-------------------------------------------------------------+
| **Parameter name**    | **Value**   | **Description**                                             |
+=======================+=============+=============================================================+
| **Path parameters**   |             |                                                             |
+-----------------------+-------------+-------------------------------------------------------------+
| sample\_barcode       | string      | Barcode of the sample to get information about. Required.   |
+-----------------------+-------------+-------------------------------------------------------------+

Response

If successful, this method returns a response body with the following
structure:

{

"kind": "cohort\_api#cohortsItem",

"aliquots": [*string*],

"biospecimen\_data": {

    "ParticipantBarcode": *string*,

    "Project": *string*,

    "SampleBarcode": *string*,

    "Study": *string*,

    "avg\_percent\_lymphocyte\_infiltration": *integer*,

    "avg\_percent\_monocyte\_infiltration": *integer*,

    "avg\_percent\_necrosis": *integer*,

    "avg\_percent\_neutrophil\_infiltration": *integer*,

    "avg\_percent\_normal\_cells": *integer*,

    "avg\_percent\_stromal\_cells": *integer*,

    "avg\_percent\_tumor\_cells": *integer*,

    "avg\_percent\_tumor\_nuclei": *integer*,

    "batch\_number": *string*,

    "bcr": *string*,

    "days\_to\_collection": *string*,

    "max\_percent\_lymphocyte\_infiltration": *string*,

    "max\_percent\_monocyte\_infiltration": *string*,

    "max\_percent\_necrosis": *string*,

    "max\_percent\_neutrophil\_infiltration": *string*,

    "max\_percent\_normal\_cells": *string*,

    "max\_percent\_stromal\_cells": *string*,

    "max\_percent\_tumor\_cells": *string*,

    "max\_percent\_tumor\_nuclei": *string*,

    "min\_percent\_lymphocyte\_infiltration": *string*,

    "min\_percent\_monocyte\_infiltration": *string*,

    "min\_percent\_necrosis": *string*,

    "min\_percent\_neutrophil\_infiltration": *string*,

    "min\_percent\_normal\_cells": *string*,

    "min\_percent\_stromal\_cells": *string*,

    "min\_percent\_tumor\_cells": *string*,

    "min\_percent\_tumor\_nuclei": *string*

},

"data\_details": [

    {

    "CloudStoragePath": *string*,

    "DataCenterName": *string*,

    "DataCenterType": *string*,

    "DataFileName": *string*,

    "DataFileNameKey": *string*,

    "DataLevel": *string*,

    "DatafileUploaded": *string*,

    "Datatype": *string*,

    "GenomeReference": *string*,

    "Pipeline": *string*,

    "Platform": *string*,

    "Project": *string*,

    "Repository": *string*,

    "SDRFFileName": *string*,

    "SampleBarcode": *string*,

    "SecurityProtocol": *string*,

    "platform\_full\_name": *string*

    },

],

"data\_details\_count": *string*,

"patient": *string*

}



+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Property name**                                          | **Value**                 | **Description**                                                                                                                                                                                                                  |
+============================================================+===========================+==================================================================================================================================================================================================================================+
| kind                                                       | cohort\_api#cohortsItem   | The resource type.                                                                                                                                                                                                               |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| aliquots[]                                                 | list                      | List of barcodes of aliquots taken from this participant.                                                                                                                                                                        |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data                                          | nested object             | Biospecimen data about the sample.                                                                                                                                                                                               |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.ParticipantBarcode                       | string                    | Participant barcode.                                                                                                                                                                                                             |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.Project                                  | string                    | Project name, .eg. “TCGA”.                                                                                                                                                                                                       |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.SampleBarcode                            | string                    | Sample barocde.                                                                                                                                                                                                                  |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.Study                                    | string                    | Tumor type abbreviation, e.g. “BRCA”.                                                                                                                                                                                            |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.avg\_percent\_lymphocyte\_infiltration   | integer                   | Average percent lymphocyte infiltration.                                                                                                                                                                                         |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.avg\_percent\_monocyte\_infiltration     | integer                   | Average percent monocyte infiltration.                                                                                                                                                                                           |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.avg\_percent\_necrosis                   | integer                   | Average percent necrosis.                                                                                                                                                                                                        |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.avg\_percent\_neutrophil\_infiltration   | integer                   | Average percent neutrophil infiltration.                                                                                                                                                                                         |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.avg\_percent\_normal\_cells              | integer                   | Average percent normal cells.                                                                                                                                                                                                    |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.avg\_percent\_stromal\_cells             | integer                   | Average percent stromal cells.                                                                                                                                                                                                   |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.avg\_percent\_tumor\_cells               | integer                   | Average percent tumor cells.                                                                                                                                                                                                     |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.avg\_percent\_tumor\_nuclei              | integer                   | Average percent tumor nuclei.                                                                                                                                                                                                    |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.batch\_number                            | string                    | Batch number in which the sample was processed.                                                                                                                                                                                  |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.bcr                                      | string                    | Biospecimen core resource, e.g. "Nationwide Children's Hospital”, “Washington University".                                                                                                                                       |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.days\_to\_collection                     | string                    | Days to collection.                                                                                                                                                                                                              |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.max\_percent\_lymphocyte\_infiltration   | string                    | Maximum percent lymphocyte infiltration.                                                                                                                                                                                         |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.max\_percent\_monocyte\_infiltration     | string                    | Maximum percent monocyte infiltration                                                                                                                                                                                            |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.max\_percent\_necrosis                   | string                    | Maximum percent necrosis.                                                                                                                                                                                                        |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.max\_percent\_neutrophil\_infiltration   | string                    | Maximum percent neutrophil infiltration.                                                                                                                                                                                         |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.max\_percent\_normal\_cells              | string                    | Maximum percent normal cells.                                                                                                                                                                                                    |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.max\_percent\_stromal\_cells             | string                    | Maximum percent stromal cells.                                                                                                                                                                                                   |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.max\_percent\_tumor\_cells               | string                    | Maximum percent tumor cells.                                                                                                                                                                                                     |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.max\_percent\_tumor\_nuclei              | string                    | Maximum percent tumor nuclei.                                                                                                                                                                                                    |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.min\_percent\_lymphocyte\_infiltration   | string                    | Minimum percent lymphocyte infiltration.                                                                                                                                                                                         |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.min\_percent\_monocyte\_infiltration     | string                    | Minimum percent monocyte infiltration.                                                                                                                                                                                           |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.min\_percent\_necrosis                   | string                    | Minimum percent necrosis.                                                                                                                                                                                                        |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.min\_percent\_neutrophil\_infiltration   | string                    | Minimum percent neutrophil infiltration.                                                                                                                                                                                         |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.min\_percent\_normal\_cells              | string                    | Minimum percent normal cells.                                                                                                                                                                                                    |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.min\_percent\_stromal\_cells             | string                    | Minimum percent stromal cells.                                                                                                                                                                                                   |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.min\_percent\_tumor\_cells               | string                    | Minimum percent tumor cells.                                                                                                                                                                                                     |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| biospecimen\_data.min\_percent\_tumor\_nuclei              | string                    | Minimum percent tumor nuclei.                                                                                                                                                                                                    |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[]                                            | list                      | List of information about each data file associated with the sample barcode.                                                                                                                                                     |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].CloudStoragePath                           | string                    | Path to file, if it exists.                                                                                                                                                                                                      |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].DataCenterName                             | string                    | Short name of the contributing data center, e.g. “bcgsc.ca”.                                                                                                                                                                     |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].DataCenterType                             | string                    | Abbreviation of the type of contributing data center, e.g. “cgcc”.                                                                                                                                                               |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].DataFileName                               | string                    | Name of the datafile stored on the DCC file system.                                                                                                                                                                              |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].DataFileNameKey                            | string                    | Key into the ISB-CGC GCS bucket for this file.                                                                                                                                                                                   |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].DatafileUploaded                           | string                    | Whether the file fit requirements to be uploaded into the project.                                                                                                                                                               |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].DataLevel                                  | string                    | Level of the type of data, depending on where it is stored in the DCC directory structure. Data levels are defined by TCGA DCC.                                                                                                  |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].Datatype                                   | string                    | Data type, e.g. "Complete Clinical Set, CNV (SNP Array)”, “DNA Methylation”, “Expression-Protein”, “Fragment Analysis Results”, “miRNASeq”, “Protected Mutations”, “RNASeq”, “RNASeqV2”, “Somatic Mutations”, “TotalRNASeqV2".   |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].GenomeReference                            | string                    | Allows a center to associate results with a specific genome build that was used as the basis for analysis, e.g. “hg19 (GRCh37)”                                                                                                  |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].Pipeline                                   | string                    | A combination of the center and the platform that can distinguish between two ways of performing the sequencing or assay for the same platform, e.g. "bcgsc.ca\_\_miRNASeq”.                                                     |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].Platform                                   | string                    | A platform (within the scope of TCGA) is a vendor-specific technology for assaying or sequencing that could possibly be customized by a GSC or CGCC, e.g. “IlluminaHiSeq\_miRNASeq”.                                             |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].platform\_full\_name                       | string                    | The full name of the sequencing platform used, e.g. "Illumina HiSeq 2000”, “Ion Torrent PGM”, “AB SOLiD System 2.0".                                                                                                             |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].Project                                    | string                    | The study for which the data was generated, e.g. “TCGA”.                                                                                                                                                                         |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].Repository                                 | string                    | A storage location where files are deposited and made available, e.g. “DCC”, “CGHub”.                                                                                                                                            |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].SDRFFileName                               | string                    | Name of SDRF file stored on the DCC file system, e.g. “bcgsc.ca\_KIRC.IlluminaHiSeq\_miRNASeq.sdrf.txt”                                                                                                                          |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].SampleBarcode                              | string                    | Sample barcode.                                                                                                                                                                                                                  |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details[].SecurityProtocol                           | string                    | An indication of the security protocol necessary to fulfill in order to access the data from the file, e.g. “"DBGap Protected Access”, “DBGap Open Access"                                                                       |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| data\_details\_count                                       | string                    | Length of data\_details list.                                                                                                                                                                                                    |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| patient                                                    | string                    | Participant barcode.                                                                                                                                                                                                             |
+------------------------------------------------------------+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+




datafilenamekey_list_from_sample
################################


Takes a sample barcode as a required parameter and
returns cloud storage paths to files associated with that sample. 
The user does not need to
be authenticated to retrieve a list of open-access file paths only. User
must be authenticated and have dbGaP authorization in order to see paths
to controlled-access files. If the user is not dbGaP authorized,
controlled-access files will not appear.

**Access control:** To call this method, you must have the following
roles:

-  None

Request

HTTP request

GET
https://api-dot-isb-cgc.appspot.com/\_ah/api/cohort\_api/v1/datafilenamekey\_list\_from\_sample

Parameters

+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
| **Parameter name**    | **Value**   | **Description**                                                                                                    |
+=======================+=============+====================================================================================================================+
| **Path parameters**   |             |                                                                                                                    |
+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
| sample\_barcode       | string      | Required. Barcode of the sample to get file paths for.                                                             |
+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
| platform              | string      | Optional. Filter file results by platform.                                                                         |
+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
| pipeline              | string      | Optional. Filter file results by pipeline.                                                                         |
+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
| token                 | string      | Optional. Access token to authenticate user.                                                                       |
+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+


Response

If successful, this method returns a response body with the following
structure:

{

"kind": "cohort\_api#cohortsItem",

"count": *string*,

"datafilenamekeys": [*string*]

}

+----------------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Property name**    | **Value**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                         |
+======================+===========================+=========================================================================================================================================================================================================================================================================================================================================================================================================================================+
| kind                 | cohort\_api#cohortsItem   | The resource type.                                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| count                | string                    | Integer representing the length of the datafilenamekeys list.                                                                                                                                                                                                                                                                                                                                                                           |
+----------------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| datafilenamekeys[]   | list                      | List of cloud storage file paths associated with each sample within the cohort. If a file path is not yet available in the metadata\_data table, the cloud storage bucket name is listed with “/file-path-not-yet-available”. If no file paths are listed (for example, if only controlled-access files are listed for that sample barcode and the user does not have dbGaP authorization), the response will not contain this field.   |
+----------------------+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


google_genomics_from_sample
###########################

Takes a sample barcode as a required parameter and returns the Google Genomics dataset id and readgroupset id associated with the sample, if any.

**Access control:** To call this method, you must have the following
roles:

-  None

Request

HTTP request

GET https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/google_genomics_from_sample

Parameters

+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
| **Parameter name**    | **Value**   | **Description**                                                                                                    |
+=======================+=============+====================================================================================================================+
| **Path parameters**   |             |                                                                                                                    |
+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
| sample\_barcode       | string      | Required. The sample whose dataset id and readgroupset id will be retrieved.                                       |
+-----------------------+-------------+--------------------------------------------------------------------------------------------------------------------+


Response

If successful, this method returns a response body with the following
structure:

{

"kind": "cohort\_api#cohortsItem",

"items": [

{

"count": *string*,

"SampleBarcode": *string*,

"GG_dataset_id": *string*,

"GG_readgroupset_id": *string*

}

] 

}

+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| **Property name**          | **Value**               | **Description**                                                                                             |
+============================+=========================+=============================================================================================================+
| kind                       | cohort\_api#cohortsItem | The resource type.                                                                                          |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| count                      | string                  | The number of items returned. Count will be either "0" or "1".                                              |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| items[]                    | list                    | If a dataset id and readgroupset id exist for the sample, this will be a list with one object.              |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| items[].SampleBarcode      | string                  | The sample barcode passed into the request.                                                                 |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| items[].GG_dataset_id      | string                  | The dataset id of the sample.                                                                               |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+
| items[].GG_readgroupset_id | string                  | The readgroupset id of the sample.                                                                          |
+----------------------------+-------------------------+-------------------------------------------------------------------------------------------------------------+


preview_cohort
##############

Takes a JSON object of
filters in the request body and previews the sample barcodes and participant barcodes in this new cohort. Authentication is not required. Example:

$ curl https:/api-dot-isb-cgc.appspot.com/\_ah/api/cohort\_api/v1/preview\_cohort -d '{"Study": "BRCA,OV"}' -H "Content-Type: application/json"

**Access control:** To call this method, you must have the following
roles:

-  None

Request

HTTP request

POST https://api-dot-isb-cgc.appspot.com/\_ah/api/cohort\_api/v1/preview\_cohort

Parameters

None

Request body

In the request body, supply a metadata resource:

{

'adenocarcinoma\_invasion ': *string*,

'age\_at\_initial\_pathologic\_diagnosis ': *string*,

'anatomic\_neoplasm\_subdivision ': *string*,

'avg\_percent\_lymphocyte\_infiltration ': *float*,

'avg\_percent\_monocyte\_infiltration ': *float*,

'avg\_percent\_necrosis ': *float*,

'avg\_percent\_neutrophil\_infiltration ': *float*,

'avg\_percent\_normal\_cells ': *float*,

'avg\_percent\_stromal\_cells ': *float*,

'avg\_percent\_tumor\_cells ': *float*,

'avg\_percent\_tumor\_nuclei ': *float*,

'batch\_number ': *integer*,

'bcr ': *string*,

'clinical\_M ': *string*,

'clinical\_N ': *string*,

'clinical\_stage ': *string*,

'clinical\_T ': *string*,

'colorectal\_cancer ': *string*,

'country ': *string*,

'country\_of\_procurement ': *string*,

'days\_to\_birth ': *integer*,

'days\_to\_collection ': *integer*,

'days\_to\_death ': integer,

'days\_to\_initial\_pathologic\_diagnosis ': *integer*,

'days\_to\_last\_followup ': *integer*,

'days\_to\_submitted\_specimen\_dx ': *integer*,

'Study ': *string*,

'ethnicity ': *string*,

'frozen\_specimen\_anatomic\_site ': *string*,

'gender ': *string*,

'height ': *integer*,

'histological\_type ': *string*,

'history\_of\_colon\_polyps ': *string*,

'history\_of\_neoadjuvant\_treatment ': *string*,

'history\_of\_prior\_malignancy ': *string*,

'hpv\_calls ': *string*,

'hpv\_status ': *string*,

'icd\_10 ': *string*,

'icd\_o\_3\_histology ': *string*,

'icd\_o\_3\_site ': *string*,

'lymph\_node\_examined\_count ': *integer*,

'lymphatic\_invasion ': *string*,

'lymphnodes\_examined ': *string*,

'lymphovascular\_invasion\_present ': *string*,

'max\_percent\_lymphocyte\_infiltration ': *integer*,

'max\_percent\_monocyte\_infiltration ': *integer*,

'max\_percent\_necrosis ': *integer*,

'max\_percent\_neutrophil\_infiltration ': *integer*,

'max\_percent\_normal\_cells ': *integer*,

'max\_percent\_stromal\_cells ': *integer*,

'max\_percent\_tumor\_cells ': *integer*,

'max\_percent\_tumor\_nuclei ': *integer*,

'menopause\_status ': *string*,

'min\_percent\_lymphocyte\_infiltration ': *integer*,

'min\_percent\_monocyte\_infiltration ': *integer*,

'min\_percent\_necrosis ': *integer*,

'min\_percent\_neutrophil\_infiltration ': *integer*,

'min\_percent\_normal\_cells ': *integer*,

'min\_percent\_stromal\_cells ': *integer*,

'min\_percent\_tumor\_cells ': *integer*,

'min\_percent\_tumor\_nuclei ': *integer*,

'mononucleotide\_and\_dinucleotide\_marker\_panel\_analysis\_status':
*string*,

'mononucleotide\_marker\_panel\_analysis\_status ': *string*,

'neoplasm\_histologic\_grade ': *string*,

'new\_tumor\_event\_after\_initial\_treatment ': *string*,

'number\_of\_lymphnodes\_examined ': *integer*,

'number\_of\_lymphnodes\_positive\_by\_he ': *integer*,

'ParticipantBarcode ': *string*,

'pathologic\_M ': *string*,

'pathologic\_N ': *string*,

'pathologic\_stage ': *string*,

'pathologic\_T ': *string*,

'person\_neoplasm\_cancer\_status ': *string*,

'pregnancies ': *string*,

'preservation\_method ': *string*,

'primary\_neoplasm\_melanoma\_dx ': *string*,

'primary\_therapy\_outcome\_success ': *string*,

'prior\_dx ': *string*,

'Project ': *string*,

'psa\_value ': *float*,

'race ': *string*,

'residual\_tumor ': *string*,

'SampleBarcode ': *string*,

'tobacco\_smoking\_history ': *string*,

'total\_number\_of\_pregnancies ': *integer*,

'tumor\_tissue\_site ': *string*,

'tumor\_pathology ': *string*,

'tumor\_type ': *string*,

'weiss\_venous\_invasion ': *string*,

'vital\_status ': *string*,

'weight ': *integer*,

'year\_of\_initial\_pathologic\_diagnosis ': *string*,

'SampleTypeCode ': *string*,

'has\_Illumina\_DNASeq ': *string*,

'has\_BCGSC\_HiSeq\_RNASeq ': *string*,

'has\_UNC\_HiSeq\_RNASeq ': *string*,

'has\_BCGSC\_GA\_RNASeq ': *string*,

'has\_UNC\_GA\_RNASeq ': *string*,

'has\_HiSeq\_miRnaSeq ': *string*,

'has\_GA\_miRNASeq ': *string*,

'has\_RPPA ': *string*,

'has\_SNP6 ': *string*,

'has\_27k ': *string*,

'has\_450k ': *string*

}

+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Parameter name**                                                   | **Value**   | **Description**                                                                                                                                              |
+======================================================================+=============+==============================================================================================================================================================+
| adenocarcinoma\_invasion                                             | string      |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| age\_at\_initial\_pathologic\_diagnosis                              | string      | Age at which a condition or disease was first diagnosed. (in years)                                                                                          |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| anatomic\_neoplasm\_subdivision                                      | string      | Text term to describe the spatial location, subdivisions and/or anatomic site name of a tumor.                                                               |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_lymphocyte\_infiltration                               | float       | Average in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen.                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_monocyte\_infiltration                                 | float       | Average in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen.                        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_necrosis                                               | float       | Average in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen.                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_neutrophil\_infiltration                               | float       | Average in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen.                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_normal\_cells                                          | float       | Average in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_stromal\_cells                                         | float       | Average in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen.                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_tumor\_cells                                           | float       | Average in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen.                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| avg\_percent\_tumor\_nuclei                                          | float       | Average in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| batch\_number                                                        | integer     | groups samples by the batch they were processed in                                                                                                           |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| bcr                                                                  | string      | A TCGA center where samples are carefully catalogued, processed, quality-checked and stored along with participant clinical information.                     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_M                                                          | string      | Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_N                                                          | string      | Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_stage                                                      | string      | Stage group determined from clinical information on the tumor (T), regional node (N) and metastases (M) and by grouping cases with similar prognosis ...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| clinical\_T                                                          | string      | Extent of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment.                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| colorectal\_cancer                                                   | string      | Text term to signify whether a patient has been diagnosed with colorectal cancer.                                                                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| country                                                              | string      | Text to identify the name of the state, province, or country in which the sample was procured.                                                               |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| country\_of\_procurement                                             | string      | Text to identify the name of the state, province, or country in which the sample was procured.                                                               |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_birth                                                      | integer     | Time interval from a person's date of birth to the date of initial pathologic diagnosis, represented as a calculated number of days.                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_collection                                                 | integer     |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_death                                                      | integer     | Time interval from a person's date of death to the date of initial pathologic diagnosis, represented as a calculated number of days.                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_initial\_pathologic\_diagnosis                             | integer     | Numeric value to represent the day of an individual's initial pathologic diagnosis of cancer.                                                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_last\_followup                                             | integer     | Time interval from the date of last followup to the date of initial pathologic diagnosis, represented as a calculated number of days.                        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| days\_to\_submitted\_specimen\_dx                                    | integer     | Time interval from the date of diagnosis of the submitted sample to the date of initial pathologic diagnosis, represented as a calculated number of d...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Study                                                                | string      | A disease study is the sum of results from all experiments for a specific cancer type (or tumor type) that TCGA is tasked to study. Within the projec...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ethnicity                                                            | string      | The text for reporting information about ethnicity based on the Office of Management and Budget (OMB) categories.                                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| frozen\_specimen\_anatomic\_site                                     | string      | Text description of the origin and the anatomic site regarding the frozen biospecimen tumor tissue sample.                                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| gender                                                               | string      | Text designations that identify gender. Gender is described as the assemblage of properties that distinguish people on the basis of their societal ro...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| height                                                               | integer     | The height of the patient in centimeters.                                                                                                                    |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| histological\_type                                                   | string      | Text term for the structural pattern of cancer cells used to define a microscopic diagnosis.                                                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| history\_of\_colon\_polyps                                           | string      | Yes/No indicator to describe if the subject had a previous history of colon polyps as noted in the history/physical or previous endoscopic report(s).        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| history\_of\_neoadjuvant\_treatment                                  | string      | Text term to describe the patient's history of neoadjuvant treatment and the kind of treament given prior to resection of the tumor.                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| history\_of\_prior\_malignancy                                       | string      | Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence.                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hpv\_calls                                                           | string      | Results of HPV tests                                                                                                                                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| hpv\_status                                                          | string      | Current HPV status                                                                                                                                           |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| icd\_10                                                              | string      | The tenth version of the International Classification of Disease (ICD), published by the World Health Organization in 1992.\_A system of numbered cate...    |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| icd\_o\_3\_histology                                                 | string      | The third edition of the International Classification of Diseases for Oncology, published in 2000, used principally in tumor and cancer registries fo...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| icd\_o\_3\_site                                                      | string      | The third edition of the International Classification of Diseases for Oncology, published in 2000, used principally in tumor and cancer registries fo...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lymph\_node\_examined\_count                                         | integer     |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lymphatic\_invasion                                                  | string      | a yes/no indicator to ask if malignant cells are present in small or thin-walled vessels suggesting lymphatic involvement.                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lymphnodes\_examined                                                 | string      | the yes/no/unknown indicator whether a lymph node assessment was performed at the primary presentation of disease.                                           |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| lymphovascular\_invasion\_present                                    | string      | the yes/no indicator to ask if large vessel (vascular) invasion or small, thin-walled (lymphatic) invasion was detected in a tumor specimen.                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_lymphocyte\_infiltration                               | integer     | Maximum in the series of numeric values to represent the percentage of lymphcyte infiltration in a malignant tumor sample or specimen.                       |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_monocyte\_infiltration                                 | integer     | Maximum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen.                        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_necrosis                                               | integer     | Maximum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen.                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_neutrophil\_infiltration                               | integer     | Maximum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen.                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_normal\_cells                                          | integer     | Maximum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_stromal\_cells                                         | integer     | Maximum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen.                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_tumor\_cells                                           | integer     | Maximum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen.                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| max\_percent\_tumor\_nuclei                                          | integer     | Maximum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| menopause\_status                                                    | string      | Text term to signify the status of a woman's menopause, the permanent cessation of menses, usually defined by 6 to 12 months of amenorrhea.                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_lymphocyte\_infiltration                               | integer     | Minimum in the series of numeric values to represent the percentage of lymphcyte infiltration in a malignant tumor sample or specimen.                       |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_monocyte\_infiltration                                 | integer     | Minimum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen.                        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_necrosis                                               | integer     | Minimum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen.                                   |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_neutrophil\_infiltration                               | integer     | Minimum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen.                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_normal\_cells                                          | integer     | Minimum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_stromal\_cells                                         | integer     | Minimum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen.                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_tumor\_cells                                           | integer     | Minimum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen.                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| min\_percent\_tumor\_nuclei                                          | integer     | Minimum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| mononucleotide\_and\_dinucleotide\_marker\_panel\_analysis\_status   | string      | Text result of microsatellite instability (MSI) testing at using a mononucleotide and dinucleotide microsatellite panel.                                     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| mononucleotide\_marker\_panel\_analysis\_status                      | string      | Text result of microsatellite instability (MSI) testing using a mononucleotide microsatellite panel.                                                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| neoplasm\_histologic\_grade                                          | string      | Numeric value to express the degree of abnormality of cancer cells, a measure of differentiation and aggressiveness.                                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| new\_tumor\_event\_after\_initial\_treatment                         | string      | Yes/No/Unknown indicator to identify whether a patient has had a new tumor event after initial treatment.                                                    |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| number\_of\_lymphnodes\_examined                                     | integer     | the total number of lymph nodes removed and pathologically assessed for disease.                                                                             |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| number\_of\_lymphnodes\_positive\_by\_he                             | integer     | Numeric value to signify the count of positive lymph nodes identified through hematoxylin and eosin (H&E) staining light microscopy.                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ParticipantBarcode                                                   | string      | The barcode assigned by TCGA to the Participant                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pathologic\_M                                                        | string      | Code to represent the defined absence or presence of distant spread or metastases (M) to locations via vascular channels or lymphatics beyond the reg...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pathologic\_N                                                        | string      | The codes that represent the stage of cancer based on the nodes present (N stage) according to criteria based on multiple editions of the AJCC's Cance...    |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pathologic\_stage                                                    | string      | The extent of a cancer, especially whether the disease has spread from the original site to other parts of the body based on AJCC staging criteria.          |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pathologic\_T                                                        | string      | Code of pathological T (primary tumor) to define the size or contiguous extension of the primary tumor (T), using staging criteria from the American ...     |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| person\_neoplasm\_cancer\_status                                     | string      | The state or condition of an individual's neoplasm at a particular point in time.                                                                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| pregnancies                                                          | string      | Value to describe the number of full-term pregnancies that a woman has experienced.                                                                          |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| preservation\_method                                                 | string      |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| primary\_neoplasm\_melanoma\_dx                                      | string      | Text indicator to signify whether a person had a primary diagnosis of melanoma.                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| primary\_therapy\_outcome\_success                                   | string      | Measure of Success                                                                                                                                           |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| prior\_dx                                                            | string      | Text term to describe the patient's history of prior cancer diagnosis and the spatial location of any previous cancer occurrence                             |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Project                                                              | string      | The study for which the data was generated.                                                                                                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| psa\_value                                                           | float       | The lab value that represents the results of the most recent (post-operative) prostatic-specific antigen (PSA) in the blood.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| race                                                                 | string      | The text for reporting information about race based on the Office of Management and Budget (OMB) categories.                                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| residual\_tumor                                                      | string      | Text terms to describe the status of a tissue margin following surgical resection.                                                                           |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SampleBarcode                                                        | string      | The barcode assigned by TCGA to a sample from a Participant                                                                                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tobacco\_smoking\_history                                            | string      | Category describing current smoking status and smoking history as self-reported by a patient.                                                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| total\_number\_of\_pregnancies                                       | integer     |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tumor\_tissue\_site                                                  | string      | Text term that describes the anatomic site of the tumor or disease.                                                                                          |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tumor\_pathology                                                     | string      |                                                                                                                                                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tumor\_type                                                          | string      | Text term to identify the morphologic subtype of papillary renal cell carcinoma.                                                                             |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| weiss\_venous\_invasion                                              | string      | The result of an assessment using the Weiss histopathologic criteria.                                                                                        |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vital\_status                                                        | string      | the survival state of the person registered on the protocol.                                                                                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| weight                                                               | integer     | the weight of the patient measured in kilograms.                                                                                                             |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| year\_of\_initial\_pathologic\_diagnosis                             | string      | Numeric value to represent the year of an individual’s initial pathologic diagnosis of cancer.                                                               |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SampleTypeCode                                                       | string      | the type of the sample tumor or normal tissue cell or blood sample provided by a participant.                                                                |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_Illumina\_DNASeq                                                | string      | Indicates if a sample has gene sequencing data. “True”, “False”, or “None”.                                                                                  |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_BCGSC\_HiSeq\_RNASeq                                            | string      | Indicates if a sample has RNA sequencing data from the IlluminaHiSeq platform and the BCGSC pipeline. “True”, “False”, or “None”.                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_UNC\_HiSeq\_RNASeq                                              | string      | Indicates if a sample has RNA sequencing data from the IlluminaHiSeq platform and the UNC pipeline. “True”, “False”, or “None”.                              |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_BCGSC\_GA\_RNASeq                                               | string      | Indicates if a sample has RNA sequencing data from the IlluminaGA platform and the BCGSC pipeline. “True”, “False”, or “None”.                               |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_UNC\_GA\_RNASeq                                                 | string      | Indicates if a sample has RNA sequencing data from the IlluminaGA platform and the UNC pipeline. “True”, “False”, or “None”.                                 |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_HiSeq\_miRnaSeq                                                 | string      | Indicates if a sample has microRNA data from the IlluminaHiSeq platform. “True”, “False”, or “None”.                                                         |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_GA\_miRNASeq                                                    | string      | Indicates if a sample has microRNA data from the IlluminaGA platform. “True”, “False”, or “None”.                                                            |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_RPPA                                                            | string      | Indicates if a sample has protein array data. “True”, “False”, or “None”.                                                                                    |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_SNP6                                                            | string      | Indicates if a sample has copy number data. “True”, “False”, or “None”.                                                                                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_27k                                                             | string      | Indicates if a sample has methylation data from the Illumina 27k platform. “True”, “False”, or “None”.                                                       |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| has\_450k                                                            | string      | Indicates if a sample has methylation data from the Illumina 450k platform. “True”, “False”, or “None”.                                                      |
+----------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response

If successful, this method returns a response body with the following
structure:

{

"kind": "cohort\_api#cohortsItem",

"patient_count": *string,*

"patients": [*string*],

"sample_count": *string,*

"samples": [*string*],

}

+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
| **Property name**   | **Value**                 | **Description**                                                                                             |
+=====================+===========================+=============================================================================================================+
| kind                | cohort\_api#cohortsItem   | The resource type.                                                                                          |
+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
| patient_count       | string                    | Number of participants in this cohort.                                                                      |
+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
| patients[]          | list                      | List of participant barcodes in this cohort.                                                                |
+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
| sample_count        | string                    | Number of samples in this cohort.                                                                           |
+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
| samples[]           | list                      | List of sample barcodes in this cohort.                                                                     |
+---------------------+---------------------------+-------------------------------------------------------------------------------------------------------------+
