class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

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

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        #visited = set()
        self.ans = 0
        def dfs(node, pre):
            
            #visited.add(node)
            d1, d2 = 0, 0
            for nei in graph[node]:
                #if nei not in visited:
                if nei != pre:
                    d = dfs(nei, node)
                    if d > d1:
                        d2 = d1
                        d1 = d

                    elif d > d2:
                        d2 = d

            self.ans = max(self.ans, d1+d2)
            return 1 + max(d1, d2)

        dfs(0, -1)
        return self.ans