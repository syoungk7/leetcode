class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        totals, used = [], []
        answer = [-1] * len(workers)
        pre = -1
        
        for w, worker in enumerate(workers):
            for b, bike in enumerate(bikes): 
                dist = abs(bike[0] - worker[0]) + abs(bike[1] - worker[1])
                totals.append((w, b, dist))
        #print(totals)
        totals.sort(key=lambda a: a[2])
        #print(totals)

        for w, b, dist in totals:
            if answer[w] == -1 and b not in used:
                answer[w] = b
                used.append(b)
    
        return answer