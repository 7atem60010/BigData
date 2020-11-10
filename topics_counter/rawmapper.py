#!/usr/bin/python3

import sys
from json import loads
lst = [

        ]
for line in sys.stdin:
    dct = loads(line)
    t = dct["body"].split()[0]
    k = dct["subreddit"]+','+t
    #SOME NLP SHIT GOES HERRE
    #v = ??
    v = 1
    if k in lst:
        print(k,v,sep='\t')


