# November 9, 2023
# Link - https://www.geeksforgeeks.org/problems/predict-the-column/1

#User function Template for python3

class Solution:
    def columnWithMaxZeros(self, arr, N):
        # Initialize the maximum count of zeros and the index of the column
        maxZeroes = 0
        maxcoli = -1  # max column index

        # Transpose the matrix to iterate over rows (original columns)
        transposed = list(zip(*arr))

        # Iterate over each row (original column)
        for col, row in enumerate(transposed):
            # Count the number of zeros in the current row (original column)
            zeroCnt = row.count(0)

            # If the current row (original column) has more zeros than the previous maximum,
            # update the maximum and the index
            if zeroCnt > maxZeroes:
                maxZeroes = zeroCnt
                maxcoli = col

        # If no zeros were found, return -1
        if maxZeroes == 0:
            return -1

        # Return the index of the column with the maximum number of zeros
        return maxcoli








#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = []
        for i in range(N):
            line = [int(x) for x in input().strip().split()]
            arr.append(line)
        ob=Solution()
        print(ob.columnWithMaxZeros(arr,N))


# } Driver Code Ends