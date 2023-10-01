# POTD October 1, 2023
# Reverse words in a given string III
# Link - https://leetcode.com/problems/reverse-words-in-a-string-iii/?envType=daily-question&envId=2023-10-01


class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into a list
        lists = s.split()
        # for each element in the list, reverse the elements and save it to a new list
        revlists = ["".join(reversed(string)) for string in lists]
        # return the list converted string with space in between words
        return " ".join(revlists)