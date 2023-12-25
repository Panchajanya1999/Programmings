class Solution:
    def numDecodings(self, s: str) -> int:
        # empty string
        if not s:
            return 0
        
        # first number can never be 0
        if s[0] == '0':
            return 0
        
        # length
        n = len(s)
        # create a 0 dp of length n+1
        dp = [0] * (n + 1)
        # initialize first and second to 1
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            # convert the current one & two digit string to int
            digit1 = int(s[i-1])
            digit2 = int(s[i-2:i])

            # update dp if digit1 is not 0
            if digit1 != 0:
                dp[i] += dp[i-1]
            
            # update dp if current 2digit is between 10-26
            if 10 <= digit2 <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
