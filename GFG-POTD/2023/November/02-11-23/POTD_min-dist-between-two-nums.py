# Novemeber 2, 2023
# Minimum Distance Between Two Numbers
# https://practice.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1


class Solution:
    def minDist(self, arr, n, x, y):
        
        # return -1 if x or y not in arr
        if x not in arr or y not in arr:
            return -1
        
        # keep a track of x and y where they are last seen
        lastx = -1
        lasty = -1
        # set a variable  mindist to infinity
        mindist = float('inf')
        
        # traverse through the array
        for i in range(n):
            if arr[i] == x:
                lastx = i
                if lasty != -1:
                    mindist = min(mindist, i - lasty)
            elif arr[i] == y:
                lasty = i
                if lastx != -1:
                    mindist = min(mindist, i - lastx)
        
        return mindist
        
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends
