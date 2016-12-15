TCGA Data in Cloud Storage
##########################

At this time, all controlled-access data files are stored in GCS in their original form, as obtained from the data repository.  

In order to access these controlled data, a user of the ISB-CGC must first be authenticated by NIH (via the ISB-CGC web-app).
Upon successful authentication, the users's dbGaP authorization will be verified.  These two steps are required before the user's
Google identity is added to the access control list (ACL) for the controlled data.  At this time, this access must be renewed
every 24 hours.


