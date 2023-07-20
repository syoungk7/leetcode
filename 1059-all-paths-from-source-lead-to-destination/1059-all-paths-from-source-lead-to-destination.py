class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path = collections.defaultdict(set)
        lst = [None for i in range(n)]
        
        for s, dest in edges:
            path[s].add(dest)
        #print(path) 
        
        def find_path(s):
            if lst[s]:
                return lst[s] == 'Pass'
            if not path[s]:
                return s == destination
             
            lst[s] = 'Test'
            for d in path[s]:
                if not find_path(d):
                    return False
            lst[s] = 'Pass'
            return True

        return find_path(source)
