#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort()
    peopleFlowerCount = [0 for x in range(k)]
    personIndex, result = 0, 0
    for price in reversed(c):
        result += (peopleFlowerCount[personIndex] + 1) * price
        peopleFlowerCount[personIndex] += 1
        personIndex = (personIndex+1) % k
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
