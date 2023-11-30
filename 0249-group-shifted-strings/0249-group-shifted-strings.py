class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group = defaultdict()
        convert = []

        for i in strings:
            for j in i:             
                    convert.append((ord(j) - ord(i[0])) % 26)

            if tuple(convert) in group:
                group[tuple(convert)].append(i)
            else:
                group[tuple(convert)] = [i]
            convert = []
    
        return group.values()