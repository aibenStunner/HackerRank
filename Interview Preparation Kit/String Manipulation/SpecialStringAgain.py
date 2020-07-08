#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0

    for i in range(len(s)):
        count += 1
        for j in range(i+1, len(s)):
            if s[i] != s[j]:
                if 2*j-i < len(s) and s[i:j] == s[j+1:2*j-i+1]:
                    count += 1
                    break
                else:
                    break
            else:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
