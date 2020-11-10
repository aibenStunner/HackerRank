#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    result = -1
    a_dict = {}
    
    for n in a:
        if n in a_dict: a_dict[n] += 1
        else: a_dict[n] = 1
    
    for n in a_dict.keys():
        if a_dict[n] + a_dict.get(n+1, 0) > result:
            result = a_dict[n] + a_dict.get(n+1, 0)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
