# November 6, 2023
# https://www.geeksforgeeks.org/problems/c-letters-collection4552/1

#User function Template for python3

class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        ans = []

        for i in range(q):
            hop = queries[i][0]
            x = queries[i][1]
            y = queries[i][2]

            if hop == 1:
                # For 1-hop distance, iterate through the possible directions
                dx = [0, -1, -1, -1, 0, 1, 1, 1]
                dy = [-1, -1, 0, 1, 1, 1, 0, -1]
            else:
                # For 2-hop distance, iterate through the extended set of directions
                dx = [0, -1, -2, -2, -2, -2, -2, -1, 0, 1, 2, 2, 2, 2, 2, 1]
                dy = [-2, -2, -2, -1, 0, 1, 2, 2, 2, 2, 2, 1, 0, -1, -2, -2]

            totalsum = 0

            for j in range(len(dx)):
                nr = x + dx[j]
                nc = y + dy[j]

                # Check if the new position is within bounds
                if 0 <= nr < n and 0 <= nc < m:
                    totalsum += mat[nr][nc]

            ans.append(totalsum)

        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = [[0]*m for x in range(n)]
        for i in range(n):
            arr = input().split()
            for j in range(m):
                mat[i][j] = int(arr[j])
        q = int(input())
        queries = [[0]*3 for x in range(q)]
        for i in range(q):
            a = input().split()
            for j in range(3):
                queries[i][j] = int(a[j])
        
        ob = Solution()
        ans = ob.matrixSum(n, m, mat, q, queries)
        for i in range(q):
            print(ans[i])
# } Driver Code Ends