#!/usr/bin/python3

import sys
from json import loads
for line in sys.stdin:
    dct = loads(line)
    print(dct["author"], 1, sep='\t')
