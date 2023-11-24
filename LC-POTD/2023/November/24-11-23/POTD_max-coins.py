class Solution:
    def maxCoins(self, piles):
        piles.sort(reverse=True)

        i, j = 1, len(piles) - 2
        ans = 0

        while i <= j:
            ans += piles[i]
            i += 2
            j -= 1

        return ans
