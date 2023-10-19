# POTD October 19, 2023
# levels of nodes in a binary tree
# LINK - https://practice.geeksforgeeks.org/problems/level-of-nodes-1587115620/1

#User function Template for python3
from collections import deque

class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        visited = set()
        queue = deque([(0, 0)])  # (node, level)

        while queue:
            current_node, level = queue.popleft()

            if current_node == X:
                return level

            visited.add(current_node)

            for neighbor in adj[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))

        return -1  # X not found in the graph


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends