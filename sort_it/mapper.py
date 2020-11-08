#!/usr/bin/python3

import sys
import json
for line in sys.stdin:
    word, count = line.strip().split()
    #print(count, word, sep='\t')
    count = int(count)
    print(f"{count:04}\t{word}")
