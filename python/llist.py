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

        if self.head is None:
            print("Linked List is empty.")

        curr_node = self.head
        lstr = ""
        while curr_node:
            lstr += str(curr_node.data) + '-->'
            curr_node = curr_node.next
        print(lstr)
    
    # print the length of the linked list4
    def length(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

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
    def prepend(self, data):
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
    
    # delete head node
    def delete_node(self, key):
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
    
    # delete a certain node at a specified location
    def delete_node_pos(self, pos):
        if pos < 0 or pos >= self.length():
            raise Exception("Invalid Index")
        
        if pos == 0: # removing head
            self.head = self.head.next
            return

        count = 0
        curr_node = self.head
        while curr_node:
            if count == pos - 1:
                curr_node.next = curr_node.next.next
            curr_node = curr_node.next
            count  += 1
    
    # deletion by value
    def delete_node_value(self, value):
        curr_node = self.head
        self.value = value
        while curr_node:
            print(curr_node.data)
            if curr_node.next.data == value:
                curr_node.next = curr_node.next.next
            print(curr_node.data)
            curr_node = curr_node.next


# code execution starts here
if __name__ == '__main__':
    llist = LinkedList()
    arr = ['1', '3', '5', '7', '9']
    for i in arr:
        llist.prepend(i)
    llist.print_list()
    print(f"The length of Linked List is {llist.length()}")
    print("Removes element at 2")
    llist.delete_node_pos(2)
    llist.print_list()
    llist.delete_node_value(3)
