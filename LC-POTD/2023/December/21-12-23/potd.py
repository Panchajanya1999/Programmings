class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # sort the points by x-coordinate
        points.sort(key=lambda x: x[0])
        # find the max difference between two consecutive x-coordinates
        return max(points[i][0] - points[i-1][0] for i in range(1, len(points)))
    
