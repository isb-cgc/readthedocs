TCGA Data by Source Repository
##############################

TCGA Data at the DCC
====================

Complete sets of open-access and controlled-access data archives were copied from the DCC on October 4th, 2015
into Google Cloud Storage.

Note that for every archive at the DCC, there may be multiple revisions of an archive.  A list of the current 
`latest archives <http://tcga-data.nci.nih.gov/datareports/resources/latestarchive>`_
can be obtained from the DCC.
The archive 
`naming convention <https://wiki.nci.nih.gov/display/TCGA/TCGA+Data+Archives#TCGADataArchives-NamingConventions>`_
includes the disease code, the platform/pipeline name, the archive type (*eg* data level), the serial index
(which is often the batch number), and the revision number.
If you want to check whether there is a newer version of a specific archive at the DCC than what we currently
have on the ISB-CGC platform, you can check the date column in the latest archive report mentioned above,
or you can compare the archive name to these lists of 
`open-access archives <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/DCC_archives.04oct2015.open.tsv>`_
and 
`controlled-access archives <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/DCC_archives.04oct2015.cntl.tsv>`_
based on our most recent upload.

Note that all "bio" archives (containing clinical, biospecimen, and other types of XML files) were recently migrated to a new
XSD which is not backwards compatible with the previous XSD.  This update took place over the course of the 
month of December 2015 and  none of these new archives are currently included in any of the current ISB-CGC BigQuery tables or files in GCS.

TCGA Data at CGHub
==================

The complete 
`listing <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/GCS_listing.v4.tsv>`_
of the (over 87,000) TCGA data files from CGHub that are currently available in Google Cloud Storage (GCS)
contains the following four columns of information: 

* unique CGHub id for the file, 
* the TCGA aliquot barcode,
* the GCS object path, and
* the size of the file in bytes.

The final complete CGHub manifest (downloaded in early July, just before CGHub shut down) is also 
`available <https://raw.githubusercontent.com/isb-cgc/readthedocs/master/docs/include/LATEST_MANIFEST.tsv>`_

TCGA Data at the GDC
====================

In July (2016), both the DCC and CGHub are scheduled to be shut down.  The official repository for all
NCI datasets, including the TCGA data is now the NCI `Genomic Data Commons <https://gdc.nci.nih.gov/>`_,
and moving forward, the ISB-CGC will be switching over to using the GDC as the official source repository 
of all new data, including the new "harmonized" TCGA data, realigned and reprocessed 
using the GRCh38 assembly (aka hg38).


