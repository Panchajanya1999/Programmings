#User function Template for python3



class Solution:
    def minNumber(self, arr,n):
        # code here
        # code here
        import math
        # create a function which will return True if the number is prime
        def isPrime(num):
            # Handle special cases
            if num <= 1:
                return False
            if num <= 3:
                return True

            # Check if the number is divisible by 2 or 3
            if num % 2 == 0 or num % 3 == 0:
                return False

            # Check for divisibility by numbers of the form 6k ± 1
            for i in range(5, int(math.sqrt(num)) + 1, 6):
                if num % i == 0 or num % (i + 2) == 0:
                    return False

            return True
        
        arrsum = sum(arr)
        # the biggest gap between two prime numbers in range
        # 1 to 10^5 is 71
        # compiled data from https://onlinegdb.com/RF5b7sxix
        for i in range(71):
            if isPrime(arrsum+i):
                return i



#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends
