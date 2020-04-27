#!/bin/python3

import os
import sys

#
# Complete the andXorOr function below.
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


def andXorOr(a):
    # equation reduction
    # (((A B) ^ (A + B)) (A ^ B)) =           
    # apply A ^ B = (A'B) + (A B')
    # ( ((A B)' (A + B)) + ((A B) (A + B)')) (A ^ B)) =   
    # apply DeMorgan law (X+Y+...)'=X'Y'Z'... and (XYZ...)'=X'+Y'+...
    # ( ((A' + B') (A + B)) + ((A B) (A' B'))) (A ^ B)) = 
    # apply Distributive Law X(Y+Z) = XY + XZ
    # (A'A + A'B + AB' + BB' + AA' + BB') (A ^ B) =       
    # apply X+X=X, XX=X
    # (A'B + AB') (A ^ B) =
    # (A ^ B) (A ^ B) = A ^ B = A xor B

    stack = Stack()
    maxSi = a[0] ^ a[1]
    for elem in a:
        while not stack.isEmpty():
            Si = elem ^ stack.peek()
            if Si > maxSi:
                maxSi = Si
            if elem < stack.peek():
                stack.pop()
            else:
                break
        stack.push(elem)
    return maxSi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
