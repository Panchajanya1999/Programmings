from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        diff = [[0] * n for _ in range(m)]
        onesRow = [0] * m
        onesCol = [0] * n
        
        for i in range(m):
            onesRow[i] = grid[i].count(1)
        
        for j in range(n):
            onesCol[j] = sum(grid[i][j] for i in range(m))
        
        for i in range(m):
            zerosRowi = n - onesRow[i]
            
            for j in range(n):
                zerosColj = m - onesCol[j]
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRowi - zerosColj
        
        return diff
