#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the maximumSum function below.
def maximumSum(a, m):
    prefix = []
    current_sum = 0
    max_mod = 0
    for num in a:
        current_sum = (num + current_sum) % m
        max_mod = max(max_mod, current_sum)
        index = bisect.bisect_left(prefix, current_sum+1)
        if index < len(prefix):
            max_mod = max(max_mod, (current_sum - prefix[index] + m) % m)
        bisect.insort_left(prefix, current_sum)
    return max_mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
