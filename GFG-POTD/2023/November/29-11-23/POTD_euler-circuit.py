class Solution:
    def isEulerCircuitExist(self, V, adj):
        odd = sum(len(edges) % 2 != 0 for edges in adj)
        if odd == 0:
            return 2
        elif odd == 2:
            return 1
        else:
            return 0
        




#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEulerCircuitExist(V, adj)
		print(ans)
# } Driver Code Ends
