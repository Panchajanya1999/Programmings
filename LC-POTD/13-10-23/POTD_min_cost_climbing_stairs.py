# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 13, 2023
# Minimum Cost Climbing Stairs
# Link - https://leetcode.com/problems/min-cost-climbing-stairs/?envType=daily-question&envId=2023-10-13

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # calculate the length of the stairs
        n = len(cost)

        # instead of taking a dp list, use variables
        prev, pprev = 0, 0

        # iteratte through the whole cost from 2..n
        for i in range(2, n + 1):
            curr = min(
                prev + cost[i - 1],
                pprev + cost[i - 2]
            )
            # swap the curr with prev and prev with prev2
            pprev, prev = prev, curr
        
        # return the first prev variable
        return prev
