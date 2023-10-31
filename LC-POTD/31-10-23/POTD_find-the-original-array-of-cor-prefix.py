# October 31, 2023
# Find the Original Array of prefix XOR
# Link - https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        # create a zero-array of length of the original pref array
        arr = [0] * n

        # the first eleemnt of the array is always same as 
        # first element of pref
        arr[0] = pref[0]

        # from 1..n-1, perform xor with pref[i] and pref[i-1]
        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i - 1]
        
        # return the array
        return arr