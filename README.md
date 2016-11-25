# xslxtocsv

This is a quick and dirty script to export one MS Office Excel
workbook in OOXML format (*.xlsx) to multiple CSV files, one per
Worksheet.  The names of output files are derived from the basename of
the input file and from the names of the Worksheets.  The script
writes [RFC4180](https://tools.ietf.org/html/rfc4180) conform
files. Empty cells are replaced with empty strings.

----------------------

##usage:

    xlsxtocsv.py [-h] [-o OUTPUTDIRECTORY] EXCELFILE

    Exports multiple CSV files from an Excel *.xlsx Workbook

    positional arguments:
      EXCELFILE           The Excel file to export

    optional arguments:
      -h, --help          show this help message and exit
       -o OUTPUTDIRECTORY  The output directory, default is the current directory.

