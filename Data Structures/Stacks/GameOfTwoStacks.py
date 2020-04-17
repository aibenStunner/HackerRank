#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    i = 0
    while i < len(a) and x >= a[i]:
        x -= a[i]
        i += 1
    
    ans = i
    j = 0
    for p in b:
        j += 1
        x -= p
        
        while x < 0 and i > 0:
            i -= 1
            x += a[i]
        
        if x >= 0: ans = max(ans, j + i)
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)
        
        fptr.write(str(result) + '\n')

    fptr.close()
