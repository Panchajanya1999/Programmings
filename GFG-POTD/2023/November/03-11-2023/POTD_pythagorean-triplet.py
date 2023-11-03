# Novemeber 3, 2023

#User function Template for python3
class Solution:
    def checkTriplet(self,arr, n):
        # code here
        
        # implement two sum 
        def twosum(nums, target):
            LEN = len(nums)
            nmap  = {}

            for i in range(LEN):
                diff = target - nums[i]
                if diff in nmap:
                    return True
                nmap[nums[i]] = i
            return False
        
        # create a list to hold the squared elements
        sarr = [i ** 2 for i in arr]
        
        # iterate through the array from the last to find any matches
        # there's a higher chance the match will be at the end of the 
        # list
        for i in reversed(sarr):
            if twosum(sarr, i):
                return True
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends