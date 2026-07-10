# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (q and not p):
            return False

        # print(f"Nodes: p = {p.val}, q = {q.val}")

        if not p and not q:
            return True

        if p.val != q.val:
            return False

        # print(f"Seems like p = q ({p.val} = {q.val})")

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # return True