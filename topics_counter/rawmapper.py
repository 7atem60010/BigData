#!/usr/bin/python3

import sys
from json import loads
lst = [

        ]
for line in sys.stdin:
    dct = loads(line)
    #SOME NLP SHIT GOES HERRE
    #v = ??
    k = dct["subreddit"]
    if k in lst:
        #t = 'huuh'
        t = dct["body"].split()[0]
        v = 1
        k += ','+t
        print(k,v,sep='\t')


