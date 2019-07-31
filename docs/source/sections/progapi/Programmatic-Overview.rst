==========================
ISB-CGC Endpoints Tutorial
==========================



Programmatic access to molecular data and metadata within the ISB-CGC platform uses a combination of ISB-CGC APIs and and Swagger UI documentation. 

The ISB-CGC API provides an interface to the ISB-CGC metadata stored in CloudSQL, and consists of several “endpoints”, implemented using Google Cloud Endpoints. Details about these endpoints can be found below. 

Some example use-cases include:


 - obtaining detailed metadata about a particular patient or sample;
 - creating (or retrieving a previously saved) cohort of patients and samples, based on a defined set of criteria;
 - retrieving a cohort's file manifest using the cohort ID;
 - retrieve a cohort's file manifest based on filters provided;
 - register, refresh, unregister a specified Gooogle Cloud Project;



The Swagger UI(ADD PROD LINK) can be used to see details about each endpoint, and also provides a convenient interface to test an endpoint through your web browser. Following the link in the previous sentence will take you to a page with a list of APIs, in which each API consists of a set of functionally-related endpoints. Together, these individual APIs make up the ISB-CGC API. 

