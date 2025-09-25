# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        cur = head
        prev = head
        for _ in range(n):
            cur = cur.next
        if not cur: return head.next
        while cur.next:
            prev, cur = prev.next, cur.next
        
        prev.next = prev.next.next

        return head
    
