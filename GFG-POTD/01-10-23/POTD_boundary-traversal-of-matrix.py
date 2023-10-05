# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors
# POTD October 1, 2023
# Boundary traversal of matrix
# Link - https://practice.geeksforgeeks.org/problems/boundary-traversal-of-matrix-1587115620/1

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        # code here 
        # WE HAVE n ROWS AND m COLUMNS
        
        # if we have only one row, return the row
        if n == 1:
            return matrix[0]
        
        # code to get the rightmost elements[m-1] from row 1..n-1
        rm = []
        for r in range(1, n-1):
            rm.append(matrix[r][m-1])
        # print(f"rightmost of middle rows - {rm}")
        
        # code to get the leftmost elements[0] from row 1..n-1
        lm = []
        # is not necessary if theres single column
        if m > 1:
            for l in range(1, n-1):
                lm.append(matrix[l][0])
            # print(f"leftmost of middle rows - {lm}")

        return matrix[0] + rm + matrix[n-1][::-1] + lm[::-1]

#{ 
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends