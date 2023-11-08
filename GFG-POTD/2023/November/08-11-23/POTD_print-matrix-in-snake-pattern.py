# November 9, 2023
# Link - https://www.geeksforgeeks.org/problems/print-matrix-in-snake-pattern-1587115621/1


#User function Template for python3

class Solution:
    
    # Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
        snake = []
        for i in range(matrix.len()):
            # Check if the row number is even using bitwise AND
            if i & 1 == 0:
                # If even row, extend the snake list with the entire row
                snake.extend(matrix[i])
            else:
                # If odd row, extend the snake list with the reversed row
                snake.extend(reversed(matrix[i]))
        return snake



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
        ans = obj.snakePattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends