# November 5, 2023
# https://leetcode.com/problems/find-the-winner-of-an-array-game/?envType=daily-question&envId=2023-11-05

from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        
        winner = arr[0]
        wins = 0

        for i in range(1, len(arr)):
            if winner > arr[i]:
                wins += 1
            else:
                winner = arr[i]
                wins = 1
            
            if wins == k:
                return winner
        
        return max(winner, max(arr))
