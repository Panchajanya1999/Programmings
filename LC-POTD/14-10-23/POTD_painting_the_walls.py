# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 14, 2023
# Painting the Walls
# Link - https://leetcode.com/problems/painting-the-walls/description/?envType=daily-question&envId=2023-10-14

from typing import List
import math

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # Get the length of walls
        n = len(cost)
        
        # Initialize a dynamic programming array with infinite values
        dp = [math.inf] * (n + 1)
        # The first index is set to 0 since it represents the cost to paint 0 walls
        dp[0] = 0

        # Loop through the walls
        for i in range(n):
            # Fill the dp list in reverse order
            for j in range(n, 0, -1):
                # Update dp[j] with the minimum of:
                # - The current dp[j] value
                # - The cost of the current wall plus the cost of the previous wall (with time constraint)
                dp[j] = min(dp[j], dp[max(j - time[i] - 1, 0)] + cost[i])

        # Return the cost to paint all walls
        return dp[n]
