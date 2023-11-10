#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        # create a stack and a string for this
        stack = []
        result = []

        for i in range(len(S) + 1):
            stack.append(i + 1)

            # If it's the last character or 'I', pop elements from the stack and append to the result
            if i == len(S) or S[i] == 'I':
                while stack:
                    result.append(stack.pop())

        # Join the result list into a string and return
        return ''.join(map(str, result))

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends