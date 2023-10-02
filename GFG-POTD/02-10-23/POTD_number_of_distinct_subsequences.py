# POTD October 2, 2023
# Number of Distinct Subsequences

#User function Template for python3

class Solution:
    def distinctSubsequences(self, s):
        # code here
        # Set the value of mod
        mod = 10 ** 9 + 7
        n = len(s)
        # create a map to strore the last index substring characters
        last = {}
        
        # Create a list of zeroes to store the subsequence of length n + 1
        # The list is n + 1 because we need to store an ermpty substring too
        dp = [0] * (n + 1)
        
        # This is the empty substring.
        # an empty string is a substring too (base case)
        dp[0] = 1
        
        for i in range(1, n+1):
            # doubles the count of distinct subsequences
            dp[i] = ( 2 * dp[i - 1]) % mod
        
            # check for current chacracter occured before or not.
            # if it does, subtract the count of the last occuring 
            # subsequence at last occurence of s[i-1]
            if s[i-1] in last:
                dp[i] = (dp[i] - dp[last[s[i - 1]] - 1] + mod) % mod
            
            # sets the last occurence
            last[s[i-1]] = i

        return dp[n]
 
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# Driver Code Ends