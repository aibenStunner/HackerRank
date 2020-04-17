#!/bin/python3

import os
import sys

class minHeap:
    def __init__(self):
        self.items = []
        self.size = len(self.items)

    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1
    
    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2
    
    def getParentIndex(self, childIndex):
        return int((childIndex - 1) / 2)
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.items[self.getRightChildIndex(index)]

    def parent(self, index):
        return self.items[self.getParentIndex(index)]

    def swap(self, indexOne, indexTwo):
        temp = self.items[indexOne]
        self.items[indexOne] = self.items[indexTwo]
        self.items[indexTwo] = temp
    
    def pop(self):
        if self.size == 0:
            raise Exception("Empty Heap!!")
        else:
            item  = self.items[0]
            self.items[0] = self.items[self.size - 1]
            del(self.items[self.size - 1])
            self.size = len(self.items)
            self.heapifyDown()
            return item
    
    def peek(self):
        if self.size == 0:
            raise Exception("Empty Heap!!")
        else:
            return self.items[0]

    def add(self, item):
        self.items.append(item)
        self.size = len(self.items)
        self.heapifyUp()
    
    def heapify(self, arr):
        for elem in arr:
            self.add(elem)

    def heapifyUp(self):
        index = self.size - 1
        while (self.hasParent(index) and self.parent(index) > self.items[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)
            if(self.items[index] < self.items[smallerChildIndex]):
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex

#
# Complete the cookies function below.
#
def cookies(k, A):
    qHeap = minHeap()
    qHeap.heapify(A)
    count = 0
    try:
        while qHeap.peek() < k:
            count += 1
            a, b = qHeap.pop(), qHeap.pop()
            newCookie = (1*a)+(2*b)
            qHeap.add(newCookie)
        return count
    except:
        return -1
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()


# def cookies(k, A):
#         from heapq import heappop,heappush,heapify

#         heapify(A)
#         fC = 0
#         try:
#                 while A[0] < k:
#                         fC+=1
#                         c1 = heappop(A)
#                         c2 = heappop(A)
#                         newCookie=(1*c1)+(2*c2)
#                         heappush(A,newCookie)
#                 return fC
#         except:
#                 return -1
