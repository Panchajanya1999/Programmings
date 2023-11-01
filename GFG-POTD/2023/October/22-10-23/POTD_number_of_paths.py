# October 22, 2023
# Number of Paths
# Link - https://practice.geeksforgeeks.org/problems/number-of-paths0926/1

#User function Template for python3
class Solution:
    def numberOfPaths(self, M, n):
        MOD = 10**9 + 7
        ways = 1

        for i in range(M - 1):
            ways = ways * (i + n) % MOD
            ways = ways * pow(i + 1, -2, MOD)

        return ways




#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)




# } Driver Code Ends