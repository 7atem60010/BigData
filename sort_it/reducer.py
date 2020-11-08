#!/usr/bin/python3

import sys

word = None
count = 0

for line in sys.stdin:
    key, value = line.strip().split()
    print(key, value)
    #print("haha\tlol")
