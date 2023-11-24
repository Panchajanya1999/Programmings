#User function Template for python3
from math import factorial
#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    # code here
	    ans = []
	    for i in range(n):
	        a = (factorial(n - 1) // factorial(n - i -1)//factorial(i)) % (10 ** 9 + 7)
	        ans.append(a)
	   
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends
