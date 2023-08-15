"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        if not tree: return None
        #tmp = []
        tmp = set()

        for i in tree:
            for j in i.children:
                #if j.val not in tmp: tmp.append(j.val)
                tmp.add(j.val)
                    
        for k in tree:
            if k.val not in tmp: return k
                
        