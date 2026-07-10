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

        if not p and not q:
            return True

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def findCandidates(self, root: Optional[TreeNode], val: int):
        if not root:
            return
    
        if root.val == val:
            self.candidates.append(root)

        self.findCandidates(root.left, val)
        self.findCandidates(root.right, val)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.candidates = []
        self.findCandidates(root, subRoot.val)

        for candidate in self.candidates:
            if self.isSameTree(candidate, subRoot):
                return True

        return False
