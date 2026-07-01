# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        i = 0
        while q:
            lvlWidth = len(q)
            for _ in range(0, lvlWidth):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            i += 1

        return i