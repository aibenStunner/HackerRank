#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # no obstacles
    n, w, e, s = n-r_q, c_q-1, n-c_q, r_q-1
    nw, ne, sw, se = min(n, w), min(n, e), min(s, w), min(s, e)

    # obstacles present
    for o in obstacles:
        row, col = o[0], o[1]

        # obstacle in west
        if row == r_q and col < c_q:
            w = min(w, c_q-col-1)
        
        # obstacle in east
        elif row == r_q and col > c_q:
            e = min(e, col-c_q-1)
        
        # obstacle in north
        elif row > r_q and col == c_q:
            n = min(n, row-r_q-1)

        # obstacle in south
        elif row < r_q and col == c_q:
            s = min(n, r_q-row-1)
        
        # obstacle in north-west
        elif row > r_q and col < c_q:
            if row-r_q == c_q-col:
                nw = min(nw, row-r_q-1)
        
        # obstacle in north-east
        elif row > r_q and col > c_q:
            if row-r_q == col-c_q:
                ne = min(ne, row-r_q-1)
        
        # obstacle in south-west
        elif row < r_q and col < c_q:
            if r_q-row == c_q-col:
                sw = min(sw, r_q-row-1)
        
        # obstacle in south-east
        elif row < r_q and col > c_q:
            if r_q-row == col-c_q:
                se = min(se, r_q-row-1)

    return n+w+e+s+nw+ne+sw+se

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
