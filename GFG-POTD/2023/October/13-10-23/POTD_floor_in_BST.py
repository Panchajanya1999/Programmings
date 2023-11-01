# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 13, 2023
# Floor is BSt
# Link - https://practice.geeksforgeeks.org/problems/floor-in-bst/1

#User function Template for python3

class Solution:
    def floor(self, root, x):
        # Code here
        ## This approach will take O(h)
        ## instead of required O(n) time.
        if not root:
            return -1  # BST is empty

        floor_value = -1
        while root:
            if root.data == x:
                # we have found the exact match, return it
                return x
            elif root.data < x:
                # If the current node value is smaller than x, update floor value and move to the right subtree
                floor_value = root.data
                root = root.right
            else:
                # If the current node value is greater than x, move to the left subtree
                root = root.left

        return floor_value


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends