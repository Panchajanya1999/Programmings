class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max([x+y for x,y in zip(nums[:len(nums)//2],nums[len(nums)//2:][::-1])])
        
