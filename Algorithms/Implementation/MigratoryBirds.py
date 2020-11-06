#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr.sort()
    
    count = 0
    max_count = -1
    bird_type = -1
    result = 0
    
    for bird in arr:
        if bird == bird_type:
            count += 1
        else:
            bird_type = bird
            count = 1
            
        if count > max_count:
            max_count = count
            result = bird
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
