#!/usr/bin/python3

import sys
from json import loads

for line in sys.stdin:
    data = loads(line)
    print(data['controversiality'] , data['score'] ,1 , sep='\t' )


