# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if node:
                if not node.right:
                    node.right, node.left = node.left, None
                    queue.append(node.right)
                else:
                    node.left, node.right = node.right, node.left
                    queue.append(node.right)
                    queue.appendleft(node.left)
            else:
                continue

        return root
