# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys

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

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    stack = Stack()
    maxes = Stack()

    n = int(input())
    for i in range(n):
        query = list(map(int, input().rstrip().split()))
        if query[0] == 1:
            if not maxes.isEmpty():
                if maxes.peek() <= query[1]:
                    maxes.push(query[1])
                stack.push(query[1])
            else:
                maxes.push(query[1])
                stack.push(query[1])
        elif query[0] == 2:
            if stack.peek() == maxes.peek():
                maxes.pop()
            stack.pop()
        elif query[0] == 3:
            fptr.write(str(maxes.peek()) + '\n')

    fptr.close()
