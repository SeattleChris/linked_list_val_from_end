#!/bin/python3

import os

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

#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNode(head, positionFromTail):
    curr = end = head
    for _ in range(positionFromTail):
        if end is None:
            raise ValueError(f"The Linked List is not long enough for {positionFromTail=}")
        end = end.next
    while end.next is not None:
        curr, end = curr.next, end.next
    return curr.data

# Main setup

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    tests = int(input())
    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        position = int(input())
        result = getNode(llist.head, position)
        fptr.write(str(result) + '\n')
    fptr.close()
