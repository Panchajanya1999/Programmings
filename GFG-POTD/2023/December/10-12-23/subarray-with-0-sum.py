#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        count = 0
        map = {0: 1}
        local_sum = 0
    
        for i in range(len(arr)):
            local_sum += arr[i]
    
            if local_sum in map:
                count += map[local_sum]
    
            map[local_sum] = map.get(local_sum, 0) + 1
    
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
