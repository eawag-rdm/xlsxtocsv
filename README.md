# xslxtocsv

This is a quick and dirty script to export one MS Office Excel workbook in OOXML format (*.xlsx) to multiple CSV files, one per Worksheet.
The names of output files are derived from the basename of the input file and from the names of the Worksheets.
The script writes [RFC4180](https://tools.ietf.org/html/rfc4180) conform files. Empty cells are replaced with 'NA'.

----------------------

##usage:

	testpyxl.py [-h] EXCELFILE

	Exports multiple CSV files from an Excel *.xlsx Workbook

	positional arguments:
	  EXCELFILE

	optional arguments:
	  -h, --help  show this help message and exit



