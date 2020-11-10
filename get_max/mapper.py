#!/usr/bin/python3

import sys
from json import loads
for line in sys.stdin:
    k,v = line.strip().split()
    print(k,v,sep='\t')
