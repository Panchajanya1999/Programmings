# October 30, 2023
# Sort Integers by The Number of 1 Bits
# link  - https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/?envType=daily-question&envId=2023-10-30

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # create a function that return the numbers of 1's in an
        # integer 
        def count1(n):
            return (format(n, 'b').count("1"), n)
        
        # use the above function as a key for sorting
        arr.sort(key = count1)
        # return the array
        return arryyy