#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    count = 0
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))

    for num in b:
        count_a = binarySearchIterative(a, num) + 1
        count_c = binarySearchIterative(c, num) + 1
        count += count_a * count_c
    return count

def binarySearchIterative(arr, x):
    left = 0
    right = len(arr) - 1
    index = -1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] <= x:
            index = mid
            left = mid + 1
        else:
            right = mid - 1
    return index  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
