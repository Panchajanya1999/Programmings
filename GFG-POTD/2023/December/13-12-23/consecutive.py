class Solution:
    def countStrings(self, n):
        power = 2 ** n
        count = 0
        
        for i in range(power):
            binary = bin(i)
            if '11' not in binary:
                count += 1
        
        return count % (10 ** 9 + 7)
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends
