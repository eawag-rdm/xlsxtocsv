# _*_ coding: utf-8 _*_ 
"""
Defines csv dialect according to RFC 4180 and registers it.
"""

import csv

class RFC4180(csv.Dialect):
    def __init__(self):
        csv.Dialect.__init__(self)
        csv.register_dialect(u'RFC4180', self)
    delimiter = b','
    doublequote = True
    escapechar = None
    lineterminator = b'\r\n'
    quotechar = b'"'
    quoting = csv.QUOTE_MINIMAL
    skipinitialspace = False
    stric = True


