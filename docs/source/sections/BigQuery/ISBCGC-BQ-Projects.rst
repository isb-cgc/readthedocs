*************************
ISB-CGC BigQuery Projects
*************************

ISB-CGC has two Google BigQuery projects. You'll need to link to these projects (from your own project) in order to see and query the ISB-CGC tables in the BigQuery Console.

 - isb-cgc
 - isb-cgc-bq
 
isb-cgc project
===============
 
The isb-cgc project contains all of the ISB-CGC BiqQuery tables created before July 2020.
 
isb-cgc-bq project
===================

The isb-cgc-bq project contains all new ISB-CGC BigQuery tables created after July 1, 2020. It will feature a more intuitive, easier to use data set and table organization, 
as well as consistent table naming both within and across programs.

This new project is a work in progress. the migration of existing tables from the isb-cgc project  will be occurring over time, and will not be all at once,
though all new tables will be created in the new project.


1) As table offerings grow, we are creating a new BQ project with new organization

2) It is isb-cgc-bq. This migration will be occurring over time, and will not be all at once, though new tables will be created in the new project.

3) Here is how to pin that project; keep isb-cgc pinned as well.

4) Here is the organization of BQ tables: 
    a) recent versus archived, and what that means 
    b) table naming convention
    c) dataset naming convention
    d) dataset convention: we did decide that 5+ tables was not the only criteria for having a separate dataset
    e) current/deprecated/archived meaning
    
    
5) Tables in isb-cgc will be retired, and labeled as deprecated as we copy them over to the new project. Table descriptions will include new table location. Eventually they will be turned into only views (with no preview ability), so existing references will continue to work correctly. Many older tables with light usage may remain in isb-cgc and not be copied over; tables with no logged recent usage may be deleted.
