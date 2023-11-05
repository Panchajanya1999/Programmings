# November 5, 2023
# https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1

from collections import Counter

class Solution:
    def topK(self, nums, k):
        # Use Counter to get frequency of each element
        counter = Counter(nums)

        # Sort based on frequency and value in descending order
        snums = sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)

        # Get the top k keys
        topk = [key for key, _ in snums[:k]]

        return topk






#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
    	
# } Driver Code Ends