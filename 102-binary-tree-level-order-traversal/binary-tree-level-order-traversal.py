# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0)]
        output = []
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                item = queue.pop(0)
                node = item[0]
                level = item[1]
                if level == len(output):
                    output.append([node.val])
                else:
                    output[level].append(node.val)
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

        return output
                
                

        