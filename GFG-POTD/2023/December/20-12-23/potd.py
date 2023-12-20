#User function Template for python3

class Solution:
    def findWinner(self, n, A):
        # code here
        res = 0
        for i in range(n):
            res ^= A[i]
        
        return 1 if not res else (n % 2) + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        A = input().split()
        for itr in range(n):
            A[itr] = int(A[itr])

        ob = Solution()
        print(ob.findWinner(n, A))

# } Driver Code Ends
