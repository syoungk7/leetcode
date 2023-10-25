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
    
#         node = head
#         node2 = head
#         old, new, out = node, node.next, node.next
#         while node2:
#             new_node = Node(node.val, None, None)
#             new_node.next = node.next
#             node.next = new_node            
#             node = new_node.next

#             node2.next.random = node2.random.next if node2.random else None
#             node2 = node2.next.next
            
#             if new:
#                 old.next = node2
#                 print(new, new.next)
#                 new.next = node2.next if new.next else None
#                 old = old.next
#                 new = new.next
        
#         return out
            