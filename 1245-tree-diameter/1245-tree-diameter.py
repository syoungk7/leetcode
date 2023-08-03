class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        # Create our graph, we know its undirect so edges are bidirectional.
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        # Start with a bfs to find a point on the longest path, starting at 0 the last
		# node left on the queue will be the furthest away from our starting location.
        q = collections.deque([])
        q.append((0, -1))
        while q:
            node, parent = q.popleft()
            for nei in graph[node]:
                if nei != parent:
                    q.append((nei, node))
        # We create a new queue and add the node that we just found.
        q = collections.deque([])
        q.append((node, 0, [node]))
        # We continue searching from that node and the last node we have on our queue will
		# be the furthest from it and hence the longest path so we return that dist.
        while q:
            node, dist, path = q.popleft()
            for nei in graph[node]:
                if nei not in set(path):
                    q.append((nei, dist + 1, path+[nei]))
                    
        return dist
#         # edges to dict 
#         # consider both case right to left and left to right
#         tree = collections.defaultdict(set)
#         for left, right in edges:
#             tree[left].add(right)
#             tree[right].add(left)        
#         #print(tree, tree[0])
            
#         # target: the longest path
#         def diameter(node, diam = 0):
#             passed = set(node)
            
#             while node:
#                 path = []
#                 for i in node:
#                     print(tree[i])
#                     for j in tree[i]:
#                         if j not in passed:
#                             path.append(j)
#                             passed.add(j)
#                 node = path
#                 diam += 1
#                 print(node, passed, diam)
#             return diam
        
#         return diameter([0], 0)

