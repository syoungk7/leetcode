class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        def manhattan_distance(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        
        grid = [(0, 0, 0)]     
        passed = set()
        
        while grid:
            dist, i, t_state = heapq.heappop(grid)
            
            if (i, t_state) in passed: continue
            
            passed.add((i, t_state))
            
            if i == len(workers): return dist
            
            for j in range(len(bikes)):
                if t_state & (1 << j) == 0:
                    m_dist = manhattan_distance(i, j)
                    n_taken = t_state | 1 << j
                    heapq.heappush(grid, (m_dist + dist, i + 1, n_taken))