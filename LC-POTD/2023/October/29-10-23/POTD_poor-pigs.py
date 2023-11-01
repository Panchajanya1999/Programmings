# October 29, 2023
# Poor Pigs
# Link - https://leetcode.com/problems/poor-pigs/description/?envType=daily-question&envId=2023-10-29

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # calculate the max time
        maxt = minutesToTest / minutesToDie + 1
        # set the count of pigs to 0
        pigs = 0
        # for each time powered by pigs is less than buckets, increment the pigs
        while math.pow(maxt, pigs) < buckets:
            pigs += 1
        # return the pigs
        return pigs