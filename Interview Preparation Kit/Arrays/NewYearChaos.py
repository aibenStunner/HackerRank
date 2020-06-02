#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in reversed(range(1, len(q)+1)):
        if q[i-1] != i:
            if i-2 >= 0 and q[i-2] == i:
                q[i-2], q[i-1] = q[i-1], q[i-2]
                bribes += 1
            elif i-3 >= 0 and q[i-3] == i:
                q[i-3], q[i-2] = q[i-2], q[i-1]
                q[i-1] = i
                bribes += 2
            else:
                print("Too chaotic")
                return
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
