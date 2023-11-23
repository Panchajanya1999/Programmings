#User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

class Solution:
    def height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = self.update_height(z)
        y.height = self.update_height(y)

        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = self.update_height(y)
        x.height = self.update_height(x)

        return x

    def insertToAVL(self, root, key):
        # add key to AVL (if it is not present already)
        # return root node

        if not root:
            return Node(key)

        if key < root.data:
            root.left = self.insertToAVL(root.left, key)
        elif key > root.data:
            root.right = self.insertToAVL(root.right, key)
        else:
            return root  # Duplicate keys not allowed

        # Update height of current node
        root.height = self.update_height(root)

        # Get the balance factor
        balance = self.balance_factor(root)

        # Left Heavy
        if balance > 1:
            # Left-Left Case
            if key < root.left.data:
                return self.right_rotate(root)
            # Left-Right Case
            elif key > root.left.data:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        # Right Heavy
        if balance < -1:
            # Right-Right Case
            if key > root.right.data:
                return self.left_rotate(root)
            # Right-Left Case
            elif key < root.right.data:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root




#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

def isBST(n, lower, upper):
    if not n:
        return True
    
    if n.data <= lower or n.data >= upper:
        return False
    
    return isBST(n.left, lower, n.data) and isBST(n.right, n.data, upper)

def isBalanced(n):
    if not n:
        return (0,True)
    
    lHeight, l = isBalanced(n.left)
    rHeight, r = isBalanced(n.right)
    
    if abs( lHeight - rHeight ) > 1:
        return (0, False)
    
    return ( 1 + max( lHeight,rHeight  ) , l and r )

def isBalancedBST(root):
    if not isBST(root, -1000000000, 1000000000):
        print("BST voilated, inorder traversal :", end=' ')
    
    elif not isBalanced(root)[1]:
        print("Unbalanced BST, inorder traversal :", end=' ')
    
    else:
        return True
    
    return False

def printInorder(n):
    if not n:
        return
    printInorder(n.left)
    print(n.data, end=' ')
    printInorder(n.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ip = [ int(x) for x in input().strip().split() ]
        
        root = None
        
        for i in range(n):
            root = Solution().insertToAVL( root, ip[i] )
            
            if not isBalancedBST( root ):
                break
        
        printInorder(root)
        print()

# } Driver Code Ends
