#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    rows, cols = len(arr), len(arr[0])
    i, j, r, check, maxSum, sum = 0, 0, 0, 0, -9999, 0
    
    while (r+i < rows):
        if (r + i == rows-2):
            break
        c = 0
        while (c+j < cols):
            if (c + j == cols-2):
                break 
            sum = 0
            for count in range(3):
                sum += arr[r+i][c+j+count]
                sum += arr[r+i+2][c+j+count]
                check += 1
                if (check == 3):
                    sum += arr[r+1][c+1]
                    check = 0
                count += 1 
            c += 1
            if (sum > maxSum):
                maxSum = sum
        r += 1
    return maxSum
              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
