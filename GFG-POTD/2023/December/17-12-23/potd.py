#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		if(n==1):
            return arr[0]
        
        num1 =  arr[0]
        num2 = max([arr[0],arr[1]])
        
        for i in range(2,n,1):
            temp = num2
            num2 = max([num1+arr[i], num2])
            num1 = temp
        return num2


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
