sample_details
##############
Given a sample barcode (of length 16, *eg* TCGA-B9-7268-01A), this endpoint returns all available "biospecimen" information about this sample, the associated patient barcode, a list of associated aliquots, and a list of "data_details" blocks describing each of the data files associated with this sample

**Example**::

	curl "https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/sample_details?sample_barcode=TCGA-ZH-A8Y6-01A"

**API explorer example**:

Click `here <https://apis-explorer.appspot.com/apis-explorer/?base=https://api-dot-isb-cgc.appspot.com/_ah/api#p/cohort_api/v1/cohort_api.cohort_endpoints.cohorts.sample_details?sample_barcode=TCGA-ZH-A8Y6-01A&/>`_ to see this endpoint in Google's API explorer.

**Request**

HTTP request::

	GET https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/sample_details

**Parameters**

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	pipeline,string,"Optional. "
	platform,string,"Optional. "
	sample_barcode,string,"Required. "


**Response**

If successful, this method returns a response body with the following structure:

.. code-block:: javascript

  {
    "aliquots": [string],
    "biospecimen_data": {
      "avg_percent_lymphocyte_infiltration": number,
      "avg_percent_monocyte_infiltration": number,
      "avg_percent_necrosis": number,
      "avg_percent_neutrophil_infiltration": number,
      "avg_percent_normal_cells": number,
      "avg_percent_stromal_cells": number,
      "avg_percent_tumor_cells": number,
      "avg_percent_tumor_nuclei": number,
      "batch_number": string,
      "bcr": string,
      "days_to_collection": string,
      "max_percent_lymphocyte_infiltration": string,
      "max_percent_monocyte_infiltration": string,
      "max_percent_necrosis": string,
      "max_percent_neutrophil_infiltration": string,
      "max_percent_normal_cells": string,
      "max_percent_stromal_cells": string,
      "max_percent_tumor_cells": string,
      "max_percent_tumor_nuclei": string,
      "min_percent_lymphocyte_infiltration": string,
      "min_percent_monocyte_infiltration": string,
      "min_percent_necrosis": string,
      "min_percent_neutrophil_infiltration": string,
      "min_percent_normal_cells": string,
      "min_percent_stromal_cells": string,
      "min_percent_tumor_cells": string,
      "min_percent_tumor_nuclei": string,
      "ParticipantBarcode": string,
      "Project": string,
      "SampleBarcode": string,
      "Study": string
    },
    "data_details": [
      {
        "CloudStoragePath": string,
        "DataCenterName": string,
        "DataCenterType": string,
        "DataFileName": string,
        "DataFileNameKey": string,
        "DatafileUploaded": string,
        "DataLevel": string,
        "Datatype": string,
        "GenomeReference": string,
        "GG_dataset_id": string,
        "GG_readgroupset_id": string,
        "Pipeline": string,
        "Platform": string,
        "platform_full_name": string,
        "Project": string,
        "Repository": string,
        "SampleBarcode": string,
        "SDRFFileName": string,
        "SecurityProtocol": string
      }
    ],
    "data_details_count": string,
    "error": string,
    "patient": string
  }

