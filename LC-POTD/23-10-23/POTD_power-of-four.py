# October 23, 2023
# Power of Four
# Link - https://leetcode.com/problems/power-of-four/description/?envType=daily-question&envId=2023-10-23

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        mask = 0x55555555
        return n > 0 and (n & (n - 1)) == 0 and (n & mask) == n