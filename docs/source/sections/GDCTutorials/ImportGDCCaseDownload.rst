Importing a GDC Case List into ISB-CGC
======================================

In addition to the file manifest, GDC also allows users to export case lists from your searches as shown in the image below:

.. image:: CaseExport.png
  
As we did with the file manifest, in this tutorial we'll look at how to bring that case list into BigQuery and create a table that you can use as the basis for analyzing data in the ISB-CGC system.  In this case, the GDC file is in JSON format, and while BigQuery does understand JSON there are special characteristics that BigQuery needs that unfortunately are not provided by the GDC file.  So to get around the incompatibility, the first step is to convert the JSON into something that BigQuery can understand.

Converting JSON to tab delimited
================================

Let's start by looking at the data that GDC has provided:

.. code-block:: javascript

  {
    "project": {
      "project_id": "TCGA-LIHC", 
      "primary_site": "Liver"
    }, 
    "case_id": "67a00f5f-c753-48f9-bc24-8287f50ec776", 
    "demographic": {
      "gender": "male"
    }, 
    "summary": {
      "data_categories": [
        {
          "file_count": 1, 
          "data_category": "DNA Methylation"
        }, 
        {
          "file_count": 1, 
          "data_category": "Clinical"
        }, 
        {
          "file_count": 1, 
          "data_category": "Biospecimen"
        }, 
        {
          "file_count": 5, 
          "data_category": "Transcriptome Profiling"
        }, 
        {
          "file_count": 16, 
          "data_category": "Simple Nucleotide Variation"
        }, 
        {
          "file_count": 4, 
          "data_category": "Copy Number Variation"
        }, 
        {
          "file_count": 4, 
          "data_category": "Raw Sequencing Data"
        }
      ]
    }
  }


For our purposes, the data in the "summary" section can be ignored.  Since ISB-CGC doesn't store all the files from GDC, having the file count stored in a table doesn't do much good.  So what is useful is the Project ID, Primary Site, Case ID and Gender.  Those can be easily parsed out and put into a tab-delimited file with a simple Python script:

.. code-block:: python

  #! /usr/bin/python
  import json
  import argparse

  def main(args):
	inputfile = open(args.inputfile,'r')
	outputfile = open(args.outputfile,'w')
	header = "project_short_name\tprimary_site\tgdc_case_id\tgender\n"	
	outputfile.write(header)	
	data = json.load(inputfile)
	
	for entry in data:	
		project = entry['project']['project_id']		
		site = entry['project']['primary_site']		
		case = entry['case_id']		
		gender = entry['demographic']['gender']		
		outputfile.write(("%s\t%s\t%s\t%s\n") % (project,site,case,gender))	
	
	outputfile.close()
	
  if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--inputfile", required = True, help = "JSON file from GDC")
	parser.add_argument("-o", "--outputfile", required = True, help = "File to save")
	args = parser.parse_args()
	main(args)

