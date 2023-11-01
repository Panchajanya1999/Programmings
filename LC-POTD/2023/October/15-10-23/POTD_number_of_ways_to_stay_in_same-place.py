# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 15, 2023
# Number of ways to stay in the same place after some steps
# link - https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        # define modulo
        mod = 10**9 + 7

        # calculate the maximum possible positions
        maxlen = min(arrLen, steps // 2 + 1)

        # create a dp to hold the number of ways to get each position
        dp = [0] * (maxlen + 1)
        dp[0] = 1

        # iterate through the steps
        for i in range(steps):
            # initialize low to 0
            low = 0
            # iterate through stairs
            for j in range(min(maxlen, i + 2, steps - i + 3)):
                # use recurrence relation to calculate the min steps
                # reqiured to move
                low, dp[j] = dp[j], (
                    dp[j] + low + dp[j + 1]
                ) % mod
        
        # return the first elemnrt of dp
        return dp[0]
