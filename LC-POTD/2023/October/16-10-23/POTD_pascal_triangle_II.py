# POTD October 16, 2023
# Pascal's Triangle II
# Link - https://leetcode.com/problems/pascals-triangle-ii/description/?envType=daily-question&envId=2023-10-16

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        This function returns the `rowIndex`th row of Pascal's triangle.

        Args:
            rowIndex: The index of the row to be returned.

        Returns:
            A list of integers representing the `rowIndex`th row of Pascal's triangle.
        """

        # Take an empty array as the output.
        res = []

        # Initialize the first element of the row to 1.
        prev = 1
        res.append(prev)

        # Iterate over the remaining elements of the row.
        for i in range(1, rowIndex + 1):

            # Calculate the current element using the formula `nCr = (nCr - 1 * (n - r + 1)) / r`.
            curr = (prev * (rowIndex - i + 1)) // i
            res.append(curr)

            # Update the previous element for the next iteration.
            prev = curr

        # Return the output array.
        return res
