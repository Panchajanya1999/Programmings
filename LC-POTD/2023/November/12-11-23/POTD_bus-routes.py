class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # If source and target are the same, no buses needed
        if source == target:
            return 0
        
        # Number of bus routes
        n = len(routes)
        
        # Create a graph where each bus stop is connected to the buses that go through it
        graph = collections.defaultdict(set)
        for i in range(n):
            for j in routes[i]:
                graph[j].add(i)
        
        # Queue for BFS traversal
        q = collections.deque()
        q.append(source)
        
        # Set to keep track of visited buses
        visited = set()
        
        # Variable to store the result (number of buses needed)
        res = 0
        
        # BFS traversal
        while q:
            res += 1
            for _ in range(len(q)):
                # Pop the current bus stop from the queue
                cur = q.popleft()
                
                # Check buses going through the current stop
                for bus in graph[cur]:
                    # Skip if the bus is already visited
                    if bus in visited:
                        continue
                    
                    # Mark the bus as visited
                    visited.add(bus)
                    
                    # Check all stops of the bus
                    for stop in routes[bus]:
                        # If the target is reached, return the result
                        if stop == target:
                            return res
                        
                        # Add the stop to the queue for further exploration
                        q.append(stop)
        
        # If target is not reached, return -1
        return -1
