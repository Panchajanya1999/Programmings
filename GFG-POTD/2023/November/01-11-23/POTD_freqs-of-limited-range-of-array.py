# November 1, 2023
# Frequency of limited range of array
# https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1

class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        # create an array with P length
        res = [0] * N
        
        # increase the count of the contents of res, consdering
        # res is a 1-based array
        for i in arr:
            # value of i shouldnt exceed N
            if i > N:
                continue
            else:
                res[i-1] += 1
            
        # copy the elements back to arr
        for i in range(N):
            arr[i] = res[i]
        
        # return the original arr
        return arr




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends