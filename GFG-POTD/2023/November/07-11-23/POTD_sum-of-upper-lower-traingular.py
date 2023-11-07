# November 7, 2023
# https://www.geeksforgeeks.org/problems/sum-of-upper-and-lower-triangles-1587115621/1


#User function Template for python3


class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here 
        # function to find the
        # sum of upper tringualr matrix
        def uts(mat):
            n = len(mat)
            # upper sum counter
            us = 0
            for i in range(n):
                for j in range(i, n):
                    us += matrix[i][j]
            return us
        
        # function to write the 
        # sum of lower triangualr
        def lts(mat):
            n = len(mat)
            # lower sum counter
            ls = 0
            for i in range(n):
                for j in range(i + 1):
                    ls += matrix[i][j]
            
            return ls
        
        # return the upper and lower triangualr sums
        return uts(matrix), lts(matrix)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]

        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        ans = obj.sumTriangles(matrix, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends