#User function Template for python3
class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        # Initialize current_sum and max_sum with the sum of the first K elements
        current_sum = max_sum = sum(Arr[:K])
        
        # Slide the window
        for i in range(K, N):
            # Add the current element and subtract the first element of the previous window
            current_sum = current_sum + Arr[i] - Arr[i-K]
            
            # Update max_sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends
