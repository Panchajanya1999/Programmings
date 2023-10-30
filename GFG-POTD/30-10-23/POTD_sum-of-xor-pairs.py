# October 30, 2023
# Sum of XOR Pairs
# link - https://practice.geeksforgeeks.org/problems/sum-of-xor-of-all-pairs0723/1

#User function Template for python3

class Solution:
    def sumXOR (self, arr, n) : 
        #Complete the function
        result = 0

        for i in range(32):  # Assuming 32-bit integers
            count_set_bits = sum((num >> i) & 1 for num in arr)
            result += (count_set_bits * (len(arr) - count_set_bits) * 2) << i
    
        return result//2
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends