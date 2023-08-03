class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        # edges to dict 
        # consider both case right to left and left to right
        tree = collections.defaultdict(list)
        for left, right in edges:
            tree[left].append(right)
            tree[right].append(left)        
        #print(tree, tree[0])
        
        # target: the longest path
        def diameter(node, node2):
            diam = 0
            level1, level2 = 0, 0
            
            for n in tree[node]:
                if n != node2:
                    dd, ll = diameter(n, node)
                    diam = max(diam, dd)
                    print(diam, ll, level1, level2)
                    if ll > level2:
                        level2 = ll
                    
                        if level2 > level1:
                            level2, level1 = level1, level2
            print(diam, level1, level2)
            return max(diam, level1+level2), max(level1+1, level2+1)

        
        
        return diameter(0, None)[0]
            
