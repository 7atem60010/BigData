#!/usr/bin/python3

import sys
from json import loads
for line in sys.stdin:
    dct = loads(line)
    print(dct["subreddit"], 1, sep='\t')
