# Your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isDeadEnd(self, root, low=1, high=float('inf')):
        if not root:
            return False

        # Check if the current node's value is a dead end
        if low == high:
            return True

        # Check left and right subtrees
        leftLeaf = self.isDeadEnd(root.left, low, root.data - 1)
        rightLeaf = self.isDeadEnd(root.right, root.data + 1, high)

        return leftLeaf or rightLeaf



#{ 
 # Driver Code Starts

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
                
        ob = Solution()
        if ob.isDeadEnd(root):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
