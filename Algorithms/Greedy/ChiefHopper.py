#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chiefHopper function below.
def chiefHopper(arr):
    init_energy = 0
    for height in reversed(arr):
        init_energy = (height+init_energy+1) // 2
    return init_energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
