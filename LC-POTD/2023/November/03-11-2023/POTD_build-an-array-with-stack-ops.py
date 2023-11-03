# November 3, 2023
# Link - https://leetcode.com/problems/build-an-array-with-stack-operations/?envType=daily-question&envId=2023-11-03

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # remove the repeated elemets from target
        stg = set(target)
        # pick the last element of target
        le = target[-1] # we will use it to create a stream of numbers
        # list to hold the result
        res = []

        for i in range(1, le + 1):
            # if i in stg, just append push else push, pop
            if i in stg:
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
        
        # return the result
        return res
