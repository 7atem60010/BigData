#!/usr/bin/python3

import sys
i = 0
for line in sys.stdin:
    i += 1
    if i > 20:
        break
    print(line.strip())
