#!/usr/bin/python3

import sys
from json import loads
for line in sys.stdin:
    dct = loads(line)
    if dct["author"] != "[deleted]":
        print(dct["author"], 1, sep='\t')
