import math
import os
import random
import re
import sys

def median(arr,n):
    arr.sort()
    if n%2==1:
        median = arr[(n//2)]
    if n%2==0:
        median = (arr[n//2 -1]+arr[(n//2)])/2    
    return float(median), n//2

def quartile(arr, n):
    quartiles = []
    if n%2==1:
        q2, p2 = median(arr, n)
        q1, _ = median(arr[:p2], len(arr[:p2]))
        quartiles.append(q1)
        quartiles.append(q2)
        q3, _ = median(arr[p2+1:], len(arr[p2+1:]))
        quartiles.append(q3)
        return quartiles
    if n%2==0:
        q2, p2 = median(arr,n)
        q1, _ = median(arr[:(len(arr)//2)], len(arr[:(len(arr)//2)]))
        quartiles.append(q1)
        quartiles.append(q2)
        q3, _ = median(arr[(len(arr)//2):], len(arr[(len(arr)//2):]))
        quartiles.append(q3)
        return quartiles

def interquartile(arr, freqArr, n):
    expandArr = []
    for i in range(n):
        for j in range (freqArr[i]):
            expandArr.append(arr[i])
    quartiles = quartile(expandArr, len(expandArr))
    return(round((quartiles[2]-quartiles[0]), 1))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    freqArr = list(map(int, input().rstrip().split()))
    iQR = interquartile(arr, freqArr, n)

    fptr.write(str(iQR) + '\n')
    fptr.close()
