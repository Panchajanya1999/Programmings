# October 27, 2023
# Bleak Numbers
# Link - https://practice.geeksforgeeks.org/problems/bleak-numbers1552/1

# User function Template for python3
import math


class Solution:
    def is_bleak(self, n):
        # Code here
        # Find the upper limit for the loop based on the number of bits in n
        max_i = int(math.log2(n)) + 1

        # Iterate over the reduced range
        for i in range(max_i):
            if n - i >= 0 and bin(n - i).count('1') == i:
                return 0

        return 1


# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.is_bleak(n)
        print(ans)
# } Driver Code Ends
