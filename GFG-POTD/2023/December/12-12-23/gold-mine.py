# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        dp = [[0 for _ in range(m)] for _ in range(n)]
    
        for i in range(n):
            dp[i][m - 1] = M[i][m - 1]
    
        for j in range(m - 2, -1, -1):
            for i in range(n):
                move_right = dp[i][j + 1]
                move_up = dp[i - 1][j + 1] if i - 1 >= 0 else 0
                move_down = dp[i + 1][j + 1] if i + 1 < n else 0
    
                dp[i][j] = M[i][j] + max(move_right, move_up, move_down)
    
        max_gold = 0
        for i in range(n):
            max_gold = max(max_gold, dp[i][0])
    
        return max_gold


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends
