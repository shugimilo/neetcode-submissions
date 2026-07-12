# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])

        devolvedTree = []
        res = []
        i = 1

        while q:
            lvlWidth = len(q)
            print(f"Iteration #{i}, level width: {lvlWidth}")
            lvl = []
            for j in range(0, lvlWidth):
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    if node.left: q.append(node.left)
                    else: q.append(None)
                    if node.right: q.append(node.right)
                    else: q.append(None)
                else:
                    lvl.append(None)
            i += 1
            devolvedTree.append(lvl)

        print(devolvedTree)

        for lvl in devolvedTree:
            l = len(lvl)-1
            print(f"Current level: {lvl}, length: {len(lvl)}")
            for i in range(0, l+1):
                if lvl[l-i]:
                    res.append(lvl[l-i])
                    break

        return res



