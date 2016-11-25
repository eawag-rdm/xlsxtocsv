# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
import datetime as dt
import openpyxl as op
import argparse
import os.path
import sys
import re
import csv

__metaclass__ = type

class RFC4180(csv.Dialect):
    def __init__(self):
        csv.Dialect.__init__(self)
    delimiter = b','
    doublequote = True
    escapechar = None
    lineterminator = b'\r\n'
    quotechar = b'"'
    quoting = csv.QUOTE_MINIMAL
    skipinitialspace = False
    stric = True

def parseargs():
    pa = argparse.ArgumentParser(description=
            'Exports multiple CSV files from an Excel *.xlsx Workbook')
    pa.add_argument('file', metavar='EXCELFILE', help='The Excel file to export')
    pa.add_argument('-o', metavar='OUTPUTDIRECTORY',
                    help='The output directory, default is the current directory',
                    default=os.getcwd())
    args = pa.parse_args(sys.argv[1:])
    return vars(args)

def _stringify(dat):
    if not isinstance(dat, basestring):
        return str(dat).encode('utf-8')
    else:
        return dat.encode('utf-8')

def _transmap(dat):
    transmap = {
        # empty cells are going to be empty strings
        None: '',
        # workaround for bug in openpyxl
        # https://bitbucket.org/openpyxl/openpyxl/issues/674/ 
        dt.datetime(1899, 12, 30, 0, 0): dt.time(0, 0),
        dt.datetime(1899, 12, 31, 0, 0): dt.datetime(1900, 1, 1, 0, 0),
    }
    return transmap[dat] if dat in transmap else dat

def _datefix(dat):
    # if typ is datetime.datetime and time-part is 0:0:0,
    # covert to datetime.date (assume xlsx cell-type is "Date").
    if (type(dat) == dt.datetime and
        (dat.hour, dat.minute, dat.second) == (0, 0, 0)):
        dat = dat.date()
    return dat

def transform(l):
    l = [_transmap(f) for f in l]
    l = [_datefix(f) for f in l]
    l = [_stringify(f) for f in l]
    return l
    
def write_csv(data, outfile):
    with open(outfile, 'wb') as fout:
        writer = csv.writer(fout, dialect='RFC4180')
        writer.writerows(data)

def main():
    csv.register_dialect(u'RFC4180', RFC4180)
    xlsxfile = parseargs()['file']
    out_prefix = os.path.splitext(os.path.basename(xlsxfile))[0]
    out_dir = parseargs()['o']
    wb = op.load_workbook(xlsxfile, data_only=True)
    for sn in wb.sheetnames:
        outfile = os.path.join(out_dir, out_prefix + '_' +
                               re.sub(r'\s+', '_', sn) + '.csv')
        data = []
        sheet = wb.get_sheet_by_name(sn)
        for l in sheet.values:
            data.append(transform(l))
        write_csv(data, outfile)


if __name__ == '__main__':
    main()

