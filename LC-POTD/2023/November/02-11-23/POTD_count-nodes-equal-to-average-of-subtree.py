# November 2, 2023
# Link - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/?envType=daily-question&envId=2023-11-02

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # store the result
        res = 0

        # perform preorder postorder traversal and perform mode check
        def posttraverse(node):
            # make res as a global variable
            nonlocal res

            # check if node is empty
            if not node:
                return 0, 0
            
            # left sum, left count = left traversal
            ls, lc = posttraverse(node.left)
            # right sum, right count = right traversal
            rs, rc = posttraverse(node.right)

            # add the numbers
            sumres = node.val + ls + rs
            # add the counts and add 1 to it
            countres = lc + rc + 1

            if sumres // countres == node.val:
                res += 1
            
            return sumres, countres
        
        posttraverse(root)
        return res