# pylint: disable=C0103, line-too-long, invalid-name, unused-import, missing-docstring, trailing-whitespace, anomalous-backslash-in-string, anomalous-unicode-escape-in-string, too-many-arguments, too-many-locals, too-many-branches, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-lines, too-few-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, too-many-branches, too-many-arguments, too-many-locals, too-many-lines, too-many-statements, too-many-instance-attributes, too-many-public-methods, too-many-nested-blocks, too-many-boolean-expressions, too-many-ancestors, C0200, W0621
# POTD Otober 11, 2023
# Number of flowers in a full bloom
# Link - https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        # declare two list start and end
        start, end = [], []
        # fillup start and end from flowers
        # which is the timign of the flowers to bloom
        for _start, _end in flowers:
            start.append(_start)
            end.append(_end)
        # sort the timings in a non-decreasing
        # order
        start.sort()
        end.sort()
        # create a list to hold the result
        res = []
        # perform binary search to find the start and end of bloom based
        # on the visitors and store the diff in a list
        for peep in people:
            res.append(bisect_right(start, peep) - bisect_left(end, peep))
        # return the list
        return res
