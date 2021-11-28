# xslxtocsv

This is a quick and dirty script to export one MS Office Excel
workbook in OOXML format (*.xlsx) to multiple CSV files, one per
Worksheet.  The names of output files are derived from the basename of
the input file and from the names of the Worksheets.  The script
writes [RFC4180](https://tools.ietf.org/html/rfc4180) conform
files. Empty cells are replaced with empty strings.

----------------------
## Unix / Linux / OSX

### Installation

`pip install git+https://github.com/eawag-rdm/xlsxtocsv.git`

+ You have to have [Git](https://git-scm.com/downloads) installed.
+ You have to have [Python 3](https://www.python.org/downloads/) installed.

### Usage:
    xlsxtocsv.py [-h] [-f EXCELFILE] [-o OUTPUTDIRECTORY]
    
    Exports multiple CSV files from an Excel *.xlsx Workbook
    
    optional arguments:
      -h, --help          show this help message and exit
      -f EXCELFILE        The Excel file to export. If omitted, a graphical file
                          chooser will be used.
      -o OUTPUTDIRECTORY  The output directory. Default is the current directory
                          if EXCELFILE was given, otherwise a file chooser will be
                          used as well.
  
## Windows

**ATTENTION: The Windows binary is not supported or updated
  anymore. Maybe it works, maybe not. If you need to use xlsxtocsv
  with a Windows computer, use the Windows Subsystem for Linux
  ([https://docs.microsoft.com/en-us/windows/wsl/install](https://docs.microsoft.com/en-us/windows/wsl/install)).**

### Installation

+ Download the installer [xlsxtocsv_setup.exe](https://github.com/eawag-rdm/xlsxtocsv/raw/master/WindowsInstaller/xlsxtocsv_setup.exe)
+ Double-click it.
+ Click "Install". Accept default options by clicking "Next" and "Install". Note: No administrative rights are required on your Windows computer to install xlsxtocsv.
+ Click "Finish" and allow your computer to reboot.

### Usage

+ After the installation there will be an entry *xlsxtocsv* in your Start Menu.
+ Click it.
+ Choose xlsx file to convert.
+ Choose directory where to put the output.
+ Observe how the csv file(s) appear in the output directory you chose.

