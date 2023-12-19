class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = self.getAvg(img, i, j)
        return res
    
    def getAvg(self, img, i, j):
        m, n = len(img), len(img[0])
        total = 0
        count = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if 0 <= x < m and 0 <= y < n:
                    total += img[x][y]
                    count += 1
        return total // count
