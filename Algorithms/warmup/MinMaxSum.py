 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sigma = []
    temp = arr
    for _ in range(len(arr)):
        tempSum = 0
        __ = arr[_]
        del temp[_]
        
        for n in temp:
            tempSum += n
        sigma.append(tempSum)

        temp.insert(_, __)
        
    print(min(sigma), max(sigma))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
