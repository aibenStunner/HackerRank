#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countArray function below.
def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    MOD = 1000000007                   # modulo value

    a = [0 for x in range(n)]          # ends in x
    b = [0 for x in range(n)]          # doesn't end in x
    a[0] = 1 if x == 1 else 0
    b[0] = 0 if x == 1 else 1

    for i in range(1, n):
        a[i] = b[i-1] % MOD
        b[i] = (a[i-1] * (k-1) + b[i-1] * (k-2)) % MOD
    return a[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
