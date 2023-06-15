class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        totals, used = {}, []
        answer = [-1] * len(workers)
        
        for w, worker in enumerate(workers):
            for b, bike in enumerate(bikes): 
                dist = abs(bike[0] - worker[0]) + abs(bike[1] - worker[1])
                #totals.append((w, b, dist))
                if dist not in totals:
                    totals[dist] = []
                totals[dist].append((w, b))

        #totals.sort(key=lambda a: a[2])
        dists = sorted(list(totals.keys()))

        #for w, b, _ in totals:
        for dist in dists:
            same_dist = totals[dist]
            same_dist.sort()
            for w, b in same_dist:
                if answer[w] == -1 and b not in used:
                    answer[w] = b
                    used.append(b)

        return answer