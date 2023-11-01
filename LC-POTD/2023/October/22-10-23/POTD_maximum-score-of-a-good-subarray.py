# POTD October 22, 2023
# Maximum Score of a Good Subarray
# Link - https://leetcode.com/problems/maximum-score-of-a-good-subarray/?envType=daily-question&envId=2023-10-22

from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Initialize the maximum score
        max_score = 0
        # Initialize a stack to track indices
        stack = []

        # Iterate through the heights, including an extra iteration for cleanup
        for i in range(len(nums) + 1):
            # Process the stack while it's not empty and the current height is smaller
            while stack and (i == len(nums) or nums[stack[-1]] > nums[i]):
                # Pop the index from the stack and calculate height and width
                height = nums[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                # Check conditions for updating the maximum score
                if (not stack or stack[-1] + 1 <= k) and i - 1 >= k:
                    max_score = max(max_score, height * width)
            # Append the current index to the stack
            stack.append(i)

        # Return the final maximum score
        return max_score
