#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result = []
    
    while len(arr) != 0:
        mini = min(arr)
        result.append(len(arr))
        
        arr = list(map(lambda x: x-mini, arr))
        arr = list(filter(lambda x: x!=0, arr))
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
