class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # count the number of arrays
        n = len(arr)

        # 25% of n
        import math
        k = math.floor((0.25) * n)

        # create a dictionary to store the counts of elements
        count = {}

        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

            # if the count of the current element is more than k, return it
            if count[i] > k:
                return i

        # if no element appears more than 25% of the time, return -1 or any other value as per the problem's requirement
        return -1

