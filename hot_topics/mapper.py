#!/usr/bin/python3

import sys
from json import loads

for line in sys.stdin:
    k,v = line.strip().split()
    v = int(v)
    print(f'{1e6-v:06}\t{k}')


