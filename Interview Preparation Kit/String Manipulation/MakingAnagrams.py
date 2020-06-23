#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count = 0
    for i in range(ord('a')-1, ord('z')+1):
        sum_a = sum(char == chr(i) for char in a)
        sum_b = sum(char == chr(i) for char in b)
        count += abs(sum_a - sum_b)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
