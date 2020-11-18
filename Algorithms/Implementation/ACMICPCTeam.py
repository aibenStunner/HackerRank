#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    max_topic = -1
    permutations = 0
    m = len(topic[0])
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            
            n = compare(topic[i], topic[j])
    
            if n > max_topic:
                permutations = 1
                max_topic = n
            
            elif n == max_topic:
                permutations += 1
            
    return [max_topic, permutations]
        
def compare(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] == '1' or b[i] == '1':
            count += 1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
