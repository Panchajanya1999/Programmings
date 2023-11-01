# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 14, 2023
# Find common nodes in two BSTs
# Link - https://practice.geeksforgeeks.org/problems/print-common-nodes-in-bst/1

#User function Template for python3


class Solution:
    
    #Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        # Initialize a global variable to store the inorder traversal of a BST
        arr = []

        # Define a helper function to perform inorder traversal of a BST
        def inorder(root):
            nonlocal arr  # Use nonlocal keyword to access the arr variable defined in the outer scope
            stack = []  # Initialize an empty stack to keep track of nodes
            curr = root  # Start from the root node
            while True:
                if curr:  # If the current node exists, push it onto the stack and move to its left child
                    stack.append(curr)
                    curr = curr.left
                elif stack:  # If the current node is None and the stack is not empty, pop a node from the stack, add it to the arr list, and move to its right child
                    curr = stack.pop()
                    arr.append(curr.data)
                    curr = curr.right
                else:  # If both the current node is None and the stack is empty, we have traversed the entire BST
                    break

        # Perform inorder traversal of the first BST and store the result in arr1
        inorder(root1)
        arr1 = arr
        arr = []

        # Perform inorder traversal of the second BST and store the result in arr2
        inorder(root2)
        arr2 = arr

        # Return the sorted list of nodes that are common in both BSTs
        return sorted(list(set(arr1) & set(arr2)))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root1=buildTree(s)
        s=input()
        root2=buildTree(s)
        ob = Solution()
        res = ob.findCommon(root1, root2)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends


