#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    d = defaultdict(lambda: 0)
    f = defaultdict(lambda: 0)
    
    result = []
    for command, value in queries:
        if command == 1:
            f[d[value]] = max(0, f[d[value]] - 1)
            d[value] += 1
            f[d[value]] += 1
        elif command == 2:
            f[d[value]] = max(0, f[d[value]] - 1)
            d[value] = max(0, d[value] - 1)
            if d[value] > 0:
                f[d[value]] += 1
        else:
            if f[value] > 0:
                result.append(1)
            else:
                result.append(0)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
