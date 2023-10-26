# Ocotober 26, 2023
# Minimum Operations
# Link - https://practice.geeksforgeeks.org/problems/find-optimum-operation4504/1

class Solution:
    def minOperation(self, n):
        # Initialize the variable ans to 0
        ans = 0

        # Iterate over the range 0 to 20
        for i in range(21):
            # Check if the i-th bit in the binary representation of n is 1
            if (n >> i) & 1:
                # Update ans to the current value of i
                ans = i

        # Add the count of set bits (1s) in the binary representation of n to ans
        ans += bin(n).count('1')

        # Return the final result
        return ans
