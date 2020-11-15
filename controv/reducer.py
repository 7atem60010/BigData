#!/usr/bin/python3
import sys

index = None
total_con = 0


for line in sys.stdin:
    key, con_ver  = line.strip().split()
    con = con_ver.split(")")
    if index is None:
        index = key
    elif index != key:

        print ('%s\t%s'% ( index, total_con  ))
 
        index = key
        total_con = 0
    
    total_con += int(con_ver[0])

print ('%s\t%s\t'% ( index, total_con  ))
