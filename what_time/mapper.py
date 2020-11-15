#!/usr/bin/python3

import sys
from json import loads
lst = [
"AskReddit","funny","pcmasterrace",

        ]
from datetime import datetime
for line in sys.stdin:
    data = loads(line)
    sub = data['subreddit']
    if sub in lst:
        time = data['created_utc']
        ts = int(time)
        ts = int(datetime.utcfromtimestamp(ts).strftime('%H'))//3
        sub += ',' + str(ts)
        print(sub,1, sep='\t')
