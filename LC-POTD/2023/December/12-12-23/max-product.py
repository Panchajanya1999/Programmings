class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # create a new list to store the elments with 1 subtrcted
        new_nums = [num - 1 for num in nums]

        # Find the max and second max
        def max12(nums: List[int]):
            max1 = max2 = float('-inf')

            for num in nums:
                if num > max1:
                    # swap elementss
                    max2, max1 = max1, num
                elif num > max2:
                    max2 = num
            
            return max1, max2
        
        res = 0
        res = (max12(new_nums)[0] * max12(new_nums)[1])
        return res
