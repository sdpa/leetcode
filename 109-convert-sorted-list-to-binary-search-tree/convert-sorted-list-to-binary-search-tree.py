# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # In the linkedList All the elements to the left of the middle node will be the left part of right. 
        # All the elements to the right of the node will be the right part of the tree. 
        # SO we recursively call buildTree which returns the child tree buit -> and then assign that to teh left and right subtree of the results 

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # cut the list
        if prev:
            prev.next = None

        root = TreeNode(slow.val)

        if slow != head:
            root.left = self.sortedListToBST(head)

        root.right = self.sortedListToBST(slow.next)

        return root
        