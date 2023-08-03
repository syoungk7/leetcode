class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        # target: the longest path
        def diameter(node, node2):
            diam, level1, level2 = 0, 0, 0
            
            for n in tree[node]:
                if n != node2:
                    dd, ll = diameter(n, node)
                    diam = max(diam, dd)

                    if ll > level2:
                        level2 = ll

                    if level2 > level1:
                        level2, level1 = level1, level2

            dd = max(diam, level1+level2)
            ll = max(level1+1, level2+1)

            return dd, ll
        
        # edges to dict 
        # consider both case right to left and left to right
        tree = collections.defaultdict(list)
        for left, right in edges:
            tree[left].append(right)
            tree[right].append(left)        
        
        return diameter(0, None)[0]
            
