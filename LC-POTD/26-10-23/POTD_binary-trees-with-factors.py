# October 26, 2023
# Binary Trees With Factors
# https://leetcode.com/problems/binary-trees-with-factors/

MOD = 10**9 + 7

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # Sort the input array
        arr.sort()
        
        # Create a set for faster lookup
        s = set(arr)
        
        # Initialize a dictionary to store results for subproblems
        dp = {x: 1 for x in arr}
        
        # Iterate over each element in the array
        for i in arr:
            # Iterate over potential factors
            for j in arr:
                # Break the inner loop if the potential factor is greater than the square root of the current element
                if j > i**0.5:
                    break
                
                # Check if j is a factor of i and i/j is also in the array
                if i % j == 0 and i // j in s:
                    # If j and i/j are the same factor, update the count by multiplying the count for j
                    if i // j == j:
                        dp[i] += dp[j] * dp[j]
                    # If j and i/j are different factors, update the count by multiplying the counts for both
                    else:
                        dp[i] += dp[j] * dp[i // j] * 2
                    
                    # Take the result modulo MOD to avoid overflow
                    dp[i] %= MOD
        
        # Sum up the counts for all elements and take the final result modulo MOD
        return sum(dp.values()) % MOD
