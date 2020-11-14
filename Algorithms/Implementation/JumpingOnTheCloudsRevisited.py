#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    i = 0
    
    while True:
        i, energy = (i+k)%n, energy-1
        
        if c[i] == 1:
            energy -= 2
            
        if i == 0:
            break
    
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
