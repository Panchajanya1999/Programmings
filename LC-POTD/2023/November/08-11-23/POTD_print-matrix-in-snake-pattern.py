# November 8, 2023
# Link - https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/description/?envType=daily-question&envId=2023-11-08

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        if t == 1 and sx == fx and sy == fy:
            return False
        
        # calculates "square" perimeter and compares it against given time
        return max((abs(sx - fx)), (abs(sy - fy))) <= t