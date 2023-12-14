#User function Template for python3

class Solution:
    def countWays(self,n,k):
        #code here.
        M = 10**9 + 7
        if n == 1:
            return k

        prev, curr = 0, k
        ans = prev + curr

        for i in range(2, n + 1):
            prev, curr = curr, (ans * (k - 1)) % M
            ans = prev + curr

        return ans % M



#{ 
 # Driver Code Starts

#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends
