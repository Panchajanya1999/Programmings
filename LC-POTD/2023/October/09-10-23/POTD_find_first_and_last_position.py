# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 9, 2023
# Problem: Find First and Last Position of Element in Sorted Array
# link - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Use Binary Search to find the target
        low = 0
        high = len(nums) - 1

        # start and end are the first and last occurence of the target
        start = -1
        end = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                # If target is found, then find the first and last occurence of the target
                start = mid
                end = mid
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                return start, end
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # If target is not found, return [-1, -1]
        return [-1, -1]