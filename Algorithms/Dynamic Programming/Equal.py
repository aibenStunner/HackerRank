#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equal function below.
def find(arr, mini):
    count = 0
    for i in range(len(arr)):
        temp = arr[i] - mini
        count += temp//5 + temp%5//2 + temp%5%2
    return count

def equal(arr):
    res = sys.maxsize 
    for i in range(5):
        res = min(res, find(arr, min(arr) - i))
    return int(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
