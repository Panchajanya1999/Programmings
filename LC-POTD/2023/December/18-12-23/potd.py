class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # sort the arrays
        nums.sort()

        # pick nums[0] and nums[1] as small diff
        sdiff = nums[1] * nums[0]
        # pick the last two digit as big diff
        bdiff = nums[-1] * nums[-2]

        # return their diffs
        return bdiff - sdiff
