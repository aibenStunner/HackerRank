#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    sortedCost = sorted(cost)
    for i in range(len(sortedCost)):
        complement = money - sortedCost[i]
        location = binarySearchIterative(sortedCost, complement, i+1)
        if location >= 0 and location < len(sortedCost) and sortedCost[location] == complement:
            result = getIndices(cost, sortedCost[i], complement)
            print(*result)
    
def binarySearchIterative(arr, x, left):
    right = len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def getIndices(cost, value1, value2):
    index1 = getIndex(cost, value1, -1) 
    index2 = getIndex(cost, value2, index1)
    index1 += 1
    index2 += 1
    return [min(index1, index2), max(index1, index2)]

def getIndex(cost, value, exclude):
    for i in range(len(cost)):
        if cost[i] == value and i != exclude:
            return i
    return -1

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)




# def binarySearchRecursive(arr, x, left, right):
#     if left > right:
#         return False
#     mid = (left + right) // 2
#     if arr[mid] == x:
#         return True
#     elif x < arr[mid]:
#         return binarySearchRecursive(arr, x, left, mid-1)
#     else:
#         return binarySearchRecursive(arr, x, mid+1, right)
