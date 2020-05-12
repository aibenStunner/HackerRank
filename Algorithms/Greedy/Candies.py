    #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    left = [1 for x in range(n)]
    right = [1 for x in range(n)]

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            left[i] = left[i-1] + 1
    for i in reversed(range(n-1)):
        if arr[i] > arr[i+1]:
            right[i] = right[i+1] +1
    return sum([max(l,r) for (l,r) in zip(left, right)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
