*********************************
Integrative Genomics Viewer (IGV)
*********************************

**Important:**  Improved integration of the IGV browser and the ISB-CGC BigQuery data tables is coming soon!  Specifically
the IGV browser will be able to access the *high-level* molecular data in the ISB-CGC BigQuery tables as well 
the *low-level* sequence data via the GA4GH API.

Accessing the IGV Browser
-------------------------

To access IGV, go to the cohort file list page. The file listing table includes a column labelled "IGV". 
For those files that also have a ReadGroupSet ID in Google Genomics, a green check mark will appear in the column. 
Clicking on that link will take you to an IGV browser view of the selected readgroupset.

(Note that "readgroupset" is a GA4GH term for a group of aligned DNA- or RNA-seq reads, 
typically from a single sample or a single BAM file.
For the CCLE and TCGA datasets hosted by the ISB-CGC, each readgroupset corresponds to a single BAM file which
in turn corresponds to the aligned DNA- or RNA-seq reads from a single sample.)

Referencing the Integrative Genomics Viewer (IGV)
-------------------------------------------------

The copyright to the Integrative Genomics Viewer is held by the Broad Institute, and the software has been 
released under the MIT License.
For details about IGV and how to reference it in publications, please follow the link by clicking either the 
"IGV Browser" text at the upper left of the IGV window or the "IGV" icon in the upper right of the IGV window,
or visit the IGV home page at www.broadinstitute.org/igv.

