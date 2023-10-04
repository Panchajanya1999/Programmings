# POTD October 3, 2023
# Column name from a given column number
# Link - https://practice.geeksforgeeks.org/problems/column-name-from-a-given-column-number4244/1

#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        
        # Create a dictionary to have a key:value pair.
        # Dictionary is faster than lists since dictionary uses
        # hash-tables and on average hash-table is faster.
        # The table looks like this -
        # {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
        # 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 
        # 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 
        # 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
        #
        alphabet_dict = {}
        for i in range(26):
            alphabet_dict[i + 1] = chr(ord('A') + i)
        
        # This is base case. 1 to 26 already exists in the dictionary
        if n <= 26:
            return alphabet_dict[n]
        
        # Create an empty string to hold the string values of the operation
        col = ""
        
        # Loop till the value of n become 0 
        while n > 0:
            # Remainder is parsed to find the alphabetical value from the dictionary
            rem = n % 26
            # Bug: Zero Remainder Error
            # The code will break if rem becomes 0.
            # To deal with zero remainder, append 'Z' to the 'col' string
            # since zero remainder means this is a perfect multiple of 26 and 26th 
            # alphabet is 'Z'. Then perform floor division of 'n' by 26 and subtract 1
            # because we are adding 'Z' to the 'col' so the subtraction makes sense.
            if rem == 0:
                col += 'Z'
                n = (n // 26) - 1
            # This goes on normally, we find the corresponding 
            # Alphabetical value from the dictionary and append it to
            # the 'col' string. Then perform floor division of 'n' by 26 to find the
            # next key.
            else: 
                col += alphabet_dict.get(rem) # type: ignore
                n //= 26
        
        # Return the reversed 'col'
        return col[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends