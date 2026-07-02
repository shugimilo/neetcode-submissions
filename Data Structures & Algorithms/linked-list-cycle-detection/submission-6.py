# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head

        while fast and fast.next:
            nxt = fast.next
            if nxt.next:
                fast = nxt.next
                if slow == fast:
                    return True
                slow = slow.next
            else:
                return False

        return False