# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        # Count nodes
        nodes = 1
        tail = head
        while tail.next:
            tail = tail.next
            nodes += 1

        # Reduce unnecessary rotations
        k = k % nodes
        if k == 0:
            return head

        # Make circular list
        tail.next = head

        # Find new tail
        steps = nodes - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        # Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head

        