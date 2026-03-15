"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # You perform depth first traversal and you add all the nodes to a quee with its level and connect them if they are the same level. 
        # Left and then right ensures the order of the next one. 

        queue = []
        level = 0
        if root:
            queue.append((root, level))
        
        while queue:
            node, level = queue.pop(0)
            if len(queue) > 0 and queue[0][1] == level:
                node.next = queue[0][0]
            else:
                node.next = None
            
            level = level + 1
            if node.left:
                queue.append((node.left, level))
            if node.right:
                queue.append((node.right, level))

        return root
            
                

            



        