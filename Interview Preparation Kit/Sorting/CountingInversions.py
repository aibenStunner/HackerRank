#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    return mergesort(arr)

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half, right_half = arr[:mid], arr[mid:]

        inversion_count = mergesort(left_half)
        inversion_count += mergesort(right_half)
        inversion_count += merge(arr, left_half, right_half)

        return inversion_count
    return 0

def merge(arr, left_half, right_half):
    i, j, k = 0, 0, 0
    inversion_count = 0
    left_len, right_len = len(left_half), len(right_half)

    while i < left_len and j < right_len:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
            inversion_count += left_len - i
        k +=1 
    while i < left_len:
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < right_len:
        arr[k] = right_half[j]
        j += 1
        k += 1

    return inversion_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


"""MERGE SORT"""
# def mergesort(arr):
#     tempArr = [0] * len(arr)
#     sort(arr, tempArr, 0, len(arr)-1)
#     return arr

# def sort(arr, tempArr, leftStart, rightEnd):
#     if leftStart >= rightEnd:
#         return
#     middle = (leftStart + rightEnd) // 2
#     sort(arr, tempArr, leftStart, middle)
#     sort(arr, tempArr, middle+1, rightEnd)
#     mergeHalves(arr, tempArr, leftStart, rightEnd)

# def mergeHalves(arr, tempArr, leftStart, rightEnd):
#     leftEnd = (leftStart + rightEnd) // 2
#     rightStart = leftEnd + 1
#     size = rightEnd - leftStart + 1

#     left = leftStart
#     right = rightStart
#     index = leftStart

#     while left <= leftEnd and right <= rightEnd:
#         if arr[left] <= arr[right]:
#             tempArr[index] = arr[left]
#             left += 1
#         else:
#             tempArr[index] = arr[right]
#             right += 1
#         index +=1
    
#     for i in range(leftEnd-left+1):
#         tempArr[i+index] = arr[i+left]
    
#     for i in range(rightEnd-right+1):
#         tempArr[i+index] = arr[i+right] 

#     for i in range(size):
#         arr[i+leftStart] = tempArr[i+leftStart]

