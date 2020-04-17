#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min, max, maxBreak, minBreak = None, None, 0, 0
    for score in scores:
        if min == None or max == None:
            min, max = score, score
        if score > max:
            max = score
            maxBreak += 1
        if score < min:
            min = score
            minBreak += 1
        
    result = [maxBreak, minBreak]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
