# POTD October 2, 2023
# Number of Good Pairs

#User function Template for python3

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        # Let's say the variable storing the value of number of good pairs is called good_pairs.
        # Let's initialize it to zero.

        l = len(nums) # number of elements in the list

        for i in range(l): # first looping through each element of matrix
            for j in range(i+1,l): # Looping again, but this time only looking at the element at index ahead of prev loop, to satisfy i<j
                if i<j:
                    if nums[i] == nums[j]:
                        good_pairs += 1 #If we find elements that are equal, we increment the good_pairs.

        return good_pairs
        