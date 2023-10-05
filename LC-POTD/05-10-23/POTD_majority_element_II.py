# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors
# POTD October 5, 2023
# Majority Element II
# Link - https://leetcode.com/problems/majority-element-ii/description/

from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Declare a list to store the numbers
        res = []
        # base case
        if not nums:
            return res
        # times is floor of n / 3
        times = len(nums) // 3
        # count holds the numbr of occurence
        # of each distinct digit in a dictionary of
        # counters
        count = Counter(nums)
        # n is the number and c is the count.

        for n, c in count.items():
            # if count is more than the times (n //3),
            # append the correspomnding number to res 
            if c > times:
                res.append(n)

        return res


def main():
    # take input of number of test cases
    t = int(input())

    # loop over all the test cases
    for _ in range(t):
        # take input of the array elements
        arr = list(map(int, input().split()))

        # calculate and print the result for each test case
        result = Solution().majorityElement(arr)
        if result: 
            print(result)

if __name__ == "__main__":
    main()
