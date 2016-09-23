import datetime as dt
import openpyxl as op
import argparse
import os.path
import sys
import re

import csv

class RFC4180(csv.Dialect):
    def __init__(self):
        csv.Dialect.__init__(self)
    delimiter = ','
    doublequote = True
    escapechar = None
    lineterminator = '\r\n'
    quotechar = '"'
    quoting = csv.QUOTE_NONNUMERIC
    skipinitialspace = False
    stric = True

def parseargs():
    pa = argparse.ArgumentParser(description=
            'Exports multiple CSV files from an Excel *.xlsx Workbook')
    pa.add_argument('file', metavar='EXCELFILE')
    args = pa.parse_args(sys.argv[1:])
    return vars(args)

def stringify(data):
    transmap = {
        # empty cells are going to be empty strings
        None: 'NA',
        # workaround for bug in openpyxl
        # https://bitbucket.org/openpyxl/openpyxl/issues/674/ 
        dt.datetime(1899, 12, 30, 0, 0): dt.time(0, 0),
        dt.datetime(1899, 12, 31, 0, 0): dt.datetime(1900, 1, 1, 0, 0),
    }
    newdata = []
    for l in data:
        nl = [transmap[f] if f in transmap else f for f in l]
        nl = [f.encode('utf-8')
              if isinstance(f, basestring) else f for f in nl]
        newdata.append([str(f) if not isinstance(f, basestring)
                        else f for f in nl])
    return newdata

def write_csv(data, outfile):
    with open(outfile, 'wb') as fout:
        writer = csv.writer(fout, dialect='RFC4180')
        writer.writerows(data)

def main():
    csv.register_dialect('RFC4180', RFC4180)
    xlsxfile = parseargs()['file']
    out_prefix = os.path.splitext(xlsxfile)[0]
    wb = op.load_workbook(xlsxfile, data_only=True)
    for sn in wb.sheetnames:
        outfile = out_prefix + '_' + re.sub(r'\s+', '_', sn) + '.csv'
        data = []
        sheet = wb.get_sheet_by_name(sn)
        for l in sheet.values:
            data.append(l)
        newdata = stringify(data)
        write_csv(newdata, outfile)


if __name__ == '__main__':
    main()

