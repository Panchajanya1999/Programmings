# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # declare a list
        res = []

        # define a function which does inorder traversal using recursion
        def inorder(root):
            #  check if root is empty
            if not root:
                return []
            else:
                # traverse the left subtree
                inorder(root.left)
                # append the middle to the res list
                res.append(root.val)
                # traverse the right subtree
                inorder(root.right)
        
        # traverse using the function
        inorder(root)

        # return the list
        return res
