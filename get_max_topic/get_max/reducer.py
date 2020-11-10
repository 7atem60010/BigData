#!/usr/bin/python3

import sys

max_word = [None,None,None]
mx = [0,0,0]

for line in sys.stdin:
    k,v = line.strip().split()
    v = int(v)
    if v>mx[0]:
        max_word[2] = max_word[1]
        mx[2] = mx[1]
        max_word[1] = max_word[0]
        mx[1] = mx[0]
        max_word[0] = k
        mx[0] = v
    elif v>mx[1]:
        max_word[2] = max_word[1]
        mx[2] = mx[1]
        max_word[1] = k
        mx[1] = v
    elif v>mx[2]:
        max_word[2] = k
        mx[2] = v

for i in range(3):
    print(max_word[i], mx[i])
