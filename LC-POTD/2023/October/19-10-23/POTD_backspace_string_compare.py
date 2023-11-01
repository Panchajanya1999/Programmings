# POTD October 19, 2023
# Backspace String Compare
# Link - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Function to implement a stack and process the given string accordingly
        def stackproc(str):
            if str is None:
                return []  # If the string is None, return an empty stack
            stack = []
            for s in str:
                if s == "#":
                    if stack:
                        stack.pop()  # Pop from the stack if encountering a backspace character (#)
                else:
                    stack.append(s)  # Push non-backspace characters onto the stack
            return stack
        
        # Check if the processed stacks for both strings are equal
        return stackproc(s) == stackproc(t)
