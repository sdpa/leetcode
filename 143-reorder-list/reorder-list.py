# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Split in middle.
        slow = fast = head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        # Reverse the 2nd half.
        prev = None
        cur = slow.next
        while(cur != None):
            new = cur.next
            cur.next = prev
            prev = cur
            cur = new
        slow.next = None
    
        # merge the 2 linkedLists.
        first = head
        second = prev

        while second:
            t1 = first.next
            first.next = second
            first = second
            second = t1

        
