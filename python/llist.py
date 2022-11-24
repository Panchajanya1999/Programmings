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

    # prints the linked list
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    # append will insert an element at the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # prepend will insert an element at the beginning of the linked list
    def prepend():
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    # insert a node after a given node
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is non-existent")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        self.head = new_node

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.insert_after_node(llist.head.next,"E")

llist.print_list()





