# POTD 17th October 2023
# Transitive Closure of a Graph
# Link - https://practice.geeksforgeeks.org/problems/transitive-closure-of-a-graph0930/1


#User function Template for python3

class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        reach = [[0] * N for _ in range(N)]

        # Initialize reach matrix with the given graph
        for i in range(N):
            for j in range(N):
                # A vertex is reachable from itself
                if i == j:
                    reach[i][j] = 1
                else:
                    reach[i][j] = graph[i][j]

        # Update reach matrix using Floyd-Warshall algorithm
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

        return reach

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        graph = []
        for i in range(0,N):
            graph.append([int(j) for j in input().split()])
        ob = Solution()
        ans = ob.transitiveClosure(N, graph)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends