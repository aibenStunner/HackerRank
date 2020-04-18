#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
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

def isBalanced(s):
    stack = Stack()
    pushChars, popChars = "<({[", ">)}]"
    for char in s:
        if char in pushChars:
            stack.push(char)
        elif char in popChars:
            if stack.isEmpty():
                return "NO"
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(char)]
                if stackTop != balancingBracket:
                    return "NO"
        else:
            return "NO"
    if stack.isEmpty():
        return "YES"
    else:
        return "NO"
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
