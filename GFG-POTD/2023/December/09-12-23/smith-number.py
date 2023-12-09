#User function Template for python3
class Solution:
    def smithNum(self, n):
            # code here
            def cd(n):
                ans = 0
                while n > 0:
                    ans += (n % 10)
                    n //= 10
                return ans
                
            digitsum = cd(n)
            
            #print(f"DigitSum: {digitsum}")
            
            primefact = 0
            temp = n
            div = 2
            
            while temp > 0 and div < n:
                while temp % div == 0:
                    primefact += cd(div)
                    temp //= div
                    #print(div)
                div += 1
            
            if temp > 1:
                return 0
            
            #print(f"PrimeFact: {primefact}")
                    
            if digitsum == primefact:
                return 1
            
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends
