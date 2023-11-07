# November 7, 2023
# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/?envType=daily-question&envId=2023-11-07

class Solution:
    # Class with method to calculate maximum number of monsters that can be eliminated

    def eliminateMaximum(self, dist, speed):
        n = len(dist) # getting the total number of monsters

        for i in range(n): # loop through each monster
            dist[i] = math.ceil(dist[i] / speed[i]) # compute time it'd take to reach the city for each monster.
        dist.sort() # sort the distances to make sure we eliminate monsters that reach the city first.

        i = 0 # initialize a counter for the monsters
        for j in range(n): # loop through each monster again
            if i >= dist[j]: 
                # if the current count (time spent fighting monsters) is greater than or equal to time it'd take for the current monster to reach the city...
                return i # ... return the count of eliminated monsters.
            i += 1 # increase the count (time) after eliminating each monster
            
        return n # if all monsters can be eliminated, return the total count of monsters