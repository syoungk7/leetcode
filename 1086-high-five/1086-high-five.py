class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ids = {}
        result = []
        for item in items:
            if item[0] not in ids:
                ids[item[0]] = [item[1]]
            else:
                ids[item[0]].append(item[1])
        
        for s_id, score in ids.items():
            heapq.heapify(score)

            while len(score) > 5:
                heapq.heappop(score)
            
            result.append([s_id, int(sum(score)/5)])
        return sorted(result, key=lambda x: x[0])
                
            