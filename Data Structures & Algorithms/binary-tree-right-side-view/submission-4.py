# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        treeLevels = self.levelOrder(root)
        print(treeLevels)
        res = []
        for lvl in treeLevels:
            res.append(lvl[-1])

        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            lvl = []
            lvlWidth = len(q)
            for _ in range(0, lvlWidth):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lvl.append(node.val)
            res.append(lvl)

        return res