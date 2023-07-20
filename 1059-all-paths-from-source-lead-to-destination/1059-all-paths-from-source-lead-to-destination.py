class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path = collections.defaultdict(set)
        lst = [None] * n
        
        for s, dest in edges:
            path[s].add(dest)
        #print(path) 
        
        def find_path(s):
            if lst[s]:
                return lst[s] == 1
            if not path[s]:
                return s == destination
             
            lst[s] = 2
            for d in path[s]:
                if not find_path(d):
                    return False
            lst[s] = 1
            return True

        return find_path(source)
