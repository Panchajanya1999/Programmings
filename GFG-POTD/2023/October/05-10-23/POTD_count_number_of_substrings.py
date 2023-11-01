# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 5, 2023
# Count the number of substrings
# Link - https://practice.geeksforgeeks.org/problems/count-number-of-substrings4528/1

#User function Template for python3

class Solution:
    def substrCount (self,s, k):
        # your code here
        # function to count the msost k characters
        def countK(s, k):
            if not s:
                return 0
            # Create an empty dictionary to store the count of
            # each character
            char_count = {}
            # Store the number of substring
            num = 0
            # Store the left index of the sliding window
            left = 0
        
            for i in range(len(s)):
                # Add the current character to the dictionary and increment
                # its count by 1
                char_count[s[i]] = char_count.get(s[i], 0) + 1
                while len(char_count) > k:
                    # decrement the count of the character at the left index
                    char_count[s[left]] -= 1
                    # pop the left character if its count becomes 0 of the left
                    # character
                    if char_count[s[left]] == 0:
                        char_count.pop(s[left])
                    # move the left index by 1 to right
                    left += 1
                # num of substring ending at the current index
                num += i - left + 1
            return num
        # return the difference between the most k characters and the most k-1
        # characters
        return countK(s, k) - countK(s, k - 1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends 