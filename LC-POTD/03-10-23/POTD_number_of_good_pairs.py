class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        l = len(nums)

        for i in range(l):
            for j in range(i+1,l):
                if i<j:
                    if nums[i] == nums[j]:
                        good_pairs += 1

        return good_pairs
        