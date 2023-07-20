class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path = collections.defaultdict(set)
        lst = [0 for i in range(n)]
        
        for s, dest in edges:
            path[s].add(dest)
        print(path) 
        
        def find_path(s):
            if len(path[s]) == 0:
                return s == destination
            elif lst[s] == 1:
                return False
            elif lst[s] == 2:
                return True
            else:
                lst[s] = 1
                for j in path[s]:
                    if not find_path(j):
                        return False
                lst[s] = 2
                return True

        return find_path(source)