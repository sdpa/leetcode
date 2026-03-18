# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return Nont
        if not head.next:
            return None
        
        p1 = head
        follower = None
        count = 1

        count = 0
        c = head
        while(c != None):
            c = c.next
            count += 1
        
        stop_idx = count - n
        i = 0
        while(p1 != None and i < stop_idx):
            follower = p1
            p1 = p1.next
            i += 1
    
        if p1 == head:
            head = p1.next
        else:
            follower.next = p1.next
    
        return head

        