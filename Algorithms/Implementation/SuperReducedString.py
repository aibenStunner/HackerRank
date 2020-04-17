#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    i=0
    while i < len(s):
        if i+1 == len(s):
            break
        if s[i] == s[i+1]:
            s = s.replace(s[i]+s[i+1], '',1)
            i = 0
        else:
            i += 1
    result = s
    if not s:
        result = "Empty String"      
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = superReducedString(s)

    fptr.write(result + '\n')
    fptr.close()
