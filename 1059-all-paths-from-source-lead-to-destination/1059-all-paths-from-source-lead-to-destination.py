class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         path = collections.defaultdict(set)
#         lst = [None for i in range(n)]
#         print(lst)
        
#         for s, dest in edges:
#             path[s].add(dest)
#         print(path) 
        
#         def find_path(s):
#             if lst[s]:
#                 return lst[s] == 1
#             if not path(s):
#                 return s == destination
             
#             lst[s] = 2
#             for d in path[s]:
#                 if not find_path(d):
#                     return False
#             lst[s] = 1
#             return True

#         return find_path(source)
        adj_list = collections.defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)

        BLACK = 1  # fully processed nodes
        GRAY = 2  # nodes being processed
        states = [None] * n
        def recurr(node):
            if states[node]:
                return states[node] == BLACK

            if not adj_list[node]:
                return node == destination

            states[node] = GRAY

            for nei in adj_list[node]:
                if not recurr(nei):
                    return False

            states[node] = BLACK
            return True

        return recurr(source)