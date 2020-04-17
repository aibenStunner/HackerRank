#!/bin/python3

import os
import sys
import heapq

def addNum(num, lowers, highers):
    if not lowers or num < -lowers[0]:
        heapq.heappush(lowers,-num)
    else:
        heapq.heappush(highers,num)
    
def rebalance(lowers, highers):
    if len(lowers) - len(highers) >= 2:
        heapq.heappush(highers,-heapq.heappop(lowers))
    elif len(highers) - len(lowers) >= 2:
        heapq.heappush(lowers,-heapq.heappop(highers))

def getMedian(lowers, highers):
    if len(lowers) == len(highers):
        return (-lowers[0] + highers[0])/2
    if len(lowers) > len(highers):
        return float(-lowers[0])
    else:
        return float(highers[0])

#
# Complete the runningMedian function below.
#
def runningMedian(a):
    maxHeap = []  # max heap, vals should go in and come out negated
    minHeap = []  # min heap, vals should go in positive
    result = []
    for v in a:
        addNum(v, maxHeap, minHeap)
        rebalance(maxHeap, minHeap)
        result.append(round(getMedian(maxHeap, minHeap),1))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

