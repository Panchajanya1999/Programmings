class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        mid = n//2
        
        for i in range(mid):
            arr.insert(2*i+1, arr[mid+i])
            arr.pop(mid+i+1)
        return arr


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends
