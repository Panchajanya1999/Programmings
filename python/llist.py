#!/bin/python3

"""
Every linked list consists of nodes. Each node has two components: 
1. Data
2. Pointer to the next node
Data allows us to store the information we want to store in the linked list. It can be
any data type. 
The next component is a pointer to the next node. This allows us to link the nodes.
The start of the linked list is called the head. head is a pointer that points to the beginning
of the linked list.
The last component of a linked list is NULL. 
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None





