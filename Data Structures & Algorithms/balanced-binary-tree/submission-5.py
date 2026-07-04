# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        depthLeft = self.maxDepth(root.left)
        depthRight = self.maxDepth(root.right)

        if abs(depthLeft - depthRight) > 1:
            return False

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right)+1