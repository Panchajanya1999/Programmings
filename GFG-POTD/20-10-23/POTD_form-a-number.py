# October 20, 23
# Form a number divisible by 3 using array digits
# Link - https://practice.geeksforgeeks.org/problems/form-a-number-divisible-by-3-using-array-digits0717/1

#User function Template for python3

class Solution:
    def isPossible(self, N, arr):
        # code here
        # Forms a single string by concatenating all the integers in the array
        arr_str = "".join(str(num) for num in arr)
        
        # Splits the string into a list of its digits
        digits = [int(digit) for digit in arr_str]
        
        # Checks if the sum of the digits is divisible by 3
        if sum(digits) % 3 == 0:
            return 1    # It's possible to form a number divisible by 3
        else:
            return 0    # It's not possible to form a number divisible by 3


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends