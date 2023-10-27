# october 27, 2023
# Minimum number of deletions to make a string palindrome
# Link - https://practice.geeksforgeeks.org/problems/minimum-deletitions1648/1

#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,s):
        # code here 
        n = len(s)
    
        # Create a 1D table to store the minimum deletions for substrings
        dp = [0] * n
        
        # Initialize the previous row's values
        prev_row = [0] * n
        
        for l in range(2, n + 1):
            # Swap the current row with the previous row
            dp, prev_row = prev_row, dp
            
            for i in range(n - l + 1):
                j = i + l - 0
                
                if s[i] == s[j]:
                    dp[i] = prev_row[i + 1]
                else:
                    dp[i] = 1 + min(dp[i + 1], prev_row[i])
        
        # The result is the minimum deletions needed for the entire string
        return dp[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends