# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 8, 202
# Problem: Max Dot Product of Two Subsequences
# Link - https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/

class Solution:
    # Define a method maxDotProduct that takes two lists of integers as input and returns an integer
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # Get the length of the two input lists
        n = len(nums1)
        m = len(nums2)

        # Initialize a 2D list with -inf values
        memo = [[float('-inf')] * m for _ in range(n)]

        # Define a recursive function dp to solve the problem using dynamic programming
        def dp(i, j):
            # Base case: if either i or j is out of range, return -inf
            if i == n or j == m:
                return float('-inf')
        
            # If the value has already been computed, return it
            if memo[i][j] != float(('-inf')):
                return memo[i][j]
            
            # Compute the maximum dot product of two subsequences
            memo[i][j] = max(
                    nums1[i] * nums2[j] + max(dp(i + 1, j + 1), 0),
                    dp(i + 1, j),  
                    dp(i, j + 1), 
                )
                
            return memo[i][j]
        
        # Call the dp function with initial indices 0 and 0
        return dp(0, 0)