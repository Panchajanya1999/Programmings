from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        meetings = sorted([(S[i], F[i], i+1) for i in range(N)], key=lambda x: (x[1], x[0]))
        res = [meetings[0][2]]
        last_finish = meetings[0][1]
        for s, f, i in meetings[1:]:
            if s > last_finish:
                res.append(i)
                last_finish = f
        return sorted(res)



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends
