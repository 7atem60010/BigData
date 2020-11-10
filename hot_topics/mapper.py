#!/usr/bin/python3

import sys
from json import loads
lst = [
"AskReddit","funny","pcmasterrace",

        ]
for line in sys.stdin:
    dct = loads(line)
    k = dct["subreddit"]
    #SOME NLP SHIT GOES HERRE
    #v = ??
    v = 1
    if k in lst:
        print(k,v,sep='\t')


