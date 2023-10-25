"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       
        if head == None: return None
        
        out = {}
        
        def new_head(node):
            if node == None: return None
            if node in out: return out[node]
            out[node] = Node(node.val)
            out[node].next = new_head(node.next)
            out[node].random = new_head(node.random)
            
            return out[node]

        return new_head(head)