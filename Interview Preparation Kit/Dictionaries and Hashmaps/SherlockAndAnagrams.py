#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n = len(s)
    result = 0
    for i in range(1, n):
        d = {}
        for j in range(n-i+1):
            substring = ''.join(sorted(s[j:j+i]))       # get substrings
            if substring not in d:
                d[substring] = 1
            else:
                d[substring] += 1
            result += d[substring] - 1 
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
