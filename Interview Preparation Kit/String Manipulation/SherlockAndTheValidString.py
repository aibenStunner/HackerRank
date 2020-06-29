#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    # create a list containing frequency count of each distinct element
    freqs = [s.count(letter) for letter in set(s)]

    if max(freqs) == min(freqs):
        return 'YES'
    # if difference between highest count and lowest count is 1
    # and there is only one letter with highest count, 
    # then return 'YES' (because we can subtract one of these 
    # letters and max=min , i.e. all counts are the same)
    elif freqs.count(max(freqs)) == 1 and max(freqs) - min(freqs) == 1:
        return 'YES'
    # if the minimum count is 1
    # then remove this letter, and check whether all the other
    # counts are the same
    elif freqs.count(min(freqs)) == 1:
        freqs.remove(min(freqs))
        if max(freqs) == min(freqs):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
