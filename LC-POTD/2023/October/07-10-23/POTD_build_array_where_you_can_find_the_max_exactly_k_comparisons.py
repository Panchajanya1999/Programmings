# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 7, 2023
# Build an array where you can find the max exactly k comparisons
# Link - https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/description/?envType=daily-question&envId=2023-10-07

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if m < k: return 0
        dp = [[1] * m] + [[0] * m for _ in range(k - 1)]
        mod = 10 ** 9 + 7
        for _ in range(n - 1):
            for i in range(k - 1, -1, -1):
                cur = 0
                for j in range(m):
                    dp[i][j] = (dp[i][j] * (j + 1) + cur) % mod
                    if i: cur = (cur + dp[i - 1][j]) % mod
        return sum(dp[-1]) % mod
