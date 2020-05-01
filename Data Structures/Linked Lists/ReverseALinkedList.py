#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    # * We have two conditions in this if statement.
    # This first condition immediately returns null
    # when the list is null. The second condition returns
    # the final node in the list. That final node is sent
    # into the "remaining" Node below.
    if head == None or head.next == None:
        return head
    
    # * When the recursion creates the stack for A -> B -> C
    # (RevA(RevB(RevC()))) it will stop at the last node and
    # the recursion will end, beginning the unraveling of the
    # nested functions from the inside, out. 
    
    remaining = reverse(head.next)

    # * Now we have the "remaining" node returned and accessible
    # to the node prior. This remaining node will be returned
    # by each function as the recursive stack unravels.

    # Assigning head to head.next.next where A is the head
    # and B is after A, (A -> B), would set B's pointer to A,
    # reversing their direction to be A <- B.
    head.next.next = head

    # * Now that those two elements are reversed, we need to set
    # the pointer of the new tail-node to null.
    head.next = None

    # * Now we return remaining so that remaining is always
    # reassigned to itself and is eventually returned by the
    # first function call.
    return remaining

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
