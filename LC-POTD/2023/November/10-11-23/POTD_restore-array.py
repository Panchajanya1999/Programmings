from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        ans = []

        root = next(iter(node for node in graph if len(graph[node]) == 1))
        stack = [root]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                ans.append(node)
                stack.extend(graph[node])

        return ans
