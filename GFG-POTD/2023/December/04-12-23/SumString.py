#User function Template for python3
class Solution:
    def isSumString (ob,S):
        # code here 
        # write a function to check the string
        def check(s1, s2, s):
            # Base case: if s is empty, the current substrings form a valid sum string
            if s == '':
                return True
            # Base case: if s is empty, the current substrings form a valid sum string
            s3 = str(
                int(s1) + int(s2)
                )
            
            n = len(s3)
            # Base case: if s is empty, the current substrings form a valid sum string
            if s[:n] == s3:
                # Recursively check the remaining part of s with updated substrings
                return check(s2, s3, s[n:])
            # If the match fails, the substrings do not form a valid sum string
            return False
        
        n = len(S)
        # Iterate through possible split points for the first two substrings
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                # Extract the first two substrings
                s1, s2 = S[:i], S[i:j]
                # Check if the remaining part of the string is a valid sum string
                if check(s1, s2, S[j:]):
                    # is a valid substring
                    return 1
        # no valid substring has been found
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        
        print(ob.isSumString(S))
# } Driver Code Ends
