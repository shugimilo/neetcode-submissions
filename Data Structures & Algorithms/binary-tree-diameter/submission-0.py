# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.recursion(root)

        return self.diameter
        
    def recursion(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        node = root
        left = 0
        right = 0

        if node.left:
            left = self.recursion(node.left)
        if node.right:
            right = self.recursion(node.right)

        total = left + right
        if total >= self.diameter:
            self.diameter = total

        return max(left, right) + 1