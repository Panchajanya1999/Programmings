#User function Template for python3

class Solution:
	def nthPoint(self,n):
		# Code here
		MOD = 10 ** 9  + 7
		
		if n < 2:
		    return 1
		   
		res = [0] * (n + 1)
		res[0] = res[1] = 1
		
		for i in range(2, n + 1):
		    res[i] = (
		        (res[i - 1] % MOD) + (res[i - 2] % MOD)
		    )
		return res[n] % MOD


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends
