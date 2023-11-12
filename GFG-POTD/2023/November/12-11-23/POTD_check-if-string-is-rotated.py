#User function Template for python3


class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        #code here
        # function to rotate string left by length 2
        def rotate_left(s):
            return s[2:] + s[:2]
        # function to rotate string right by length 2
        def rotate_right(s):
            return s[-2:] + s[:-2]
        
        # if length of strings is not equal, return False
        return len(str1) == len(str2) and (str2 in rotate_left(str1) or str2 in rotate_right(str1))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends