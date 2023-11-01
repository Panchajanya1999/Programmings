# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors
# POTD October 4, 2023
# Roman Numbver to Integer
# Link - https://practice.geeksforgeeks.org/problems/roman-number-to-integer3201/1

#User function Template for python3

class Solution:
    def romanToDecimal(self, S):
        # create a dictionary for roman to decimal
        roman_to_decimal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        # Initialize the deciaml and prev_value
        decimal = 0
        prev_value = 0
        # Iterate through each character in the 
        # string
        for c in S:
            # Look up the deciaml value in the
            # dictionary
            value = roman_to_decimal[c]
            # if the current value is more than
            # the previous value, subtract
            # twice the previous value
            if value > prev_value:
                decimal += value - 2 * prev_value
            # Else just add up the value
            else:
                decimal += value
            # Update the previous value
            prev_value = value
        return decimal
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends