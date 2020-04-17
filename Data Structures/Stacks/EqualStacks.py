#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
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

def equalStacks(h1, h2, h3):
    '''Stack implementation'''
    s1 = Stack()
    s2 = Stack()
    s3 = Stack()
    totalHeight = 0

    for i in reversed(range(len(h1))):
       totalHeight += h1[i]
       s1.push(totalHeight)
    totalHeight = 0

    for i in reversed(range(len(h2))):
        totalHeight += h2[i]
        s2.push(totalHeight)
    totalHeight = 0

    for i in reversed(range(len(h3))):
        totalHeight += h3[i]
        s3.push(totalHeight)
    totalHeight = 0

    while True:
        if(s1.isEmpty() or s2.isEmpty() or s3.isEmpty()):
            return 0
        
        s1TotalHeight = s1.peek()
        s2TotalHeight = s2.peek()
        s3TotalHeight = s3.peek()

        if (s1TotalHeight == s2TotalHeight == s3TotalHeight):
            return s1TotalHeight
        
        if (s1TotalHeight >= s2TotalHeight and s1TotalHeight >= s3TotalHeight):
            s1.pop()
        elif (s2TotalHeight >= s3TotalHeight and s2TotalHeight >= s1TotalHeight):
            s2.pop()
        elif (s3TotalHeight >= s2TotalHeight and s3TotalHeight >= s1TotalHeight):
            s3.pop()





    '''Set implementation'''

    # s1 = sum(h1)
    # n1 = set() 
    # for i in h1:
    #     n1.add(s1)
    #     s1 -= i
    # s2 = sum(h2)
    # n2 = set()
    # for i in h2:
    #     n2.add(s2)
    #     s2 -= i
    # s3 = sum(h3)
    # n3 = set()
    # for i in h3:
    #     n3.add(s3)
    #     s3 -= i
    # try :
    #     l = n1.intersection(n2).intersection(n3)
    #     return max(l)
    # except:
    #     return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
