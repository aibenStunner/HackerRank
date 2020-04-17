#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    count = 0
    for num in str(n):
        try:
            if n % int(num) == 0:
                count += 1
        except ZeroDivisionError:
            pass
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)
        print(result)

        fptr.write(str(result) + '\n')

    fptr.close()