.. csv-table::
	:header: "**Parameter name**", "**Value**", "**Description**"
	:widths: 50, 10, 50

	aliquots[], list, "List of barcodes of aliquots taken from this participant."
	biospecimen_data, nested object, "Biospecimen data about the sample."
	biospecimen_data.avg_percent_lymphocyte_infiltration, number, "Average in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_monocyte_infiltration, number, "Average in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_necrosis, number, "Average in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_neutrophil_infiltration, number, "Average in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_normal_cells, number, "Average in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_stromal_cells, number, "Average in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_tumor_cells, number, "Average in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.avg_percent_tumor_nuclei, number, "Average in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.batch_number, string, "Groups samples by the batch they were processed in."
	biospecimen_data.bcr, string, "A TCGA center where samples are carefully catalogued, processed, quality-checked and stored along with participant clinical information."
	biospecimen_data.days_to_collection, string, ""
	biospecimen_data.max_percent_lymphocyte_infiltration, string, "Maximum in the series of numeric values to represent the percentage of lymphocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_monocyte_infiltration, string, "Maximum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_necrosis, string, "Maximum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_neutrophil_infiltration, string, "Maximum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_normal_cells, string, "Maximum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_stromal_cells, string, "Maximum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_tumor_cells, string, "Maximum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.max_percent_tumor_nuclei, string, "Maximum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_lymphocyte_infiltration, string, "Minimum in the series of numeric values to represent the percentage of lymphcyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_monocyte_infiltration, string, "Minimum in the series of numeric values to represent the percentage of monocyte infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_necrosis, string, "Minimum in the series of numeric values to represent the percentage of cell death in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_neutrophil_infiltration, string, "Minimum in the series of numeric values to represent the percentage of neutrophil infiltration in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_normal_cells, string, "Minimum in the series of numeric values to represent the percentage of normal cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_stromal_cells, string, "Minimum in the series of numeric values to represent the percentage of stromal cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_tumor_cells, string, "Minimum in the series of numeric values to represent the percentage of tumor cells in a malignant tumor sample or specimen."
	biospecimen_data.min_percent_tumor_nuclei, string, "Minimum in the series of numeric values to represent the percentage of tumor nuclei in a malignant tumor sample or specimen."
	biospecimen_data.ParticipantBarcode, string, "Participant barcode."
	biospecimen_data.Project, string, "Project name, e.g. 'TCGA'."
	biospecimen_data.SampleBarcode, string, "The barcode assigned by TCGA to a sample from a Participant."
	biospecimen_data.Study, string, "Tumor type abbreviation, e.g. 'BRCA'. "
	data_details[], list, "List of information about each data file associated with the sample barcode."
	data_details[].CloudStoragePath, string, "Google Cloud Storage path to file."
	data_details[].DataCenterName, string, "Short name of the contributing data center, e.g. bcgsc.ca."
	data_details[].DataCenterType, string, "Abbreviation of the type of contributing data center, e.g. cgcc."
	data_details[].DataFileName, string, "Name of the datafile stored on the DCC file system."
	data_details[].DataFileNameKey, string, "Key into the ISB-CGC GCS bucket for this file."
	data_details[].DatafileUploaded, string, "Whether the file fit requirements to be uploaded into the project."
	data_details[].DataLevel, string, "Level of the type of data, depending on where it is stored in the DCC directory structure. Data levels are defined by TCGA DCC."
	data_details[].Datatype, string, "Data type, e.g. Complete Clinical Set, CNV (SNP Array), DNA Methylation, Expression-Protein, Fragment Analysis Results, miRNASeq, Protected Mutations, RNASeq, RNASeqV2, Somatic Mutations, TotalRNASeqV."
	data_details[].GenomeReference, string, "Allows a center to associate results with a specific genome build that was used as the basis for analysis, e.g. hg19 (GRCh37)"
	data_details[].GG_dataset_id, string, "Google genomics dataset id."
	data_details[].GG_readgroupset_id, string, "Google genomics readgroupset id."
	data_details[].Pipeline, string, "A combination of the center and the platform that can distinguish between two ways of performing the sequencing or assay for the same platform, e.g. bcgsc.ca__miRNASeq."
	data_details[].Platform, string, "A platform (within the scope of TCGA) is a vendor-specific technology for assaying or sequencing that could possibly be customized by a GSC or CGCC, e.g. IlluminaHiSeq_miRNASeq."
	data_details[].platform_full_name, string, "The full name of the sequencing platform used, e.g. Illumina HiSeq 2000, Ion Torrent PGM, AB SOLiD System 2.0."
	data_details[].Project, string, "The study for which the data was generated, e.g. TCGA."
	data_details[].Repository, string, "A storage location where files are deposited and made available, e.g. DCC, CGHub."
	data_details[].SampleBarcode, string, "Sample barcode."
	data_details[].SDRFFileName, string, "Name of SDRF file stored on the DCC file system, e.g. bcgsc.ca_KIRC.IlluminaHiSeq_miRNASeq.sdrf.txt"
	data_details[].SecurityProtocol, string, "An indication of the security protocol necessary to fulfill in order to access the data from the file, e.g. DBGap Protected Access, DBGap Open Access"
	data_details_count, string, "Length of data_details list."
	error, string, "Deprecated."
	patient, string, "Participant barcode."
