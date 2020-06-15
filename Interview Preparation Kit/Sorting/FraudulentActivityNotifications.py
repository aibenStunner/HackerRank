#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    # initialize counting sort array
    counting_sort_list = [0] * 201
    end = d

    # count sort
    for i in range(end):
        counting_sort_list[expenditure[i]] += 1
    current = 0
    notifications = 0

    # determine if even or odd to aid median getting
    if d%2 == 0:
        median_position = d // 2
    else:
        median_position = d // 2 + 1
    
    expenditure_length = len(expenditure)

    # move along expenditure list
    while end < expenditure_length:
        median = get_median(counting_sort_list, d, median_position)
        if expenditure[end] >= median * 2:
            notifications += 1

        # modify the counting_sort_list
        counting_sort_list[expenditure[current]] -= 1
        counting_sort_list[expenditure[end]] += 1
        current += 1
        end += 1
    return notifications


def get_median(counting_sort_list, d, median_position):
    counter, left = 0, 0

    # find number where we pass through the median
    while counter < median_position:
        counter += counting_sort_list[left]
        left += 1
    
    # step back one time
    right = left
    left -= 1
    
    # if odd,  or both left and right of even are same order
    if counter > median_position or d%2 != 0:
        return left
    else:
        # find right value for even
        while counting_sort_list[right] == 0:
            right += 1
        return(left+right) / 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
