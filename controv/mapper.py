#!/usr/bin/python3

import sys
import json



#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    data = json.loads(line)
    if data['ups']+data['downs'] == 0:
        con_ver = 0
    else:
        con_ver = data['score']/ (data['ups']+data['downs'])
    print(data['subreddit'] , con_ver )

