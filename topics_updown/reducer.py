#!/usr/bin/python3

import sys

index = None
max = 0
min = 1000000
count_ups = 0  
#count_downs = 0

for line in sys.stdin:
    key, ups  = line.strip().split()
    if index is None:
        index = key
    elif index != key:
        print ('%s\t%d'% ( index, count_ups ))
 
        index = key
        count_ups = 0  
        #count_downs = 0

    count_ups += int(ups)
    #count_downs += int(downs)

print ('%s\t%d'% ( index, count_ups  ))
