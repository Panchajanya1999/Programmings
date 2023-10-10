# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 10, 2023
# Minimum Number of Operations to Make Array Continuous
# Link - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/

class Solution(object):
    def minOperations(self, nums):
        # Use a set to get unique elements and sort them.
        unique_elements = sorted(set(nums))

        # Initialize variables to keep track of unique elements and minimum operations.
        unique_len = len(unique_elements)
        ans = len(nums)

        # Iterate over unique elements to find minimum operations.
        j = 0
        for i in range(unique_len):
            while j < unique_len and unique_elements[j] - unique_elements[i] <= len(nums) - 1:
                j += 1
            ans = min(ans, len(nums) - (j - i))

        return ans
