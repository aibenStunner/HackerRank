#!/bin/python3

import os
import sys
from heapq import heappush, heappop

#
# Complete the minimumAverage function below.
#
def minimumAverage(customers, n):
    customers.sort(reverse=True)
    minHeap = []
    time_waiting, current_time = 0, 0

    while customers or minHeap:
        while customers and customers[-1][0] <= current_time:
            heappush(minHeap, customers.pop()[::-1])
        if minHeap:
            current_task = heappop(minHeap)
            current_time += current_task[0]
            time_waiting += current_time - current_task[1]
        else:
            heappush(minHeap, customers.pop()[::-1])
            current_time = minHeap[0][1]
    return time_waiting // n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers, n)

    fptr.write(str(result) + '\n')

    fptr.close()
