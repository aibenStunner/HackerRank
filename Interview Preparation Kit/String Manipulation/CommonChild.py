#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    n = len(s1)
    prev, curr = [0]*(n+1), [0]*(n+1) 
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev[j-1]
            else:
                if curr[j-1] > prev[j]:
                    curr[j] = curr[j-1]
                else:
                    curr[j] = prev[j]
        curr, prev = prev, curr
    return prev[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
