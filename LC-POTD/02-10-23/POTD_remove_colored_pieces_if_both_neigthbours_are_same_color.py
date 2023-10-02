# POTD October 2, 2023
# Remove Colored Pieces if Both Neighbors are the Same Color
# Link - https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Both Alice and Bob starts with zero
        alice = 0
        bob = 0
        # calculate the length of the colors
        n = len(colors)

        # loop from 1st index to n-1 ( since we need previous and
        # next element for comparison )
        for i in range(1, n - 1):
            # 'AAA' or 'BBB' has previous, current, next element same
            if colors[i] == colors[i-1] == colors[i+1]:
                # if triplets are same and and element from
                # the triplet is "A", then Alice increments
                # else Bob increments
                if colors[i] == "A":
                    alice += 1
                else: 
                    bob += 1
        # Return True if Alice is greater than Bob else return False
        # Comparison is boolean
        return alice > bob
