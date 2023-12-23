#User function Template for python3
from collections import defaultdict

class Solution:
    def countOccurence(self, arr, n, k):
        div = n // k
        count = defaultdict(int)
        
        for num in arr:
            count[num] += 1
        
        keys = [key for key, value in count.items() if value > div]
        return len(keys)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
