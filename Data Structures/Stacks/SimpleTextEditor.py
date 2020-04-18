# Enter your code here. Read input from STDIN. Print output to STDOUTimport os
import os

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
    
    S = ""
    opStack = Stack()

    n = int(input())

    for i in range(n):
        query = list(map(str, input().rstrip().split()))
        if query[0] == '1':       # Append
            opStack.push(S) 
            S += query[1]
        elif query[0] == '2':     # Delete
            opStack.push(S)
            S = S[:-int(query[1])]
        elif query[0] == '3':     # Print
            fptr.write(str(S[int(query[1])-1]) + '\n')
        elif query[0] == '4':     # Undo
            S = opStack.pop()

    fptr.close()
