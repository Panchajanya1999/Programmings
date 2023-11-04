# November 4, 2023
# Link - https://www.geeksforgeeks.org/problems/find-transition-point-1587115620/1

class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        
        # check whether the array is valid or not
        # since the array is sorted, the last element 
        # should have a 1
        if arr[-1] != 1:
            return -1
        
        # implement binary search to find the first
        # occurenc of 1
        def bsearch(arr, target):
            # length of the array
            n = len(arr)
            # set high and low pointers
            low, high = 0, n - 1
            # set the result var which will hold the index
            res = -1
            
            while low <= high:
                # find the mid element
                mid = (low + high) // 2
                
                if arr[mid] == target:
                    # update the value and continue searching
                    res = mid
                    # update high to mid - 1
                    high = mid - 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return res
        
        # return the result of binary search
        return bsearch(arr, 1)


#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr, n))

# } Driver Code Ends