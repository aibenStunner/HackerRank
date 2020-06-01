#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    if len(ar) == 0:
        return 0

    num_pairs = 0
    temp_colors = []
    for color in ar:
        if color in temp_colors:
            num_pairs += 1
            temp_colors.remove(color)
        else:
            temp_colors.append(color)
    return num_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
