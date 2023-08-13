class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        new = defaultdict(list)
        avg = []
        for i, j in items:
            new[i].append(j)

        for k in sorted(new.keys()):
            top5 = sorted(new[k], reverse = True)[0:5]
            avg.append([k, int(sum(top5)/5)])

        return avg
                              