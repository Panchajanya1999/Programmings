#User function Template for python3

class Solution:
    def minimumStep(self, n, memo={}):
        if n in memo:
            return memo[n]

        if n == 1:
            return 0

        if n % 3 == 0:
            result = 1 + self.minimumStep(n // 3, memo)
        else:
            result = 1 + self.minimumStep(n - 1, memo)

        memo[n] = result
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minimumStep(n))
# } Driver Code Ends
