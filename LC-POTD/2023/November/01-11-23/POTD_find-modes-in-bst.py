# November 1, 2023
# Find Mode in Binary Search Tree
# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # create a traversal array
        self.traversal = []

        # we need to do inorder traversal
        def inorder(root):
            # root is empty
            if not root:
                return
            # append the root to traversal
            self.traversal.append(root.val)
            # traverse left
            inorder(root.left)
            # traverse right
            inorder(root.right)
        
        # start the traversal
        inorder(root)

        # create a dictionary using Counter library
        traversal_freq = collections.Counter(self.traversal)

        # find the maximum from the values
        m = max(traversal_freq.values())

        # create a list which holds the modes and return it
        return [mode for mode in traversal_freq if traversal_freq[mode] == m]