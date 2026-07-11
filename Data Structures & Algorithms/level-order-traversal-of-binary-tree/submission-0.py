# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []

        # depth = self.maxDepth(root)

        outer_i = 0
        inner_i = 0

        while q:
            print(f"Outer iteration #{outer_i}, len(q): {len(q)}\nq = [", end="")
            for i in range(0, len(q)):
                if i == len(q) - 1:
                    print(f"{q[i].val}]")   
                else:
                    print(f"{q[i].val}", end=", ")
            lvl = []
            for _ in range(0, len(q)):
                node = q.popleft()
                print(f"Inner iteration #{inner_i}, popped node: {node.val}")
                lvl.append(node.val)
                print(f"Appending node: {node.val}")
                if node.left:
                    q.append(node.left)
                    print(f"Adding left node to q: {node.left.val}")
                if node.right:
                    q.append(node.right)
                    print(f"Adding right node to q: {node.right.val}")
                inner_i += 1
            print(f"Appending lvl: {lvl}\n")
            res.append(lvl)
            outer_i += 1

        return res

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right)+1