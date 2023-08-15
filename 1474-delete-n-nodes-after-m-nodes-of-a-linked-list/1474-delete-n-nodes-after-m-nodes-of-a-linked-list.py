# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        tmp = head
        
        while tmp:
            
            for _ in range(m-1):
                if tmp.next: tmp = tmp.next
                else: return head

            for _ in range(n):
                if tmp.next: tmp.next = tmp.next.next
                else: return head
            
            if tmp:
                tmp = tmp.next
        return head