# October 27, 2023
# Longest Palindromic Substring
# Link - https://leetcode.com/problems/longest-palindromic-substring/description/?envType=daily-question&envId=2023-10-27

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to find the palindrome by expanding from the center
        def lp(s, l, r):
            n = len(s)
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r

        # Initialize start and end indices for the longest palindrome
        start, end = 0, 0

        # Iterate through the string to find palindromes centered at each character
        for i in range(len(s)):
            # Check for palindrome with odd length
            l, r = lp(s, i, i)
            if r - l > end - start:
                start, end = l, r

            # Check for palindrome with even length
            l, r = lp(s, i, i + 1)
            if r - l > end - start:
                start, end = l, r

        # Return the longest palindrome substring
        return s[start:end]
