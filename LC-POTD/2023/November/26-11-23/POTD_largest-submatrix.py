class Solution(object):
    def largestSubmatrix(self, matrix):
        # Get the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])

        # Update the matrix to store the cumulative count of consecutive ones
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        # Initialize the variable to store the maximum area
        ans = 0

        # Iterate through each row of the matrix
        for i in range(m):
            # Sort the row in descending order based on the cumulative count
            matrix[i].sort(reverse=True)

            # Iterate through each column in the sorted row
            for j in range(n):
                # Update the maximum area by considering the current element
                ans = max(ans, matrix[i][j] * (j + 1))

        # Return the maximum area
        return ans
