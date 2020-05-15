#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    MOD = 1000000007
    result = 0
    a = [1 for x in range(len(n))]      # weight
    b = [1 for x in range(len(n))]      # weight sum

    for i in range(1, len(n)):
        a[i] = (10 * a[i-1]) % MOD
        b[i] = (b[i-1] + a[i]) % MOD
    
    for  i in range(len(n)):
        result += (int(n[i]) * b[len(n)-i-1] * (i+1)) % MOD
        result %= MOD
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
