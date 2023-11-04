# November 4, 2023
# Link - https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/?envType=daily-question&envId=2023-11-04

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # there are ants in the farthest position, movinf to the left
        mL = max(left, default = 0)

        # there are some ants in the nearest postion, moving to the right
        mR = n - min(right, default = n)

        # return the time when all ants fall
        return max(mL, mR)