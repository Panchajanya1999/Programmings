class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        ret = 1

        for i in range(1, len(arr)):
            if arr[i] > ret:
                ret += 1

        return ret