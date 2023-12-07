class Solution:
    def largestOddNumber(self, num: str) -> str:
        # create a function which returns true if the number is odd
        
        # use AND operator to check if the last digit is odd
        def isOdd(num):
            return int(num) & 1
        
        # find the maximum possible odd number in the string with its substrings
        for i in range(len(num)-1, -1, -1):
            if isOdd(num[i]):
                return num[:i+1]
        return ""
        
