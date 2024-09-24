# xslxtocsv

This is a quick and dirty script to export one MS Office Excel
workbook in OOXML format (*.xlsx) to multiple CSV files, one per
Worksheet.  The names of output files are derived from the basename of
the input file and from the names of the Worksheets.  The script
writes [RFC4180](https://tools.ietf.org/html/rfc4180) conform
files. Empty cells are replaced with empty strings.

----------------------

## Installation

> Python is required!

### With Git
```bash
pip install git+https://github.com/eawag-rdm/xlsxtocsv.git
```

### Without Git
Download and unzip the files from **GitHub**. Open the unzipped folder in a terminal and type:

```bash
pip install .
```

## Usage:
    xlsxtocsv.py [-h] [-f EXCELFILE] [-o OUTPUTDIRECTORY]
    
    Exports multiple CSV files from an Excel *.xlsx Workbook
    
    optional arguments:
      -h, --help          show this help message and exit
      -f EXCELFILE        The Excel file to export. If omitted, a graphical file
                          chooser will be used.
      -o OUTPUTDIRECTORY  The output directory. Default is the current directory
                          if EXCELFILE was given, otherwise a file chooser will be
                          used as well.
  
