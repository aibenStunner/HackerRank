import math
import os
import random
import re
import sys

def sd(arr, n):
    u = mean(arr)
    sd = 0
    for x in arr:
        sd += (x-u)**2
    return float(math.sqrt(sd/n))

def mean(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

    return float(sum/len(arr))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    SD = round(sd(arr, n), 1)

    fptr.write(str(SD)+'\n')
    fptr.close()
