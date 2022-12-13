/* 
Linked list programming in C using structure for demonstration purpose
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>


// Node contains data and next
struct Node {
    int data;
    struct Node* next;
};

/* code to print the linked list*/
void printlist(struct Node* n) {
    while (n != NULL) {
        printf(" %d", n -> data);
        n = n -> next;
    }
}

/* Adding a node to the front of the node*/
void prepend(struct Node** head_ref, int ndata) {
    
    // allocate the node
    struct Node* new_node = ( struct Node* )malloc(sizeof( struct Node ));

    // put in the data
    new_node -> data = ndata;
    
    // make next of new node as head
    new_node -> next = (*head_ref);

    // move the head to point to the new node
    (*head_ref) = new_node;
    
}

/* Adding a node after a given node */
void append(struct Node* prev_node, int ndata) {

    // check if the given prev_node is NULL, since we cannot append to
    // a NULL node
    if (prev_node == NULL) {
        printf("given previous node is NULL");
        return;
    }

    // Allocate a new node
    struct Node* new_node = ( struct Node* )malloc(sizeof( struct Node ));

    // put in the data
    new_node -> data = ndata;

    // make next of new_node as next of prev_node
    new_node -> next = prev_node -> next;

    // move the next of prev_nnode to new node
    prev_node -> next = new_node;

}

/* Append at the end */
void appendend(struct Node** head_ref, int ndata) {

    // allocate a node
    struct Node* new_node = ( struct Node* )malloc(sizeof( struct Node ));

    struct Node *last = *head_ref;

    // put in the data
    new_node -> data = ndata;

    // make the next as null
    new_node -> next = NULL;


}

/* Deltion from a linked list
    -- Deletion from Beginning
*/
void deleteN(Node ** head, int pos) {
    Node * temp;
    Node * prev;
    temp = *head;
    prev = *head;

    for (int i = 0; i < pos; i++) {
        if (i == 0 && pos == 1) {
            *head = (*head) -> next;
            free(temp);
        }
        else {
            if ( i == pos - 1 && temp) {
                prev -> next = temp -> next;
                free(temp);
            }
            else{
                prev = temp;

                
            }
        }
    }

}

// creating a linked lust with 3 nodes
int main() {
    struct Node* head = NULL;
    struct Node* second = NULL;
    struct Node* third = NULL;

    // allocate three nodes in heap
    head = ( struct Node* )malloc(sizeof( struct Node ));
    second = ( struct Node* )malloc(sizeof( struct Node ));
    third = ( struct Node* )malloc(sizeof( struct Node ));

    // we will be keeping three data to each node,
    // head will hold 1, second will hold 2 while third will hold 3
    head -> data = 1;
    second -> data = 2;
    third -> data = 3;

    // point the next nodes
    head -> next = second;
    second -> next = third;
    third -> next = NULL;

    // print the linked list
    printlist(head);

    return 0;
}