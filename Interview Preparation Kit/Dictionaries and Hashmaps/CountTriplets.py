#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    left_dict = {}
    right_dict = {}
    count = 0

    # populate right dictionary with frequency of numbers
    for num in arr:
        if num not in right_dict:
            right_dict[num] = 1
        else:
            right_dict[num] += 1
    
    # cycle through numbers (using GP a/r, a, a*r)
    for num in arr:
        left_count, right_count = 0, 0
        a = num
        right_dict[a] -= 1

        if a/r in left_dict and a%r == 0:
            left_count = left_dict[a/r]
        if a*r in right_dict:
            right_count = right_dict[a*r]
        
        count += left_count * right_count

        if a not in left_dict:
            left_dict[a] = 1
        else:
            left_dict[a] += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
