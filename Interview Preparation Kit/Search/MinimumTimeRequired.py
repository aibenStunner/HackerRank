#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    smallest = min(machines)
    largest = max(machines)

    minRate = math.ceil(goal / len(machines))
    minDays = minRate * smallest
    maxDays = minRate * largest

    while minDays < maxDays:
        midDays = math.floor((minDays + maxDays) / 2)
        totalDays = sum([math.floor(midDays / machine) for machine in machines])
        
        if totalDays < goal:
            minDays = midDays + 1
        else:
            maxDays = midDays
    return minDays

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
