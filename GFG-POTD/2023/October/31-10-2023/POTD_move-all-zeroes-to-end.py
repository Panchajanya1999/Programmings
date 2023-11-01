# October 31, 2023
# Move all zeroes to end of array
# link - https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1

#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
		# code here
		# initialize the pointer j at -1
		j = -1
		# place the pointer j at the first j
		for i in range(n):
			if arr[i] == 0:
				# place j
				j = i
				break

		# check for non-zero elements
		if j == -1:
			return arr

		# move the pointers i and j accordingly and swap them
		for i in range(j + 1, n):
			if arr[i] != 0:
				arr[i], arr[j] = arr[j], arr[i]
				# incement j by 1
				j += 1

		# return the array
		return arr


# {
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.pushZerosToEnd(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1
# } Driver Code Ends
