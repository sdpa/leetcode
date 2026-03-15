# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:


        res = []
        def dfs(root, path, currSum):

            if not root:
                return
            currSum = currSum + root.val
            path.append(root.val)
            if targetSum == currSum and not root.left and not root.right:
                res.append(path.copy())
            # Add curret node to the currSum

           
            dfs(root.left, path, currSum)
            dfs(root.right, path, currSum)
            path.pop()

        dfs(root, [], 0)
        return res
            

        