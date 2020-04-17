#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for i in range(n+1)]
    for query in queries:
        arr[query[0] - 1] += query[2]
        if query[1] <= len(arr):
            arr[query[1]] -= query[2]
    max = x = 0
    for i in arr:
        x = x + i
        if(max < x):
            max = x
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
