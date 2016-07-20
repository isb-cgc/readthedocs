*********************************
Integrative Genomics Viewer (IGV)
*********************************

Accessing the IGV Browser
-------------------------

To access IGV, go to the cohort file list page (through the "View Files" link at the top of the page). The file listing table includes a column labelled "IGV".

For those files that also have a ReadGroupSet ID in Google Genomics, a "GA4GH" label with a checkbox will appear in the column.  For those files that are available in cloud storage, a "Cloud Storage" label with a checkbox will appear in the column. A user can only select the cloud storage checkbox to view controlled access data if he or she has been authenticated and authorized through the user details page. Otherwise the user can view the checkbox but there will be a disabled cursor icon when the user hovers over in an attempt to select the checkbox. (Open source data such as the CCLE project does not require authentication and authorization, therefore you will not be presented with the disabled cursor icon when you are trying to view this data in the IGV viewer.) You can select a maximum of five files you want to view at the same time in the IGV viewer through selecting the relevant checkboxes on possibly multiple pages of files.  Once you have selected the appropriate files to view in the IGV viewer, pressing the "Launch IGV" button will launch the IGV viewer.

NOTES:
 - You will only be able to view controlled access sequence files if you have `logged in as a registered dbGaP authorized user <Gaining-Access-To-TCGA-Contolled-Access-Data.html>`_.
 - You will need to disable your browser pop-up blocker to view files with IGV.  If you see a 403 error when using the IGV viewer, the pop-up blocker is the cause of that error.  Turn off the blocker and try again.

("ReadGroupSet" is a GA4GH term for a group of aligned DNA- or RNA-seq reads, 
typically from a single sample or a single BAM file.
For the CCLE and TCGA datasets hosted by the ISB-CGC, each ReadGroupSet corresponds to a single BAM file which
in turn corresponds to the aligned DNA- or RNA-seq reads from a single sample. IGV can also view BAM files (with associated BAM Index Files) that are stored on a Google Drive.  These are the type of files that are being viewed with the link "Cloud Storage".).

Acknowledgements
----------------

The copyright to the Integrative Genomics Viewer is held by the Broad Institute, and the software has been 
released under the MIT License.  For more information about IGV please see the 
`IGV home page <http://www.broadinstitute.org/software/igv/home>`_ or the 
`IGV github repo <https://github.com/igvteam/igv>`_.

We are grateful to the IGV team for their assistance in integrating IGV into the ISB-CGC web-app.

Robinson J T, Thorvaldsdottir H, Winckler W, Guttman M, Lander E S, Getz G & Mesirov J P, *Integrative genomics viewer*, 
`Nature Biotechnology 29, 24-26 (2011) <http://www.nature.com/nbt/journal/v29/n1/abs/nbt.1754.html>`_.

Thorvaldsdottir H, Robinson J T, Mesirov J P, 
*Integrative Genomics Viewer (IGV): high-performance genomics data visualization and exploration*,
`Briefings in Bioinformatics 14, 178-192 (2013) <http://bib.oxfordjournals.org/content/14/2/178.full?keytype=ref&%2520ijkey=qTgjFwbRBAzRZWC>`_.
