# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Find the node of the subTree. 
        if not subRoot or not root:
            return False
        
        if(self.isSame(root, subRoot)):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSame(self, a: Optional[TreeNode], b: Optional[TreeNode]):
        if not a and not b:
            return True
        if (a and not b) or (not a and b):
            return False
        if a.val != b.val:
            return False
        
        return self.isSame(a.left, b.left) and self.isSame(a.right, b.right)

        