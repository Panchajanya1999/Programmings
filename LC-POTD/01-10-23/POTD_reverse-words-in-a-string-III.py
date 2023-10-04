# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors
# POTD October 1, 2023
# Reverse words in a given string III
# Link - https://leetcode.com/problems/reverse-words-in-a-string-iii/?envType=daily-question&envId=2023-10-01

class Solution:
    """
    @param s: a string
    """
    def reverseWords(self, s: str) -> str:
        """
        Time Complexity - O(n)
        Space Complexity - O(n)
        """
        # Split the string into a list
        lists = s.split()
        # for each element in the list, reverse the elements and save it to a new list
        revlists = ["".join(reversed(string)) for string in lists]
        # return the list converted string with space in between words
        return " ".join(revlists)
