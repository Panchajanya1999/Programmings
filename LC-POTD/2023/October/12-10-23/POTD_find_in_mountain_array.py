# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 12, 2023
# Find in Mountain Array
# link - https://leetcode.com/problems/find-in-mountain-array/description/?envType=daily-question&envId=2023-10-12

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        # define a binary search function with a 'reverse' boolean
        def bsearch(low, high, target, array, reverse):
            # chances are there high and low could be same
            while high != low:
                mid = low + (high - low) // 2
                if reverse: # the array is reversed, that is decreasing slope
                    if array.get(mid) > target:
                        low = mid + 1
                    else:
                        high = mid
                else: # increasing slope
                    if array.get(mid) < target:
                        low = mid + 1
                    else:
                        high = mid
            return low
        
        # find the peak index
        def find_peak(low, high, array):
            # use binary search logic again
            while low != high:
                mid = low + (high - low) // 2
                if array.get(mid) < array.get(mid + 1):
                    low = mid + 1
                else:
                    high = mid
            return low
        
        ## We will perform basically three operations
        # 1. Find the peak index
        # 2. Look for the target in the increasing slope
        # 3. if not found in #2, look in the decrerasing slope
        # 4. If still not found which means the item is absent
        #       return -1

        # find the lengthh of the mountain
        # predefined API
        n = mountain_arr.length()

        # look for the peak index
        peakidx = find_peak(1, n - 2, mountain_arr)

        # check for the targert in the increasing slope
        incidx = bsearch(0, peakidx, target, mountain_arr, False)
        if mountain_arr.get(incidx) == target:
            return incidx

        # check for the targert in the decreasing slope
        decidx = bsearch(peakidx + 1, n -1, target, mountain_arr, True)
        if mountain_arr.get(decidx) == target:
            return decidx
        
        return -1
