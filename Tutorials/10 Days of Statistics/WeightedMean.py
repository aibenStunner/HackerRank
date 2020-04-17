import math
import os
import random
import re
import sys


def weightedMean(arr, weights, n):
    weight = 0
    sW = 0
    for i in range(n):
        weight += arr[i]*weights[i]
        sW += weights[i]
    return float(weight/sW)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    
    WW = round(weightedMean(arr,weights,n), 1)
    fptr.write(str(WW) + '\n')
    fptr.close()
