#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    d = {k:v for v, k in enumerate(arr)}
    i = 0
    m = len(arr)
    while k > 0 and m > 1:
        if arr[i] != m:
            arr[i], arr[d[m]] = arr[d[m]], arr[i]
            d[arr[d[m]]], d[m] = d[m], i          
            k -= 1
        m -= 1
        i += 1
    return arr
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
