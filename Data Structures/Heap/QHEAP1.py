import os

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

    def peek(self):
        if self.size == 0:
            raise Exception("Empty Heap!!")
        else:
            return self.items[0]
    
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

    def add(self, item):
        self.items.append(item)
        self.size = len(self.items)
        self.heapifyUp()
    
    def remove(self, item):
        self.items.remove(item)
        self.size = len(self.items)
        self.heapifyDown()

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

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    qheap = minHeap()
    n = int(input())
    for i in range(n):
        query = list(map(int, input().rstrip().split()))
        if query[0] == 1:
            qheap.add(query[1])
        elif query[0] == 2:
            qheap.remove(query[1])
        elif query[0] == 3:
            # fptr.write(str(qheap.peek()) + '\n')
            print(qheap.peek())

    fptr.close()
