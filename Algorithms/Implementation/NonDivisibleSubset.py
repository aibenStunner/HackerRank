#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    remainder_counts = [0] * k
    count = 0
    
    for num in s:
        remainder_counts[num%k] += 1
    
    count = min(remainder_counts[0], 1)
    
    if k % 2 == 0:
        count += 1
    
    for i in range(1, k//2 + 1):
        if i != k - i:
            count += max(remainder_counts[i], remainder_counts[k-i])
    
    return count
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
