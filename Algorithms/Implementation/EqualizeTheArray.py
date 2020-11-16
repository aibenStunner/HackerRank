#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    freq = {}
    
    for num in arr:
        if num in freq: freq[num] += 1
        else: freq[num] = 1
    
    maxi = max(list(freq.values()))
    
    return len(arr) - maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
