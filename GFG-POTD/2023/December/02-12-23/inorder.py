#User function Template for python3

class Solution:
    def isRepresentingBST(self, arr, N):
        # code here
        # in InOrder traversal of BST, the elements 
        # should be in sorted order.
        for i in range(N-1):
            if arr[i+1] < arr[i]:
                return 0
        return 1





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.isRepresentingBST(arr, N))
# } Driver Code Ends
