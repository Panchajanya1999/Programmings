# POTD 16th October
# Making a Large Island
# Link - https://practice.geeksforgeeks.org/problems/making-a-large-island/1

from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        # Function to perform depth-first search (DFS) to label connected components
        rows = len(grid)
        area = 0
        def dfs(r, c, idx):
            grid[r][c] = idx
            nonlocal area
            area += 1
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nr, nc = r + dr, c + dc
                # Check if the neighbor is within bounds and is part of the same island
                if 0 <= nr < rows and 0 <= nc < rows and grid[nr][nc] == 1:
                    dfs(nr, nc, idx)
        
        # Label connected components and store their areas in a hashmap
        label = 2
        hashmap = {}

        for r in range(rows):
            for c in range(rows):
                if grid[r][c] == 1:
                    area = 0
                    dfs(r, c, label)
                    hashmap[label] = area
                    label += 1
        
        # If there are no islands, return 1 (a single cell)
        if len(hashmap) == 0:
            return 1
        _max = max(hashmap.values())

        # Iterate through each cell with value 0 and calculate the maximum island size after connecting it
        for r in range(rows):
            for c in range(rows):
                if grid[r][c] == 0:
                    res = 1
                    visit = set()
                    for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        nr, nc = r + dr, c + dc
                        # Check if the neighbor is within bounds and is part of a labeled island
                        if 0 <= nr < rows and 0 <= nc < rows and grid[nr][nc] != 0 and grid[nr][nc] not in visit:
                            res += hashmap[grid[nr][nc]]
                            visit.add(grid[nr][nc])
                    _max = max(_max, res)
        
        return _max


# Driver Code Starts

class IntMatrix:
    def __init__(self) -> None:
        pass
    
    def Input(self, n, m):
        matrix = []
        # Matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    
    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        grid = IntMatrix().Input(n, n)
        obj = Solution()
        res = obj.largestIsland(grid)
        print(res)

# Driver Code Ends


