# POTD - October 17, 2023
# Validate Binary Tree Nodes
# Link - https://leetcode.com/problems/validate-binary-tree-nodes/


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Dictionary to store parent-child relationships
        parent = {}
        
        # Enumerate through each parent and its corresponding children
        for p, child in enumerate(zip(leftChild, rightChild)):
            # Iterate through the children
            for c in child:
                # If the child is -1, it means there's no child, so skip
                if c == -1:
                    continue 
                
                # If the child already has a parent, it's not a valid binary tree
                if c in parent:
                    return False 
                
                # If the parent already has a child and it's not the current child, it's not a valid binary tree
                if p in parent and parent[p] == c:
                    return False 
                
                # Assign the current parent to the child
                parent[c] = p
        
        # Find the root(s) of the tree (nodes with no parent)
        root = set(range(n)) - set(parent.keys())
        
        # If there is more than one root or no root, it's not a valid binary tree
        if len(root) != 1:
            return False 
        
        # Helper function to count the number of nodes in the subtree rooted at a given node
        def count(root):
            if root == -1:
                return 0
            return 1 + count(leftChild[root]) + count(rightChild[root])
        
        # Check if the number of nodes in the tree is equal to the total number of nodes
        return count(root.pop()) == n
