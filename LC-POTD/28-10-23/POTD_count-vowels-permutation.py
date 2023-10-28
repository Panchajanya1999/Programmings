# October 28, 2023
# Count Vowels Permutation
# link - https://leetcode.com/problems/count-vowels-permutation/description/?envType=daily-question&envId=2023-10-28

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # initialize counts
        cA = 1
        cE = 1
        cI = 1
        cO = 1
        cU = 1

        # iterate from 1 .. n-1
        for length in range(1, n):
            # calculate the next counts
            ncA = cE
            ncE = (cA + cI) % MOD
            ncI = (cA + cE + cO + cU) % MOD
            ncO = (cI + cU) % MOD
            ncU = cA

            # update the counts
            cA = ncA
            cE = ncE
            cI = ncI
            cO = ncO
            cU = ncU

        # return the sums
        tot = (cA + cE + cI + cO + cU) % MOD
        return int(tot)