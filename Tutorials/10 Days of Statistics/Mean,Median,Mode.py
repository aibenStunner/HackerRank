import math
import os
import random
import re
import sys
import itertools

def mode(arr,n):
    arr.sort()
    mode = None
    tempCount = 0
    for i in range(n):
        count = arr.count(arr[i])
        if count > tempCount:
            tempCount = count
            mode = arr[i]
    return int(mode) 

def median(arr,n):
    arr.sort()
    if n%2==1:
        print(arr)
        median = arr[(n//2)]
    if n%2==0:
        median = (arr[n//2 -1]+arr[(n//2)])/2    
    return float(median)

def mean(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

    return float(sum/len(arr))

def mmm(arr, n):
    MMM = []
    MMM.append(round(mean(arr), 1))
    MMM.append(round(median(arr, n), 1))
    MMM.append(mode(arr, n))
    return MMM
    # Mean = round(mean(arr), 1)
    # Median = round(median(arr, n), 1)
    # Mode = mode(arr, n)
    # print(Mean)
    # print(Median)
    # print(Mode)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    MMM = mmm(arr, n)

    fptr.write('\n'.join(map(str, MMM)))
    fptr.close()
