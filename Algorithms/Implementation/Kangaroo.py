#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (v2 > v1 and x2 > x1):
        result = "NO"
        return result
    for i in itertools.count(1):
        if ((x2+(i*v2)) == (x1+(i*v1))) and ((x2+(i*v2))%(x1+(i*v1)) == 0 or (x1+(i*v1))%(x2+(i*v2)) == 0):
            print(i)
            result = "YES"
            return result
        if i == 10000:
            result = "NO"
            return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    
    fptr.write(result + '\n')

    fptr.close()
