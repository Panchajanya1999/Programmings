
#User function Template for python3
class Solution:
    
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,matrix,n):
        # code here 
        if n==1:
            return matrix[0][0]
        if n==2:
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        det=0
        for i in range(n):
            det+=matrix[0][i]*self.cofactor(matrix,n,0,i)
        return det  
    def cofactor(self,matrix,n,p,q):
        temp=[]
        for i in range(n):
            row=[]
            for j in range(n):
                if i!=p and j!=q:
                    row.append(matrix[i][j])
            if len(row)>0:
                temp.append(row)
        return (-1)**(p+q)*self.determinantOfMatrix(temp,n-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends
