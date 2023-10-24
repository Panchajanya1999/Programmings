#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        # code here
        n = len(string)
        dp = [[False for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if string[i] == string[i+1]:
                dp[i][i+1] = True
        for gap in range(2,n):
            for i in range(n-gap):
                j = i+gap
                if string[i] == string[j] and dp[i+1][j-1]:
                    dp[i][j] = True
        ans = [float('inf')]
        self.solve(string,0,dp,ans,[])
        
        return ans[0]
    
    def solve(self,string,index,dp,ans,temp):
        if index == len(string):
            ans[0] = min(ans[0],len(temp)-1)
            return
        for i in range(index,len(string)):
            if dp[index][i]:
                temp.append(string[index:i+1])
                self.solve(string,i+1,dp,ans,temp)
                temp.pop()
        return
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends