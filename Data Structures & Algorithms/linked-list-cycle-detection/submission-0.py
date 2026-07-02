# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        
        current = head

        while current:
            if current in seen:
                return True
            else:
                seen.append(current)
                current = current.next

        return False
            