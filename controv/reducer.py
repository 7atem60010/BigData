#!/usr/bin/python3

import sys

index = None
count = 0
scores = 0
avg  = 0

for line in sys.stdin:
    #print('a7a\tlol')
    #continue
    key, score, counts = line.strip().split()
    #key = 'a7a'
    #score = 1
    #counts = 1
    if index is None:
        index = key
    elif index != key:
        avg  = scores / count
        print ('%s\t%s\t%s'% ( index, count , avg  ))
 
        index = key
        count = 0
    
    count += int(counts)
    scores += int(score)     
if count != 0 and index is not None:
    avg = scores/count
    print (1,2,sep='\t')
    pass
else:
    print('a7a\t7')
