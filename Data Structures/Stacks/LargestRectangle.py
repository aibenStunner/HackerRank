#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
class Stack:
    def __init__(self):
        self.items = []
    #method to check the stack is empty or not
    def isEmpty(self):
        return self.items == []
    #method for pushing an item
    def push(self, item):
        self.items.append(item)
    #method for popping an item
    def pop(self):
        return self.items.pop()
    #check what item is on top of the stack without removing it
    def peek(self):
        return self.items[-1]
    #method to get the size
    def size(self):
        return len(self.items)
    #to view the entire stack
    def fullStack(self):
        return self.items

def largestRectangle(h):
    heightStack, positionStack = Stack(), Stack()
    tempSize, maxSize = 0, 0
    for pos in range(len(h)):
        height = h[pos]
        if (heightStack.isEmpty() or height > heightStack.peek()):
            heightStack.push(height)
            positionStack.push(pos)
        elif (height < heightStack.peek()):
            while (not heightStack.isEmpty() and height < heightStack.peek()):
                tempHeight = heightStack.pop()
                tempPos = positionStack.pop()
                tempSize = tempHeight * (pos - tempPos)
                maxSize = max(tempSize, maxSize)
            heightStack.push(height)
            positionStack.push(tempPos)
    while not heightStack.isEmpty():
        tempHeight = heightStack.pop()
        tempPos = positionStack.pop()
        tempSize = tempHeight * (len(h) - tempPos)
        maxSize = max(tempSize, maxSize)
    return maxSize


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
