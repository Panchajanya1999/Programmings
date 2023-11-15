#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def betterString(self, str1, str2):
        # Code here
        
        # function to return the number of distinct
        # subsequences of str
        def countSub(s):
            # create an array to store index
            # of last
            last = [-1] * 256

            # length of input string
            n = len(s)

            # dp[i] is going to store count of distinct
            # subsequences of length i.
            dp = [0] * (n + 1)

            # Empty substring has only one subsequence
            dp[0] = 1

            # Traverse through all lengths from 1 to n.
            for i in range(1, n + 1):
                # Number of subsequences with substring
                # str[0..i-1]
                dp[i] = (2 * dp[i - 1])

                # If current character has appeared
                # before, then remove all subsequences
                # ending with previous occurrence.
                if (last[ord(s[i - 1])] != -1):
                    dp[i] = (dp[i] - dp[last[ord(s[i - 1])]])

                    # Mark occurrence of current character
                last[ord(s[i - 1])] = (i - 1)

                    # +1 is for empty subsequence
            return dp[n] + 1
        
        return str1 if countSub(str1) == countSub(str2) else str1 if countSub(str1) > countSub(str2) else str2

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends