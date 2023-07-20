class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        path = collections.defaultdict(set)
        lst = [None for i in range(n)]
        
        for s, dest in edges:
            path[s].add(dest)
        #print(path) 
        Test, Pass = 1, 2
        def find_path(s):
            if lst[s]:
                return lst[s] == Test
            if not path[s]:
                return s == destination
             
            lst[s] = Pass
            for d in path[s]:
                if not find_path(d):
                    return False
            lst[s] = Test
            return True

        return find_path(source)
