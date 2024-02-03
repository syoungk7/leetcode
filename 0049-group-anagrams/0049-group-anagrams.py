class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs:
            word = ''.join(sorted(s))
            if word in out.keys():
                out[word].append(s)
            else:
                out[word] = [s]
        return out.values()